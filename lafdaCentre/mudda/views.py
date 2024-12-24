from django.shortcuts import render
from .models import Mudda, SearchQuery, Comment
from .forms import MuddaForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q #The Q object is a powerful tool provided by Django's ORM that allows you to create complex database queries using Python code.
# Create your views here.

def index(request):
    return render(request, 'index.html')

# view01: lisitng all muddaas
def mudda_list(request):
    muddas=Mudda.objects.all().order_by('-created_at')
    return render(request, 'mudda_list.html', {'muddas':muddas})

# view02: create mudda (yhi std way hai!!)
@login_required
def mudda_create(request):
    if request.method=="POST":
        form = MuddaForm(request.POST, request.FILES)
        if form.is_valid(): #jb bhi form save hota hai, user bydefault aata hai 
            mudda=form.save(commit=False)
            mudda.userID=request.user
            mudda.save()
            return redirect('mudda_list')
    else:
        form=MuddaForm()
    return render(request, 'mudda_form.html', {'form':form})

#view03: editing our tweet
@login_required
def edit_mudda(request, mudda_id):
    mudda=get_object_or_404(Mudda, pk=mudda_id, userID=request.user)
    if request.method=='POST':
        form = MuddaForm(request.POST, request.FILES, instance=mudda)
        if form.is_valid():
            mudda=form.save(commit=False)
            mudda.userID=request.user
            mudda.save()
            return redirect('mudda_list')

    else:
        form=MuddaForm(instance=mudda)
        
        return render(request, 'mudda_form.html', {'form':form})
    
#view04: delete mudda
def del_mudda(request, mudda_id):
    mudda=get_object_or_404(Mudda, pk=mudda_id, userID=request.user)
    if request.method=='POST':
        mudda.delete()
        return redirect('mudda_list')
    return render(request, 'mudda_del_confirm.html', {'mudda':mudda})

def register(request):
        if request.method=='POST':
            form=UserRegistrationForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request, user)
                return redirect('mudda_list')
        else:
            form=UserRegistrationForm()
        
        return render(request, 'registration/register.html', {'form': form})

def searchMudda(request):
    query = request.GET.get('q', '')
    if query:
        muddas = Mudda.objects.filter(
            Q(mudda_desc__icontains=query) |
            Q(userID__username__icontains=query)
        )
    else:
        muddas = []

    return render(request, 'search.html', {'muddas': muddas, 'query': query})

@login_required
def like_mudda(request, mudda_id):
    mudda=get_object_or_404(Mudda, id=mudda_id)
    if request.user in mudda.likes_count.all():
        mudda.likes_count.remove(request.user) #agr same user hua to remove krdo :)

    else:
        mudda.likes_count.add(request.user) #agr like nhi hai, to like krdo

    return redirect('mudda_list')

@login_required
def add_comment(request, mudda_id):
    mudda = get_object_or_404(Mudda, id=mudda_id)
    if request.method == 'POST':
        content=request.POST.get('content')
        if content:  # Ensure the comment is not empty
            Comment.objects.create(mudda=mudda, user=request.user, content=content)
    return redirect('mudda_list')  # Redirect back to the mudda list or detail page
            
