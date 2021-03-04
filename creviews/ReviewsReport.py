from django.http import HttpResponseRedirect
from django.shortcuts import render
from creviews.models import App
from creviews.models import Review
from creviews.models import Report
from datetime import datetime
from datetime import timedelta

now = datetime.now()
today_date = now.strftime("%Y-%m-%d")


def weekly_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_positive_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Positive',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_negative_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Negative',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_neutral_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Neutral',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_appreciation_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Appreciation',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_bug_report_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Bug Report',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_feature_suggestion_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Feature Suggestion',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_personal_experience_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Personal Experience',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_crash_report_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Crash Report',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def weekly_question_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Question',
                                                date__gte=now.date() - timedelta(days=7),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'reports.html', context)


def monthly_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)

    context = {
        'day_title': 'Monthly Report',
        'title': 'Download',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }

    return render(request, 'MonthlyReports.html', context)


def monthly_positive_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Positive',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_negative_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Negative',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_neutral_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Neutral',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_appreciation_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Appreciation',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_bug_report_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Bug Report',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_feature_suggestion_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Feature Suggestion',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_personal_experience_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Personal Experience',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_crash_report_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Crash Report',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)


def monthly_question_review_report(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    date_review = []
    date_analysis = []
    review_rating = []
    reviews = []
    sentiment = []
    user_name = []
    for app in data:
        data_review = Review.objects.filter(app=app.app_ID)
        for review in data_review:
            data_report = Report.objects.filter(review=review.review_ID, result='Question',
                                                date__gte=now.date() - timedelta(days=30),
                                                date__lte=today_date)
            for report in data_report:
                date_analysis.append(report.date)
                date_review.append(review.date)
                user_name.append(review.reviewer_username)
                reviews.append(review.content)
                review_rating.append(review.rating)
                sentiment.append(report.result)
    context = {
        'day_title': 'Weekly Report',
        'title': 'Reports',
        'reviews_data': zip(date_analysis, date_review, user_name, reviews, review_rating, sentiment),
    }
    return render(request, 'MonthlyReports.html', context)
