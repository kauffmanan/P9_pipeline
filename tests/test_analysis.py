import unittest
import pandas as pd
from src.analysis.bias_correction import correct_bias
from src.analysis.causal_inference import perform_causal_inference

class TestAnalysis(unittest.TestCase):

    def test_correct_bias(self):
        """
        Test the bias correction function.
        """
        dummy_data = pd.DataFrame({
            'id': range(5),
            'a': [40, 42, 45, 48, 50],
        })
        corrected_data = correct_bias(dummy_data, "survey_pointing")
        
        # Test if the dataframe is returned with the same number of rows
        self.assertEqual(len(corrected_data), len(dummy_data))
        # Test a value
        self.assertAlmostEqual(corrected_data['a'][0], 42.0)

    def test_perform_causal_inference(self):
        """
        Test the causal inference function.
        """
        dummy_data = pd.DataFrame({
            'id': range(100),
            'a': pd.np.random.normal(45, 5, 100),
            'is_clustered': pd.np.random.randint(0, 2, 100)
        })
        p_value = perform_causal_inference(dummy_data, "propensity_score")
        
        # Test if the p-value is a float between 0 and 1
        self.assertIsInstance(p_value, float)
        self.assertGreaterEqual(p_value, 0.0)
        self.assertLessEqual(p_value, 1.0)

if __name__ == '__main__':
    unittest.main()