import logging
import os
import daiquiri

from functools import lru_cache

from core import config


@lru_cache()
def get_settings():
    return config.Settings()


LOG_LEVEL = get_settings().log_level

daiquiri.setup(level=LOG_LEVEL)
logger = daiquiri.getLogger(__name__)
