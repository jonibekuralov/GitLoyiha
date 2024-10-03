from django.shortcuts import render, get_object_or_404
from .models import Category, News
from django.http import Http404


# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {'news_list': news_list}

    return render(request, "news/news_list.html", context=context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {'news': news}

    return render(request, "news/news_detail.html", context=context)


def HomePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:3]
    local_1 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[1]
    local_2 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[2]
    local_3 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[3]
    local_4 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[4]
    sport_1 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[1]
    sport_2 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[2]
    sport_3 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[3]
    sport_4 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[4]
    jahon_one = News.published.all().filter(category__name="Jahon").order_by("-publish_time")
    qiziqarli_yangilik = News.published.all().filter(category__name="Qiziqali_yangilik").order_by("-publish_time")
    iqtisodiyot1 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[1]
    iqtisodiyot2 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[2]
    iqtisodiyot3 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[3]
    iqtisodiyot4 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[4]
    fan_texnika = News.published.all().filter(category__name="FAN_TEXNIKA").order_by("-publish_time")[0]
    fan_texnika2 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[0]
    fan_texnika3 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[1]
    fan_texnika4 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[2]
    fan_texnika5 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[3]
    jamiyat1 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[0]
    jamiyat2 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[1]
    jamiyat3 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[2]
    jamiyat4 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[3]
    jamiyat5 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[4]
    context = {
        "news_list": news_list,
        "categories": categories,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "jahon_one": jahon_one,
        "sport_1": sport_1,
        "sport_2": sport_2,
        "sport_3": sport_3,
        "sport_4": sport_4,
        "qiziqarli_yangilik": qiziqarli_yangilik,
        "iqtisodiyot1": iqtisodiyot1,
        "iqtisodiyot2": iqtisodiyot2,
        "iqtisodiyot3": iqtisodiyot3,
        "iqtisodiyot4": iqtisodiyot4,
        "fan_texnika1": fan_texnika,
        "fan_texnika2": fan_texnika2,
        "fan_texnika3": fan_texnika3,
        "fan_texnika4": fan_texnika4,
        "fan_texnika5": fan_texnika5,
        "jamiyat1": jamiyat1,
        "jamiyat2": jamiyat2,
        "jamiyat3": jamiyat3,
        "jamiyat4": jamiyat4,
        "jamiyat5": jamiyat5,
    }

    return render(request, 'news/index.html', context)


def UzbekistanPageview(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[0]
    local_1 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[9]
    local_11 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[10]
    local_12 = News.published.all().filter(category__name="Uzbekistan").order_by("-publish_time")[11]

    context = {
        "categories": categories,
        "news_list": news_list,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
    }

    return render(request, 'news/uzbekistan.html', context)


def JahonPageview(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[0]
    local_1 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[9]
    local_11 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[10]
    local_12 = News.published.all().filter(category__name="Jahon").order_by("-publish_time")[11]

    context = {
        "categories": categories,
        "news_list": news_list,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
    }

    return render(request, 'news/jahon.html', context)


def Fan_texnikaPageview(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[0]
    local_1 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[9]
    local_11 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[10]
    local_12 = News.published.all().filter(category__name="Fan_texnika").order_by("-publish_time")[11]

    context = {
        "categories": categories,
        "news_list": news_list,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
    }

    return render(request, 'news/fan_texnika.html', context)


def IqtisodiyotPageview(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[0]
    local_1 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[9]
    local_11 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[10]
    local_12 = News.published.all().filter(category__name="Iqtisodiyot").order_by("-publish_time")[11]

    context = {
        "categories": categories,
        "news_list": news_list,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
    }

    return render(request, 'news/Iqtisodiyot.html', context)


def SportPageview(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[0]
    local_1 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[9]
    local_11 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[10]
    local_12 = News.published.all().filter(category__name="Sport").order_by("-publish_time")[11]

    context = {
        "categories": categories,
        "news_list": news_list,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
    }

    return render(request, 'news/Sport.html', context)


def JamiyatPageview(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[0]
    local_1 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[0]
    local_2 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[1]
    local_3 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[2]
    local_4 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[3]
    local_5 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[4]
    local_6 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[5]
    local_7 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[6]
    local_8 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[7]
    local_9 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[8]
    local_10 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[9]
    local_11 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[10]
    local_12 = News.published.all().filter(category__name="Jamiyat").order_by("-publish_time")[11]

    context = {
        "categories": categories,
        "news_list": news_list,
        "local_1": local_1,
        "local_2": local_2,
        "local_3": local_3,
        "local_4": local_4,
        "local_5": local_5,
        "local_6": local_6,
        "local_7": local_7,
        "local_8": local_8,
        "local_9": local_9,
        "local_10": local_10,
        "local_11": local_11,
        "local_12": local_12,
    }

    return render(request, 'news/jamiyat.html', context)


def contact(request):
    data = News.objects.filter(status=News.Status.Published)
    category = Category.objects.all()

    context = {
        "data": data,
        "category": category
    }

    return render(request, 'news/contact.html', context)


def single(request):
    data = News.objects.filter(status=News.Status.Published)
    category = Category.objects.all()

    context = {
        "data": data,
        "category": category
    }

    return render(request, 'news/single.html', context)







# from django.shortcuts import render, redirect
# from .models import Video
# from .forms import VideoForm
#
# def video_list(request):
#     videos = Video.objects.all()
#     return render(request, 'news/video_list.html', {'videos': videos})
#
# def upload_video(request):
#     if request.method == 'POST':
#         form = VideoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('video_list')
#     else:
#         form = VideoForm()
#     return render(request, 'news/upload_video.html', {'form': form})
