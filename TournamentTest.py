import task
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = task.Runner("Усэйн", 10)
        self.run_2 = task.Runner("Андрей", 9)
        self.run_3 = task.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.keys():
            pass

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_1(self):
        race_1 = task.Tournament(90, self.run_1, self.run_3)
        TournamentTest.all_results[1] = race_1.start()

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_2(self):
        race_2 = task.Tournament(90, self.run_2, self.run_3)
        TournamentTest.all_results[2] = race_2.start()

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race_3(self):
        race_3 = task.Tournament(90, self.run_1, self.run_2, self.run_3)
        TournamentTest.all_results[3] = race_3.start()



if __name__ == '__main__':
    unittest.main()
