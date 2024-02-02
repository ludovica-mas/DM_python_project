import pandas as pd
from transformers import pipeline
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Load the emotion analysis model
emotion_analyzer = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

#Define a function for text preprocessing
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
  
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    processed_text = ' '.join(filtered_words)
    return processed_text

#Load your Excel sheet into a DataFrame
df = pd.read_excel(r"C:\Users\990840\Desktop\database_libri_python.xlsx")
print(df.head())

#Apply preprocessing to the 'Reviews' column
df['Reviews_processed'] = df['Reviews'].apply(preprocess_text)

#Apply emotion analysis to the 'Reviews_processed' column
df['Emotion'] = df['Reviews_processed'].apply(lambda x: emotion_analyzer(x)[0]['label'])

print(df)
df.to_excel('percorso_del_tuo_nuovo_file.xlsx', index=False)

#User interaction to suggest a book
def suggest_books():
    print("Good morning dear reader, today I would like to suggest some very interesting books, voted among the best of 2023 according to Goodreads' ranking.")

    # Ask for the desired literary genre
    genre_input = input("To suggest the most suitable one for your desires, please indicate one of these literary genres: fiction, history, mystery and thriller, horror, fantasy, science fiction, romance, young adult, nonfiction, humor\n")

    # Ask for the desired emotion
    emotion_input = input("To propose the suitable story, tell me what emotion you would like to feel while reading: anger, fear, joy, neutral, disgust, sadness, surprise.\n")


    # Filter the DataFrame based on user responses
    filtered_df = df[((df['Genre'].apply(lambda x: genre_input in x))) |
                      (df['Subgenre'].apply(lambda x:genre_input in x)) &
                     (df['Emotion'].apply(lambda x: emotion_input in x))]

    # Display the titles and authors of suggested books
    if not filtered_df.empty:
        print("\nHere are some books that might interest you:")
        for index, row in filtered_df.iterrows():
            print(f"Title: {row['Title']}\nAuthor: {row['Author']}\n")

        # Ask the user which book they are interested in
        chosen_book_title = input("Which book are you interested in? Enter the title here:\n")

        # Get information corresponding to the user's choice
        chosen_book_info = filtered_df[filtered_df['Title'] == chosen_book_title].iloc[0]

        # Display the book description
        print("\nHere is the book's description:")
        print(chosen_book_info['Description'])

        # Display the price and purchase link
        print(f"\nYou can purchase this book for {chosen_book_info['Price']} euro on Amazon through this link: {chosen_book_info['Amazon Link']}")
    else:
        print("\nI'm sorry, I couldn't find books that match your preferences.")

def main():
    while True:
        suggest_books()

        # Ask the user if they want another suggestion
        another_suggestion = input("Do you want to get another book suggestion? (yes/no)\n").lower()

        # If the answer is not "yes," exit the loop
        if another_suggestion != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
