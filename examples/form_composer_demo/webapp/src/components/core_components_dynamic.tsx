/*
 * Copyright (c) Meta Platforms and its affiliates.
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import * as React from "react";
import { FormComposer } from "mephisto-addons";

// Required import for custom validators
import * as customValidators from "custom-validators";
// Required import for custom triggers
import * as customTriggers from "custom-triggers";

type DirectionsPropsType = {
  children: React.ReactNode;
};

function Directions({ children }: DirectionsPropsType) {
  return (
    <div className="card mb-4">
      <div className="card-body container">{children}</div>
    </div>
  );
}

function LoadingScreen() {
  return <Directions>Loading...</Directions>;
}

type FormComposerBaseFrontendPropsType = {
  taskData: ConfigTaskType;
  onSubmit?: Function;
  onError?: Function;
  finalResults?: FormComposerResultsType;
};

function FormComposerBaseFrontend({
  taskData,
  onSubmit,
  onError,
  finalResults = null,
}: FormComposerBaseFrontendPropsType) {
  let initialConfigFormData: ConfigFormType = taskData?.form;

  if (!initialConfigFormData) {
    return <div>Passed form data is invalid... Recheck your task config.</div>;
  }

  return (
    <div>
      <FormComposer
        data={initialConfigFormData}
        onSubmit={onSubmit}
        finalResults={finalResults}
        // Required for custom validators
        customValidators={customValidators}
        // Required for custom triggers
        customTriggers={customTriggers}
      />
    </div>
  );
}

export { LoadingScreen, FormComposerBaseFrontend };
