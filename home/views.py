from django.shortcuts import render


# Create your views here.


# Step 2: Defining about function

# Step 3: Will be done by creating the html page

def index(request):
    template_data ={}
    template_data['title'] = 'Home Page'
    return render(request, 'home/index.html' ,{'template_data':template_data})

def about(request):
    template_data ={}
    template_data['title'] = 'About'
    return render(request, 'home/about.html',{'template_data':template_data})



# The render function takes the request as the first argument,
# and the second argument ('home/index.html') represents the path to the templates file to be rendered.
