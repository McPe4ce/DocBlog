from datetime import datetime
from django.shortcuts import render


def index(request):
    date = datetime.today()
    return render(request, "Docblog/index.html", context={"name": "Philip", "date": date})