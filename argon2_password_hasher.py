from argon2 import PasswordHasher, Type

ph = PasswordHasher(
    memory_cost=102400,
    time_cost=2,
    parallelism=8,
    hash_len=64,
    type=Type.ID
    )

password = input('Unhashed password: ')
passwordHash = ph.hash(password)
print('Hash result: ' + passwordHash)

parts = passwordHash[1:].split('$')
print('Salt: ' + parts[3])
print('Hashed password: ' + parts[4])

print('Verified: ' + str(ph.verify(passwordHash, password)))

print('Rehash needed: ' + str(ph.check_needs_rehash(passwordHash)))
