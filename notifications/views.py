from django.shortcuts import render, redirect

from .forms import Create_Notification_Form
from .models import Notifications
from users.models import CustomUser


# Create your views here.
def NotificationList(request):
    notifications = Notifications.objects.all()
    user = CustomUser.objects.get(username=request.user.username)
    context = {
        "notifications": notifications,
        "user": user
    }

    return render(request, template_name="notifications.html", context=context)


def Create_Notification(request):
    if request.user.is_staff:
        if request.method == 'POST':
            if request.user.is_authenticated:
                form = Create_Notification_Form(request.POST)
                if form.is_valid():
                    title = form.cleaned_data['title']
                    body = form.cleaned_data['body']
                    notification = Notifications.objects.create(
                        title=title,  # Replace with the actual field you want to save
                        body=body,
                    )
                    return redirect('home')
        else:
            form = Create_Notification_Form()
            return render(request, "create_notifications.html", {"form": form})
