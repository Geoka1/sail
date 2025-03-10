__version__ = "0.12.1"
__package_name__ = "SAIL"
_logging_level = "INFO"
import os

os.environ["SKIP_LOG_RESET"] = "True"


def set_logging_level(logging_level):
    global _logging_level
    _logging_level = logging_level


def get_logging_level():
    return _logging_level
