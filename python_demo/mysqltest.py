import pymysql

# id = 20120001
# user = 'Bob'
# age = 20
#
# db = pymysql.connect(host='192.168.8.231', port=3306, db='spiders', user='spider', password='spider')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id, name, age) values (%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()

db = pymysql.connect(host='192.168.8.231', port=3306, db='spiders', user='spider', password='spider')
cursor = db.cursor()
# Insert
def insertDb(table, data):
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table = table, keys = keys, values = values)
    print(sql)
    print(tuple(data.values()))
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            db.commit()
    except Exception as e:  #必须使用as 才能打出具体错误信息
        print(str(e))
        print('Failed')
        db.rollback()
    db.close()

# Insert Or Update
def inOrUpDb(table, data):
    keys =  ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table = table, keys = keys, values = values)
    update = ','.join([" {key} = %s".format(key = key) for key in data])  # 注意写法上的空格，打出SQL
    sql += update

    print(sql)
    try:
        if cursor.execute(sql, tuple(data.values()) * 2):
            print('Successful')
            db.commit()
    except Exception as e:
        print(str(e))
        print('Failed')
        db.rollback()
    db.close()

# Delete
def deleteDb(table, condition):
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table = table, condition = condition)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(str(e))
        print('Failed')
        db.rollback()
    db.commit()

# Select
def selectDb():
    sql = 'SELECT * FROM students WHERE age > 19'
    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print('Row:', row)
            row = cursor.fetchone()
    except Exception as e:
        print(str(e))

data = {
    'id' : 20120002,
    'name' : 'Bob',
    'age' : 21
}
table = 'students'
#inOrUpDb(table, data)
selectDb()