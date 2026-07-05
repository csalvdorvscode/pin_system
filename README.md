# 🔐 PIN System

A simple Python project that simulates a PIN authentication system.

## Features

- User authentication with a PIN
- Maximum of 3 login attempts
- Account lock after too many failed attempts
- Input validation (only numeric characters are accepted)
- PIN stored as a string to support leading zeros (e.g. "0123")

## Technologies

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/yourusername/pin-system.git
```

2. Open the project folder.

3. Run:

```bash
python pin_system.py
```

## Example

```
PIN SYSTEM

Enter your PIN: 1111
Incorrect PIN (1/3)

Enter your PIN: hello
Invalid input. Only numbers are allowed. (2/3)

Enter your PIN: 1234
Correct PIN. Access granted.
```

## What I Learned

This project helped me practice:

- while loops
- if / else statements
- input validation with `isdigit()`
- string comparison
- variables
- writing clean and readable Python code

## Future Improvements

- Hide the PIN while typing.
- Generate a random PIN.
- Store the PIN securely using hashing.
- Allow the user to change the PIN.
