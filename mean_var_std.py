import numpy as np

def calculate(data_list):
    if len(data_list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(data_list).reshape((3, 3))

    # Calculate statistics once and reuse
    means = np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(matrix)
    variances = np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(matrix)
    std_devs = np.std(matrix, axis=0), np.std(matrix, axis=1), np.std(matrix)
    maxs = np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(matrix)
    mins = np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(matrix)
    sums = np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(matrix)

    calculations = {
        "mean": [means[0].tolist(), means[1].tolist(), means[2].item()],
        "variance": [variances[0].tolist(), variances[1].tolist(), variances[2].item()],
        "standard deviation": [std_devs[0].tolist(), std_devs[1].tolist(), std_devs[2].item()],
        "max": [maxs[0].tolist(), maxs[1].tolist(), maxs[2].item()],
        "min": [mins[0].tolist(), mins[1].tolist(), mins[2].item()],
        "sum": [sums[0].tolist(), sums[1].tolist(), sums[2].item()],
    }

    return calculations
