import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def setup_function():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM magazines;
        DELETE FROM authors;
    """)
    conn.commit()

def test_create_article():
    author = Author.create("Maguire Smith")
    mag = Magazine.create("British Vogue", "Fashion")
    article = Article.create("Beauty", author.id, mag.id)

    assert article.title == "Beauty"
    assert article.author_id == author.id
    assert article.magazine_id == mag.id
