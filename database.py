import aiosqlite

DB_NAME = "DataBase.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS clicks (
                user_id INTEGER,
                button TEXT,
                count INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, button)
            )
        """)
        await db.commit()

async def add_click(user_id: int, button: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT INTO clicks (user_id, button, count) VALUES (?, ?, 1)
            ON CONFLICT(user_id, button) DO UPDATE SET count = count + 1
        """,
            (user_id, button),
        )
        await db.commit()

async def get_clicks(user_id: int, button: str) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("""
            SELECT count FROM clicks WHERE user_id = ? AND button = ?  
        """,
            (user_id, button),
        ) as cursor:
            row = await cursor.fetchone()
        return row[0] if row else 0 