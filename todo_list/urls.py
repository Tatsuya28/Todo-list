from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import tasks.views as views

urlpatterns = [
    path('',  views.index, name="home"),
    path('add-collection/',  views.add_collection, name="add-collection"),
    path('delete-collection/<int:collection_pk>',  views.delete_collection, name="delete-collection"),
    path('add-task/',  views.add_task, name="add-task"),
    path('delete-task/<int:task_pk>/',  views.delete_task, name="delete-task"),
    path('get-tasks/<int:collection_pk>/',  views.get_tasks, name="get-tasks"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
