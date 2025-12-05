
import re

class BaseValidator:
    def validate(self, password):
        raise NotImplementedError("Validator must implement validate()")


class LengthValidator(BaseValidator):
    MIN_LENGTH = 8
    def validate(self, password):
        if len(password) < self.MIN_LENGTH:
            return f"Password must be at least {self.MIN_LENGTH} characters"


class CharacterValidator(BaseValidator):
    def validate(self, password):
        if not re.search(r"[A-Z]", password):
            return "Password must contain at least one uppercase letter"
        if not re.search(r"[0-9]", password):
            return "Password must contain at least one digit"
        if not re.search(r"[!@#$%^&*(),.?":{}|<>]", password):
            return "Password must contain at least one special character"


class BlacklistValidator(BaseValidator):
    BLACKLIST = {"password", "123456", "test", "12345678"}

    def validate(self, password):
        if password.lower() in self.BLACKLIST:
            return "Password is too common or insecure"
