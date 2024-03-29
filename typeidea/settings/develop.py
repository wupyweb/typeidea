from .base import *  # NOQA
import os


DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

THEME = 'bootstrap'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'themes', THEME, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_ROOT = 'staticfiles'     # 部署之后静态资源路径，collectionstatic命令可以收集静态文件到此目录中
STATICFILES_DIRS = (            # 定义静态资源寻找目录
    os.path.join(BASE_DIR, 'themes', THEME, 'static'),
)
STATIC_URL = '/static/'         # 重写静态资源url

INSTALLED_APPS += [
    'debug_toolbar',
    # # 'pympler',
    # 'silk'
]
# MIDDLEWARE += [
#     # 'debug_toolbar.middleware.DebugToolbarMiddleware',
#     'silk.middleware.SilkyMiddleware'
# ]

INTERNAL_IPS = ['127.0.0.1']

# djdt_flamegraph火焰图, 
# DEBUG_TOOLBAR_PANELS = [
#     'djdt_flamegraph.FlamegraphPanel',
# ]
# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': 'https://code.jquery.com/jquery-3.6.0.min.js',
# }
# DEBUG_TOOLBAR_PANELS = [
#     'pympler.panels.MemoryPanel',
# ]