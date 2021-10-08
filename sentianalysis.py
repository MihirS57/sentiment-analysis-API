import spacy
import nltk
''' nltk.download("vader_lexicon")
nltk.download("punkt") '''
from nltk.sentiment.vader import SentimentIntensityAnalyzer

token_list = []
filter_token = []
lemma = []
nlp = spacy.load("en_core_web_sm")

def get_me_my_result(phrase):
    doc = nlp(phrase)
    print(doc)
    token_list = [token for token in doc]
    filter_token = [token for token in token_list if not token.is_stop]
    lemma = [token.lemma_ for token in filter_token]
    final = ""
    for item in lemma:
        final = final+item+" "
    sia = SentimentIntensityAnalyzer()
    senti_dict = sia.polarity_scores(phrase)
    return senti_dict;
