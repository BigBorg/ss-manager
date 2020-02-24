# encoding:utf8
DEBUG = True
SUPER_USER = "****"
SUPER_USER_PASSWORD = "****"
SECRET_KEY = "****"
PERMANENT_SESSION_LIFETIME = 3600
RECAPTCHA_PUBLIC_KEY = "****"
RECAPTCHA_PRIVATE_KEY = "****"
RECAPTCHA_VERIFY_SERVER = "https://recaptcha.net/recaptcha/api/siteverify"
RECAPTCHA_SCRIPT = "http://recaptcha.net/recaptcha/api.js"

# celery setting
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
