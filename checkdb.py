import sqlite3

conn = sqlite3.connect('contacts.sqlite')

user_input = input('Please enter a name to find: ')

query = f'SELECT * FROM contacts WHERE name = ?'

# If we need to pass a tuple with one value then we need to add a comma
#  after the value, variable, etc.
for name, phone, email in conn.execute(query, (user_input, )):
    print(f'name: {name}, phone: {phone}, email: {email}')

conn.close()
