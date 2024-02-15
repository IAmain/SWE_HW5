import random
import string

def generate_user_data():
  usernames = ['user' + str(i) for i in range(1,11)]
  passwords = [''.join(random.choices(string.ascii_letters + string.digits, k=8)) for i in range(10)]
  birthdates = [f'{random.randint(1950,2000)}-{random.randint(1,12)}-{random.randint(1,28)}' for i in range(10)]
  addresses = [f'{random.randint(1,999)} Fake St, City {random.randint(1,99)}, ST {random.choice(string.ascii_uppercase)} {random.randint(10, 99)}' for i in range(10)]
  ssn = [f'{random.randint(100000000,999999999)}' for i in range(10)]
  products = [f'ID-{"".join(random.choices(string.ascii_lowercase, k=5))}' for i in range(10)]
  salespeople = ['salesperson' + str(i) for i in range(1,6) for _ in range(2)]
  
  user_records = []
  for i in range(10):
    user_records.append({
      'username': usernames[i],
      'password': passwords[i],  
      'birthdate': birthdates[i],
      'address': addresses[i],
      'ssn': ssn[i],
      'productPurchased': products[i],  
      'salesperson': random.choice(salespeople)
    })
  
  return user_records

# Step Two: Key/Value Pairs
user_data = generate_user_data() 
data_store = {}

for record in user_data:
  user_id = record['username']
  data_store[user_id] = record

# Step Three: Search Engine  
print(data_store['user5']) 

# Search by State
state = 'CA'
for user_id, record in data_store.items():
  if record['address'].split(',')[1].strip() == state:
    print(record)
    
# Search by Salesperson 
salesperson = 'salesperson3'  
for user_id, record in data_store.items():
  if record['salesperson'] == salesperson:
    print(record)