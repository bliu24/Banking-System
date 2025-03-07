# Banking-System

A command-line banking system that allows users to manage accounts with basic transactions and persistent storage in CSV format.

## Features

- **Create Account**: Open a new account with a name and initial balance
- **Deposit/Withdraw**: Add or withdraw funds (no overdrafts allowed)
- **Transfer**: Send money between accounts
- **Persistent Storage**: Automatically saves/loads data to `accounts.csv`
- **Input Validation**: Ensures valid names and transaction amounts

## Installation

1. **Prerequisites**:  
   Ensure [Python 3.x](https://www.python.org/downloads/) is installed.

2. **Clone Repository**:
   ```bash
   git clone https://github.com/yourusername/simple-banking-system.git
   cd simple-banking-system

## Usage

### Start the system:
```bash
python banking_system.py
```

### menu options:
1. Create Account
   - Enter name (letters/spaces only)
   - Set initial balance (>=$0)

2. Deposit Money
   - Enter Account ID
   - Enter positive amount

3. Withdraw Money
   - Enter Account ID
   - Enter positive amount (balance cannot go negative)

4. Transfer Money
   - Provide sender/receiver Account IDs
   - Enter transfer amount

5. Check Balance
   - View account details by ID

6. Exit
   - Saves data automatically

## Testing

### Run unit tests to verify functionality:
```bash
python -m unittest test_banking_system.py
```

### Test coverage:
- Account creation with valid/invalid inputs
- Deposit/withdraw validation
- Transfer restrictions
- csv persistence
- certain edge cases



