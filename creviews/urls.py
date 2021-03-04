from django.urls import path
from . import views
from creviews import UserApps, UserProfile, ReviewsReport, RepliesReport, Analyze, User

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('forgetPassword', views.forget_password, name='forget_password'),
    path('resetPassword', User.reset_account_password, name='reset_password'),
    path('updatePassword', views.update_password, name='update_password'),
    path('home', User.register_user, name='home'),
    path('homeMenu', User.login_user, name='home_menu'),
    path('dashboard', Analyze.dashboard, name='dashboard'),
    path('chatBot', RepliesReport.weekly_replies_report, name='chatBot'),
    path('profile', UserProfile.display_profile, name='profile'),
    path('updateProfile', UserProfile.update_profile, name='update_Profile'),
    path('changePassword', UserProfile.change_password, name='change_password'),
    path('apps', UserApps.display_apps, name='apps'),
    path('addApps', UserApps.registered_app, name='add_app_details'),
    path('delete_items/<str:pk>/', UserApps.delete_app, name="delete_items"),
    path('reports', ReviewsReport.weekly_review_report, name='reports'),
    path('logout', views.logout, name='logout'),
    path('user_del', User.user_del, name='user_del'),
    path('send_complain', User.send_complain, name="send_complain"),
    path('monthlyReport', ReviewsReport.monthly_review_report, name="monthly_Report"),
    path('monthlyReplies', RepliesReport.monthly_replies_report, name="monthly_Replies"),
    path('analysis', Analyze.analysis_home, name="monthly_Replies"),
    path('processing', Analyze.processing_data, name='processing_data'),

    path('weeklyReportPositive', ReviewsReport.weekly_positive_review_report, name='positive_data'),
    path('weeklyReportNegative', ReviewsReport.weekly_negative_review_report, name='negative_data'),
    path('weeklyReportNeutral', ReviewsReport.weekly_neutral_review_report, name='neutral_data'),
    path('weeklyReportAppreciation', ReviewsReport.weekly_appreciation_review_report, name='appreciation_data'),
    path('weeklyReportBugs', ReviewsReport.weekly_bug_report_review_report, name='bug_report_data'),
    path('weeklyReportFeature', ReviewsReport.weekly_feature_suggestion_review_report, name='featureSuggestion_data'),
    path('weeklyReportExperience', ReviewsReport.weekly_personal_experience_review_report,
         name='personalExperienceData'),
    path('weeklyReportQuestion', ReviewsReport.weekly_question_review_report, name='question_data'),
    path('weeklyReportCrash', ReviewsReport.weekly_crash_report_review_report, name='crash_report_data'),

    path('monthlyReportPositive', ReviewsReport.monthly_positive_review_report),
    path('monthlyReportNegative', ReviewsReport.monthly_negative_review_report),
    path('monthlyReportNeutral', ReviewsReport.monthly_neutral_review_report),
    path('monthlyReportAppreciation', ReviewsReport.monthly_appreciation_review_report),
    path('monthlyReportBugs', ReviewsReport.monthly_bug_report_review_report),
    path('monthlyReportFeature', ReviewsReport.monthly_feature_suggestion_review_report),
    path('monthlyReportExperience', ReviewsReport.monthly_personal_experience_review_report),
    path('monthlyReportQuestion', ReviewsReport.monthly_question_review_report),
    path('monthlyReportCrash', ReviewsReport.monthly_crash_report_review_report),

]