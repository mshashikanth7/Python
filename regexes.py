import re
email = input("what's your email?").strip().lower()

if "@" in email:
    print("valid")
else:
    print("Invalid")
