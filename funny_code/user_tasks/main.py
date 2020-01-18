
import os
from celery import Celery


if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'funny_code.settings'

# 
celery_app = Celery('funny_code')
# 导入celery 配置
celery_app.config_from_object('funny_code.settings')
# 自动的注册任务：
celery_app.autodiscover_tasks(['user_tasks.my_task'])

# 启动celery
# celery -A user_taks.main worker -l info