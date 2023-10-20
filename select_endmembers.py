from pysptools import abundance_maps

def select_endmembers(data, num_endmembers):
    # Convert data to spectral library object
    lib = abundance_maps.SpectralLibrary(data)
    
    # Apply N-FINDR algorithm to select endmembers
    endmembers = lib.nfindr(num_endmembers)
    
    return endmembers
