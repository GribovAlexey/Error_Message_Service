from django.contrib.auth.models import User


def user_count(request):
    print("I am here")
    users = User.objects.all().count() if User.objects.all().count() else 0
    print(users)
    return {'user_amount': users}
