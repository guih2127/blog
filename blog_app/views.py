from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.shortcuts import redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def post_list(request):
	all_posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
	paginator = Paginator(all_posts, 3)

	page = request.GET.get('page')
	posts = paginator.get_page(page)

	if 'search' in request.GET:
		search_term = request.GET['search']
		posts = all_posts.filter(Q(text__icontains=search_term) | Q(title__icontains=search_term))

	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
		 post = form.save(commit=False)
		 post.author = request.user	
		 post.published_date = timezone.now()
		 post.save()
		 return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form': form})