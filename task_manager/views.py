from django.shortcuts import render
from django.utils.translation import gettext as _

class User:
    pass


def index(request):
    user = User()
    user.auth = 0
    return render(
        request,
        "index.html",
        context={'user': user}
    )