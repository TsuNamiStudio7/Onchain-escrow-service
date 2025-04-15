from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

with open("Escrow_abi.json") as f:
    abi = json.load(f)

bytecode = "0xYourCompiledBytecodeHere"

buyer = w3.eth.accounts[0]
seller = w3.eth.accounts[1]
arbiter = w3.eth.accounts[2]

Escrow = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Escrow.constructor(seller, arbiter).build_transaction({
    "from": buyer,
    "value": w3.to_wei(1, "ether"),
    "nonce": w3.eth.get_transaction_count(buyer),
    "gas": 3000000,
    "gasPrice": w3.to_wei("20", "gwei")
})

signed_tx = w3.eth.account.sign_transaction(tx_hash, private_key="0xYourPrivateKeyHere")
tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("Contract deployment sent. Tx hash:", tx.hex())
