import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Creating DataFrame from CSV
file_path = "data/faq.csv"#creates a string to hold the file path
print(type(file_path)) # confirming var file_path is a str

df = pd.read_csv(file_path, header=0, )#requires a string

df.dropna(inplace=True)

vectorizer = TfidfVectorizer()#wizardry that is able to 'Convert a collection of raw documents to a matrix of TF-IDF features.'
vectorizer.fit(np.concatenate((df.Question, df.Answer)))#

vectorized_questions = vectorizer.transform(df.Question)#vectorizing the questions from faq
vectorized_answers = vectorizer.transform(df.Answer)#vectorizing the answers from faq

def start_chatbot():
    """Initialize and run the chatbot conversation"""
    print("Chatbot initialized! Ask me questions about Daniel Garcia. Type 'quit' to exit.")
    while True:
        question = input("You: ")

        # Exit condition
        if question.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        vectorized_user_question = vectorizer.transform([question])#vectorizing the user question
        similarities = cosine_similarity(vectorized_user_question, vectorized_questions)#gets list of possible matching questions
        closest_question = np.argmax(similarities, axis=1)# gets the highest match from vectorized data.
        print(f"Chatbot: {df.Answer.iloc[closest_question].values[0]}")

        break
start_chatbot()