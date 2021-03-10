from celery import Celery
import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('render',
             broker='redis://',
             backend='redis://',
             include=['pyrt.tasks'])

if __name__ == '__main__':
    app.start()
