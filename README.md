# Language Identification Project

Welcome to the Language Identification project! This initiative aims to develop a system that accurately identifies the language of a given text using Natural Language Processing (NLP). The project involves analyzing text in various languages, including Estonian, Tamil, French, Spanish, and Chinese, through data preprocessing, model selection, and deployment using Streamlit.

## Project Overview

### Objectives
1. **Data Preprocessing:** Clean and prepare the dataset for analysis, ensuring it is suitable for model training.
2. **Model Selection:** Select and train appropriate algorithms to identify different languages.
3. **Language Detection:** Implement a model that accurately classifies the language of input text.
4. **Deployment:** Create a user-friendly interface using Streamlit to predict the language of user-provided text.

## Getting Started

### Prerequisites
To work on this project, ensure you have the following:
- Python 3.x
- Necessary Python libraries: Pandas, NumPy, Scikit-learn, Streamlit, and Pickle.

### Installation
1. **Clone the Repository:** Download the project files from the repository.
2. **Navigate to Project Directory:** Access the project's main folder.
3. **Install Required Packages:** Install the necessary Python libraries using the provided requirements file.

## Usage

### Data Preparation
- **Import Libraries:** Begin by importing essential libraries for data manipulation and model training.
- **Load the Dataset:** Read the dataset containing text and corresponding language labels.
- **Split Data:** Separate the data into features (text) and target variable (language labels).

### Model Training
- **Text Vectorization:** Transform the text data into numerical format for model processing.
- **Data Splitting:** Divide the data into training and testing sets to evaluate the model's performance.
- **Model Training:** Train the model using a suitable algorithm, such as Naive Bayes, to classify languages.
- **Model Evaluation:** Assess the model's accuracy by comparing predictions with actual language labels.

### Model Saving
- **Save the Model:** Store the trained model for future use.
- **Save Vectorizer:** Save the text vectorization model to transform new text inputs during deployment.

### Deployment with Streamlit
- **Create Streamlit App:** Develop an interactive web application that allows users to input text and receive language predictions.
- **Run the Application:** Launch the Streamlit app locally to test the language identification functionality.

## Contributions
We welcome contributions to this project. If you would like to contribute, please submit pull requests. For significant changes, consider opening an issue to discuss your proposed modifications.

### Importance of Language Identification

In today's globalized world, language identification plays a crucial role in breaking communication barriers. It enhances digital accessibility, allowing applications to serve users in their native languages. This project demonstrates how NLP can foster inclusivity and improve user experiences across diverse linguistic backgrounds.

