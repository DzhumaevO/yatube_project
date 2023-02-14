# posts/urls.py (главный файл url проекта)
# По умолчанию в проект Django подключена система администрирования
from django.contrib import admin
# Функция include позволит использовать path() из других файлов.
# Импортируем!
from django.urls import include, path 

urlpatterns = [    
    # Дорогой Джанго, если на сервер пришёл любой запрос (''),
    # перейди в файл urls приложения posts 
    # и проверь там все path() на совпадение с запрошенным URL
    path('', include('posts.urls', namespace='posts')),
    # Если в приложении posts не найдётся совпадений -
    # Django продолжит искать совпадения здесь, в головном файле urls.py.

    # Встроенная админка Django подключена «из коробки» по адресу admin/
    path('admin/', admin.site.urls),
]