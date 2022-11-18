#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import unittest

from decentra_network.accounts.account import Account
from decentra_network.accounts.get_accounts import GetAccounts
from decentra_network.accounts.get_balance import GetBalance
from decentra_network.accounts.get_sequance_number import GetSequanceNumber
from decentra_network.accounts.save_accounts import SaveAccounts
from decentra_network.blockchain.block.block_main import Block
from decentra_network.blockchain.block.save_block import SaveBlock
from decentra_network.lib.clean_up import CleanUp_tests


class Test_Accounts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        CleanUp_tests()

    def test_dumb_account(self):

        new_account = Account("test_account", 1, 1)

        dumped_account = new_account.dump_json()

        the_json = {
            "address": "test_account",
            "balance": 1,
            "sequence_number": 1,
        }

        self.assertEqual(dumped_account, the_json)

    def test_load_accounts(self):

        the_json = {
            "address": "test_account",
            "balance": 1,
            "sequence_number": 1,
        }

        loaded_account = Account.load_json(the_json)

        loaded_account_json = loaded_account.dump_json()

        self.assertEqual(loaded_account_json, the_json)

    def test_get_hash(self):

        the_account = Account("test_account", 1, 1)

        the_hash = "7fe8746bb0feae44e73aa4e6182e3ca577c4a5d5e219cd468adafd2ec4086550"

        the_account_hash = the_account.get_hash()

        self.assertEqual(the_hash, the_account_hash)

    def test_string_account(self):

        the_account = Account("test_account", 1, 1)

        account_string = "test_account"

        the_account_string = str(the_account)

        self.assertEqual(account_string, the_account_string)

    def test_GetBalance_not_list_account(self):

        the_account = Account("dbd811a12104827240153c8fd2f25a294a851ec8", 10,
                              1)
        the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15,
                                1)
        the_account_3 = Account("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 20,
                                1)

        temp_path = "db/test_GetBalance_not_list_account.db"

        SaveAccounts(the_account, temp_path)
        SaveAccounts(the_account_2, temp_path)
        SaveAccounts(the_account_3, temp_path)

        account_list = GetAccounts(temp_path)

        block = Block("alieren")
        block.minumum_transfer_amount = 5

        result = GetBalance("the_account_4",
                            account_list=account_list,
                            block=block)

        self.assertEqual(result, -5)

    def test_GetBalance(self):

        the_account = Account("dbd811a12104827240153c8fd2f25a294a851ec8", 10,
                              1)
        the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15,
                                1)
        the_account_3 = Account("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 20,
                                1)

        temp_path = "db/test_GetBalance_not_list_account.db"

        SaveAccounts(the_account, temp_path)
        SaveAccounts(the_account_2, temp_path)
        SaveAccounts(the_account_3, temp_path)

        account_list = GetAccounts(temp_path)

        block = Block("alieren")
        block.minumum_transfer_amount = 5

        result = GetBalance("test_account",
                            account_list=account_list,
                            block=block)
        self.assertEqual(result, 5)
        result_2 = GetBalance("test_account_2",
                              account_list=account_list,
                              block=block)
        self.assertEqual(result_2, 10)
        result_3 = GetBalance("test_account_3",
                              account_list=account_list,
                              block=block)
        self.assertEqual(result_3, 15)

    def test_GetBalance_non_block(self):

        the_account = Account("dbd811a12104827240153c8fd2f25a294a851ec8", 10,
                              1)
        the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15,
                                1)
        the_account_3 = Account("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 20,
                                1)

        temp_path = "db/test_GetBalance_non_block_account.db"

        SaveAccounts(the_account, temp_path)
        SaveAccounts(the_account_2, temp_path)
        SaveAccounts(the_account_3, temp_path)

        account_list = GetAccounts(temp_path)

        block = Block("alieren")
        block.minumum_transfer_amount = 5
        custom_TEMP_BLOCK_PATH = "db/test_GetBalance_non_block.db"
        SaveBlock(block, custom_TEMP_BLOCK_PATH)

        result = GetBalance(
            "test_account",
            account_list=account_list,
            custom_TEMP_BLOCK_PATH=custom_TEMP_BLOCK_PATH,
        )
        self.assertEqual(result, 5)
        result_2 = GetBalance(
            "test_account_2",
            account_list=account_list,
            custom_TEMP_BLOCK_PATH=custom_TEMP_BLOCK_PATH,
        )
        self.assertEqual(result_2, 10)
        result_3 = GetBalance(
            "test_account_3",
            account_list=account_list,
            custom_TEMP_BLOCK_PATH=custom_TEMP_BLOCK_PATH,
        )
        self.assertEqual(result_3, 15)

    def test_GetBalance_non_block_non_record(self):

        the_account = Account("dbd811a12104827240153c8fd2f25a294a851ec8", 10,
                              1)
        the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15,
                                1)
        the_account_3 = Account("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 20,
                                1)

        temp_path = "db/test_GetBalance_not_list_account.db"

        SaveAccounts(the_account, temp_path)
        SaveAccounts(the_account_2, temp_path)
        SaveAccounts(the_account_3, temp_path)

        account_list = GetAccounts(temp_path)

        block = Block("alieren")
        block.minumum_transfer_amount = 5
        custom_TEMP_BLOCK_PATH = "db/test_GetBalance_non_block_no_record.db"

        result = GetBalance(
            "test_account",
            account_list=account_list,
            custom_TEMP_BLOCK_PATH=custom_TEMP_BLOCK_PATH,
        )
        self.assertEqual(result, None)
        result_2 = GetBalance(
            "test_account_2",
            account_list=account_list,
            custom_TEMP_BLOCK_PATH=custom_TEMP_BLOCK_PATH,
        )
        self.assertEqual(result_2, None)
        result_3 = GetBalance(
            "test_account_3",
            account_list=account_list,
            custom_TEMP_BLOCK_PATH=custom_TEMP_BLOCK_PATH,
        )
        self.assertEqual(result_3, None)

    def test_GetSequanceNumber_not_list_account(self):

        the_account = Account("dbd811a12104827240153c8fd2f25a294a851ec8", 10,
                              1)
        the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15,
                                2)
        the_account_3 = Account("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 20,
                                3)
        temp_path = "db/test_GetSequanceNumber_not_list_account.db"

        SaveAccounts(the_account, temp_path)
        SaveAccounts(the_account_2, temp_path)
        SaveAccounts(the_account_3, temp_path)

        account_list = GetAccounts(temp_path)
        result = GetSequanceNumber("onuratakan", account_list=account_list)

        self.assertEqual(result, 0)

    def test_GetSequanceNumber(self):

        the_account = Account("dbd811a12104827240153c8fd2f25a294a851ec8", 10,
                              1)
        the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15,
                                2)
        the_account_3 = Account("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 20,
                                3)

        temp_path = "db/test_GetSequanceNumber.db"

        SaveAccounts(the_account, temp_path)
        SaveAccounts(the_account_2, temp_path)
        SaveAccounts(the_account_3, temp_path)

        account_list = GetAccounts(temp_path)

        result = GetSequanceNumber("test_account", account_list=account_list)
        self.assertEqual(result, 1)
        result_2 = GetSequanceNumber("test_account_2",
                                     account_list=account_list)
        self.assertEqual(result_2, 2)
        result_3 = GetSequanceNumber("test_account_3",
                                     account_list=account_list)
        self.assertEqual(result_3, 3)

    def test_SaveAccounts_GetAccounts(self):

        the_account = Account("dbd811a12104827240153c8fd2f25a294a851ec8", 10,
                              1)
        the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15,
                                2)
        the_account_3 = Account("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 20,
                                3)

        temp_path = "db/test_SaveAccounts_GetAccounts.db"

        SaveAccounts(the_account, temp_path)
        SaveAccounts(the_account_2, temp_path)
        SaveAccounts(the_account_3, temp_path)

        result = GetAccounts(temp_path)
        result.execute("SELECT * FROM account_list")
        result_list = result.fetchall()
        account_list = [
            ("dbd811a12104827240153c8fd2f25a294a851ec8", 1, 10),
            ("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 2, 15),
            ("7340ac0cdf3f7b59cba4ec6348ee8e41d0c24ef1", 3, 20),
        ]
        self.assertEqual(len(result_list), len(account_list))
        for i in range(3):
            self.assertEqual(result_list[i][0], account_list[i][0])
            self.assertEqual(result_list[i][1], account_list[i][1])
            self.assertEqual(result_list[i][2], account_list[i][2])


unittest.main(exit=False)
