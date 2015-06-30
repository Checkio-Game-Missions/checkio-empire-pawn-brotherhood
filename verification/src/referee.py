from checkio_referee import RefereeBase, ENV_NAME


import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(set(str(x) for x in data))
"""


def set_repr(data, f):
    return repr("{}({})".format(f, set(data["input"])))


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "safe_pawns"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "safePawns"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: cover,
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: set_repr,
    }

