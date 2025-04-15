# 🔐 Onchain Escrow Service

A simple on-chain escrow system that ensures funds are held securely between buyer and seller until successful service delivery.

---

## 🧱 Smart Contract

- Buyer deploys and funds the contract.
- Seller waits for buyer to release funds.
- Arbiter can refund the buyer if needed.

---

## 🐍 Python Scripts

- `deploy_escrow.py` – Deploys the contract.
- `interact_escrow.py` – Handles release and refund interactions.
- `Escrow_abi.json` – ABI required to interact via web3.py.

---

## 🧪 How to Use

1. Compile `Escrow.sol` using Remix or Hardhat.
2. Paste ABI and Bytecode to corresponding files.
3. Run deployment script.
4. Run `release()` or `refund()` functions as needed.

---

## ⚖️ Roles

- `buyer`: deploys and funds the contract.
- `seller`: receives funds after approval.
- `arbiter`: trusted 3rd party who can refund if dispute occurs.

---

## 🔐 Security Notes

- Only arbiter can issue refund.
- Only buyer can release funds.
- Once released/refunded, contract is closed.

---

## 📌 Possible Extensions

- UI for users to deploy and manage escrows.
- Multi-signature approval logic.
- Dispute resolution module.
