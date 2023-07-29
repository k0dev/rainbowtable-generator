import hashlib
import itertools

def md5_encrypt(string):
    return hashlib.md5(string.encode("utf-8")).hexdigest()

plain_to_hash = {}
hash_to_plain = {}

starting = input("Prefix: ")
ending = input("Suffix: ")
alphabet = input("Alphabet: ")
middle_len = int(input("Password length excluding prefix and suffix: "))

print("Calculating rainbow table...")
possibilities = itertools.product(alphabet, repeat=middle_len)
for middle in possibilities:
    plain = starting + ''.join(middle) + ending
    hashed = md5_encrypt(plain)
    plain_to_hash[plain] = hashed
    hash_to_plain[hashed] = plain

print("Done!")

while True:
    choice = input("\nLookup [p]lain or [h]ash? (or [q]uit) ")
    if choice == "p":
        plain = input("  plain: ")
        print(plain_to_hash[plain])
    elif choice == "h":
        hashed = input("  hash: ")
        print(hash_to_plain[hashed])
    elif choice == "q":
        break
