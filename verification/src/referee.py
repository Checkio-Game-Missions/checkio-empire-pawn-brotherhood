from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(set(str(x) for x in data))
"""


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "safe_pawns"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
