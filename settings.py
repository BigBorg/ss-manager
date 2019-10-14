# encoding:utf8
DEBUG = True
SUPER_USER = "never tell you"
SUPER_USER_PASSWORD = "never tell you"
SECRET_KEY = "never tell you"
PERMANENT_SESSION_LIFETIME = 3600
RECAPTCHA_PUBLIC_KEY = "apply for yourself"
RECAPTCHA_PRIVATE_KEY = "apply for yourself"
RECAPTCHA_VERIFY_SERVER = "https://recaptcha.net/recaptcha/api/siteverify"
RECAPTCHA_SCRIPT = "http://recaptcha.net/recaptcha/api.js"

# celery setting
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
