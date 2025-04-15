from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
contract_address = "0xYourContractAddressHere"

with open("Escrow_abi.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)

buyer = w3.eth.accounts[0]
arbiter = w3.eth.accounts[2]

def release():
    tx = contract.functions.releaseFunds().build_transaction({
        "from": buyer,
        "nonce": w3.eth.get_transaction_count(buyer),
        "gas": 100000,
        "gasPrice": w3.to_wei("20", "gwei")
    })
    signed = w3.eth.account.sign_transaction(tx, private_key="0xYourPrivateKeyHere")
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print("Released funds:", tx_hash.hex())

def refund():
    tx = contract.functions.refundBuyer().build_transaction({
        "from": arbiter,
        "nonce": w3.eth.get_transaction_count(arbiter),
        "gas": 100000,
        "gasPrice": w3.to_wei("20", "gwei")
    })
    signed = w3.eth.account.sign_transaction(tx, private_key="0xYourArbiterKeyHere")
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print("Refunded buyer:", tx_hash.hex())
