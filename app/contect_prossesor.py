from .models import News, Category, ContactData


def lasted_news(request):
    lasted_news = News.published.all().order_by("-publish_time")[:10]
    categories = Category.objects.all()
    contact_data = ContactData.objects.all()
    context = {
        'lastest_news': lasted_news,
        'categories': categories,
        'contact_data': contact_data
    }
    return context