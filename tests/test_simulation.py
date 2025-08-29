import unittest
import numpy as np
from src.simulation.n_body_simulator import NBodySimulator

class TestNBodySimulator(unittest.TestCase):

    def test_run_simulation(self):
        """
        Test the run_simulation method.
        """
        simulator = NBodySimulator(planet_9_mass=10.0)
        test_tnos = np.random.rand(5, 3)
        results = simulator.run_simulation(test_tnos)
        
        # For this placeholder, we just check if the output has the same shape
        self.assertEqual(results.shape, test_tnos.shape)

if __name__ == '__main__':
    unittest.main()