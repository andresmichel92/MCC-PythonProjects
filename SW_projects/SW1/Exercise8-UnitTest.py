import Exercise8, statistics, unittest, statistics, sys, io


class TestExercise8(unittest.TestCase):

    def test_median(self):
        lista_test = [24, 24, 23]
        assert statistics.median(lista_test) == Exercise8.median(lista_test)
        lista_test2 = [24, 24, 23, 22]
        assert statistics.median(lista_test2) == Exercise8.median(lista_test2)

    def test_mean(self):
        lista_test = [24, 24, 23]
        assert statistics.mean(lista_test) == Exercise8.E4.calculate_mean(lista_test)

    def test_main(self):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        Exercise8.main()
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        assert type(output)==type("string")

    def test_std_dev(self):
        lista_test3=[1,2,3]
        assert statistics.pstdev(lista_test3) == Exercise8.E4.std_deviation(lista_test3)

    def data_sets(self):
        assert type(Exercise8.dataset1) == type([1,2,3])
        assert type(Exercise8.dataset2) == type([1, 2, 3])


