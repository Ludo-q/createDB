import sqlite3

conn = sqlite3.connect('contacts.sqlite')

for name, phone, email in conn.execute('SELECT * FROM contacts'):
    print(f'name: {name}, phone: {phone}, email: {email}')

conn.close()
