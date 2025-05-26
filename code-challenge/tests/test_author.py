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
    author = Author.create("Marienne Lin")
    assert author.name == "Marienne Lin"
    assert isinstance(author.id, int)

def test_author_articles_and_magazines():
    author = Author.create("M.B Stephenson")
    mag = Magazine.create("Vogue Weekly", "Celebrity Lifestyle")
    Article.create("Women Empowerment", author.id, mag.id)
    Article.create("New York Fashion Week", author.id, mag.id)
    
    articles = author.articles()
    magazines = author.magazines()

    assert len(articles) == 2
    assert len(magazines) == 1

