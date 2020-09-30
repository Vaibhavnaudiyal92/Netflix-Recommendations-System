import pickle
import pandas as pd

dataset = pd.read_csv(path of movie dataset)
from sklearn.feature_extraction.text import TfidfVectorizer

tfv = TfidfVectorizer(min_df=3,  max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 6),
            stop_words = 'english')


indices = pd.Series(dataset.index, index=dataset['title_lower']).drop_duplicates()

# Fitting the TF-IDF on the 'overview' text
tfv_matrix = tfv.fit_transform(dataset['Information'])

from sklearn.metrics.pairwise import sigmoid_kernel

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

def recommendation(title, sig=sig):
    # Get the index corresponding to original_title
    title = title.lower()
    idx = indices[title]

    # Get the pairwsie similarity scores
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 10 most similar movies
    sig_scores = sig_scores[1:11]

    # Movie indices
    movie_indices = [i[0] for i in sig_scores]

    # Top 10 most similar movies
    return dataset.iloc[movie_indices]


