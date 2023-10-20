import numpy as np
from sklearn.decomposition import NMF

def spectral_unmixing(vswir_data, num_endmembers):
    # Normalize the VSWIR data
    vswir_data_normalized = vswir_data / np.max(vswir_data)
    
    # Apply Non-negative Matrix Factorization (NMF) to perform spectral unmixing
    model = NMF(n_components=num_endmembers, init='random', random_state=0)
    endmember_abundances = model.fit_transform(vswir_data_normalized)
    endmember_spectra = model.components_
    
    # Calculate the reconstruction error
    reconstruction_error = np.linalg.norm(vswir_data_normalized - np.dot(endmember_abundances, endmember_spectra))
    
    return endmember_spectra, endmember_abundances, reconstruction_error
