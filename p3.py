import random
import string

dictionary_words = ['password', '123456', 'qwerty', 'abc123'] 

accepted_passwords = []

for i in range(40):
  password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
  
  # Check dictionary words
  if password in dictionary_words:
    print(f"Password {password} is a dictionary word. Deleting..")
    continue 
  
  # Check for any special symbol
  if not any(char in string.punctuation for char in password):
    print(f"Password {password} has no special symbols. Deleting..")
    continue

  print(f"The password {password} accepted.")

  # Archive the accepted passwords
  accepted_passwords.append(password)

print(f"\nGenerated {len(accepted_passwords)} accepted passwords:")
print(accepted_passwords)