from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^@_15gd+7!w^9%bj82n94)xba4=g@1mndy^&7s!lm3xu)4$+-8'
DEBUG = True

ALLOWED_HOSTS = ["*"]  # يمكنك تضييقها لاحقاً



# ===============================
# 🔹 APPLICATIONS
# ===============================
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Prometheus (قبل التطبيقات الأخرى)
    'django_prometheus',

    # مشاريعك
    'rest_framework',
    'corsheaders',
    'courses',
]



# ===============================
# 🔹 MIDDLEWARE
# ===============================
MIDDLEWARE = [
    # Prometheus middleware (يجب أن يكون الأول)
    'django_prometheus.middleware.PrometheusBeforeMiddleware',

    # CORS
    'corsheaders.middleware.CorsMiddleware',

    # Django middlewares
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Prometheus (يجب أن يكون الأخير)
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]


ROOT_URLCONF = 'course_service.urls'



# ===============================
# 🔹 TEMPLATES
# ===============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'course_service.wsgi.application'



# ===============================
# 🔹 DATABASE CONFIG
# ===============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_course_4p3t',
        'USER': 'django_course_4p3t_user',
        'PASSWORD': 'WYuwzTOFSSsNGGCAQQM7vvdOfYohRU95',
        'HOST': 'dpg-d4kpunfpm1nc738drqg0-a.oregon-postgres.render.com',
        'PORT': '5432',
        'OPTIONS': {"sslmode": "require"},
    }
}



# ===============================
# 🔹 LANGUAGE & TIMEZONE
# ===============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True



# ===============================
# 🔹 STATIC
# ===============================
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# ===============================
# 🔹 CORS SETTINGS
# ===============================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",   # React frontend
    "http://localhost:8080",   # Spring Boot
]

# لتسهيل العمل (يمكنك استعماله أثناء التطوير فقط)
# CORS_ALLOW_ALL_ORIGINS = True



# ===============================
# 🔹 REST FRAMEWORK
# ===============================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
