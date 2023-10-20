from pysptools import abundance_maps

def estimate_abundances(data, endmembers):
    # Convert data to spectral image object
    img = abundance_maps.SpectralImage(data)
    
    # Apply LS algorithm to estimate abundances
    abundances = img.ls(endmembers)
    
    return abundances
