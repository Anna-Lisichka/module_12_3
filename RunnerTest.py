import task
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        road = task.Runner('Wall Street')
        for i in range(10):
            road.walk()
        self.assertEqual(road.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner= task.Runner('Peter')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        partner1 = task.Runner('Kate')
        partner2 = task.Runner('Anna')
        for _ in range(10):
            partner1.walk()
            partner2.run()


if __name__ == '__main__':
    unittest.main()


