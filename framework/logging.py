from framework.utils.data_manager import DataManager, BASE_DIR

DEBUG = DataManager().get_config_data().debug

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
        'warning': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / "test_project/logs/warnings.log",
            'maxBytes': 10000000,
            'backupCount': 2,
            'level': 'WARNING',
            'formatter': 'verbose',
        },
        'info_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / "test_project/logs/info_logs.log",
            'maxBytes': 10000000,
            'backupCount': 2,
            'level': 'INFO',
            'formatter': 'verbose',
        },
        'info_stdout': {
            'level': 'INFO',
            'formatter': 'verbose',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['warning', 'info_file' if DEBUG == 'False' else 'info_stdout'],
        }
    },
}
