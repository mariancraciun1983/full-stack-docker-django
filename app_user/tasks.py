from celery import task
from django.core import mail
from django.contrib.auth.models import User
from .models import UserEmailTemplate
from django.conf import settings
from django.template import Template, Context


def prepare_email_template(user, template_id, extraContext):
    template = UserEmailTemplate.objects.get(id=template_id)
    cdict = {"user": user}
    cdict.update(extraContext)
    context = Context(cdict)
    t_body = Template(template.body)
    t_body_html = Template(template.body_html)
    return {
        "title": template.title,
        "body": t_body.render(context),
        "body_html": t_body_html.render(context),
    }


# mail.send_email is already async no need for @task
def send_email(user, template_id, context={}):
    template = prepare_email_template(user, template_id, context)
    return mail.send_mail(
        template['title'],
        template['body'],
        settings.EMAIL_FROM,
        [user.email],
        html_message=template['body_html'],
        fail_silently=False,
    )
