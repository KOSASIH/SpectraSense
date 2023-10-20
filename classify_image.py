from sklearn.svm import SVC

def classify_image(data, labels):
    # Flatten the data and labels
    flattened_data = data.reshape(-1, data.shape[-1])
    flattened_labels = labels.flatten()
    
    # Initialize and train the SVM classifier
    svm = SVC()
    svm.fit(flattened_data, flattened_labels)
    
    # Perform classification on the entire image
    classified_image = svm.predict(flattened_data)
    
    # Reshape the classified image to its original shape
    classified_image = classified_image.reshape(data.shape[:-1])
    
    return classified_image
