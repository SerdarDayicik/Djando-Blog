from django.shortcuts import render,redirect,get_object_or_404,reverse  
from .forms import ArticleForm
from .models import Article,Commentt
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",
                      {"articles": articles})
    articles = Article.objects.all()

    context = {
        "articles" : articles 
    }
    return render(request,"articles.html",context)









def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
       article = form.save(commit=False)
       article.author = request.user
       article.save()
       messages.success(request,"Başariyla Makale Oluşturuldu") 
       return redirect("article:dashboard")
    
    context={
        "form":form
    }
    return render(request,"addarticle.html",context)

def detail(request,id):
    article = Article.objects.filter(id = id).first()
    comments = article.comments.all()
    context = {
        "article":article,
        "comments": comments
    }
    return render(request,"detail.html",context)

@login_required(login_url="user:login")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
       article = form.save(commit=False)
       article.author = request.user
       article.save()
       messages.success(request,"Başariyla Makale Oluşturuldu") 
       return redirect("article:dashboard")
    context = { 
        "form": form
    }
    return render(request,"update.html",context)

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request,"Makale Başariyla silindi")
    return redirect("article:dashboard")


def addComment(request,id):
    article = get_object_or_404(Article,id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Commentt(comment_author = comment_author,comment_content = comment_content)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))