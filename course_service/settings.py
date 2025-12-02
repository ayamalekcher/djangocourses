from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^@_15gd+7!w^9%bj82n94)xba4=g@1mndy^&7s!lm3xu)4$+-8'
DEBUG = True  # Mettre False en production

ALLOWED_HOSTS = ["*"]  # Tu peux limiter aux domaines Render plus tard

# ===============================
# APPLICATIONS
# ===============================
INSTALLED_APPS = [
    # Prometheus doit être en premier
    'django_prometheus',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tes apps
    'rest_framework',
    'corsheaders',
    'courses',
]

# ===============================
# MIDDLEWARE
# ===============================
MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',  # doit être premier

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_prometheus.middleware.PrometheusAfterMiddleware',   # doit être dernier
]

ROOT_URLCONF = 'course_service.urls'

# ===============================
# TEMPLATES
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
# DATABASE
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
# LANGUAGE & TIMEZONE
# ===============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===============================
# STATIC
# ===============================
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===============================
# CORS
# ===============================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5174",
    
]


# ===============================
# REST FRAMEWORK
# ===============================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
