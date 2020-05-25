from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
    
def people(request):
    return render(request, 'people.html')

def sns(request):
    return render(request, 'sns.html')
    
def milestone(request):
    return render(request, 'milestone.html')

def error404(request):
    return render(request, "404.html", status=404)

def error500(request):
    return render(request, "404.html", status=500)