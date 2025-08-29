import yaml
from data_ingestion import fetch_data
from simulation import n_body_simulator
from analysis import bias_correction, causal_inference
from visualization import plot_results

def main():
    """
    Main function to run the TNO analysis pipeline.
    """
    print("Starting TNO analysis pipeline...")

    # Load configuration
    with open("config/pipeline_config.yaml", 'r') as f:
        config = yaml.safe_load(f)

    # 1. Data Ingestion
    tno_data = fetch_data.fetch_tno_data("http://example.com/tno_data.csv")
    raw_data_path = config['paths']['raw_data'] + "tno_data.csv"
    tno_data.to_csv(raw_data_path, index=False)
    print(f"Raw data saved to {raw_data_path}")

    # 2. N-body Simulation
    simulator = n_body_simulator.NBodySimulator(config['simulation']['planet_9_mass'])
    # In a real pipeline, you would load TNOs for simulation
    simulated_tnos = simulator.run_simulation(tno_data[['a', 'e', 'i']].to_numpy())

    # 3. Bias Correction
    corrected_data = bias_correction.correct_bias(tno_data, config['analysis']['bias_correction_method'])

    # 4. Causal Inference
    p_value = causal_inference.perform_causal_inference(corrected_data, config['analysis']['causal_inference_model'])
    print(f"Evidence for Planet 9 (p-value): {p_value}")

    # 5. Visualization
    plot_path = config['paths']['results'] + "figures/orbital_distribution.png"
    plot_results.plot_orbital_distribution(corrected_data, plot_path)

    print("TNO analysis pipeline finished successfully.")

if __name__ == '__main__':
    main()