from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q

from .models import Posts


def get_category_count():
    queryset = Posts.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset


def search(request):
    queryset = Posts.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'query': query,
    }
    return render(request,'search_results.html', context)


def home(request):

    category_count = get_category_count()

    featured = Posts.objects.filter(featured=True)
    all_posts = Posts.objects.all().order_by('-timestamp')
    latest = Posts.objects.order_by('-timestamp')[0:3]

    paginator = Paginator(all_posts, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'obj_list': featured,
        # 'all_posts': all_posts,
        'queryset': paginated_queryset, # menja allpost
        'latest': latest,
        'page_request_var': page_request_var,
        'category_count': category_count,
    }

    return render(request, 'index.html', context)



def post_detail(request, id):

    post_detail = Posts.objects.get(id=id)

    context = {
        'post_detail': post_detail,
    }
    return render(request, 'post-detail.html', context)
