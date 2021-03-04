import joblib
import pandas as pd
import string
import re
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer

ngram_cv = CountVectorizer(binary=True, ngram_range=(1, 2))


def svm_model():
    heshe = stopwords.words('english')
    nltk.download('stopwords')
    nltk.download('wordnet')
    df = pd.read_csv('creviews/datasetSA.csv')
    replace_wo_space = re.compile("[.;:!\'?,\"()\[\]]")
    replace_with_space = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")
    reviews = df['review'].str.replace(replace_wo_space, '').str.lower()
    reivews = reviews.str.replace(replace_with_space, '')
    reviews_stopworded = reviews.apply(lambda x: ' '.join([word for word in str(x).split()
                                                           if word not in heshe]))
    lem = WordNetLemmatizer()
    reviews_lem = reviews_stopworded.apply(lambda x: ' '.join([lem.lemmatize(word) for word in str(x).split()]))
    ngram_cv.fit(reviews_lem)
    X = ngram_cv.transform(reviews_lem)
    target = df['Sentiment'].astype(str)
    X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.2, random_state=42)
    # I had to set the max_iter because it was not able to converge the SVM in the default 1,000 iterations
    grid_params = {'C': [0.25, 0.5, 0.75, 1.0]}
    svm = GridSearchCV(LinearSVC(multi_class='ovr', max_iter=50000, random_state=42), grid_params, cv=5)
    svm.fit(X_train, y_train)
    y_train_pred = svm.predict(X_train)
    # print("Training accuracy is {}".format(accuracy_score(y_train, y_train_pred)))
    y_test_pred = svm.predict(X_test)
    # print("Testing accuracy is {}".format(accuracy_score(y_test, y_test_pred)))
    filename = 'finalized_model.sav'
    joblib.dump(svm, filename)


def get_word_net_pos(pos_tag):
    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def clean_text(text):
    # lower text
    text = text.lower()
    # tokenize text and remove puncutation
    text = [word.strip(string.punctuation) for word in text.split(" ")]
    # remove words that contain numbers
    text = [word for word in text if not any(c.isdigit() for c in word)]
    # remove stop words
    stop = stopwords.words('english')
    text = [x for x in text if x not in stop]
    # remove empty tokens
    text = [t for t in text if len(t) > 0]
    # pos tag text
    pos_tags = pos_tag(text)
    # lemmatize text
    text = [WordNetLemmatizer().lemmatize(t[0], get_word_net_pos(t[1])) for t in pos_tags]
    # remove words with only one letter
    text = [t for t in text if len(t) > 1]
    # join all
    text = " ".join(text)
    return text


def predict_review(review):
    loaded_model = joblib.load('finalized_model.sav')
    text_clean = clean_text(review)
    s = pd.Series(text_clean)
    s = ngram_cv.transform(s)
    result = loaded_model.predict(s)
    new_result = str(result)[1:-1]
    sentiment = new_result.replace("'", "")
    return sentiment
