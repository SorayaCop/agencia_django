from agencia_app.models import Post
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
    
def blog(request):
        post = Post.objects.all( )
        return render(request, 'blog.html', {'post' : post})

def about(request):
    return render(request, 'about.html')



def post_detail(request, id):
    template_name = 'new.html' 
    new = Post.objects.get(id=id) 
    context = { 'post': new }
        
    return render(request, template_name, context) 


