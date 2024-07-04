from connector.DatabaseDriver import DatabaseDriver


# 通过姓名获取score表中全部数据

# 通过姓名获取成绩表中全部数据
def get_score_name_by_all(driver: DatabaseDriver, name):
    result = driver.queryAll(
        'select * from score where score.name = "{}"'.format(
            name))
    return result


# 获取score表中全部数据
def get_score_all(driver: DatabaseDriver):
    result = driver.queryAll(
        'select * from score')
    return result


# 获取学生学号和学生姓名
def get_score_name_username(driver: DatabaseDriver):
    result = driver.queryAll(
        'select name,username from score')
    return result


# 插入学生成绩
def insert_score(driver: DatabaseDriver, username, name, sex, chinese, math, english):
    update: int = driver.update(
        f'insert into score(username,name,sex,chinese,math,english) values ("{username}","{name}","{sex}",{chinese},{math},{english});')
    return update


# 通过学生学号和姓名删除学生成绩
def delete_score_by_name_username(driver: DatabaseDriver, name, username):
    update: int = driver.update('delete from score where name = "{}" and username = "{}";'.format(name, username))


# 通过学生学号修改成绩
def update_score_by_username(driver: DatabaseDriver, username, name, sex, chinese, math, english):
    update: int = driver.update(
        f'update score set name = "{name}",sex="{sex}",chinese = {chinese},math ={math},english = {english} where username = "{username}";')
    return update
