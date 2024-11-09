// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

contract Demo {

    // State variable to store the balance
    uint private newbal = 3500;

    // Function to deposit money
    function deposit(uint x) public {
        newbal += x;
    }

    // Function to withdraw money, reverts if insufficient balance
    function withdraw(uint x) public {
        if (newbal < x) {
            revert("Insufficient balance");
        }
        newbal -= x;
    }

    // Function to show the current balance
    function show() public view returns (uint) {
        return newbal;
    }
}