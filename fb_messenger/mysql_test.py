import pymysql.cursors

import pymysql


connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='mysql',
                             db='facebook',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:

    with connection.cursor() as cursor:
        # Create a new record
        sql = "insert into talks (userid,text,seq) (`asd`,`asd`,`12`)"
        cursor.execute(sql)
    connection.commit()

finally:

    connection.close()


