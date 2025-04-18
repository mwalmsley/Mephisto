#!/usr/bin/env python3

# Copyright (c) Meta Platforms and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
import os
import shlex
import shutil
import subprocess
from typing import Optional
from typing import TYPE_CHECKING

import sh  # type: ignore

import mephisto.abstractions.architects.router as router_module
from mephisto.utils.logger_core import get_logger

if TYPE_CHECKING:
    from mephisto.data_model.task_run import TaskRun

ROUTER_ROOT_DIR = os.path.dirname(router_module.__file__)
NODE_SERVER_SOURCE_ROOT = os.path.join(ROUTER_ROOT_DIR, "node")
FLASK_SERVER_SOURCE_ROOT = os.path.join(ROUTER_ROOT_DIR, "flask")
CROWD_SOURCE_PATH = "static/wrap_crowd_source.js"
TASK_CONFIG_PATH = "static/task_config.json"
CURR_MEPHISTO_CORE_PACKAGE_VERSION = "1.5.4"

logger = get_logger(name=__name__)


def can_build(build_dir: str, task_run: "TaskRun") -> bool:
    """Determine if the build dir is properly formatted for
    being able to have the router built within. This is a
    validation step that should be run before build_router.
    """
    # TODO(#97) incorporate this step into the blueprint
    # task builder test, as once the task is built, it
    # should be able to have the server build as well.
    # TODO(#651) actually implement this when the full build
    # process for the router is decided
    return True


def install_router_files() -> None:
    """
    Create a new build including the node_modules
    """
    return_dir = os.getcwd()
    os.chdir(NODE_SERVER_SOURCE_ROOT)

    packages_installed = subprocess.call(["npm", "install"])
    if packages_installed != 0:
        raise Exception(
            "please make sure node is installed, otherwise view " "the above error for more info."
        )

    os.chdir(return_dir)


def build_node_router(build_dir: str, task_run: "TaskRun") -> str:
    """Build requirements for the NPM router"""
    install_router_files()
    return NODE_SERVER_SOURCE_ROOT


def build_flask_router(build_dir: str, task_run: "TaskRun") -> str:
    # Everything should already be built
    return FLASK_SERVER_SOURCE_ROOT


def build_router(
    build_dir: str,
    task_run: "TaskRun",
    version: str = "node",
    server_source_path: Optional[str] = None,
) -> str:
    """
    Copy expected files from the router source into the build dir,
    using existing files in the build dir as replacements for the
    defaults if available
    """
    logger.info(f"Started building router `{version}`")
    logger.debug(f"{task_run=}\n{server_source_path=}")

    if server_source_path is not None:
        # Giving a server source takes precedence over the build
        server_source_directory_path = server_source_path
    elif version == "node":
        server_source_directory_path = build_node_router(build_dir, task_run)
    elif version == "flask":
        server_source_directory_path = build_flask_router(build_dir, task_run)
    else:
        logger.error(f"Cannot build router for not configured version: {version}")
        raise Exception(f"Unexpected router version: {version}")

    local_server_directory_path = os.path.join(build_dir, "router")
    logger.debug(f"{local_server_directory_path=}")

    # Delete old server files
    sh.rm(shlex.split("-rf " + local_server_directory_path))

    # Copy over a clean copy into the server directory
    logger.debug(f"Copying '{server_source_directory_path}' -> '{local_server_directory_path}'")
    shutil.copytree(server_source_directory_path, local_server_directory_path)

    # Copy the required wrap crowdsource path
    local_crowd_source_path = os.path.join(local_server_directory_path, CROWD_SOURCE_PATH)
    logger.debug(f"{local_crowd_source_path=}")

    crowd_provider = task_run.get_provider()
    shutil.copy2(crowd_provider.get_wrapper_js_path(), local_crowd_source_path)

    # Copy the task_run's json configuration
    local_task_config_path = os.path.join(local_server_directory_path, TASK_CONFIG_PATH)
    logger.debug(f"{local_task_config_path=}")

    blueprint = task_run.get_blueprint()
    logger.debug(f"{blueprint=}")

    with open(local_task_config_path, "w+") as task_fp:
        frontend_args = blueprint.get_frontend_args()
        frontend_args["mephisto_core_version"] = CURR_MEPHISTO_CORE_PACKAGE_VERSION
        frontend_args["provider_type"] = crowd_provider.PROVIDER_TYPE

        json.dump(frontend_args, task_fp)

    # Consolidate task files as defined by the task
    TaskBuilderClass = blueprint.TaskBuilderClass
    task_builder = TaskBuilderClass(task_run, task_run.args)
    logger.debug(f"{task_builder=}")

    task_builder.build_in_dir(local_server_directory_path)

    logger.info(f"Finished building router")
    return local_server_directory_path
