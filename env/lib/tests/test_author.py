import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
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

def test_create_author():
    author = Author.create("Jane Doe")
    assert author.name == "Jane Doe"
    assert isinstance(author.id, int)

def test_author_articles_and_magazines():
    author = Author.create("Mark Twain")
    mag = Magazine.create("Writers Weekly", "Literature")
    Article.create("Famous Words", author.id, mag.id)
    Article.create("Even More Words", author.id, mag.id)
    
    articles = author.articles()
    magazines = author.magazines()

    assert len(articles) == 2
    assert len(magazines) == 1