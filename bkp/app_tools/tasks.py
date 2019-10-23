from celery import task
import time


@task
def tools_test_task(secs):
    print("Sleeping %s" % (secs,))
    time.sleep(secs)
    print('Done')
    return 'I slept for %s seconds' % (secs,)