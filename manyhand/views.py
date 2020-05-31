from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'manyhand/index.html', context)

