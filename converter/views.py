from django.shortcuts import render
from django.views.generic import View
from .forms import QuillForm
import json
from bs4 import BeautifulSoup


class Home(View):
    def get(self, request):
        form = QuillForm()
        context = {'form':form}
        return render(request, 'base.html', context)
    
    def post(self, request):
        html = request.POST['content']
        if html == None or html == '':
            clean_html = html
        else:
            clean_html = json.loads(html)['html']
            soup = BeautifulSoup(clean_html, 'html.parser')
            pretiffied_html = soup.prettify()
        context = {'html':pretiffied_html}
        return render(request, 'partials/converted.html', context)
