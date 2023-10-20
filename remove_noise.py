from scipy.ndimage import median_filter

def remove_noise(data):
    # Apply median filtering with a kernel size of 3x3
    filtered_data = median_filter(data, size=(3, 3))
    
    return filtered_data
