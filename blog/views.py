from django.shortcuts import render


post = [
    {'author': 'Harish Yadav',
     'title': 'Blog Post 1',
     'content': 'First Blog Post',
     'date_posted': '19 sept 2019',
    },

    {'author': 'Hawa Singh',
    'title': 'Blog Post 2',
    'content': 'Second Blog Post',
    'date_posted': '19 sept 2019',
    }
]


def home(request):
    context={
        'posts':post
    }
    return render(request, 'home.html',context)









