from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def article(request, num_article):
    if num_article not in ["01", "02", "03"]:
        return render(request, f"blog/article_not_found.html")
    return render(request, f"blog/article_{num_article}.html")