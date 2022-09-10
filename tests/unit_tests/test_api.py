#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import contextlib
import copy
import json
import os
import sys
import time
from urllib import response

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import threading
import unittest
import urllib

import requests

import decentra_network
from decentra_network.accounts.account import Account
from decentra_network.accounts.get_accounts import GetAccounts
from decentra_network.accounts.get_balance import GetBalance
from decentra_network.accounts.save_accounts import SaveAccounts
from decentra_network.api.main import start
from decentra_network.blockchain.block.block_main import Block
from decentra_network.blockchain.block.save_block import SaveBlock
from decentra_network.config import (
    CONNECTED_NODES_PATH, LOADING_ACCOUNTS_PATH, LOADING_BLOCK_PATH,
    LOADING_BLOCKSHASH_PART_PATH, LOADING_BLOCKSHASH_PATH,
    MY_TRANSACTION_EXPORT_PATH, PENDING_TRANSACTIONS_PATH, TEMP_ACCOUNTS_PATH,
    TEMP_BLOCK_PATH, TEMP_BLOCKSHASH_PART_PATH, TEMP_BLOCKSHASH_PATH)
from decentra_network.lib.clean_up import CleanUp_tests
from decentra_network.lib.config_system import get_config
from decentra_network.lib.settings_system import (save_settings,
                                                  t_mode_settings,
                                                  the_settings)
from decentra_network.node.server.server import server
from decentra_network.node.unl import Unl
from decentra_network.transactions.my_transactions.get_my_transaction import \
    GetMyTransaction
from decentra_network.transactions.my_transactions.save_my_transaction import \
    SaveMyTransaction
from decentra_network.transactions.my_transactions.save_to_my_transaction import \
    SavetoMyTransaction
from decentra_network.transactions.pending.delete_pending import DeletePending
from decentra_network.transactions.pending.get_pending import GetPendingLen
from decentra_network.transactions.transaction import Transaction
from decentra_network.wallet.ellipticcurve.get_saved_wallet import \
    get_saved_wallet
from decentra_network.wallet.ellipticcurve.save_wallet_list import \
    save_wallet_list
from decentra_network.wallet.ellipticcurve.wallet_create import wallet_create
from decentra_network.wallet.print_wallets import print_wallets

decentra_network.api.main.custom_block = Block("Onur")
decentra_network.api.main.custom_current_time = int(time.time()) + 25
decentra_network.api.main.custom_sequence_number = 0
decentra_network.api.main.custom_balance = 100000

decentra_network.api.main.custom_TEMP_BLOCK_PATH = "db/test_API_BLOCK_PATH.json"
decentra_network.api.main.custom_TEMP_ACCOUNTS_PATH = "db/test_API_ACCOUNTS_PATH.json"
decentra_network.api.main.custom_TEMP_BLOCKSHASH_PATH = (
    "db/test_API_BLOCKSHASH_PATH.json")
decentra_network.api.main.custom_TEMP_BLOCKSHASH_PART_PATH = (
    "db/test_API_BLOCKSHASH_PART_PATH.json")

the_account_2 = Account("15562b06dc6b1acd6e8c86031e564e0c451c7a73", 15, 1)
temp_path = "db/test_API.db"
SaveAccounts(the_account_2, temp_path)

decentra_network.api.main.account_list = GetAccounts(temp_path)

decentra_network.api.main.custom_wallet = "test_account_2"


def perpetual_time_test():
    os.chdir(get_config()["main_folder"])
    with open("test_block_get_page_off_test.txt", "w") as f:
        f.write("Hello World")


decentra_network.api.main.custom_consensus_trigger = perpetual_time_test


class Test_API(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        CleanUp_tests()
        decentra_network.api.main.account_list = GetAccounts(temp_path)

        cls.custom_TEMP_BLOCK_PATH0 = TEMP_BLOCK_PATH.replace(
            ".json", "_0.json").replace("temp_", "test_temp_")
        cls.custom_TEMP_BLOCK_PATH1 = TEMP_BLOCK_PATH.replace(
            ".json", "_1.json").replace("temp_", "test_temp_")
        cls.custom_TEMP_BLOCK_PATH2 = TEMP_BLOCK_PATH.replace(
            ".json", "_2.json").replace("temp_", "test_temp_")
        cls.custom_LOADING_BLOCK_PATH0 = LOADING_BLOCK_PATH.replace(
            ".json", "_0.json").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_BLOCK_PATH1 = LOADING_BLOCK_PATH.replace(
            ".json", "_1.json").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_BLOCK_PATH2 = LOADING_BLOCK_PATH.replace(
            ".json", "_2.json").replace("loading_", "test_loading_temp_")

        cls.custom_TEMP_ACCOUNTS_PATH0 = TEMP_ACCOUNTS_PATH.replace(
            ".db", "_0.db").replace("temp_", "test_temp_")
        cls.custom_TEMP_ACCOUNTS_PATH1 = TEMP_ACCOUNTS_PATH.replace(
            ".db", "_1.db").replace("temp_", "test_temp_")
        cls.custom_TEMP_ACCOUNTS_PATH2 = TEMP_ACCOUNTS_PATH.replace(
            ".db", "_2.db").replace("temp_", "test_temp_")
        cls.custom_LOADING_ACCOUNTS_PATH0 = LOADING_ACCOUNTS_PATH.replace(
            ".db", "_0.db").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_ACCOUNTS_PATH1 = LOADING_ACCOUNTS_PATH.replace(
            ".db", "_1.db").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_ACCOUNTS_PATH2 = LOADING_ACCOUNTS_PATH.replace(
            ".db", "_2.db").replace("loading_", "test_loading_temp_")

        cls.custom_TEMP_BLOCKSHASH_PATH0 = TEMP_BLOCKSHASH_PATH.replace(
            ".json", "_0.json").replace("temp_", "test_temp_")
        cls.custom_TEMP_BLOCKSHASH_PATH1 = TEMP_BLOCKSHASH_PATH.replace(
            ".json", "_1.json").replace("temp_", "test_temp_")
        cls.custom_TEMP_BLOCKSHASH_PATH2 = TEMP_BLOCKSHASH_PATH.replace(
            ".json", "_2.json").replace("temp_", "test_temp_")
        cls.custom_LOADING_BLOCKSHASH_PATH0 = LOADING_BLOCKSHASH_PATH.replace(
            ".json", "_0.json").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_BLOCKSHASH_PATH1 = LOADING_BLOCKSHASH_PATH.replace(
            ".json", "_1.json").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_BLOCKSHASH_PATH2 = LOADING_BLOCKSHASH_PATH.replace(
            ".json", "_2.json").replace("loading_", "test_loading_temp_")

        cls.custom_TEMP_BLOCKSHASH_PART_PATH0 = TEMP_BLOCKSHASH_PART_PATH.replace(
            ".json", "_0.json").replace("temp_", "test_temp_")
        cls.custom_TEMP_BLOCKSHASH_PART_PATH1 = TEMP_BLOCKSHASH_PART_PATH.replace(
            ".json", "_1.json").replace("temp_", "test_temp_")
        cls.custom_TEMP_BLOCKSHASH_PART_PATH2 = TEMP_BLOCKSHASH_PART_PATH.replace(
            ".json", "_2.json").replace("temp_", "test_temp_")
        cls.custom_LOADING_BLOCKSHASH_PART_PATH0 = LOADING_BLOCKSHASH_PART_PATH.replace(
            ".json", "_0.json").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_BLOCKSHASH_PART_PATH1 = LOADING_BLOCKSHASH_PART_PATH.replace(
            ".json", "_1.json").replace("loading_", "test_loading_temp_")
        cls.custom_LOADING_BLOCKSHASH_PART_PATH2 = LOADING_BLOCKSHASH_PART_PATH.replace(
            ".json", "_2.json").replace("loading_", "test_loading_temp_")

        cls.custom_CONNECTED_NODES_PATH0 = CONNECTED_NODES_PATH.replace(
            "connected_nodes", "connected_nodes_test_0")
        cls.custom_CONNECTED_NODES_PATH1 = CONNECTED_NODES_PATH.replace(
            "connected_nodes", "connected_nodes_test_1")
        cls.custom_CONNECTED_NODES_PATH2 = CONNECTED_NODES_PATH.replace(
            "connected_nodes", "connected_nodes_test_2")

        cls.custom_PENDING_TRANSACTIONS_PATH0 = PENDING_TRANSACTIONS_PATH.replace(
            "pending_transactions", "pending_transactions_test_0")
        cls.custom_PENDING_TRANSACTIONS_PATH1 = PENDING_TRANSACTIONS_PATH.replace(
            "pending_transactions", "pending_transactions_test_1")
        cls.custom_PENDING_TRANSACTIONS_PATH2 = PENDING_TRANSACTIONS_PATH.replace(
            "pending_transactions", "pending_transactions_test_2")

        cls.node_0 = server(
            "127.0.0.1",
            10000,
            save_messages=True,
            custom_TEMP_BLOCK_PATH=cls.custom_TEMP_BLOCK_PATH0,
            custom_LOADING_BLOCK_PATH=cls.custom_LOADING_BLOCK_PATH0,
            custom_TEMP_ACCOUNTS_PATH=cls.custom_TEMP_ACCOUNTS_PATH0,
            custom_LOADING_ACCOUNTS_PATH=cls.custom_LOADING_ACCOUNTS_PATH0,
            custom_TEMP_BLOCKSHASH_PATH=cls.custom_TEMP_BLOCKSHASH_PATH0,
            custom_LOADING_BLOCKSHASH_PATH=cls.custom_LOADING_BLOCKSHASH_PATH0,
            custom_TEMP_BLOCKSHASH_PART_PATH=cls.
            custom_TEMP_BLOCKSHASH_PART_PATH0,
            custom_LOADING_BLOCKSHASH_PART_PATH=cls.
            custom_LOADING_BLOCKSHASH_PART_PATH0,
            custom_CONNECTED_NODES_PATH=cls.custom_CONNECTED_NODES_PATH0,
            custom_PENDING_TRANSACTIONS_PATH=cls.
            custom_PENDING_TRANSACTIONS_PATH0,
            custom_variables=True,
        )

        cls.node_1 = server(
            "127.0.0.1",
            10001,
            save_messages=True,
            custom_TEMP_BLOCK_PATH=cls.custom_TEMP_BLOCK_PATH1,
            custom_LOADING_BLOCK_PATH=cls.custom_LOADING_BLOCK_PATH1,
            custom_TEMP_ACCOUNTS_PATH=cls.custom_TEMP_ACCOUNTS_PATH1,
            custom_LOADING_ACCOUNTS_PATH=cls.custom_LOADING_ACCOUNTS_PATH1,
            custom_TEMP_BLOCKSHASH_PATH=cls.custom_TEMP_BLOCKSHASH_PATH1,
            custom_LOADING_BLOCKSHASH_PATH=cls.custom_LOADING_BLOCKSHASH_PATH1,
            custom_TEMP_BLOCKSHASH_PART_PATH=cls.
            custom_TEMP_BLOCKSHASH_PART_PATH1,
            custom_LOADING_BLOCKSHASH_PART_PATH=cls.
            custom_LOADING_BLOCKSHASH_PART_PATH1,
            custom_CONNECTED_NODES_PATH=cls.custom_CONNECTED_NODES_PATH1,
            custom_PENDING_TRANSACTIONS_PATH=cls.
            custom_PENDING_TRANSACTIONS_PATH1,
            custom_variables=True,
        )
        cls.node_2 = server(
            "127.0.0.1",
            10002,
            save_messages=True,
            custom_TEMP_BLOCK_PATH=cls.custom_TEMP_BLOCK_PATH2,
            custom_LOADING_BLOCK_PATH=cls.custom_LOADING_BLOCK_PATH2,
            custom_TEMP_ACCOUNTS_PATH=cls.custom_TEMP_ACCOUNTS_PATH2,
            custom_LOADING_ACCOUNTS_PATH=cls.custom_LOADING_ACCOUNTS_PATH2,
            custom_TEMP_BLOCKSHASH_PATH=cls.custom_TEMP_BLOCKSHASH_PATH2,
            custom_LOADING_BLOCKSHASH_PATH=cls.custom_LOADING_BLOCKSHASH_PATH2,
            custom_TEMP_BLOCKSHASH_PART_PATH=cls.
            custom_TEMP_BLOCKSHASH_PART_PATH2,
            custom_LOADING_BLOCKSHASH_PART_PATH=cls.
            custom_LOADING_BLOCKSHASH_PART_PATH2,
            custom_CONNECTED_NODES_PATH=cls.custom_CONNECTED_NODES_PATH2,
            custom_PENDING_TRANSACTIONS_PATH=cls.
            custom_PENDING_TRANSACTIONS_PATH2,
            custom_variables=True,
        )
        Unl.save_new_unl_node(cls.node_0.id)
        Unl.save_new_unl_node(cls.node_1.id)
        Unl.save_new_unl_node(cls.node_2.id)
        time.sleep(2)
        cls.node_0.connect("127.0.0.1", 10001)
        cls.node_0.connect("127.0.0.1", 10002)
        time.sleep(2)
        cls.node_2.connect("127.0.0.1", 10001)

        print(cls.node_0.clients)
        print(cls.node_1.clients)
        print(cls.node_2.clients)
        print("started")

        backup = sys.argv
        sys.argv = [sys.argv[0]]

        cls.result = start(port=7777, test=True)
        cls.proc = threading.Thread(target=cls.result.run)
        cls.proc.start()

        sys.argv = backup
        decentra_network.api.main.custom_server = cls.node_0
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.node_0.stop()
        cls.node_1.stop()
        cls.node_2.stop()

        time.sleep(2)

        cls.node_1.join()
        cls.node_2.join()
        cls.node_0.join()

        for a_client in cls.node_0.clients:
            the_dict = {}
            the_dict["id"] = a_client.id
            the_dict["host"] = a_client.host
            the_dict["port"] = a_client.port
            cls.node_0.connected_node_delete(the_dict)

        for a_client in cls.node_1.clients:
            the_dict = {}
            the_dict["id"] = a_client.id
            the_dict["host"] = a_client.host
            the_dict["port"] = a_client.port
            cls.node_1.connected_node_delete(the_dict)

        for a_client in cls.node_2.clients:
            the_dict = {}
            the_dict["id"] = a_client.id
            the_dict["host"] = a_client.host
            the_dict["port"] = a_client.port
            cls.node_2.connected_node_delete(the_dict)

        cls.result.close()

        CleanUp_tests()

    def test_print_wallets_page(self):
        response = urllib.request.urlopen("http://localhost:7777/wallet/print")
        result = str(json.loads(response.read())).replace("'", """\"""")

        data = str(json.dumps(print_wallets()))

        self.assertEqual(result, data)

    def test_change_wallet_page(self):
        backup_settings = the_settings()

        original_saved_wallets = get_saved_wallet()
        save_wallet_list({})

        password = "123"

        temp_private_key = wallet_create(password)
        temp_private_key_2 = wallet_create(password)

        response = urllib.request.urlopen(
            "http://localhost:7777/wallet/change/1")
        result = str(json.loads(response.read())).replace("'", """\"""")

        data = str(json.dumps(print_wallets()))

        self.assertEqual(result, data)

        control = False
        if "CURRENTLY USED" in print_wallets()[1]:
            control = True

        self.assertTrue(control)
        save_settings(backup_settings)
        save_wallet_list(original_saved_wallets)

    def test_create_wallet_page(self):
        backup_settings = the_settings()

        original_saved_wallets = get_saved_wallet()
        save_wallet_list({})

        password = "123"

        response = urllib.request.urlopen(
            f"http://localhost:7777/wallet/create/{password}")
        response = urllib.request.urlopen(
            f"http://localhost:7777/wallet/create/{password}")
        result = str(json.loads(response.read())).replace("'", """\"""")

        data = str(json.dumps(print_wallets()))

        self.assertEqual(result, data)
        self.assertEqual(len(print_wallets()), 2)

        save_settings(backup_settings)
        save_wallet_list(original_saved_wallets)

    def test_delete_wallets_page(self):
        backup_settings = the_settings()

        original_saved_wallets = get_saved_wallet()
        save_wallet_list({})

        password = "123"

        response = urllib.request.urlopen(
            f"http://localhost:7777/wallet/create/{password}")
        response = urllib.request.urlopen(
            f"http://localhost:7777/wallet/create/{password}")
        response = urllib.request.urlopen(
            "http://localhost:7777/wallet/change/1")
        response = urllib.request.urlopen(
            f"http://localhost:7777/wallet/delete")
        result = str(json.loads(response.read())).replace("'", """\"""")

        data = str(json.dumps(print_wallets()))

        self.assertEqual(result, data)
        self.assertEqual(len(print_wallets()), 1)

        save_settings(backup_settings)
        save_wallet_list(original_saved_wallets)

    def test_send_coin_data_page(self):

        backup = GetMyTransaction()
        backup_settings = the_settings()

        original_saved_wallets = get_saved_wallet()
        save_wallet_list({})
        SaveMyTransaction([])

        password = "123"
        response = urllib.request.urlopen(
            f"http://localhost:7777/wallet/create/{password}")
        request_body = {
            "data": "<data>",
            "to_user": "<address>",
            "amount": 5000,
            "password": password,
        }
        response = requests.post("http://localhost:7777/send/",
                                 data=request_body)
        response_result = response.text
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(response_result)
        time.sleep(3)

        self.assertNotEqual(response_result, "false")
        the_tx = Transaction.load_json(json.loads(response_result))
        self.assertEqual(the_tx.data, "<data>")

        new_my_transactions = GetMyTransaction()
        self.assertEqual(len(new_my_transactions), 1)

        DeletePending(the_tx)
        SaveMyTransaction(backup)
        save_settings(backup_settings)
        save_wallet_list(original_saved_wallets)

    def test_balance_wallets_page(self):
        response = urllib.request.urlopen(
            "http://localhost:7777/wallet/balance")
        response_result = response.read()
        the_balance_int = float(
            (response_result.decode("utf-8")).replace("\n", ""))

        self.assertEqual(
            the_balance_int,
            float(
                GetBalance(
                    decentra_network.api.main.custom_block,
                    decentra_network.api.main.custom_wallet,
                    account_list=decentra_network.api.main.account_list,
                )),
        )

    def test_node_start_page(self):
        response = urllib.request.urlopen(
            "http://localhost:7777/node/start/localhost/7778")
        first_len = len(self.node_0.clients)
        time.sleep(2)
        self.node_0.connect("localhost", 7778)
        time.sleep(2)
        second_len = len(self.node_0.clients)
        self.assertNotEqual(first_len, second_len)

    def test_node_stop_page(self):
        response = urllib.request.urlopen(
            "http://localhost:7777/node/start/localhost/7779")
        time.sleep(2)
        response = urllib.request.urlopen("http://localhost:7777/node/stop")
        time.sleep(2)
        first_len = len(self.node_0.clients)
        with contextlib.suppress(ConnectionRefusedError):
            self.node_0.connect("localhost", 7779)
        time.sleep(2)
        second_len = len(self.node_0.clients)
        self.assertEqual(first_len, second_len)

    def test_node_connect_page(self):
        response = urllib.request.urlopen(
            "http://localhost:7777/node/start/localhost/7780")
        first_len = len(self.node_0.clients)
        time.sleep(2)
        response = urllib.request.urlopen(
            "http://localhost:7777/node/connect/127.0.0.1/10000")
        time.sleep(2)
        second_len = len(self.node_0.clients)
        self.assertNotEqual(first_len, second_len)

    def test_node_connectmixdb_page(self):
        first_len_0 = len(self.node_0.clients)
        first_len_1 = len(self.node_1.clients)
        first_len_2 = len(self.node_2.clients)

        temp_node = server("127.0.0.1", 10058)
        backup_1 = copy.copy(decentra_network.api.main.custom_server)
        backup_2 = copy.copy(
            decentra_network.api.main.custom_CONNECTED_NODES_PATH)
        decentra_network.api.main.custom_server = temp_node
        decentra_network.api.main.custom_CONNECTED_NODES_PATH = (
            self.node_0.CONNECTED_NODES_PATH)
        response = urllib.request.urlopen(
            "http://localhost:7777/node/connectmixdb")
        time.sleep(2)

        second_len_0 = len(self.node_0.clients)
        second_len_1 = len(self.node_1.clients)
        second_len_2 = len(self.node_2.clients)
        self.assertEqual(first_len_0, second_len_0)
        self.assertNotEqual(first_len_1, second_len_1)
        self.assertNotEqual(first_len_2, second_len_2)
        temp_node.stop()
        time.sleep(2)
        temp_node.join()

        decentra_network.api.main.custom_server = backup_1
        decentra_network.api.main.custom_CONNECTED_NODES_PATH = backup_2

    def test_node_newunl_page(self):
        key = f"onuratakan{str(int(time.time()))}"
        response = urllib.request.urlopen(
            f"http://localhost:7777/node/newunl/?{key}")
        self.assertTrue(Unl.node_is_unl(key))
        Unl.unl_node_delete(key)

    def test_node_id_page(self):
        response = urllib.request.urlopen(f"http://localhost:7777/node/id")
        self.assertEqual(
            ((((response.read()).decode("utf-8")).replace("'", "")).replace(
                """\"""", "")).replace("\n", ""),
            server.id,
        )

    def test_settings_test_on_off_page(self):
        temp_settings = the_settings()
        changed_value = "on" if temp_settings["test_mode"] is False else "off"
        response = urllib.request.urlopen(
            f"http://localhost:7777/settings/test/{changed_value}")
        new_settings = the_settings()
        expected_alue = True if changed_value == "on" else False
        self.assertEqual(new_settings["test_mode"], expected_alue)

        default = "off" if temp_settings["test_mode"] is False else "on"
        response = urllib.request.urlopen(
            f"http://localhost:7777/settings/test/{default}")

        new_settings = the_settings()
        self.assertEqual(new_settings["test_mode"], temp_settings["test_mode"])

    def test_settings_debug_on_off_page(self):
        temp_settings = the_settings()
        changed_value = "on" if temp_settings["debug_mode"] is False else "off"
        response = urllib.request.urlopen(
            f"http://localhost:7777/settings/debug/{changed_value}")
        new_settings = the_settings()
        expected_alue = True if changed_value == "on" else False
        self.assertEqual(new_settings["debug_mode"], expected_alue)

        default = "off" if temp_settings["debug_mode"] is False else "on"
        response = urllib.request.urlopen(
            f"http://localhost:7777/settings/debug/{default}")

        new_settings = the_settings()
        self.assertEqual(new_settings["debug_mode"],
                         temp_settings["debug_mode"])

    def test_block_get_page_off_test(self):
        temp_settings = the_settings()
        t_mode_settings(False)
        first_len = len(self.node_0.our_messages)

        response = urllib.request.urlopen("http://localhost:7777/block/get")
        time.sleep(2)
        second_len = len(self.node_0.our_messages)

        self.assertNotEqual(first_len, second_len)

        self.assertEqual(self.node_0.our_messages[-1]["action"],
                         "sendmefullblock")

        t_mode_settings(temp_settings["test_mode"])

    def test_block_get_page(self):

        backup_1 = copy.copy(decentra_network.api.main.custom_TEMP_BLOCK_PATH)
        backup_2 = copy.copy(
            decentra_network.api.main.custom_TEMP_ACCOUNTS_PATH)
        backup_3 = copy.copy(
            decentra_network.api.main.custom_TEMP_BLOCKSHASH_PATH)
        backup_4 = copy.copy(
            decentra_network.api.main.custom_TEMP_BLOCKSHASH_PART_PATH)

        decentra_network.api.main.custom_TEMP_BLOCK_PATH = self.node_0.TEMP_BLOCK_PATH
        decentra_network.api.main.custom_TEMP_ACCOUNTS_PATH = (
            self.node_0.TEMP_ACCOUNTS_PATH)
        decentra_network.api.main.custom_TEMP_BLOCKSHASH_PATH = (
            self.node_0.TEMP_BLOCKSHASH_PATH)
        decentra_network.api.main.custom_TEMP_BLOCKSHASH_PART_PATH = (
            self.node_0.TEMP_BLOCKSHASH_PART_PATH)

        temp_settings = the_settings()
        t_mode_settings(True)

        response = urllib.request.urlopen("http://localhost:7777/block/get")
        time.sleep(2)

        self.assertTrue(os.path.exists("test_block_get_page_off_test.txt"))
        os.remove("test_block_get_page_off_test.txt")

        t_mode_settings(temp_settings["test_mode"])
        decentra_network.api.main.custom_consensus_trigger_result.cancel()

        decentra_network.api.main.custom_TEMP_BLOCK_PATH = backup_1
        decentra_network.api.main.custom_TEMP_ACCOUNTS_PATH = backup_2
        decentra_network.api.main.custom_TEMP_BLOCKSHASH_PATH = backup_3
        decentra_network.api.main.custom_TEMP_BLOCKSHASH_PART_PATH = backup_4

        self.assertEqual(self.node_0.our_messages[-1]["action"],
                         "fullblockshash_part")
        self.assertEqual(self.node_0.our_messages[-1]["byte"], "end")

    def test_export_the_transactions(self):
        custom_MY_TRANSACTION_EXPORT_PATH = MY_TRANSACTION_EXPORT_PATH.replace(
            "my_transaction", "test_export_the_transactions")
        the_transaction_json = {
            "sequance_number": 1,
            "signature":
            "MEUCIHABt7ypkpvFlpqL4SuogwVuzMu2gGynVkrSw6ohZ/GyAiEAg2O3iOei1Ft/vQRpboX7Sm1OOey8a3a67wPJaH/FmVE=",
            "fromUser":
            "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE0AYA7B+neqfUA17wKh3OxC67K8UlIskMm9T2qAR+pl+kKX1SleqqvLPM5bGykZ8tqq4RGtAcGtrtvEBrB9DTPg==",
            "toUser": "onur",
            "data": "blockchain-lab",
            "amount": 5000.0,
            "transaction_fee": 0.02,
            "transaction_time": 1656764224,
        }
        the_transaction = Transaction.load_json(the_transaction_json)
        custom_transactions = [[the_transaction, "validated"]]
        decentra_network.api.main.custom_transactions = custom_transactions
        decentra_network.api.main.custom_MY_TRANSACTION_EXPORT_PATH = (
            custom_MY_TRANSACTION_EXPORT_PATH)
        response = urllib.request.urlopen(
            "http://localhost:7777/export/transactions/csv")
        # read the file and check the content
        with open(custom_MY_TRANSACTION_EXPORT_PATH, "r") as f:
            content = f.read()
            expected_content = """sequance_number,signature,fromUser,toUser,data,amount,transaction_fee,transaction_time,is_valid
1,MEUCIHABt7ypkpvFlpqL4SuogwVuzMu2gGynVkrSw6ohZ/GyAiEAg2O3iOei1Ft/vQRpboX7Sm1OOey8a3a67wPJaH/FmVE=,MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE0AYA7B+neqfUA17wKh3OxC67K8UlIskMm9T2qAR+pl+kKX1SleqqvLPM5bGykZ8tqq4RGtAcGtrtvEBrB9DTPg==,onur,blockchain-lab,5000.0,0.02,1656764224,validated
"""
            self.assertEqual(content, expected_content)

    def test_export_transaction_json_page(self):
        backup = GetMyTransaction()
        new_transaction = Transaction(1, "", "", "", "", 1, 1, 1)
        SavetoMyTransaction(new_transaction, validated=True)

        response = urllib.request.urlopen(
            "http://localhost:7777/export/transactions/json")

        expected_result = "[{sequance_number: 1, signature: , fromUser: , toUser: , data: , amount: 1.0, transaction_fee: 1.0, transaction_time: 1} | True]"

        self.assertEqual(
            str((((response.read()).decode("utf-8")).replace("'", "")).replace(
                """\"""", "")).replace("\n", ""),
            expected_result,
        )

        SaveMyTransaction(backup)

    def test_status_page(self):
        custom_first_block = Block("Onur")
        custom_new_block = Block("Onur")
        custom_new_block.sequance_number += 1
        custom_connections = self.node_0.clients
        the_transaction_json = {
            "sequance_number": 1,
            "signature":
            "MEUCIHABt7ypkpvFlpqL4SuogwVuzMu2gGynVkrSw6ohZ/GyAiEAg2O3iOei1Ft/vQRpboX7Sm1OOey8a3a67wPJaH/FmVE=",
            "fromUser":
            "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE0AYA7B+neqfUA17wKh3OxC67K8UlIskMm9T2qAR+pl+kKX1SleqqvLPM5bGykZ8tqq4RGtAcGtrtvEBrB9DTPg==",
            "toUser": "onur",
            "data": "blockchain-lab",
            "amount": 5000.0,
            "transaction_fee": 0.02,
            "transaction_time": 1656764224,
        }
        the_transaction = Transaction.load_json(the_transaction_json)
        custom_transactions = [[the_transaction, "validated"]]
        custom_new_block.validating_list = [the_transaction]
        decentra_network.api.main.custom_first_block = custom_first_block
        decentra_network.api.main.custom_new_block = custom_new_block
        decentra_network.api.main.custom_connections = custom_connections
        decentra_network.api.main.custom_transactions = custom_transactions
        result = urllib.request.urlopen("http://localhost:7777/status")
        result = json.loads(result.read().decode("utf-8"))
        self.assertEqual(result["status"], "Working")
        self.assertEqual(result["last_transaction_of_block"],
                         str(the_transaction.dump_json()))
        self.assertEqual(
            result["transactions_of_us"],
            str([
                f"{str(i[0].__dict__)} | {str(i[1])}"
                for i in custom_transactions
            ]),
        )

    def test_404_page(self):
        response = requests.get("http://localhost:7777/404")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, '"404"\n')

    def test_405_page(self):
        response = requests.post(
            "http://localhost:7777/status", data={"data": "test"})
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.text, '"405"\n')

    def test_500_page(self):
        response = requests.post(
            "http://localhost:7777/send/", data={"data": "test"})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.text, '"500"\n')


unittest.main(exit=False)
