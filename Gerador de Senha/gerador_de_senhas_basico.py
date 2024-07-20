import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def generate_password(n):
  password = ""
  for i in range(n):
    password += random.choice(characters)
  return password
print(generate_password(8))