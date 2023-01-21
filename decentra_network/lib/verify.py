#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import json
import os
import sys

from hashlib import sha256


sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from decentra_network.wallet.ellipticcurve.ecdsa import Ecdsa
from decentra_network.wallet.wallet_import import wallet_import
from decentra_network.wallet.ellipticcurve.publicKey import PublicKey

from decentra_network.config import SIGNS_PATH


from decentra_network.lib.config_system import get_config

from decentra_network.wallet.ellipticcurve.publicKey import PublicKey
from decentra_network.wallet.ellipticcurve.signature import Signature


def verify(path: str) -> bool:
    """
    Verifies the signature of the sign file.

    Args:
        path (str): Path of the sign file
    """
    sign_json = None
    os.chdir(get_config()["main_folder"])
    with open(path, "r") as sign_file:
        sign_json = json.load(sign_file)

    if sign_json is None:
        return False

    return Ecdsa.verify(
        sign_json["data"],
        Signature.fromBase64(sign_json["signature"]),
        PublicKey.fromPem(sign_json["publickey"]),
    )


if __name__ == "__main__":
    from decentra_network.lib.sign import sign
    print(verify(sign("Onur Atakan", "123")))
