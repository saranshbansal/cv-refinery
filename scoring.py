from constants import *


def get_scoring_data(role: str) -> dict:
    if role is ROLE_TYPES[0]:
        return PROFILE_FE_SCORE_MAP
    else:
        return PROFILE_BE_SCORE_MAP
