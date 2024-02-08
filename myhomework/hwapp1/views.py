from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def main(request):
    html = '''
        <title>Моя первая HTML страница </title>
        <h1>Моя первая HTML страница</h1>
        <p>Привет Django!!! <br>
        Логирование - это процесс записи информации о работе приложения. Обычно
        это запись в файлы. Хотя можно писать логи и в базы данных, и просто выводить
        в консоль. Логи позволяют отслеживать работу приложения, выявлять ошибки
        и проблемы, а также анализировать производительность приложения.</p>
        '''
    logger.info('Main page accessed')
    return HttpResponse(html)


def about(request):
    html = '''
            <title>О нас</title>
            <h1>Мы учимся в Geekbrains</h1>
            <p>Изучаем Django!!! <br>
            Для настройки логирования в Django необходимо изменить файл settings.py. В
            этом файле определяются параметры логирования, такие как уровень
            логирования, формат вывода, место хранения логов и т.д .Конфигурация
            логирования в файле settings.py в Django происходит через словарь LOGGING.</p>
            '''
    logger.info('About page accessed')
    return HttpResponse(html)

# Create your views here.
