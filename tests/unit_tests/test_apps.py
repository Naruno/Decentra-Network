#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
import time
import unittest

from apps.apps_trigger import AppsTrigger
from blockchain.block.block_main import Block
from lib.config_system import get_config
from transactions.transaction import Transaction



class Test_apps(unittest.TestCase):

    def test_AppsTrigger_App(self):
        block = Block("onur")
        the_transaction = Transaction(1, 1, 1, 1, 1, 1, 1, 1)
        the_transaction.transaction_time = time.time()
        block.validating_list.append(the_transaction)
        AppsTrigger(block)
        time.sleep(2)
        os.chdir(get_config()["main_folder"])
        self.assertTrue(
            os.path.isfile(
                f"apps/testing_app/{block.validating_list[0].transaction_time}.tx"
            ))


unittest.main(exit=False)
