import harperdb

url = "HARPERDB CLOUD URL"
username = "INSTANCE USERNAME"
password = "INSTANCE PASSWORD"

db = harperdb.HarperDB(
    url=url,
    username=username,
    password=password
)

SCHEMA = "tutorial_repo"
TABLE = "tutorials"
TABLE_TODAY = "tutorial_today"


def insert_tutorial(tutorial_data):
    return db.insert(SCHEMA, TABLE, [tutorial_data])

def delete_tutorial(tutorial_id):
    return db.delete(SCHEMA, TABLE, [tutorial_id])

def get_all_tutorials():
    try:
        return db.sql(f"select video_id,channel,title,duration from {SCHEMA}.{TABLE}")
    except harperdb.exceptions.HarperDBError:
        return []

def get_tutorial_today():
    return db.sql(f"select * from {SCHEMA}.{TABLE_TODAY} where id = 0")

def update_tutorial_today(tutorial_data, insert=False):
    tutorial_data['id'] = 0
    if insert:
        return db.insert(SCHEMA, TABLE_TODAY, [tutorial_data])
    return db.update(SCHEMA, TABLE_TODAY, [tutorial_data])

