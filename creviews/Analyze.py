from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from creviews.dataScraping import get_most_relevant_reviews
from creviews.models import App, Report
from creviews.models import Review
from creviews.dataForAnalysis import perform_sentimental_analysis, generate_replies

from datetime import datetime
from datetime import timedelta

now = datetime.now()
today_date = now.strftime("%Y-%m-%d")


def analysis_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')

    current_user = request.user
    user_id = current_user.id
    if App.objects.filter(user_id=user_id).exists():
        context = {
            'title': 'Analysis',
        }
        return render(request, 'analyze.html', context)
    else:
        context = {
            'title': 'Analysis',
        }
        return render(request, 'managesource.html', context)


def processing_data(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    for app_bundle in data:
        review_id, content, rating, user_name, date_time = get_most_relevant_reviews(app_bundle.app_ID)
        for rev_id, rev, score, name, date_time_rev in zip(review_id, content, rating, user_name, date_time):
            if Review.objects.filter(review_ID=rev_id, content=rev, date=date_time_rev, rating=score, app=app_bundle,
                                     reviewer_username=name).exists():
                pass
            else:
                b = Review(review_ID=rev_id, content=rev, date=date_time_rev, rating=score, app=app_bundle,
                           reviewer_username=name)
                b.save()
    perform_sentimental_analysis(data)
    generate_replies(data)

    return redirect('dashboard')


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id

    if App.objects.filter(user_id=user_id).exists():
        data_app = App.objects.filter(user_id=user_id)
        positive = 0
        negative = 0
        neutral = 0
        question = 0
        appreciation = 0
        bug_report = 0
        crash_report = 0
        feature_suggestion = 0
        personal_experience = 0
        total = 0
        for app in data_app:

            data_reviews = Review.objects.filter(app=app.app_ID)
            for review_data in data_reviews:
                data_report = Report.objects.filter(review=review_data.review_ID,
                                                    date__gte=now.date() - timedelta(days=7),
                                                    date__lte=today_date)
                for report in data_report:

                    if report.result == "Positive":
                        positive = positive + 1
                    elif report.result == "Negative":
                        negative = negative + 1
                    elif report.result == "Neutral":
                        neutral = neutral + 1
                    elif report.result == "Appreciation":
                        appreciation = appreciation + 1
                    elif report.result == "Bug Report":
                        bug_report = bug_report + 1
                    elif report.result == "Feature Suggestion":
                        feature_suggestion = feature_suggestion + 1
                    elif report.result == "Personal Experience":
                        personal_experience = personal_experience + 1
                    elif report.result == "Question":
                        question = question + 1
                    elif report.result == "Crash Report":
                        crash_report = crash_report + 1

        total = positive + negative + neutral + personal_experience + question + crash_report + bug_report + appreciation + feature_suggestion
        context = {
            'title': 'Dashboard',
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'appreciation': appreciation,
            'bug_report': bug_report,
            'feature_suggestion': feature_suggestion,
            'personal_experience': personal_experience,
            'question': question,
            'crash_report': crash_report,
            'total': total,
            'date': today_date

        }
        return render(request, 'dashboard.html', context=context)
    else:
        context = {
            'title': 'Dashboard',

        }
        return render(request, 'managesource.html', context=context)
