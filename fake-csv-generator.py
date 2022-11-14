from faker import Faker
import random
import csv

# initialize a generator
fake = Faker('it_IT')

transactions = []
fields = ['user_name', 'user_birth_date', 'user_birth_city', 'seller', 'seller_address', 'transaction_amount', 'transaction_date']
#create some fake data
for u in range (10):
    user = fake.name()
    user_birth_date = fake.date_between(start_date='-40y', end_date='-20y').strftime('%Y-%m-%d')
    user_birth_city = fake.city()
    for c in range (10):
        seller = fake.company()
        seller_address = fake.address().replace('\n',' ')
        for t in range (10):
            transaction_amount_unit = random.randint(1,250)
            transaction_amount_decimal = random.randint(1,100)
            transaction_amount = str(transaction_amount_unit) + ',' + str(transaction_amount_decimal)
            transaction_date = fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d')
            transaction = [user, user_birth_date, user_birth_city, seller, seller_address, transaction_amount, transaction_date]
            transactions.append(transaction)

random.shuffle(transactions)

for transaction in transactions:
    print(transaction)

with open('HappyPay.csv', 'w', newline='') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f, quoting=csv.QUOTE_ALL)
      
    write.writerow(fields)
    write.writerows(transactions)