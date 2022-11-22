import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_mail = 'new_email@mail.com'
phone = input('Please enter a phone number: ')

update_sql = f'UPDATE contacts SET email = ? WHERE phone = ?'
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_mail, phone))
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
