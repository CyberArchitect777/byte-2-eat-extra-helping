from django.shortcuts import render


def display_about(request):

    return render(
        request,
        "about/about.html", {
        }
    )
