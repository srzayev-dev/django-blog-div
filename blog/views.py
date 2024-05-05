from django.shortcuts import render


def home(request):
    #return HttpResponse('<h1>Hello World</h1>')
    context = {
        'name': 'Seymur Rzayev',
        'Sadiq': '27',
    }
    return render(request, 'home.html', context)

