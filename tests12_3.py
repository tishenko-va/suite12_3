import unittest
from unittest import TestCase
import runner

class TournamentTest(TestCase):
    is_frozen = True

    def setUp(self):
        self.Useyn = runner.Runner('Усэйн', 10)
        self.Andrey = runner.Runner("Андрей", 9)
        self.Nick = runner.Runner("Ник", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for i in TournamentTest.all_results.items():
            print()

    @unittest.skipIf(is_frozen, 'Тесты в этом файле заморожены')
    def test_1(self):
         t1 = runner.Tournament(90, self.Useyn, self.Nick)
         TournamentTest.all_results = t1.start()
         last_place_key = max(TournamentTest.all_results)  # Получаем наибольший ключ
         last_runner = TournamentTest.all_results[last_place_key]  # Бегун на последнем месте
         self.assertTrue(last_runner.name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом файле заморожены')
    def test_2(self):
         t1 = runner.Tournament(90, self.Andrey, self.Nick)
         TournamentTest.all_results = t1.start()
         last_place_key = max(TournamentTest.all_results)  # Получаем наибольший ключ
         last_runner = TournamentTest.all_results[last_place_key]  # Бегун на последнем месте
         self.assertTrue(last_runner.name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом файле заморожены')
    def test_3(self):
         t1 = runner.Tournament(90, self.Andrey, self.Useyn, self.Nick)
         TournamentTest.all_results = t1.start()
         last_place_key = max(TournamentTest.all_results)  # Получаем наибольший ключ
         last_runner = TournamentTest.all_results[last_place_key]  # Бегун на последнем месте
         self.assertTrue(last_runner.name == 'Ник')


class RunnerTest(TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом файле заморожены')
    def test_walk(self):
        runner1 = runner.Runner('name')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом файле заморожены')
    def test_run(self):
        runner2 = runner.Runner('name')
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом файле заморожены')
    def test_challenge(self):
        runner1 = runner.Runner('runner1')
        runner2 = runner.Runner('runner2')
        for i in range(10):
            runner1.walk()
            runner1.run()
            runner2.walk()
            runner2.run()
        self.assertEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
