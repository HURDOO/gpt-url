from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URL
import string
import random

def home(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_url = generate_short_url()
        url = URL(long_url=long_url, short_url=short_url)
        url.save()
        short_url_full = request.build_absolute_uri('/') + short_url
        return render(request, 'shorten.html', {'short_url': short_url_full})
    return render(request, 'home.html')

def generate_short_url():
    letters = string.ascii_lowercase + string.digits
    while True:
        short_url = ''.join(random.choice(letters) for i in range(6))
        if not URL.objects.filter(short_url=short_url).exists():
            return short_url

def redirect_url(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
        return redirect(url.long_url)
    except URL.DoesNotExist:
        return HttpResponse('Short URL does not exist')

