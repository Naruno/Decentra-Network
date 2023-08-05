---
layout: default
title: Ovenden Incentive Program
parent: Baklava TestNet
nav_order: 2
---

# Ovenden Incentive Program

In Baklava we are introduce an incentive for testing our official applications and after all the Integration library. You can get your incentive with this document.

## Requirements
- You should have an registered baklava user. If you dont have you can register via [this link](https://naruno.org/baklava-testnet/).


## Application 1: Address Ping System

### What is Address Ping System?
[Address Ping System](https://github.com/Naruno/Address-Ping-System) (APS) is a tool designed to check the online status of servers associated with blockchain addresses in Naruno. With APS, you can ensure that the servers you want to communicate with are online and reachable before sending any messages or making any transactions.

### Installation
You can install APS via this command:
```console
pip3 install address_ping_system
```

### Usage
You should send an ping to our official address to get your incentive:

* Please give an free port for APS. You can set this port via `--port` argument. If you dont set this argument APS will use 4444 port.

```console
aps --password YourWalletPass --port 4444 ping c923c646f2d73fcb8f626afacb1a0ade8d98954a
```

*Then wait for 5 minutes.


{: .highlight }

> If you get the `True` message you will get your incentive. Don't sent twice time because everyone can get only one incentive.

{: .highlight }

> If you can get the `True` message and you are an registered baklava user and you didnt send multiple time just close application with `Ctrl+C` and try again after 5 minutes.


### Controlling Your Incentive
We will set your incentives as global in all networks. But the loads are take time. We will notificate on [Discord](https://discord.gg/Vpn2tfEEWc). After loading you can check your incentive via this command:

```console
narunocli --getbalance
```