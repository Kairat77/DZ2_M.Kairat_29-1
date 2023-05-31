import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("Прикинь работает!")

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id TEXT PRIMARY KEY, username TEXT, "
               "name TEXT, age INTEGER,direction TEXT,"
               "groupp TEXT, photo TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.executemany("INSERT INTO mentors VALUES "
                       "(?, ?, ?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    await message.answer_photo(
        random_user[6],
        caption=f"{random_user[1]}\n{random_user[2]} {random_user[3]} "
                f"{random_user[4]} {random_user[5]} \n{random_user[0]}"
    )

async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", tuple(user_id))
    db.commit()