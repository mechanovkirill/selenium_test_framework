from framework.utils.data_manager import ConfigData, BASE_DIR

DEBUG = ConfigData().debug

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {name} {levelname} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / "test_project/testing.log",
            'maxBytes': 10000000,
            'backupCount': 20,
            'level': 'WARNING',
            'formatter': 'verbose',
        },
        'info': {
            'level': 'INFO',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers': {
        '': {
            'level': 'WARNING' if DEBUG == 'False' else 'INFO',
            'handlers': ['default' if DEBUG == 'False' else 'info'],
        }
    },
}
