#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import argparse
import json
import os
import random
import sys
import time
import urllib.request


class Decentra_Network_Docker:

    def __init__(self, number_of_nodes=3, number_of_security_circle=1):
        self.number_of_nodes = number_of_nodes - 1
        self.number_of_security_circle = number_of_security_circle
        nodes_list = list(range(self.number_of_nodes))
        self.circles = [
            nodes_list[x:x + (
                (self.number_of_nodes + 1) // self.number_of_security_circle)]
            for x in range(
                0,
                len(nodes_list),
                ((self.number_of_nodes + 1) // self.number_of_security_circle),
            )
        ]

        random_amount = (int(
            10 * (self.number_of_security_circle / self.number_of_nodes))
                         if self.number_of_security_circle != 1 else 0)

        for _ in range(random_amount):
            random_circle = random.randint(0, len(self.circles) - 1)
            random_node = random.randint(0, self.number_of_nodes - 1)
            self.circles[random_circle].append(random_node)

    def start(self):
        time.sleep(self.number_of_nodes)
        self.debug_and_test_mode()
        self.creating_the_wallets()
        self.starting_the_nodest()
        self.unl_nodes_settting()
        self.connecting_the_nodes()
        self.creating_the_block()
        time.sleep(25)

    def install(self):
        self._command_to_system(
            "docker image tag ghcr.io/decentra-network/api decentra-network-api",
            "docker network create --subnet=172.19.0.0/16 dn-net",
        )

        for i in range(self.number_of_nodes):
            os.system(f"docker tag decentra-network-api {i}")

    def delete(self):
        self._command_to_system(
            "docker rm -f $(docker ps -a -q -f ancestor=decentra-network-api)",
            "docker volume rm $(docker volume ls -q -f name=decentra-network)",
        )

        os.system("docker network rm dn-net")

    def _command_to_system(self, first_command: str, second_command: str):
        time.sleep(self.number_of_nodes)
        os.system(first_command)
        os.system(second_command)

    def run(self):
        time.sleep(self.number_of_nodes)
        os.system(
            "docker run -v decentra-network-db:/app/Decentra-Network/decentra_network/db/ -v decentra-network-logs:/app/Decentra-Network/decentra_network/logs/ --network dn-net -p 8000:8000 -p 7999:7999 -dit decentra-network-api"
        )
        for i in range(self.number_of_nodes):
            os.system(
                f"docker run -v decentra-network-db-{i}:/app/Decentra-Network/decentra_network/db/ -v decentra-network-logs-{i}:/app/Decentra-Network/decentra_network/logs/ --network dn-net -p {8100 + i + 1}:8000 -p {8010 + i + 1}:{8010 + i + 1} -dit {i}"
            )

    def debug_and_test_mode(self):
        time.sleep(self.number_of_nodes)
        urllib.request.urlopen("http://localhost:8000/settings/test/on")
        urllib.request.urlopen("http://localhost:8000/settings/debug/on")
        for i in range(self.number_of_nodes):
            urllib.request.urlopen(
                f"http://localhost:{8100 + i + 1}/settings/debug/on")

    def creating_the_wallets(self):
        time.sleep(self.number_of_nodes)
        urllib.request.urlopen("http://localhost:8000/wallet/create/123")

        for i in range(self.number_of_nodes):
            urllib.request.urlopen(
                f"http://localhost:{8100 + i + 1}/wallet/create/123")

    def starting_the_nodest(self):
        time.sleep(self.number_of_nodes)
        urllib.request.urlopen(
            "http://localhost:8000/node/start/172.19.0.2/7999")
        for i in range(self.number_of_nodes):
            urllib.request.urlopen(
                f"http://localhost:{8100 + i + 1}/node/start/172.19.0.{i+3}/{8010 + i + 1}"
            )

    def unl_nodes_settting(self):
        time.sleep(self.number_of_nodes)
        node_id_1 = json.loads(
            urllib.request.urlopen(
                "http://localhost:8000/node/id").read().decode())
        for i in range(self.number_of_nodes):
            urllib.request.urlopen(
                f"http://localhost:{8100 + i + 1}/node/newunl/?{node_id_1}")

        if self.number_of_security_circle == 1:
            for i in range(self.number_of_nodes):
                node_id_2 = json.loads(
                    urllib.request.urlopen(
                        f"http://localhost:{8100 + i + 1}/node/id").read().
                    decode())
                urllib.request.urlopen(
                    f"http://localhost:8000/node/newunl/?{node_id_2}")
                for i_n in range(self.number_of_nodes):
                    if i != i_n:
                        urllib.request.urlopen(
                            f"http://localhost:{8100 + i_n + 1}/node/newunl/?{node_id_2}"
                        )
        else:
            for circle in self.circles:
                for i in circle:
                    node_id_2 = json.loads(
                        urllib.request.urlopen(
                            f"http://localhost:{8100 + i + 1}/node/id").read().
                        decode())
                    urllib.request.urlopen(
                        f"http://localhost:8000/node/newunl/?{node_id_2}")
                    for i_n in circle:
                        if i != i_n:
                            urllib.request.urlopen(
                                f"http://localhost:{8100 + i_n + 1}/node/newunl/?{node_id_2}"
                            )

    def connecting_the_nodes(self):
        time.sleep(self.number_of_nodes)
        for i in range(self.number_of_nodes):
            urllib.request.urlopen(
                f"http://localhost:8000/node/connect/172.19.0.{i+3}/{8010 + i + 1}"
            )
        time.sleep(15)

        if self.number_of_security_circle == 1:
            for i in range(self.number_of_nodes):
                for i_n in range(self.number_of_nodes):
                    if i != i_n:
                        urllib.request.urlopen(
                            f"http://localhost:{8100 + i + 1}/node/connect/172.19.0.{i_n+3}/{8010 + i_n + 1}"
                        )
                time.sleep(15)
        else:
            for circle in self.circles:
                for i in circle:
                    for i_n in circle:
                        if i != i_n:
                            urllib.request.urlopen(
                                f"http://localhost:{8100 + i + 1}/node/connect/172.19.0.{i_n+3}/{8010 + i_n + 1}"
                            )
                    time.sleep(15)

    def creating_the_block(self):
        time.sleep(self.number_of_nodes)
        urllib.request.urlopen("http://localhost:8000/block/get")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=
        "This is an open source decentralized application network. In this network, you can develop and publish decentralized applications."
    )

    parser.add_argument("-nn", "--nodenumber", type=int, help="Node Number")

    parser.add_argument("-scn",
                        "--securitycirclenumber",
                        type=int,
                        help="Security Circle Number")

    parser.add_argument("-i", "--install", action="store_true", help="Install")

    parser.add_argument("-d", "--delete", action="store_true", help="delete")

    parser.add_argument("-r", "--run", action="store_true", help="run")

    parser.add_argument("-s", "--start", action="store_true", help="start")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()

    if args.securitycirclenumber is not None:
        temp_environment = Decentra_Network_Docker(args.nodenumber,
                                                   args.securitycirclenumber)
    else:
        temp_environment = Decentra_Network_Docker(args.nodenumber)

    if args.delete:
        temp_environment.delete()

    if args.install:
        temp_environment.install()

    if args.run:
        temp_environment.run()

    if args.start:
        temp_environment.start()
