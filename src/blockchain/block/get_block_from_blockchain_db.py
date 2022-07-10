#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from accounts.get_accounts import GetAccounts
from blockchain.block.blocks_hash import GetBlockshash
from blockchain.block.blocks_hash import GetBlockshash_part
from blockchain.block.get_block import GetBlock
from config import BLOCKS_PATH


def GetBlockstoBlockchainDB(
    sequance_number,
    custom_BLOCKS_PATH=None,
    custom_TEMP_ACCOUNTS_PATH=None,
    custom_TEMP_BLOCKSHASH_PATH=None,
    custom_TEMP_BLOCKSHASH_PART_PATH=None,
):
    """
    Gets the block from the blockchain database
    """
    try:
        the_BLOCKS_PATH = (
            BLOCKS_PATH if custom_BLOCKS_PATH is None else custom_BLOCKS_PATH
        )
        the_block = GetBlock((the_BLOCKS_PATH + str(sequance_number) + ".block.json"))
        the_accounts = GetAccounts(
            (the_BLOCKS_PATH + str(sequance_number) + ".accounts.json")
        )
        the_blockshash = GetBlockshash(
            the_BLOCKS_PATH + str(sequance_number) + ".blockshash.json"
        )
        the_blockshashpart = GetBlockshash_part(
            the_BLOCKS_PATH + str(sequance_number) + ".blockshashpart.json"
        )

        return [the_block, the_accounts, the_blockshash, the_blockshashpart]
    except FileNotFoundError:
        return False
