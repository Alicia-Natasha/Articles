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
    mag = Magazine.create("Tech Today", "Technology")
    assert mag.name == "Tech Today"
    assert mag.category == "Technology"

def test_contributors_and_titles():
    mag = Magazine.create("Science World", "Science")
    author = Author.create("Einstein")
    Article.create("Relativity", author.id, mag.id)
    titles = mag.article_titles()
    contributors = mag.contributors()
    
    assert titles == ["Relativity"]
    assert len(contributors) == 1