import pytest
from main import BooksCollector
@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    collector.add_new_book('Баз Лайтер')
    collector.set_book_genre('Баз Лайтер', 'Мультфильмы')
    collector.add_new_book('ОНО')
    collector.set_book_genre('ОНО', 'Ужасы')
    collector.add_new_book('Скарамуш')
    collector.set_book_genre('Скарамуш', 'Комедии')
    collector.add_new_book('Собака Баскервилей')
    collector.set_book_genre('Собака Баскервилей', 'Детективы')
    collector.add_new_book('Солярис')
    collector.set_book_genre('Солярис', 'Фантастика')
    return collector