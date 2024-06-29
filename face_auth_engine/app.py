import os
import cv2
import numpy as np
import hashlib
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained ResNet50 model
model = resnet50(pretrained=True)
model.eval()

# Define the transformation for the input image
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def extract_features(image):
    """
    Extract features from an image using the ResNet model.
    
    Args:
        image (np.ndarray): Image array.
        
    Returns:
        np.ndarray: Extracted features.
    """
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = transform(img)
    img = img.unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        features = model(img)
    
    return features.numpy()

def generate_id(features):
    """
    Generate a unique ID from the extracted features.
    
    Args:
        features (np.ndarray): Extracted features.
        
    Returns:
        str: Generated unique ID.
    """
    features_str = np.array2string(features)
    hash_object = hashlib.sha256(features_str.encode('utf-8'))
    face_id = hash_object.hexdigest()
    return face_id

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        # Read the image file
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        
        # Extract features and generate face ID
        features = extract_features(img)
        face_id = generate_id(features)
        
        return jsonify({'face_id': face_id})

if __name__ == "__main__":
    app.run(debug=True)
