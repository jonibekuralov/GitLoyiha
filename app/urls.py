from django.urls import path
from .views import news_list, news_detail, HomePageView, single, contact, UzbekistanPageview, JahonPageview, \
    Fan_texnikaPageview, IqtisodiyotPageview, SportPageview, JamiyatPageview, upload_video, video_list

urlpatterns = [
    path("", HomePageView, name="homepage"),
    path('upload/', upload_video, name='upload_video'),
    path('videos/', video_list, name='video_list'),
    path("Uzbekistan", UzbekistanPageview, name="uzbekistan"),
    path("Fan_texnika", Fan_texnikaPageview, name="fan_texnika"),
    path("iqtisodiyot/", IqtisodiyotPageview, name="iqtisodiyot"),
    path("Sport", SportPageview, name="sport"),
    path("Jamiyat", JamiyatPageview, name="jamiyat"),
    path("Jahon", JahonPageview, name="jahon"),
    path("single/", single, name="single"),
    path("News", news_list, name='news_all'),
    path("news/<int:id>/", news_detail, name='news_detail_page'),
    path("Contact", contact, name="contact"),
]
