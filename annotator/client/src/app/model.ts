import type { AnnotationWindowState_t } from '../annotation_window/model'
import type { AnnotationsState_t } from '../annotations/model'
import type { WorldlinesState_t } from '../worldlines/model'

export type State_t = {
  annotation_window: AnnotationWindowState_t,
  annotations: AnnotationsState_t,
  worldlines: WorldlinesState_t,
  dataset: string,
};