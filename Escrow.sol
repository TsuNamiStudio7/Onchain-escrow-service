// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Escrow {
    address public buyer;
    address public seller;
    address public arbiter;
    uint256 public amount;
    bool public isFunded;
    bool public isReleased;
    bool public isRefunded;

    constructor(address _seller, address _arbiter) payable {
        buyer = msg.sender;
        seller = _seller;
        arbiter = _arbiter;
        amount = msg.value;
        isFunded = true;
    }

    modifier onlyArbiter() {
        require(msg.sender == arbiter, "Not authorized");
        _;
    }

    modifier onlyBuyer() {
        require(msg.sender == buyer, "Not authorized");
        _;
    }

    function releaseFunds() public onlyBuyer {
        require(isFunded && !isReleased && !isRefunded, "Invalid state");
        payable(seller).transfer(amount);
        isReleased = true;
    }

    function refundBuyer() public onlyArbiter {
        require(isFunded && !isReleased && !isRefunded, "Invalid state");
        payable(buyer).transfer(amount);
        isRefunded = true;
    }

    function getStatus() external view returns (string memory) {
        if (isReleased) return "Released to Seller";
        if (isRefunded) return "Refunded to Buyer";
        if (isFunded) return "In Escrow";
        return "Not Funded";
    }
}
