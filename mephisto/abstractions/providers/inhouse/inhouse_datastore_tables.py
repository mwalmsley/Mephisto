#!/usr/bin/env python3

# Copyright (c) Meta Platforms and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

"""
WARNING: In this module you can find initial table structures, but not final.
There are can be changes in migrations. To see actual fields, constraints, etc.,
see information in databases or look through all migrations for current database
"""

from mephisto.abstractions.databases import local_database_tables

CREATE_IF_NOT_EXISTS_WORKERS_TABLE = """
    CREATE TABLE IF NOT EXISTS workers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        worker_id TEXT UNIQUE,
        is_blocked BOOLEAN default false
    );
"""

CREATE_IF_NOT_EXISTS_MIGRATIONS_TABLE = local_database_tables.CREATE_IF_NOT_EXISTS_MIGRATIONS_TABLE
