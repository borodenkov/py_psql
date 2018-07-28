import psycopg2

connect = psycopg2.connect(database='test_base', user='test_user', host='localhost', password='test_password')
cursor = connect.cursor()





# cursor.execute("CREATE TABLE tbl(id INT, data JSON);")

# cursor.execute('INSERT INTO tbl VALUES (1, \'{ "name":"Tester" }\');')
# connect.commit()


def read_logs(log):



cursor.execute("SELECT * FROM tbl;")
for row in cursor:
    print(row)

connect.close()