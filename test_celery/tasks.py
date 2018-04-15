from __future__ import absolute_import
from test_celery.celery import app
import time

import time


@app.task
def longtime_add(x, y):
    # Wait for 5 seconds
    time.sleep(5)
    print 'long time task finished'

    return "{} + {} = {}".format(x, y, (x + y))
