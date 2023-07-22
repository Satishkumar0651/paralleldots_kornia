# paralleldots_kornia

This repository contains a Flask application for performing LoFTR inference on two input images and returning the matched image with keypoints.

## Description

The LoFTR Inference app is built using Flask and allows you to upload two images, perform LoFTR inference on them, and visualize the matched image with keypoints. It utilizes the LoFTR model for feature matching and provides a simple web interface to interact with the application.

## Features

- Upload two images and perform LoFTR inference
- Visualize the matched image with keypoints
- Lightweight and easy to use


## Setup

1. Clone the repository:
   git clone https://github.com/Satishkumar0651/paralleldots_kornia.git
3. Install the required dependencies. Make sure you have Python 3.x and pip installed. Run the following command:
   pip install -r requirements.txt
4. Run the locally using
   python app.py
5. Build docker image and container
   a) create a Dockerfile with required commands
   b) Build image/container using these commands
    docker build -t paralleldots_kornia .
    docker stop paralleldots_kornia-container
    docker rm paralleldots_kornia-container
    docker run -d --name paralleldots_kornia-container -p 80:80 -v $(pwd):/app paralleldots_kornia
## Usage
###Cloud Run (GCP)
1. Open your Postman select post method and enter the url https://paralleldots-kornia-jezaajyhzq-uc.a.run.app/match_mages
2. select two images under the Body- form data and press send
3. The resultant image will be shown in the resultant tab in Postman 
Local Machine
1. Start the Flask application:
3. Open your browser and navigate to `http://localhost:8000`.

4. Upload two images using the provided form and click the "Match Images" button.

5. The application will perform LoFTR inference on the images and display the matched image with keypoints.

## Dependencies

Despendencies are in requirements.txt

## Steps
The LoFTR Inference app is a Flask-based web application that performs LoFTR (Learnable Frontend for TRiangulation) inference on two input images and returns the matched image with keypoints.

Here's a step-by-step explanation of what the app does:

* The user interacts with the app through a web interface. They are required to upload two images using a provided form.

* When the user submits the form, the Flask server receives the two uploaded images.

* The app then processes the images using the LoFTR model. LoFTR is a deep learning model specifically designed for feature matching tasks.

* The input images are preprocessed, including resizing and converting them to grayscale, as LoFTR works on grayscale images.

* The app utilizes the LoFTR model, which is loaded from a pre-trained model checkpoint. The model takes the preprocessed images as input and performs feature matching.

* The output of the LoFTR model is a set of keypoints and descriptors that represent corresponding features in the two input images.

* The app utilizes the OpenCV library to find the fundamental matrix and inliers between the keypoints from the two images. This helps in determining the geometric relationship between the images and filtering out outliers.

* Using the keypoints, descriptors, fundamental matrix, and inliers, the app generates a visualization of the matched image with keypoints. The matched keypoints are connected by lines, and the inlier keypoints are highlighted.

* The resulting visualization is saved as a PNG image.

* Finally, the app returns the saved image as the output, which can be viewed by the user in their web browser.

* The app provides a simple and intuitive way to perform LoFTR inference on two images and visualize the matched keypoints. It can be used for various computer vision tasks that involve feature matching, such as image alignment, object recognition, and structure-from-motion.



## Demo

Add a demo GIF or screenshot here to showcase the functionality of your app.

<img width="1329" alt="Screenshot 2023-07-15 at 10 13 39 AM" src="https://github.com/Satishkumar0651/paralleldots_kornia/assets/38080759/48d4d6bd-3e00-47b3-b0ec-fc37d8a6cd1a">
