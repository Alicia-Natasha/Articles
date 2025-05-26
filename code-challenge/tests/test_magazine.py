import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
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

def test_create_magazine():
    mag = Magazine.create("W Monthly", "Lifestyle")
    assert mag.name == "W Monthly"
    assert mag.category == "Lifestyle"

def test_contributors_and_titles():
    mag = Magazine.create("W", "Lifestyle")
    author = Author.create("Barbra Walters")
    Article.create("Hot Gossip", author.id, mag.id)
    titles = mag.article_titles()
    contributors = mag.contributors()
    
    assert titles == ["Hot Gossip"]
    assert len(contributors) == 1
