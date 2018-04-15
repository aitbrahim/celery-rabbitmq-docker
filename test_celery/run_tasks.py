from test_celery.tasks import longtime_add

import time


if __name__ == '__main__':
    result = longtime_add.delay(4, 4)
    print 'Task result:', result.get(timeout=6)
