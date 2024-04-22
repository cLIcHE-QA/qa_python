import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_genre_age_rating_default_value_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_more_than41_characters_not_add_to_list(self):
        collector = BooksCollector()
        long_book_name = 'Семен Бобров: Рассвет полночи. Херсонида. В 2-х томах. Том 1'
        collector.add_new_book(long_book_name)
        assert long_book_name not in collector.get_books_genre()

    def test_set_book_genre_add_genre_to_book_shows_success(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_genre_empty_list_shows_success(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize(
        'book_name, genre, expected_result',
        [
            ['Хроники Нарнии', 'Фантастика', {'Хроники Нарнии': 'Фантастика'}],
            ['Неизвестная книга', None, {'Неизвестная книга': ''}]
        ]
    )
    def test_get_book_genre_get_two_books_shows_success(self, book_name, genre, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == expected_result

    def test_get_books_with_specific_genre_comedy_shows_only_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Зодиак')
        collector.add_new_book('Дневник Бриджит Джонс')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Зодиак', 'Детективы')
        collector.set_book_genre('Дневник Бриджит Джонс', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Дневник Бриджит Джонс']

    def test_get_book_genre_found_genre_success_found(self):
        collector = BooksCollector()
        collector.add_new_book('О дивный новый мир')
        collector.set_book_genre('О дивный новый мир', 'Фантастика')
        assert collector.books_genre.get('О дивный новый мир') == 'Фантастика'

    def test_get_books_for_children_get_one_book_shows_success(self):
        collector = BooksCollector()
        collector.add_new_book('Хроники Нарнии')
        collector.add_new_book('Особо опасен')
        collector.add_new_book('Ходячий замок')
        collector.set_book_genre('Хроники Нарнии', 'Фантастика')
        collector.set_book_genre('Особо опасен', 'Детективы')
        collector.set_book_genre('Ходячий замок', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Хроники Нарнии', 'Ходячий замок']

    def test_add_book_in_favorites_add_one_book_added_to_list(self):
        collector = BooksCollector()
        collector.add_new_book('Снеговик')
        collector.add_book_in_favorites('Снеговик')
        assert collector.get_list_of_favorites_books() == ['Снеговик']

    def test_delete_book_from_favorites_delete_two_books_delisted(self):
        collector = BooksCollector()
        collector.add_new_book('Исчезнувшая')
        collector.add_new_book('451 градус по Фаренгейту')
        collector.add_new_book('Кладбище домашних животных')
        collector.add_book_in_favorites('Исчезнувшая')
        collector.add_book_in_favorites('451 градус по Фаренгейту')
        collector.add_book_in_favorites('Кладбище домашних животных')
        collector.delete_book_from_favorites('451 градус по Фаренгейту')
        collector.delete_book_from_favorites('Исчезнувшая')
        assert collector.get_list_of_favorites_books() == ['Кладбище домашних животных']
