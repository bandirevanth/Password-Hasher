import hashlib

while True:
    user_inp = input("Enter Password: ")
    hashed_pass = hashlib.sha256(str.encode(user_inp)).hexdigest()
    print(f"Hashed Password: {hashed_pass}")
