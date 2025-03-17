# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Jashanpreet Singh Sidhu

## Assignment
Assignment 1: This task will create essential classes that will be part of a larger system. These classes will implement the concepts covered in Module 01, particularly encapsulation, by using private attributes along with public accessors and mutators. The classes will also undergo extensive unit testing, including the planning of those tests. Remember, the classes developed in this assignment will be used in future tasks, so selecting meaningful identifiers and providing thorough documentation will be crucial as the project evolves throughout the semester.

Assignment 2: This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.

Assignment 3: This assignment will tackle scalability and maintainability issues in the current service charge calculation system. If PiXELL River Financial adds new account types with different charge formulas, problems like bloated subclasses and repeated code could arise. To improve this, the Strategy Pattern will be used to simplify and scale the service charge functionality. Additionally, the Observer Pattern will notify clients of large transactions or when their account balance falls below a minimum threshold.

## Encapsulation
Private Attributes: The use of double underscores (__) makes the account_number, client_number, and balance attributes private, preventing direct access from outside the class.

Public Accessors: Getter methods (@property) allow controlled access to these private attributes, enabling read-only access while maintaining encapsulation.

Methods for Modification: Methods like deposit and withdraw ensure that any changes to the balance are validated, preventing invalid operations (e.g., negative amounts or exceeding the balance).

Data Integrity: Encapsulation ensures the internal state of the object remains consistent by restricting direct manipulation and enforcing validation through methods.

## Polymorphism
Polymorphism in the BankAccount subclasses is achieved through method overriding. The BankAccount class defines an abstract method get_service_charges(), which is implemented differently in each subclass (e.g., ChequingAccount, SavingsAccount, InvestmentAccount). Each subclass provides its own logic for calculating service charges, but the method signature remains the same.


## Strategy Pattern
In this application, the Strategy Pattern is used to encapsulate the different algorithms for calculating service charges based on varying account conditions. The Strategy Pattern allows the service charge calculation logic to be separated from the main account logic, making it more flexible and maintainable.