import logging
from typing import Optional, cast

from bot.log import CustomLogger


def get_logger(name: Optional[str] = None) -> CustomLogger:
    """Utility to make mypy recognise that logger is of type `CustomLogger`."""
    return cast(CustomLogger, logging.getLogger(name))
