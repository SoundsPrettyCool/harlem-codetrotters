# from keybert import KeyBERT
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
nltk.download('stopwords')
nltk.download('punkt')

def get_time(time_str_input):
    time_str_input = time_str_input.replace("\n", "")
    time_str_input = time_str_input[1:-2]
    return time_str_input


def classify_text(text_input, model):
    text_input = text_input.replace("\n", "")
    labels = f"{model}"
    # labels = model.extract_keywords(text_input, keyphrase_ngram_range=(1, 3), stop_words="english", top_n=12)
    return labels

def remove_stop_words(input_text):
    tokens = word_tokenize(input_text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in tokens if word not in stop_words]
    cleaned_text = " ".join(filtered_words)
    return cleaned_text

def remove_punctuation(input_text):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = input_text.translate(translator)
    return clean_text

with open("../data/sample_data.txt") as f:
    data = f.readlines()
    data = [d.strip() for d in data if len(d.strip()) > 0]
    results = []
    i = 0
    while i < len(data):
        single_entry = {"name": "", "time": "", "text": "", "labels": []}
        speaker, text = data[i: i + 2]
        all_data = speaker.split(" ")
        if len(all_data) == 2:
            name = all_data[0]
            time_str = all_data[1]
        elif len(all_data) == 3:
            first_str = all_data[0]
            second_str = all_data[1]
            name = f"{first_str} {second_str}"
            time_str = all_data[2]
        else:
            name = all_data[0]
            second_str = ""
            print(all_data)
        time_str = get_time(time_str)

        clean_text = remove_stop_words(text.lower())
        clean_text = remove_punctuation(clean_text)

        position = classify_text(text, i)

        single_entry["name"] = name
        single_entry["time"] = time_str
        single_entry["text"] = clean_text
        single_entry["labels"] = position
        results.append(single_entry)
        i += 2

pd.DataFrame(results).to_csv("../data/cleaned_data.csv", index=False)



print("DONE Preprocessing")


