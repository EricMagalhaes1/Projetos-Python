import hashlib


correct_password = "MyPassword123567"


h = hashlib.new('SHA256')
h.update(correct_password.encode())

password_hash = h.hexdigest()
print(password_hash)

user_input = "MyPassword123567"
h = hashlib.new('SHA256')
h.update(user_input.encode())
input_hash = h.hexdigest()

print(input_hash == password_hash)
