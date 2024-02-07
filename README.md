# DM_python_project
## Book Recommendation based on Sentiment Analysis
![pink panter](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGxuMzBwa2VoeGJnM2p6NGIzcXp6azNrMWM2Z2xmN29vOTh4dWZ5OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZCmDhIFeF1s2c/giphy.gif)

### Overview
This project implements a sentiment analysis system based on the DistilRoBERTa model using the Hugging Face Transformers library. The program performs sentiment analysis of book reviews contained in the dataset and assigns an emotion to each book. With this model, you can classify emotions in English text data. The model was trained on 6 diverse datasets and predicts Ekman's 6 basic emotions, plus a neutral class:

anger 🤬 disgust 🤢 fear 😨 joy 😀 neutral 😐 sadness 😭 surprise 😲
### Prerequisites
Python 3
Required Python Libraries: pandas, transformers, nltk

Optional Python Libraries: openpyxl (if there is an error reading the Excel file, this library may be necessary)
### Installation
Clone the repository:
git clone https://github.com/ludovica-mas/DM_python_project/sentiment_analysis_book_review.py 
Navigate to the project directory:
cd DM_python_project 
Install the required Python libraries:
pip install pandas transformers nltk openpyxl 
### Usage
Ensure your dataset is in Excel format and contains the necessary columns (Title, Author, Genre, Subgenre, Reviews, Description, Price, Amazon Link).
Run the script sentiment_analysis_book_review.py:
python sentiment_analysis_book_review.py 
### Project Structure
sentiment_analysis_book_review.py: Main script containing sentiment analysis and book recommendation implementation.
database_libri_python.xlsx: Excel file containing book data.
README.md: This README file providing instructions and information about the project.
### Functionality
Sentiment Analysis:
Utilizes a sentiment analysis model "j-hartmann/emotion-english-distilroberta-base" based on DistilRoBERTa to analyze sentiment from book reviews.
Preprocesses reviews by removing stopwords and other data cleaning methods before analysis.
Book Recommendation System:
Users interact with the system by selecting desired literary genres and emotional experiences they seek from reading.
The system filters book data based on user preferences and suggests relevant books.
Provides detailed book descriptions and purchase links.
### Authors
Ludovica Mastrantuono, Michela Carriera

