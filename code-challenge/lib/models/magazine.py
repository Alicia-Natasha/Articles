import sqlite3
from ..db.connection import get_connection
from .article import Article

class Magazine:
    all = []

    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @classmethod
    def create(cls, name, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        id = cursor.lastrowid
        return cls(id, name, category)

    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self.name, self.category, self.id))
        conn.commit()

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
        conn.commit()
        Magazine.all.remove(self)

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [Article(row["id"], row["title"], row["author_id"], row["magazine_id"]) for row in rows]

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        from .author import Author
        return [Author(row["id"], row["name"]) for row in rows]

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [row["title"] for row in rows]
