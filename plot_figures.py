# plot_figures.py
# Sample script to generate visualizations for legal data

import pandas as pd
import matplotlib.pyplot as plt

def plot_term_frequency(csv_path):
    df = pd.read_csv(csv_path)
    df.plot(x="Term", y="Frequency", kind="bar")
    plt.title("Term Frequency")
    plt.savefig("figures/figure_term_frequency.png")

# Example usage
# plot_term_frequency("KWIC_Frequency_by_Principle.csv")
