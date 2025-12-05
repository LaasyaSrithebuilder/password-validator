
from django.conf import settings
from django.utils.module_loading import import_string

def run_validators(password):
    errors = []
    for path in settings.PASSWORD_VALIDATORS:
        validator_class = import_string(path)
        validator = validator_class()
        msg = validator.validate(password)
        if msg:
            errors.append(msg)
    return errors
