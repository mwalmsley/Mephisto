/*
 * Copyright (c) Meta Platforms and its affiliates.
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

export const DELAY_PROGRESSBAR_RESIZING_MSEC: number = 1000;

export const STORAGE_PRESAVED_ANNOTATION_TRACKS_KEY: string =
  "annotation_tracks";

export const DEFAULT_SEGMENT: SegmentType = {
  end_sec: 0,
  start_sec: 0,
  title: "",
};

// in case user does not specify any field
export const DEFAULT_SEGMENT_FIELDS: SegmentFieldsType = [
  {
    id: "id_title",
    label: "Segment name",
    name: "title",
    type: "input",
  },
];

export const INIT_ANNOTATION_TRACK: TrackObjectedType = {
  title: "",
  segments: {},
};

// When we click on segment, we simulate clicking on track as well, and it must be first,
// but setting states is async
export const DELAY_CLICK_ON_SECTION_MSEC: number = 200;

// When we create a new segment, if it's inside alreadycreated segment,
// we show error message under progress bar.
// If we show it immediately, it can be hidden with effect of setting currently in change segment
export const DELAY_SHOW_OVERLAPPING_MESSAGE_MSEC: number = 200;

export const START_NEXT_SECTION_PLUS_SEC: number = 0;

export const COLORS: string[] = [
  "blue",
  "green",
  "orange",
  "purple",
  "red",
  "yellow",
  "brown",
];

export const MIN_SEGMENT_WIDTH_PX: number = 6;
export const MIN_SEGMENT_WIDTH_MOBILE_PX: number = 3;

export const POPOVER_INVALID_SEGMENT_CLASS: string = "with-segment-validation";

export const POPOVER_INVALID_SEGMENT_PROPS: {
  [key: string]: string | boolean;
} = {
  "data-html": true,
  "data-placement": "top",
  "data-content": "Please fix provided data before continuing",
  "data-toggle": "popover",
  "data-trigger": "hover",
};

export const CHAPTERS_SETTINGS: Partial<TextTrack> = {
  kind: "chapters",
  label: "Segments",
  language: "en",
  mode: "showing",
};
