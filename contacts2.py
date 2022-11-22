import sqlite3

db = sqlite3.connect('contacts.sqlite')

update_sql = 'UPDATE contacts SET email="updated_email@mail.com"'
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f'{update_cursor.rowcount} rows updated')

print()
print(f'Are connections the same: {db == update_cursor.connection}')
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute('SELECT * FROM contacts'):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.close()
