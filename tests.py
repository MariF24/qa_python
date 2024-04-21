
import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_not_empty_dict_true(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Колобок')
        assert 'Колобок' in books_collector.books_genre

    def test_set_book_genre_if_book_add_in_dict(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Шрек')
        books_collector.set_book_genre('Шрек', 'Мультфильмы')
        assert books_collector.books_genre['Шрек'] == 'Мультфильмы'

    def test_get_book_genre_if_genre_add(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Шрек')
        books_collector.set_book_genre('Шрек', 'Мультфильмы')
        assert books_collector.books_genre.get('Шрек')


    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы'])
    def test_get_books_with_specific_genre_input_two_genre(self, genre):
        books_collector = BooksCollector()
        books_collector.add_new_book('Люди в черном')
        books_collector.set_book_genre('Люди в черном', 'Фантастика')
        assert books_collector.get_books_with_specific_genre

    def test_get_books_genre_if_dict_add(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Шрек')
        books_collector.set_book_genre('Шрек', 'Мультфильмы')
        assert books_collector.books_genre == {'Шрек':'Мультфильмы'}


    def test_get_books_for_children_is_true(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Шрек')
        books_collector.set_book_genre('Шрек', 'Мультфильмы')
        assert books_collector.get_books_for_children

    def test_add_book_in_favorites_if_add_in_books_genre(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Оно')
        books_collector.add_book_in_favorites('Оно')
        assert 'Оно' in books_collector.favorites

    def test_delete_book_from_favorites_if_add_in_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Маша и медведь')
        books_collector.add_book_in_favorites('Маша и медведь')
        books_collector.delete_book_from_favorites('Маша и медведь')
        assert 'Маша и медведь' not in books_collector.favorites



    def test_get_list_of_favorites_books_if_book_add(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Маша и медведь')
        books_collector.add_book_in_favorites('Маша и медведь')
        assert books_collector.favorites == ['Маша и медведь']



