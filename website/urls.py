from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.base, name="base"),
    path('', views.logo_navbars, name="logo_navbar"),
    path('', views.btn_navbars, name='btn_navbar'),
    path('', views.desc_contents, name='desc_content'),
    path('', views.btn_contents, name='btn_content'),
    path('', views.desc_offers, name='desc_offer'),
    path('', views.content_offers, name='content_offer'),
    path('', views.desc_mountains, name='desc_mountain'),
    path('', views.content_mountains, name='content_mountain'),
    path('', views.title_ctas, name='title_cta'),
    path('', views.btn_ctas, name='btn_cta'),
    path('', views.content_footers, name='content_footer'),
]
