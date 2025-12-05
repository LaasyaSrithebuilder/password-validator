
SECRET_KEY = "dummy"

INSTALLED_APPS = ["core"]

ROOT_URLCONF = "backend.urls"

PASSWORD_VALIDATORS = [
    "core.validators.LengthValidator",
    "core.validators.CharacterValidator",
    "core.validators.BlacklistValidator",
]
