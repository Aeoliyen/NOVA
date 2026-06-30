import sqlite3
from datetime import datetime
from pathlib import Path


class MemoryManager:
    def __init__(self, db_path="data/nova.db"):
        Path("data").mkdir(exist_ok=True)
        self.db_path = db_path
        self._init_db()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    content TEXT NOT NULL,
                    importance INTEGER DEFAULT 1,
                    created_at TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_memory(self, category, content, importance=1):
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO memories (category, content, importance, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (category, content, importance, datetime.now().isoformat())
            )
            conn.commit()

    def list_memories(self, limit=10):
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT id, category, content, importance, created_at
                FROM memories
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,)
            ).fetchall()
        return rows