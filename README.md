# qa_python
# BooksCollector

Проект для управления коллекцией книг с возможностью присвоения жанров, отметки избранных книг и фильтрации по жанрам.

## О проекте

Реализован класс `BooksCollector`, позволяющий добавлять книги, задавать жанры, получать списки книг по жанру и другие функции.

## Запуск тестов

Для запуска тестов используется `pytest`.

## Список тестов

test_add_new_book_add_two_books
test_set_book_genre_sets_genre_true
test_get_book_genre_name_returns_genre
test_get_books_with_specific_genre_genre_returns_name
test_get_books_genre_returns_all_books
test_get_books_for_children_returns_allowed_fixture
test_get_books_for_children_returns_allowed
test_add_book_in_favorites_one_book_added
test_delete_book_from_favorites_book_removed
test_get_list_of_favorites_books_returns_list

#### Структура проекта
main.py — файл с классом BooksCollector

tests.py — файл с тестами для класса

conftest.py — фикстуры для pytest

.gitignore — файлы и папки, игнорируемые Git

##### Автор
Irina Bartnovskaia