from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    ACTIVATE = (
        'activate',
        timedelta(minutes=15),
    )
    RECOVERY_PASSWORD = (
        'recovery_password',
        timedelta(minutes=15),
    )

    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime
