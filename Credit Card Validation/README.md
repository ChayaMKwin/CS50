# Credit Card Validator
#### This is a simple credit card validator program written in Python.

## Description

📝 Input: You're asked to *enter your credit card number*.

🛑 Validation: The program checks if what you entered is actually a number. If it's not, it tells you it's invalid and stops.

🔢 Length Check: It counts how many digits are in your credit card number. It should be either 13, 15, or 16 digits long. If it's not, it says it's invalid and stops.

🔑 Checksum Calculation: It does some fancy math (called the Luhn algorithm) to make sure your credit card number seems legit.

✔️ Checksum Check: The program verifies if the math adds up. If it doesn't, it means there might be a mistake in the number, so it says it's invalid and stops.

💳 Card Type: It looks at the first couple of digits to figure out what kind of credit card you have (Visa, Mastercard, or American Express).

🎉 Result: Finally, it tells you the type of card you have, or if it doesn't recognize it, it says it's invalid.
