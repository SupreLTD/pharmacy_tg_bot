import pymysql
from pymysql.cursors import DictCursor


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='admin',
    db='drugs',
    charset='utf8mb4',
    cursorclass=DictCursor
)


def get_pharmacy(product_id):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('select ph.name, ph.address from product p '
                       'join pharmacy ph on p.pharmacy_id = ph.id and p.id = %s' % product_id)
        return cursor.fetchone()
