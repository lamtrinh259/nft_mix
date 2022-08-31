#!/usr/bin/python3
from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import (
    get_account,
    get_breed,
    fund_with_link,
    listen_for_event,
)
import time
from web3 import Web3


def main():
    # dev = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    fund_with_link(advanced_collectible.address, amount=Web3.toWei(0.1, "ether"))
    transaction = advanced_collectible.createCollectible({"from": account})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    # time.sleep(35)
    print("Collectible created!")
    # listen_for_event(
    #     advanced_collectible, "ReturnedCollectible", timeout=200, poll_interval=10
    # )
    # requestId = transaction.events["RequestedCollectible"]["requestId"]
    # token_id = advanced_collectible.requestIdToTokenId(requestId)
    # breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    # print("Dog breed of tokenId {} is {}".format(token_id, breed))
