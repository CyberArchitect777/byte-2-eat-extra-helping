from django.shortcuts import render

# Create your views here.


def display_index(request):

    return render(
        request,
        "index/index.html", {
        }
    )
