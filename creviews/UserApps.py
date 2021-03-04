from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from creviews.dataScraping import id_check, get_app_details_using_id
from creviews.models import App


def registered_app(request):
    app_id = request.POST['app_ID']
    user = request.user
    if id_check(app_id):
        app_name, app_category = get_app_details_using_id(app_id)
        if App.objects.filter(app_ID=app_id, name=app_name, category=app_category).exists():
            messages.info(request, "*Application exits* ")
            return HttpResponseRedirect('profile')
        else:
            b = App(app_ID=app_id, name=app_name, category=app_category, user=user)
            b.save()
    else:
        messages.info(request, "*Invalid App ID* ")
        return HttpResponseRedirect('profile')

    return redirect('apps')


def delete_app(request, pk):
    appDelete = App.objects.get(app_ID=pk)
    if request.method == 'POST':
        appDelete.delete()
        return redirect('apps')

    return render(request, 'delete_app.html', {'title': 'Delete apps'})


def display_apps(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('login')
    current_user = request.user
    user_id = current_user.id
    data = App.objects.filter(user_id=user_id)
    context = {

        'title': 'Apps',
        'reviews_data': data
    }
    return render(request, 'view_app.html', context)
