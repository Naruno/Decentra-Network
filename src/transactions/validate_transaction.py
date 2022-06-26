#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


from distutils.log import info
import pickle
import os

from lib.config_system import get_config
from config import MY_TRANSACTION_PATH

from transactions.get_my_transaction import GetMyTransaction
from transactions.save_my_transaction import SaveMyTransaction


def ValidateTransaction(tx):
    """
    Validates the transaction.
    """

    tx_list = GetMyTransaction()
    for i in tx_list:
        if i[0].signature == tx.signature:
            i[1] = True
    SaveMyTransaction(tx_list)
