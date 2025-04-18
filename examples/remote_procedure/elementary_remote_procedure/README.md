<!---
  Copyright (c) Meta Platforms and its affiliates.
  This source code is licensed under the MIT license found in the
  LICENSE file in the root directory of this source tree.
-->

# Mephisto Elementary remote procedure example

This task is a _very simplistic_ bare-bones example of being able to set up a task where the frontend directly connects to the backend
using the `useMephistoRemoteProcedureTask` hook from the `mephisto-core` package.
It should serve as a decent example of how to get a `RemoteProcedureBlueprint` task up off the ground.

Deploying the task as-is brings up a page where the user needs to click the "query backend" button enough times
for the task to be considered ready to submit.

It makes use of the function_registry to use a `"handle_with_model"` method that, admittedly, doesn't use any models,
but hopefully demonstrates where a model can fit into this type of task.

As it stands, these queries are still just a single request to single response model,
but that should be sufficient for most tasks that want to have a backend in-the-loop for an otherwise frontend-heavy task.

## End-to-end example

Now let's see how the whole end-to-end list of commands looks like for the example `Elementary remote procedure`:

```shell
# 1. In your console

docker-compose -f docker/docker-compose.dev.yml up
docker exec -it mephisto_dc bash

# 2.Inside Docker container

cd /mephisto/examples/remote_procedure/elementary_remote_procedure
python ./run_task__local__inhouse.py
```
