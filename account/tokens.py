from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int) -> str:

        return text_type(user.pk) + text_type(timestamp) + text_type(user.is_active)

        return super()._make_hash_value(user, timestamp)


account_activation_token = AccountActivationTokenGenerator()
