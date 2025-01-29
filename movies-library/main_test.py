import unittest
from main import MoviesLibrary


class TestMoviesLibrary(unittest.TestCase):
    def test_add_movie(self):
        library = MoviesLibrary(['Комедия'])
        library.add_movie('Комедия', 'Фильм 1')
        self.assertEqual(library.recommend('Комедия'), ['Фильм 1'])

    def test_recommend_empty_genre(self):
        library = MoviesLibrary(['Комедия'])
        self.assertEqual(library.recommend('Комедия'), [])

    def test_shared_movie_list_bug(self):
        library = MoviesLibrary(['Комедия', 'Ужасы'])
        library.add_movie('Комедия', 'Фильм 1')
        library.add_movie('Ужасы', 'Фильм 2')
        self.assertEqual(library.recommend('Комедия'), ['Фильм 1'])
        self.assertEqual(library.recommend('Ужасы'), ['Фильм 2'])  # Здесь тест упадёт!


if __name__ == '__main__':
    unittest.main()

