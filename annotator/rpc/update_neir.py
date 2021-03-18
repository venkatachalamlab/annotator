from logging import Logger
from pathlib import Path
from typing import List

from annotator.data import AnnotationTable, WorldlineTable, Annotation
from neuronir.methods.update import update_frame

from ._utilities import default_args

@default_args("_now, False, False")
def update_neir(
    dataset: Path,
    annotations: AnnotationTable,
    worldlines: WorldlineTable,
    window_state,
    arg: str,
    logger: Logger
) -> List[dict]:
	"""
	arg: time, recompile_model, update_children
		time: Time to run neuronir for.
		recompile_model: Rerun build_model() in neuronir.
		update_children: Also run neuronir on all child frames.
	"""

	arg_list = arg.replace(" ", "").split(",")

	if arg_list[0] == '_now':
		t_idx = window_state['t_idx']
	else:
		t_idx = int(arg_list[0])
	recompile_model = arg_list[1] in ['True', 'Y', 'y']
	update_children = arg_list[2] in ['True', 'Y', 'y']

	t_list, results, worldline_id, provenance = update_frame(
		dataset_path=Path(dataset),
		annotation=annotations.df,
		t_idx=t_idx,
		recompile_model=recompile_model,
		update_children=update_children
	)

	for t in t_list:
		annot_t = annotations.get_t(t)
		ids = list(annot_t.df['id'])
		for i in ids:
			annot = asdict(annot_t.get(i))
			w_idx = worldline_id.index(annot['worldline_id'])
			A = Annotation(
				t_idx=t,
				x=results[0, w_idx, 0],
				y=results[0, w_idx, 1],
				z=results[0, w_idx, 2],
				worldline_id=annot['worldline_id'],
				parent_id=0,
				provenance=provenance[t, w_idx]
			)
			annotations.update(i, A)

	return [{"type": "annotations/get_annotations"}]