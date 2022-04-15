---
title: Function Test
parent: Systems
nav_order: 3
---

# Using the Docker Test

You must pull images and tag must be decentra-network-api

## Install From Github Packages

`docker pull ghcr.io/decentra-network/api:latest`

## Running Auto Test

`python3 Decentra-Network/tests/functional_tests/docker/test_decentra_network_docker.py`

## Start the Network Only

`python3 Decentra-Network/auto_builders/docker.py -nn 3 -d -i -r -s`

-nn = node number
