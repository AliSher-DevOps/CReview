import play_scraper
from google_play_scraper import Sort, reviews
import pandas as pd


def get_most_relevant_reviews(id):
    result, continuation_token = reviews(
        id,
        lang='en',  # defaults to 'en'
        country='us',  # defaults to 'us'
        sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
        count=100,  # defaults to 100
    )
    df = pd.DataFrame(result)
    review_id = []
    content = []
    rating = []
    user_name = []
    date = []
    for username in df['userName']:
        user_name.append(username)
    for rewID in df['reviewId']:
        review_id.append(rewID)
    for contents in df['content']:
        content.append(contents)
    for score in df['score']:
        rating.append(score)
    for datetime in df['at']:
        date.append(datetime)
    return review_id, content, rating, user_name, date


def id_check(id):
    status = False
    result, continuation_token = reviews(
        id,
        count=1,
    )
    if len(result) != 0:
        status = True
    return status


def get_app_details_using_id(id):
    app_detail = play_scraper.details(id)
    title = app_detail['title']
    category = app_detail['category']
    new_string = str(category)[1:-1]
    category_new = new_string.replace("'", "")
    return title, category_new
