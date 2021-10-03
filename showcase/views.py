from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ShowcasePost
from .forms import PostForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('showcase')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




class showcase(ListView):
  template_name = 'showcase.html'

  def get_queryset(self):
    return ShowcasePost.objects.all()

def post_new(request):
  if(request.method == "POST"):
    form = PostForm(request.POST, request.FILES)
    if(form.is_valid()):
      post= form.save(commit=False)
      post.save()
      return redirect('showcase')
  else:
    form = PostForm()
  return render(request, 'post_edit.html', {'form': form})
