from sklearn.metrics import mean_squared_error

def calculate_rmse(data, endmembers, abundances):
    # Reconstruct mixed pixel spectra using endmembers and abundances
    reconstructed_data = np.dot(abundances, endmembers)
    
    # Calculate RMSE error between original and reconstructed data
    rmse = mean_squared_error(data, reconstructed_data, squared=False)
    
    return rmse
