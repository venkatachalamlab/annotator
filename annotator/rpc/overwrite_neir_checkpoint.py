from logging import Logger
from pathlib import Path
from typing import List

from annotator.data import AnnotationTable, WorldlineTable
from neuronir.methods.overwrite import overwrite_checkpoint

from ._utilities import default_args


@default_args("None, None, False")
def overwrite_neir_checkpoint(
    dataset: Path,
    annotations: AnnotationTable,
    worldlines: WorldlineTable,
    window_state,
    arg: str,
    logger: Logger
) -> List[dict]:
	"""
	arg: key, value, recompile_model
		key: Name of item in checkpoint to overwrite.
		value: New item to write into checkpoint.
		recompile_model: Rerun build_model() in neuronir.
	"""

	arg_list = arg.replace(" ", "").split(",")

	key = str(arg_list[0])
	value = eval(arg_list[1])
	recompile_model = arg_list[2] in ['True', 'Y', 'y']

	overwrite_checkpoint(dataset, key, value, recompile_model)

	return [{"type": "annotations/get_annotations"}]
