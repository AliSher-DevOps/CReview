from creviews.models import Review
from creviews.models import Report
from creviews.sentimentalAnalysis import predict_review
from appAnalyzerReplies import predict
from creviews.models import Reply
from datetime import datetime

now = datetime.now()
today_date = now.strftime("%Y-%m-%d")


def perform_sentimental_analysis(app_bundle):
    for app in app_bundle:
        data = Review.objects.filter(app=app.app_ID)
        for review_data in data:
            result_sentiment = predict_review(review_data.content)
            if Report.objects.filter(review=review_data, result=result_sentiment).exists():
                pass
            else:
                b = Report(review=review_data, result=result_sentiment, date=today_date)
                b.save()


def generate_replies(app_bundle):
    for app in app_bundle:
        data = Review.objects.filter(app=app.app_ID)
        for review_data in data:
            result_reply = predict(review_data.content)
            if Reply.objects.filter(review=review_data, reply_content=result_reply).exists():
                pass
            else:
                b = Reply(review=review_data, reply_content=result_reply, date=today_date)
                b.save()
