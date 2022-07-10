#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import os
from hashlib import sha256

from config import PENDING_TRANSACTIONS_PATH
from lib.config_system import get_config


def DeletePending(tx):
    os.chdir(get_config()["main_folder"])
    file_name = sha256((tx.signature).encode("utf-8")).hexdigest()
    for entry in os.scandir(PENDING_TRANSACTIONS_PATH):
        if entry.name == f"{file_name}.json":
            os.remove(entry.path)
