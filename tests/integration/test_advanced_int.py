import pytest
from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    listen_for_event,
)
import time
from web3 import Web3


def test_can_create_advanced_collectible_integration(
    get_keyhash,
    chainlink_fee,
):
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        get_keyhash,
        chainlink_fee,
        {"from": get_account(), "gasPrice": Web3.toWei("25", "gwei")},
    )
    get_contract("link_token").transfer(
        advanced_collectible.address, chainlink_fee * 3, {"from": get_account()}
    )
    # Act
    advanced_collectible.createCollectible({"from": get_account()})
    time.sleep(75)
    listen_for_event(
        advanced_collectible, "breedAssigned", timeout=200, poll_interval=10
    )
    # Assert
    assert advanced_collectible.tokenCounter() > 0
