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


def is_product_available(product_id):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("select 1 from product where id = %s", (product_id))
        return list(cursor)


def add(user_id, product_id):
    if is_product_available(product_id):
        with connection.cursor() as cursor:
            sql = "INSERT INTO basket (`user_id`, `product_id`) VALUES (%s,%s)"
            cursor.execute(sql, (user_id, product_id))
        connection.commit()
        return True
    else:
        return False


def remove(user_id, product_id):
    with connection.cursor() as cursor:
        sql = "delete from basket where `user_id` = %s and `product_id` = %s"
        cursor.execute(sql, (user_id, product_id))
    connection.commit()


def get_basket(user_id):
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('select p.id, p.name, p.price from basket b '
                       'join product p on b.product_id = p.id and b.user_id = %s' % user_id)
        return list(cursor)


def make_order(user_id):
    with connection.cursor() as cursor:
        sql = "delete from basket where `user_id` = %s"
        cursor.execute(sql, (user_id))
    connection.commit()
