// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MarksManagement {

    // Define owner address
    address owner;

    // Struct to store student information
    struct Student {
        int ID;
        string fName;
        string lName;
        int marks;
    }

    // Counter for the number of students
    int public stdCount = 0;

    // Mapping to store student records
    mapping(int => Student) public stdRecords;

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to add new student records
    function addNewRecords(int _ID, string memory _fName, string memory _lName, int _marks) public onlyOwner {
        stdCount = stdCount + 1;
        stdRecords[stdCount] = Student(_ID, _fName, _lName, _marks);
    }

    // Function to add bonus marks to the last added student
    function bonusMarks(int _bonus) public onlyOwner {
        stdRecords[stdCount].marks = stdRecords[stdCount].marks + _bonus;
    }
}
