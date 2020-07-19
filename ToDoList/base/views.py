from django.shortcuts import render

# Create your views here.

sampleToDos = [
    {
        'id': 1,
        'content': 'Study DP',
        'dateAdded': '24th August 2020',
        'deadline': '30th August 2020'
    },
    {
        'id': 2,
        'content': 'Study Binary Seach',
        'dateAdded': '15th August 2020',
        'deadline': '23th August 2020'
    }
]


def Home(request):
    context = {
        'toDos': sampleToDos,
        'title': 'Home'
    }
    return render(request, 'base/home.html', context)
