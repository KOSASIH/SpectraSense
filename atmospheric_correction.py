import spectral

def atmospheric_correction(data):
    # Convert data to spectral image object
    img = spectral.ImageArray(data)
    
    # Apply atmospheric correction using the DOS algorithm
    corrected_img = img.atmospheric_correction()
    
    # Convert corrected image back to numpy array
    corrected_data = corrected_img.load()
    
    return corrected_data
