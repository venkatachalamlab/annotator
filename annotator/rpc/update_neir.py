from dataclasses import asdict
from logging import Logger
from pathlib import Path
from typing import List

from annotator.data import AnnotationTable, WorldlineTable, Annotation
from neuronir.methods.update import update_frame

from ._utilities import default_args

@default_args("_now, True, False, False")
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
		update_children: Also run neuronir on all child frames.
	"""

	arg_list = arg.replace(" ", "").split(",")

	if arg_list[0] == '_now':
		t_idx = window_state['t_idx']
	else:
		t_idx = int(arg_list[0])
	restrict_update = arg_list[1] in ['True', 'Y', 'y']
	recompile_model = arg_list[2] in ['True', 'Y', 'y']
	update_children = arg_list[3] in ['True', 'Y', 'y']

	t_list, results, worldline_id, provenance = update_frame(
		dataset_path=Path(dataset),
		annotation=annotations.df,
		t_idx=t_idx,
		restrict_update=restrict_update,
		recompile_model=recompile_model,
		update_children=update_children
	)

	for t in range(len(t_list)):
		annot_t = annotations.get_t(t_list[t])
		ids = list(annot_t.df['id'])
		for i in ids:
			annot = asdict(annot_t.get(i))
			w_idx = worldline_id.index(annot['worldline_id'])
			annotations.update(
				i,
				{'x': (results[t, w_idx, 0] + 1)/2,
				 'y': (results[t, w_idx, 1] + 1)/2,
				 'z': (results[t, w_idx, 2] + 1)/2,
				 'provenance': provenance[t, w_idx]}
			)

	return [{"type": "annotations/get_annotations"}]