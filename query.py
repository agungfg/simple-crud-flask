import pymysql
import datetime


class Database:
    # Koneksi Database Menggunakan mysql
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "pabji"
        db = "db_payment"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    # Menampilkan Semua Data Ke Data Table
    def list_payment(self):
        self.cur.execute("SELECT id, create_date, modified_date, item, count, price, paid, deleted_at FROM payment LIMIT 50")
        result = self.cur.fetchall()
        return result

    # Insert Payment dari Modal Insert
    def insert_payment(self, inputs):
        self.cur.execute("INSERT INTO payment (id, create_date, modified_date, item, count, price, paid, deleted_at) VALUES (NULL, '%s', '%s', '%s', '%i', '%i', '0', NULL)" % (datetime.datetime.now(), datetime.datetime.now(), inputs[0], int(inputs[1]), int(inputs[2])))
        self.con.commit()

    # Update Data
    def update_payment(self, inputs):
        self.cur.execute("UPDATE payment SET modified_date='%s', item='%s', count='%i', price='%i', paid='%i' WHERE id='%i'" % (datetime.datetime.now(), inputs[0], int(inputs[1]), int(inputs[2]), int(inputs[3]), int(inputs[4])))
        self.con.commit()

    # Menghapus Data
    def delete_payment(self, id):
        self.cur.execute("DELETE FROM payment WHERE id='%i'" % (id))
        self.con.commit()

    # Get Data Default Modal Update
    def list_payment_updates(self, id):
        self.cur.execute("SELECT item, count, price, paid FROM payment WHERE id='%i'" % int(id))
        result = self.cur.fetchall()
        return result
