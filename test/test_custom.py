# pylint: skip-file
import unittest
from testing_imports import *
from HTMLTestRunner import HTMLTestRunner

class CustomTestsEx2(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2020, 2021, 2022])
    def test_custom_ex2a(self):
        filtered_df = find_max_col(self.data, "age", ['long_name' , 'player_positions', 'age'])
        expected = pd.DataFrame({"age": [54]})
        # Comparing dataframes is a bit complex, you can use this if you are sure that there are no NaNs
        self.assertTrue(
            (filtered_df.reset_index(drop=True) == expected.reset_index(drop=True)).all().all())
 
        
class CustomTestsEx3(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2020, 2021, 2022])
    def test_public_ex3a(self):
        female_bmi = calculate_bmi(self.data, "Female", 2021, ['short_name', 'year', 'age', 'overall', 'potential'])
        self.assertEqual(female_bmi["short_name"].iloc[0], "M. Rapinoe")
        self.assertEqual(female_bmi["BMI"].iloc[0], 20.761)                                            
                                                
                                                
class CustomTestsEx4(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2020, 2021, 2022])

                                                
    def test_public_ex4b(self):
        ids = [261799,158023]
        columns_of_interest = ['short_name', 'age', 'overall', 'potential']
        data_dict = players_dict(self.data, ids, columns_of_interest)
        data_dict = clean_up_players_dict(data_dict, [("potential", "one")])
        self.assertCountEqual(data_dict[61799]["overall"], [66])
        self.assertCountEqual(data_dict[158023]["potential"], [94])                                              
                                                
 if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CustomTestsEx2))
    suite.addTest(unittest.makeSuite(CustomTestsEx3))
    suite.addTest(unittest.makeSuite(CustomTestsEx4))
    runner = HTMLTestRunner(log=True, verbosity=2, output='reports',
                            title='PAC4', description='PAC4 custom tests',
                            report_name='Custom tests')
    runner.run(suite)
