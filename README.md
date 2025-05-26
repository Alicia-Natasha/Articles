# Articles Code Challenge
A simple content publishing platform built with Python and SQLite. This project models relationships between **Authors**, **Magazines**, and **Articles**, allowing users to manage and retrieve associated data efficiently.

---

## Project Structure

Articles/
│
├── code-challenge/
│ ├── lib/
│ │ ├── models/
│ │ │ ├── author.py
│ │ │ ├── magazine.py
│ │ │ └── article.py
│ │ └── db/
│ │ ├── database.db
│ │ └── connection.py
│ └── tests/
│ ├── test_author.py
│ ├── test_magazine.py
│ └── test_article.py
├── setup_db.py
└── README.md

---

## Features

- Models for `Author`, `Magazine`, and `Article` with relationships.
- Validations and constraints (e.g., title uniqueness, proper lengths).
- SQL queries for aggregate and association-based data.
- Full test coverage using `pytest`.
- DRY and readable codebase using OOP best practices.

---

## Getting Started

1. Clone the repository
```bash
git clone <your-repo-url>
cd Articles

2. Create and activate a virtual environment (optional but recommended)
python3 -m venv env
source env/bin/activate

3. Install dependencies
pip install -r requirements.txt

Or if there's no requirements.txt, just install:

pip install pytest

4. Set up the database
python3 setup_db.py

You should see:
✅ Database schema created successfully.


Running Tests
Make sure the database is set up before running tests:

pytest
All tests should pass if your models are implemented correctly.

 Example Usage
from models.author import Author
from models.magazine import Magazine
from models.article import Article

# Create records
author = Author.create("Maguire Smith")
mag = Magazine.create("British Vogue", "Fashion")
article = Article.create("Beauty", author.id, mag.id)

# Query relationships
print(author.articles())         # List of articles written by Maguire
print(magazine.contributors())   # List of authors who wrote British Vogue
✅ Requirements
Python 3.8+

SQLite3

pytest (for testing)

## Contributor
Alicia Natasha

## License
This project is open source and available under the MIT License.
