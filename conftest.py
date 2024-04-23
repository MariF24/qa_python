import pytest

from main import BooksCollector
@pytest.fixture # фикстура, которая создаёт компанию
def item_of_class():
    books_collector = BooksCollector()
    return books_collector