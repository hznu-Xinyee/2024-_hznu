import sqlite3


class DatabaseDriver:
    # 初始化连接数据库
    def __init__(self, db_path="db/score_management.db"):
        self.path = db_path
        self.connect = sqlite3.connect(self.path)

    def query(self, sql):
        if self.connect:
            cursor = self.connect.cursor()
            return cursor.execute(sql).fetchone()

    def queryAll(self, sql) -> list:
        if self.connect:
            cursor = self.connect.cursor()
            return cursor.execute(sql).fetchall()

    def update(self, sql):
        if self.connect:
            result = self.connect.execute(sql)
            self.connect.commit()
            return result.fetchone()

    def close(self):
        if self.connect:
            self.connect.close()


# 数据库连接代码测试
# if __name__ == "__main__":
#     database = DatabaseDriver("../db/score_management.db")
#     print(database.queryAll('select * from user'))
#     database.close()
