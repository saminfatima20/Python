import numpy as np

def analyze_data(data_array):
    """
    Performs basic statistical analysis on a NumPy array.

    Args:
        data_array (np.ndarray): The input NumPy array for analysis.

    Returns:
        dict: A dictionary containing the calculated statistics.
    """
    if not isinstance(data_array, np.ndarray):
        raise TypeError("Input must be a NumPy array.")
    if data_array.size == 0:
        return {
            "mean": None,
            "median": None,
            "std_dev": None,
            "min_val": None,
            "max_val": None
        }

    mean_val = np.mean(data_array)
    median_val = np.median(data_array)
    std_dev_val = np.std(data_array)
    min_val = np.min(data_array)
    max_val = np.max(data_array)

    return {
        "mean": mean_val,
        "median": median_val,
        "std_dev": std_dev_val,
        "min_val": min_val,
        "max_val": max_val
    }

# Example Usage:
if __name__ == "__main__":
    # Create a sample dataset using NumPy
    data = np.array([10, 12, 15, 11, 13, 18, 14, 16, 20, 9])

    print(f"Original Data: {data}")

    # Analyze the data
    statistics = analyze_data(data)

    # Print the results
    print("\nStatistical Analysis:")
    for stat, value in statistics.items():
        print(f"{stat.replace('_', ' ').title()}: {value:.2f}")

    # Example with an empty array
    empty_data = np.array([])
    empty_stats = analyze_data(empty_data)
    print(f"\nAnalysis of empty array: {empty_stats}")