# Face Recognition and Analysis

This Python script performs face recognition and analysis on images. It uses the `DeepFace` library for face detection and analysis, and a custom Keras model for predicting the height of a person based on their face.

## Dependencies

- os
- cv2
- csv
- numpy
- PIL
- DeepFace
- keras_core

## Installation

To install this project using git, follow these steps:

1. First, clone the repository to your local machine. Open your terminal and run:

```bash
git clone https://github.com/DrZuse/face-detection-height-prediction.git
```

2. Navigate to the directory of the cloned repository:

```bash
cd face-detection-height-prediction
```

3. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Now, you should be able to run the script in your local environment. Remember to place your input images in the `./input` directory before running the script. 

Please note that you need to have `git` and `python` installed on your machine to perform these steps. If you encounter any issues, please refer to the respective package's documentation.

## How to Run

1. Place your input images in the `./input` directory.
2. Run the script `python3 run.py`. The script will create an `./output` directory if it doesn't exist.
3. The output images and CSV files will be saved in the `./output` directory.

## Functions

### output_data(output, file, output_obj, image)

This function creates a CSV file for each image, with each row containing the following information for each detected face:

- File name
- Face ID
- Face rating (confidence)
- Age
- Gender
- Race
- Emotion
- Predicted height

The function also draws rectangles around the detected faces in the image and saves the image.

### face_recognition(input, output)

This function performs face recognition and analysis on each image in the input directory. For each detected face, it:

- Extracts the face from the image.
- Analyzes the face to determine the age, gender, race, and emotion.
- Loads a Keras model and uses it to predict the height of the person based on the face.
- Adds the analysis results to an output object.
- Calls `output_data()` to save the analysis results and image.

## Main Execution

If the script is run as the main program, it calls `face_recognition()` with `./input` as the input directory and `./output` as the output directory.

## Note

Please ensure that the Keras model file `face_to_height_model.h5` is present in the same directory as the script. This model is used to predict the height of a person based on their face. If the model file is not present, the script will not be able to make height predictions. 

## Disclaimer

This script is intended for educational purposes only. The accuracy of the face recognition, analysis, and height prediction may vary depending on the quality of the input images and the performance of the `DeepFace` library and the Keras model. Always use this script responsibly and respect the privacy of others.