from dataclasses import asdict
from logging import Logger
from pathlib import Path
from typing import List

from annotator.data import AnnotationTable, WorldlineTable, Annotation
from neuronir.methods.update import update_frame

from ._utilities import default_args


@default_args("_now, True, False")
def update_neir(
    dataset: Path,
    annotations: AnnotationTable,
    worldlines: WorldlineTable,
    window_state,
    arg: str,
    logger: Logger
) -> List[dict]:
	"""
	arg: time, restrict_update, recompile_model, update_children
		time: Time to run neuronir for.
		restrict_update: Update only around partial manual annotations.
		recompile_model: Rerun build_model() in neuronir.
	"""

	arg_list = arg.replace(" ", "").split(",")

	if arg_list[0] == '_now':
		t_idx = window_state['t_idx']
	else:
		t_idx = int(arg_list[0])
	restrict_update = arg_list[1] in ['True', 'Y', 'y']
	recompile_model = arg_list[2] in ['True', 'Y', 'y']

	ret = update_frame(
		dataset=Path(dataset),
		annotation=annotations.df,
		t_idx=t_idx,
		restrict_update=restrict_update,
		recompile_model=recompile_model,
	)
	if ret is None:
		return [{"type": "annotations/get_annotations"}]
	else:
		t_list, results, worldline_id, provenance = ret

	for t in range(len(t_list)):
		annot_t = annotations.get_t(t_list[t])
		ids = list(annot_t.df['id'])
		wlid = []
		for i in ids:
			annot = asdict(annot_t.get(i))
			wlid.append(annot['worldline_id'])
		for i, w in enumerate(worldline_id):
			if w not in wlid:
				A = Annotation(
					t_idx=window_state["t_idx"],
					x=(results[t, i, 0] + 1)/2,
					y=(results[t, i, 1] + 1)/2,
					z=(results[t, i, 2] + 1)/2,
					worldline_id=w,
					parent_id=0,
					provenance=b'NEIR'
				)
				annotations.insert(A)
			else:
				idx = wlid.index(w)
				annotations.update(
					ids[idx],
					{'x': (results[t, i, 0] + 1)/2,
					 'y': (results[t, i, 1] + 1)/2,
					 'z': (results[t, i, 2] + 1)/2,
					 'provenance': provenance[t, i]}
				)

	return [{"type": "annotations/get_annotations"}]
