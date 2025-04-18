#!/usr/bin/env python3

# Copyright (c) Meta Platforms and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os

from mephisto.tools.building_react_apps.utils import clean_single_react_app
from mephisto.tools.scripts import build_custom_bundle
from mephisto.utils.console_writer import ConsoleWriter

REPO_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
PACKAGES_PATH = os.path.join(REPO_PATH, "packages")
ANNOTATED_PACKAGES_PATH = os.path.join(PACKAGES_PATH, "annotated")

logger = ConsoleWriter()


# --- CLEAN ---


def clean_annotated_bbox_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(ANNOTATED_PACKAGES_PATH, "bbox")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_annotated_keypoint_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(ANNOTATED_PACKAGES_PATH, "keypoint")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_annotated_shell_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(ANNOTATED_PACKAGES_PATH, "shell")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_annotated_video_player_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(ANNOTATED_PACKAGES_PATH, "video-player")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_annotation_toolkit_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(PACKAGES_PATH, "annotation-toolkit")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_bootstrap_chat_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(PACKAGES_PATH, "bootstrap-chat")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_global_context_store_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(PACKAGES_PATH, "global-context-store")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_mephisto_review_hook_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(PACKAGES_PATH, "mephisto-review-hook")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_mephisto_core_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(PACKAGES_PATH, "mephisto-core")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


def clean_mephisto_addons_package(remove_package_locks: bool, verbose: bool = False):
    webapp_path = os.path.join(PACKAGES_PATH, "mephisto-addons")
    clean_single_react_app(webapp_path, remove_package_locks=remove_package_locks, verbose=verbose)


# --- BUILD ---


def build_annotated_bbox_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{ANNOTATED_PACKAGES_PATH}/bbox'[/blue]")

    build_custom_bundle(
        ANNOTATED_PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="bbox",
        build_command="build",
    )


def build_annotated_keypoint_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{ANNOTATED_PACKAGES_PATH}/keypoint'[/blue]")

    build_custom_bundle(
        ANNOTATED_PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="keypoint",
        build_command="build",
    )


def build_annotated_shell_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{ANNOTATED_PACKAGES_PATH}/shell'[/blue]")

    build_custom_bundle(
        ANNOTATED_PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="shell",
        build_command="build",
    )


def build_annotated_video_player_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{ANNOTATED_PACKAGES_PATH}/video-player'[/blue]")

    build_custom_bundle(
        ANNOTATED_PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="video-player",
        build_command="build",
    )


def build_annotation_toolkit_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{PACKAGES_PATH}/annotation-toolkit'[/blue]")

    build_custom_bundle(
        PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="annotation-toolkit",
        build_command="build",
    )


def build_bootstrap_chat_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{PACKAGES_PATH}/bootstrap-chat'[/blue]")

    build_custom_bundle(
        PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="bootstrap-chat",
        build_command="build",
    )


def build_global_context_store_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{PACKAGES_PATH}/global-context-store'[/blue]")

    build_custom_bundle(
        PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="global-context-store",
        build_command="build",
    )


def build_mephisto_review_hook_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{PACKAGES_PATH}/mephisto-review-hook'[/blue]")

    build_custom_bundle(
        PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="mephisto-review-hook",
        build_command="build",
    )


def build_mephisto_core_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{PACKAGES_PATH}/mephisto-core'[/blue]")

    build_custom_bundle(
        PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="mephisto-core",
        build_command="build",
    )


def build_mephisto_addons_package(force_rebuild: bool = False, verbose: bool = False):
    if verbose:
        logger.info(f"[blue]Building '{PACKAGES_PATH}/mephisto-addons'[/blue]")

    build_custom_bundle(
        PACKAGES_PATH,
        force_rebuild=force_rebuild,
        webapp_name="mephisto-addons",
        build_command="build",
    )
