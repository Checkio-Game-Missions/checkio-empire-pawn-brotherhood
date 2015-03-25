from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(set(str(x) for x in data))
"""


def set_repr(f, data):
    repr("{}({})".format(f, set(data["input"])))


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "safe_pawns"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": set_repr,
        "python_3": set_repr,
        "javascript": None
    }

