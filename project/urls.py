from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from _bases.views import Home, HtmlHome, HtmlSearchResultsView

urlpatterns = [
    # admin urls
    path('dj-admin/', admin.site.urls),  # standard django admin url

    # rest_framework api urls (common prefix is api/v1/)
    path('api/v1/', include([
        path('', include('celebs.api.urls')),
        path('', include('movies.api.urls')),
        path('', include('reviews.api.urls')),
        path('', include('users.api.urls')),
    ])),

    # html urls (common prefix is html/)
    path('html/', include([
        path('celeb/', include('celebs.urls_html')),
        path('movie/', include('movies.urls_html')),
        path('user/', include('users.urls_html')),

        path('search/', HtmlSearchResultsView.as_view(), name='html_search'),
        path('', HtmlHome.as_view(), name='html_home'),
    ])),

    # vue urls
    path('celeb/', include('celebs.urls')),
    path('movie/', include('movies.urls')),
    path('review/', include('reviews.urls')),
    path('user/', include('users.urls')),

    # home url
    path('', Home.as_view(), name='home')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns \
      + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
