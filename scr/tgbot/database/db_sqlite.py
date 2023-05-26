from typing import Any
import sqlite3 as sq

from settings.const import DB_NAME

class DataBaseHelper:
    def __init__(self):
        self.dbname = DB_NAME
        self.connect = sq.connect(self.dbname)
        self.cursor = self.connect.cursor()
    
    @property
    def setup_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS "users" (
            "id"	INTEGER NOT NULL UNIQUE,
            "username"	VARCHAR NOT NULL,
            "firstname"	VARCHAR,
            "lastname"	VARCHAR,
            "register_date"	DATE,
            PRIMARY KEY("id")
        );
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS "tickets" (
            "id"	INTEGER NOT NULL UNIQUE,
            "user"	INTEGER NOT NULL,
            "question"	TEXT,
            "question_time"	DATE,
            "answer"	TEXT,
            "answer_time"	DATE,
            PRIMARY KEY("id" AUTOINCREMENT),
            FOREIGN KEY("user") REFERENCES "users"("id")
        );
            """
        )
        self.connect.commit()

    def register_user_in_db(self, data: list) -> None:
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO users
            VALUES (?, ?, ?, ?, datetime())
            """, (
            data[0],
            data[1],
            data[2],
            data[3]
            )
        )
        self.connect.commit()
    
    def user_get_register_date(self, data: str) -> list:
        return self.cursor.execute(
            """
            SELECT register_date
            FROM users WHERE id == (?);
            """,(data,)
        ).fetchall()
    
    def save_active_ticket(self, data: list) -> None:
        self.cursor.execute(
            """
            INSERT INTO tickets
            VALUES (?, ?, ?, datetime(), ?, ?);
            """, (None, data[0], data[1], None, None)
        )
        self.connect.commit()

    def show_active_ticket(self) -> list:
        return self.cursor.execute(
            """
            SELECT id, user, question FROM tickets WHERE answer IS NULL
            """
        ).fetchall()
    
    def user_last_ticket(self) -> list:
        return self.cursor.execute(
            f"""
            SELECT id FROM tickets
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchall()
    
    def answer_to_ticket(self, data: list):
        self.cursor.execute(
            f"""
            UPDATE tickets
            SET answer = "{data[0]}", answer_time = datetime()
            WHERE tickets.id = (?);
            """, (data[1],)
        )
        self.connect.commit()
