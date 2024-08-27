import pandas as pd
from prompts import male_names, female_names
from gensim.models import Word2Vec
from gensim.utils import tokenize, simple_preprocess

stopwords = [ 'stop', 'the', 'to', 'and', 'a','an', 'in', 'who', 'about', 'it', 'is', 'am', 'are' 'I', 'that', 'had', 'on', 'for', 'were', 'was', 'of', 'with', 'every', 'into', 'as', 'each', 'but', 'under', 'at']
name_lst = male_names + female_names


#   Function remove_data, takes sentece as one string, output the string cleaned for names and specific words 
def remove_names_stopwords(input_string):
    word_tokens = tokenize(input_string)
    # Remove names and custom stopwords
    cleaned_string = [w for w in word_tokens if not w in name_lst]
    cleaned_string = [w for w in cleaned_string if not w in stopwords]
    return cleaned_string

dir = ''
df = pd.read_csv(dir, sep=',')

# preprocces text data 
data = pd.DataFrame(data=df['Answer'].apply(lambda s: str(remove_names_stopwords(s))))
data = data.apply(simple_preprocess)

# create a W2V-model
model = Word2Vec(
        window=10,
        min_count=2,
)

# build vocabulary of the text data 
model.build_vocab(data, progress_per=1000)

# train the model 
model.train(data, total_examples=model.corpus_count, epochs=model.epochs)

# save the model 
model_dir = ''
model.save(model_dir)

