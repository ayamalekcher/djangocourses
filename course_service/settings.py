from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^@_15gd+7!w^9%bj82n94)xba4=g@1mndy^&7s!lm3xu)4$+-8'
DEBUG = True

ALLOWED_HOSTS = ['*']  # pour accepter les requêtes locales (tu peux restreindre plus tard)


# ===============================
# 🔹 APPLICATIONS
# ===============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
'django_prometheus',
    # Ajoutés :
    'rest_framework',
    'corsheaders',     # <--- important
    'courses',         # ton app Django
]

# ===============================
# 🔹 MIDDLEWARE
# ===============================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # <--- doit être AVANT CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    ...
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]
    

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'course_service.urls'

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
# 🔹 BASE DE DONNÉES
# ===============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_course_4p3t',
        'USER': 'django_course_4p3t_user',
        'PASSWORD': 'WYuwzTOFSSsNGGCAQQM7vvdOfYohRU95',
        'HOST': 'dpg-d4kpunfpm1nc738drqg0-a.oregon-postgres.render.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require'
        }
    }
}



# ===============================
# 🔹 LANGUE / FUSEAU HORAIRE
# ===============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ===============================
# 🔹 STATIC FILES
# ===============================
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ===============================
# 🔹 CORS CONFIGURATION
# ===============================
# Autoriser ton microservice Spring Boot (port 8080)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

# Pour tester facilement, tu peux activer tout (à désactiver plus tard)
# CORS_ALLOW_ALL_ORIGINS = True

# ===============================
# 🔹 REST FRAMEWORK (optionnel)
# ===============================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React
]

