import logging
from logging.config import dictConfig


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "formatter": "simple",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 5,
        },
    },
    "loggers": {
        "": {"handlers": ["console", "file"], "level": "DEBUG"},    # 默认logger
        "app": {"handlers": ["console", "file"], "level": "DEBUG", "propagate": False}, # propagate: 是否传播到默认logger
    },
}

dictConfig(logging_config)

logger = logging.getLogger(__name__)
logger.info("Logging initialized")
logger.debug("Debug message")
logger.error("Error message")


app_logger = logging.getLogger("app")
app_logger.info("Logging initialized")
app_logger.debug("Debug message")
app_logger.error("Error message")