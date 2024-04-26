Machine Learning VGG Facial Analysis
This project utilizes the pre-trained VGG-Face-Model along with the DeepFace library in Python to analyze dominant emotions from the facial expressions of individuals in photographs. The aim is to identify and quantify emotional reactions such as disgust, anger, fear, happiness, sadness, surprise, and neutrality.

Features
Emotion Analysis: Determine the dominant emotion displayed in a facial expression.
Input Compatibility: Accepts images in JPG, JPEG, or PNG formats. Higher quality images yield better analysis results.
Output:
Annotated image with the dominant emotion labeled.
A plot figure visualizing the emotion percentages.
A comprehensive Pandas DataFrame output with emotion data for each analyzed face.
Output Format
The output data is structured in a Pandas DataFrame as follows:

Image Name	Dominant Emotion	Disgust (%)	Angry (%)	Fear (%)	Happy (%)	Sad (%)	Surprise (%)	Neutral (%)
example_image.jpg	Happy	1.2	3.4	0.5	94.3	0.1	0.2	0.3
Example Use Case
In an illustrative scenario, this project was applied to images from the 2024 NFL Draft Picks to determine the emotional reactions of the picks upon being selected.

Installation
To set up this project, you will need Python and the following libraries:

bash
Copy code
pip install deepface
Usage
Below is a quick guide on how to use this project:

Prepare your images in the accepted formats.
Run the analysis script provided in the repository.
Check the output folder for the annotated images and emotion results DataFrame.
Contributing
Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
VGG-Face-Model developers for their pre-trained model.
DeepFace library maintainers for providing a robust framework for facial analysis.
