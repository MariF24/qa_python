
import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_not_empty_dict_true(self, item_of_class):
        item_of_class.add_new_book('Колобок')
        assert 'Колобок' in item_of_class.books_genre

    def test_set_book_genre_if_book_add_in_dict(self, item_of_class):
        item_of_class.add_new_book('Шрек')
        item_of_class.set_book_genre('Шрек', 'Мультфильмы')
        assert item_of_class.books_genre['Шрек'] == 'Мультфильмы'

    def test_get_book_genre_if_genre_add(self, item_of_class):
        item_of_class.add_new_book('Шрек')
        item_of_class.set_book_genre('Шрек', 'Мультфильмы')
        assert item_of_class.books_genre.get('Шрек')


    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы'])
    def test_get_books_with_specific_genre_input_two_genre(self, item_of_class, genre):
        item_of_class.add_new_book('Люди в черном')
        item_of_class.set_book_genre('Люди в черном', 'Фантастика')
        assert item_of_class.get_books_with_specific_genre

    def test_get_books_genre_if_dict_add(self,item_of_class):
        item_of_class.add_new_book('Шрек')
        item_of_class.set_book_genre('Шрек', 'Мультфильмы')
        assert item_of_class.books_genre == {'Шрек':'Мультфильмы'}


    def test_get_books_for_children_is_true(self,item_of_class):
        item_of_class.add_new_book('Шрек')
        item_of_class.set_book_genre('Шрек', 'Мультфильмы')
        assert item_of_class.get_books_for_children

    def test_add_book_in_favorites_if_add_in_books_genre(self,item_of_class):
        item_of_class.add_new_book('Оно')
        item_of_class.add_book_in_favorites('Оно')
        assert 'Оно' in item_of_class.favorites

    def test_delete_book_from_favorites_if_add_in_favorites(self,item_of_class):
        item_of_class.add_new_book('Маша и медведь')
        item_of_class.add_book_in_favorites('Маша и медведь')
        item_of_class.delete_book_from_favorites('Маша и медведь')
        assert 'Маша и медведь' not in item_of_class.favorites



    def test_get_list_of_favorites_books_if_book_add(self,item_of_class):
        item_of_class.add_new_book('Маша и медведь')
        item_of_class.add_book_in_favorites('Маша и медведь')
        assert item_of_class.favorites == ['Маша и медведь']



    @pytest.mark.parametrize('len_name', ['', 'Винни-пух и все-все-все-все-все-все-все-в', 'Винни-пух и все-все-все-все-все-все-все-все-все-все'])
    def test_add_new_book_negative_len_name_error(self, len_name, item_of_class):
        assert not item_of_class.add_new_book(len_name)

    @pytest.mark.parametrize('len_name', ['Винни-пух и все-все-все', 'Винни-пух и все-все-все-все-все-все-все-', 'Винни-пух и все-все-все-все-все-все-все'])
    def test_add_new_book_positive_len_name_true(self, len_name, item_of_class):
        item_of_class.add_new_book(len_name)
        assert item_of_class.books_genre != None



