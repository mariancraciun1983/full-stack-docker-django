from django.shortcuts import render
from django.http import HttpResponse
from django.core import mail
from .tasks import tools_test_task

def index(request):
  print('index')
  return render(request, 'tools/index.html')

def test_async(request):
  task = tools_test_task.delay(10)
  return HttpResponse(task.task_id)

def test_wait(request):
  task = tools_test_task.delay(10)
  # wait for the results
  result = task.wait(timeout=None, interval=0.5)
  return HttpResponse(result)


def test_ajax(request):
  if 'task_id' in request.GET:
    task_id = request.GET['task_id']
    res = tools_test_task.AsyncResult(task_id)
    # check if task is done
    if res.ready():
      return HttpResponse(res.get())
    else:
      return HttpResponse(res.state)

  return HttpResponse()

def test_email(request):
  emails = (
    ('Hey Man', "I'm The Dude! So that's what you call me.", 'dude@aol.com', ['mr@lebowski.com']),
    ('Dammit Walter', "Let's go bowlin'.", 'dude@aol.com', ['wsobchak@vfw.org']),
  )
  results = mail.send_mass_mail(emails)
  print(results)
  return HttpResponse()