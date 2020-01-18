from user_tasks.main import celery_app
from django.core.mail import send_mail
from django.conf import settings



@celery_app.task(name='send_verify')
def send_verify(email=None,code=None):
    subject = 'AID1906邮箱验证码'

    html_message = '<p>尊敬的学员，您好：</p>'\
        '<p>欢迎来到老龚课堂</p>'\
        '<p>您的邮箱为：%s,您的邮箱验证码为:<b>%s</b>,该验证码10分钟之内有效</p>'%(email,code)
    try:
        send_mail(subject,'',settings.EMAIL_FROM,　[email], html_message=html_message)
    except Exception as e:
        raise ValueError('发送邮件失败！')
