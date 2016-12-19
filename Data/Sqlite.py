# -*- coding: utf-8 -*-

import sqlite3


class DB_Sqlite3:
    # 获得数据库handler
    def __init__(self):
        # TODO config文件配置数据库
        self.con = con = sqlite3.connect(r"test.db")
        self.cur = con.cursor()

    # 创建表
    def TB_C(self, table, command):
        crt_tb_sql = """
        CREATE TABLE IF NOT EXISTS %s(\
            %s
        );
        """ % (table, command)
        self.cur.execute(crt_tb_sql)

    # 读取表
    def TB_R(self, table):
        select_tb_sql = "SELECT * FROM %s" % table
        self.cur.execute(select_tb_sql)
        return self.cur.fetchall()

    # 插入表项
    def TB_I(self, table, key, value):
        insert_sql = "INSERT INTO %s (%s) VALUES (%s)" % \
                     (table, key,  (r'?,'*len(value))[:-1])
        self.cur.execute(insert_sql, value)
        self.con.commit()

    # 删除表
    def TB_D(self, table):
        drp_tb_sql = "DROP TABLE IF EXISTS %s" % table
        self.cur.execute(drp_tb_sql)

    def __del__(self):
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    command = """
        	id integer primary key autoincrement unique not null,
        	name varchar(100),
        	city varchar(100)
    """
    # select_sql = "select * from Untitled"
    db = DB_Sqlite3()

    db.TB_C('test', command)
    db.TB_I('test', 'name, city', ('Mark', 'Shenzhen'))
    print(db.TB_R('test'))
    db.TB_D('test')

    del db

