from django.http import HttpResponseRedirect
from django.shortcuts import render
from creviews.models import App
from creviews.models import Review
from creviews.models import Reply
from datetime import datetime
from datetime import timedelta

now = datetime.now()
today_date = now.strftime("%Y-%m-%d")


def weekly_replies_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_reply = []
    reviews = []
    replies = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID, date__gte=now.date() - timedelta(days=7),
                                            date__lte=today_date)
        for review in data_review:
            data_report = Reply.objects.filter(review=review.review_ID, date__gte=now.date() - timedelta(days=7),
                                               date__lte=today_date)
            for reply in data_report:
                date_review.append(review.date)
                date_reply.append(reply.date)
                reviews.append(review.content)
                replies.append(reply.reply_content)

    context = {
        'day_title': 'Weekly Report',
        'title': 'Download',
        'reviews_data': zip(date_review, date_reply, reviews, replies),
    }
    return render(request, 'chatBot.html', context=context)


def monthly_replies_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_reply = []
    reviews = []
    replies = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID, date__gte=now.date() - timedelta(days=30),
                                            date__lte=today_date)
        for review in data_review:
            data_report = Reply.objects.filter(review=review.review_ID, date__gte=now.date() - timedelta(days=30),
                                               date__lte=today_date)
            for reply in data_report:
                date_review.append(review.date)
                date_reply.append(reply.date)
                reviews.append(review.content)
                replies.append(reply.reply_content)

    context = {

        'title': 'Download',
        'day_title': 'Monthly Report',
        'reviews_data': zip(date_review, date_reply, reviews, replies),
    }
    return render(request, 'chatBot.html', context=context)
