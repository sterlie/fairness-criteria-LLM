
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

from prompts import male_names, female_names

# Import data into data-frame
directory = ''
df = pd.read_csv(directory, sep=' ')

male_names = [n.lower() for n in male_names]
female_names = [n.lower() for n in female_names]
name_lst = male_names + female_names

def custom_tokenizer(text):
    # Tokenizer-pattern to ignore hyphens as seperators 
    pattern = r"(?u)\b[\w-]+\b"  # Matches words containing letters, hyphens, and apostrophes

    tokens = re.findall(pattern, text)
    # Filter out single-letter tokens
    tokens = [token for token in tokens if len(token) > 1]
    # Filter out names 
    tokens = [w for w in tokens if not w in name_lst]

    return tokens

# Define stopwords 
stopwords = set([ 'stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were', 'was', 'of', 'with', 'every', 'into', 'as', 'each', 'but', 'under', 'at'])

# Function returnning Bag of words of given data 
def BoW(data):
    vectorizer = CountVectorizer(tokenizer=custom_tokenizer, stop_words=stopwords)
    X = vectorizer.fit_transform(data)
    df_bow = pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names_out())

    word_counts = df_bow.sum(axis=0)

    # Create a DataFrame to store word counts and sort it in descending order
    word_counts_df = pd.DataFrame({'Word': word_counts.index, 'Count': word_counts.values})
    word_counts_df = word_counts_df.sort_values(by='Count', ascending=False)
    
    return word_counts_df
