from conftest import collector
from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_sets_genre_true(self, collector):

        collector.add_new_book('Баз Лайтер')
        collector.set_book_genre('Баз Лайтер', 'Мультфильмы')
        assert collector.books_genre['Баз Лайтер'] == "Мультфильмы"


    @pytest.mark.parametrize('name, genre', [('Баз Лайтер', 'Мультфильмы'),
                                             ('ОНО', 'Ужасы'),
                                             ('Скарамуш', 'Комедии'),
                                             ('Собака Баскервилей', 'Детективы'),
                                             ('Солярис', 'Фантастика')])
    def test_get_book_genre_name_returns_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre



    def test_get_books_with_specific_genre_genre_returns_name(self):
        collector = BooksCollector()
        collector.books_genre = {'Баз Лайтер': 'Мультфильмы', 'ОНО': 'Ужасы', 'Скарамуш': 'Комедии',
                                 'Собака Баскервилей': 'Детективы', 'Солярис': 'Фантастика', 'Валли':'Мультфильмы'}

        assert sorted(collector.get_books_with_specific_genre('Мультфильмы')) == ['Баз Лайтер', 'Валли']

    def test_get_books_genre_returns_all_books(self):
        collector = BooksCollector()
        collector.books_genre = {'Баз Лайтер': 'Мультфильмы', 'ОНО': 'Ужасы', 'Скарамуш': 'Комедии',
                                 'Собака Баскервилей': 'Детективы', 'Солярис': 'Фантастика'}

        assert collector.get_books_genre() == {
        'Баз Лайтер': 'Мультфильмы',
        'ОНО': 'Ужасы',
        'Скарамуш': 'Комедии',
        'Собака Баскервилей': 'Детективы',
        'Солярис': 'Фантастика'
    }


    @pytest.mark.parametrize('name, genre, expected', [('Баз Лайтер', 'Мультфильмы', ['Баз Лайтер']),
                                                           ('ОНО', 'Ужасы', []), ('Скарамуш', 'Комедии', ['Скарамуш']),
                                                           ('Собака Баскервилей', 'Детективы', []),
                                                           ('Солярис', 'Фантастика', ['Солярис'])])
    def test_get_books_for_children_returns_allowed(self, collector, name, genre, expected):

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == expected

    def test_add_book_in_favorites_one_book_added(self, collector):

        collector.add_new_book('Баз Лайтер')
        collector.add_book_in_favorites('Баз Лайтер')

        assert collector.get_list_of_favorites_books() == ['Баз Лайтер']

    def test_delete_book_from_favorites_book_removed(self, collector):

        collector.add_new_book('ОНО')
        collector.add_book_in_favorites('ОНО')

        collector.delete_book_from_favorites('ОНО')
        assert collector.get_list_of_favorites_books() == []


    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()

        collector.books_genre = {'Баз Лайтер':'Мультфильмы', 'ОНО':'Ужасы', 'Скарамуш':'Комедии', 'Собака Баскервилей':'Детективы', 'Солярис':'Фантастика'}

        collector.favorites = ['Баз Лайтер', 'ОНО', 'Скарамуш', 'Собака Баскервилей','Солярис']

        assert collector.get_list_of_favorites_books() == ['Баз Лайтер', 'ОНО', 'Скарамуш', 'Собака Баскервилей', 'Солярис']