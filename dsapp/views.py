from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
    
def people(request):
    return render(request, 'people.html')

def sns(request):
    return render(request, 'sns.html')
<<<<<<< HEAD
    
=======
    
def milestone(request):
    return render(request, 'milestone.html')
>>>>>>> deploy_v1
