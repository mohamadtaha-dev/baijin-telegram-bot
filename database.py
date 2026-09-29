import sqlite3
from datetime import datetime
from config import *


conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    telegram_id INTEGER PRIMARY KEY,
    name TEXT,
    coins INTEGER,
    xp INTEGER,
    level INTEGER,
    stage INTEGER,
    hearts INTEGER,
    last_reward TEXT
)
""")

conn.commit()



def add_user(user_id, name):

    cursor.execute(
        "SELECT telegram_id FROM users WHERE telegram_id=?",
        (user_id,)
    )

    if cursor.fetchone() is None:

        cursor.execute("""
        INSERT INTO users
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            user_id,
            name,
            START_COINS,
            START_XP,
            START_LEVEL,
            START_STAGE,
            START_HEARTS,
            ""
        ))

        conn.commit()



def get_user(user_id):

    cursor.execute(
        "SELECT * FROM users WHERE telegram_id=?",
        (user_id,)
    )

    return cursor.fetchone()



def next_stage(user_id):

    cursor.execute("""
    UPDATE users
    SET stage = stage + 1
    WHERE telegram_id=?
    """,
    (user_id,))

    conn.commit()



def add_reward(user_id, coins, xp):

    cursor.execute("""
    UPDATE users
    SET
    coins = coins + ?,
    xp = xp + ?
    WHERE telegram_id=?
    """,
    (
        coins,
        xp,
        user_id
    ))

    conn.commit()

    update_level(user_id)



def update_level(user_id):

    user = get_user(user_id)

    if user:

        new_level = (user[3] // 100) + 1

        if new_level > user[4]:

            cursor.execute("""
            UPDATE users
            SET level=?
            WHERE telegram_id=?
            """,
            (
                new_level,
                user_id
            ))

            conn.commit()



def remove_heart(user_id):

    cursor.execute("""
    UPDATE users
    SET hearts = hearts - 1
    WHERE telegram_id=? AND hearts > 0
    """,
    (user_id,))

    conn.commit()



def get_hearts(user_id):

    cursor.execute("""
    SELECT hearts
    FROM users
    WHERE telegram_id=?
    """,
    (user_id,))

    result = cursor.fetchone()

    if result:
        return result[0]

    return 0



def get_profile(user_id):

    user = get_user(user_id)

    return f"""
👤 {user[1]}

🪙 سکه: {user[2]}
⭐ XP: {user[3]}
🏆 Level: {user[4]}
🎮 مرحله: {user[5]}
❤️ قلب: {user[6]}
"""



def leaderboard():

    cursor.execute("""
    SELECT name, level, xp
    FROM users
    ORDER BY level DESC, xp DESC
    LIMIT 10
    """)

    return cursor.fetchall()



def daily_reward(user_id):

    cursor.execute("""
    SELECT last_reward
    FROM users
    WHERE telegram_id=?
    """,
    (user_id,))

    result = cursor.fetchone()


    today = datetime.now().strftime("%Y-%m-%d")


    if result[0] == today:
        return False


    cursor.execute("""
    UPDATE users
    SET
    coins = coins + 50,
    xp = xp + 20,
    hearts = hearts + 1,
    last_reward = ?
    WHERE telegram_id=?
    """,
    (
        today,
        user_id
    ))


    conn.commit()
    # اضافه کردن ستون جایزه روزانه اگر وجود ندارد
try:
    cursor.execute("""
    ALTER TABLE users
    ADD COLUMN last_reward TEXT
    """)
    conn.commit()

except sqlite3.OperationalError:
    pass