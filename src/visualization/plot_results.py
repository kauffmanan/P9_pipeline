import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_orbital_distribution(data: pd.DataFrame, output_path: str):
    """
    Plots the orbital distribution of TNOs.
    
    Args:
        data: The TNO data to plot.
        output_path: The path to save the plot to.
    """
    print("Generating orbital distribution plot...")
    plt.figure(figsize=(10, 6))
    plt.hist(data['a'], bins=20, color='blue', alpha=0.7)
    plt.xlabel("Semi-major axis (au)")
    plt.ylabel("Number of TNOs")
    plt.title("Orbital Distribution of TNOs")
    
    # Ensure the output directory exists
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")
    plt.close()

if __name__ == '__main__':
    # Example usage
    dummy_data = pd.DataFrame({
        'a': np.random.normal(45, 5, 1000),
    })
    plot_orbital_distribution(dummy_data, "results/figures/orbital_distribution.png")