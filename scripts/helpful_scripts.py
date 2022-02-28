from decimal import Decimal
from brownie import accounts, network, config, MockV3Aggregator, accounts
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMAL = 8
STARTING_PRICE = 2000000000000000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active in FORKED_LOCAL_ENVIRONMENT:
        return accounts[0]
    else:
        # accounts.add(config["wallets"]["from_key"])
        # return config["wallets"]["from_key"]
        # print(accounts.add(config["wallets"]["from_key"]))
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    account = get_account()
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks")

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMAL, STARTING_PRICE, {"from": account})
        print("Deployed a new Mock because the length of MockV3Aggregator was 0")
    # print("mock aggregator is ", mock_aggregator)
    print("Mock deployed!")

    # print("Mocks deployed on ", mock_aggregator)
