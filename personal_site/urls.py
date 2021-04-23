from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from personal_site import settings

urlpatterns = [
    path('', include("site_about_us.urls", namespace="about_us")),
    path('', include("site_resume.urls", namespace="resumes")),
    path('', include("site_blog.urls", namespace="blogs")),
    path('', include("site_work.urls", namespace="works")),
    path('', include("site_contact.urls", namespace="contact")),
    path('admin/', admin.site.urls),
]
handler404 = 'personal_site.views.view_404'
handler403 = 'personal_site.views.view_403'
handler400 = 'personal_site.views.view_400'
handler500  = 'personal_site.views.view_500'

if settings.DEBUG:
    # ADD ROOT STATIC FILES
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # ADD MEDIA STATIC FILES
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
