# PIN SYSTEM

correct_pin = "1234"  # Stored as a string to allow leading zeros (e.g., "0123")
attempts = 0
max_attempts = 3

print("PIN SYSTEM")

while attempts < max_attempts:
    user_pin = input("Enter PIN: ")

    # Validate that the input contains only numbers
    if not user_pin.isdigit():
        attempts += 1
        print(f"Invalid input. Only numbers are allowed. ({attempts}/{max_attempts})")
        continue  # Skip the rest of the loop and move to the next attempt

    if user_pin == correct_pin:
        print("Correct PIN. Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN ({attempts}/{max_attempts})")

if attempts == max_attempts:
    print("Account locked")

