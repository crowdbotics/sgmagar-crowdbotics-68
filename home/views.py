from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'dj-paypal', 'url': 'http://pypi.python.org/pypi/dj-paypal/0.6.0'},
	{'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
	{'name':'aa_stripe', 'url': 'http://pypi.python.org/pypi/aa_stripe/0.4.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-68',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
