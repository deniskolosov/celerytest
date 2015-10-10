# celerytest
Вычисляет факториал из чисел, заданных в файлах с использованием Celery

### Установка и запуск
Для работы понадобится RabbitMQ, Python3, SQLAlchemy и Celery

Установка для Ubuntu/Debian:
`sudo apt-get install rabbitmq-server`
`pip install -r requirements.txt`

Далее нужно запустить Celery
`$ celery -A tasks worker`

и сами задачи
`$ python compute_factorials.py file1 file2 file3`

где `file1 file2 file3` – файлы, содержащие числа, для которых нужно посчитать факториал.
