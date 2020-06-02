from celery import Celery
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('render',
             broker='amqp://',
             backend='amqp://',
             include=['runner'])

if __name__ == '__main__':
    app.start()