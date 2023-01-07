#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from decentra_network.blockchain.candidate_block.candidate_block_main import (
    candidate_block,
)
from decentra_network.blockchain.block.block_main import Block
from decentra_network.node.unl import Unl


def GetCandidateBlocks(custom_nodes_list=None, block: Block = None):
    """
    Collects candidate blocks and candidate block hashes
    from connected unl nodes and returns them in the
    candidate_block class
    """

    nodes = (
        Unl.get_as_node_type(Unl.get_unl_nodes())
        if custom_nodes_list is None
        else custom_nodes_list
    )

    the_candidate_blocks = []
    the_candidate_block_hashes = []

    for node in nodes:
        if node.candidate_block is not None:
            the_candidate_blocks.append(node.candidate_block)
        if node.candidate_block_hash is not None:
            the_candidate_block_hashes.append(node.candidate_block_hash)

    if block is not None:
        new_list = []

        signature_list = []

        for element in block.validating_list:
            new_list.append(element.dump_json())
            signature_list.append(element.signature)
        the_candidate_blocks.append(
            {
                "action": "myblock",
                "transaction": new_list,
            })

        the_candidate_block_hashes.append(
            data={
                "action": "myblockhash",
                "hash": block.hash,
            })

    not_none_the_candidate_blocks = []

    for candidate_block in the_candidate_block_hashes:
        if candidate_block["hash"] == None:
            not_none_the_candidate_blocks.append(candidate_block)

    return candidate_block(the_candidate_blocks, not_none_the_candidate_blocks)
