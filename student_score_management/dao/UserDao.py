from connector.DatabaseDriver import DatabaseDriver
import connector.DatabaseDriver


# 获取用户表中密码
def register_user(driver: DatabaseDriver, username: str, password: str, job: str):
    result: tuple = driver.query('select password from user where username = "{}"'.format(username))
    if result is None:
        update: int = driver.update(
            'insert into user(username,password,job) values ("{}","{}","{}");'.format(username, password, job))
    else:
        return 0
    return update


# 获取用户表中登录信息
def login(driver: DatabaseDriver, username: str, password: str) -> tuple:
    result: tuple = driver.query('select username,password,job from user where username = "{}" '
                                 'and password="{}"'.format(username, password))
    return result


# 通过学号或教师号获取成绩表中全部数据
def get_user_by_all(driver: DatabaseDriver, username) -> tuple:
    result: tuple = driver.query(
        'select score.* from score , user where user.username = score.username and score.username = "{}"'.format(
            username))
    return result
