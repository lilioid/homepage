from django.conf import settings
from simple_openid_connect.integrations.django.user_mapping import FederatedUserData
from simple_openid_connect.integrations.django.user_mapping import (
    UserMapper as BaseUserMapper,
)

from homepage.core import models


class CustomUserMapper(BaseUserMapper):
    def automap_user_attrs(self, user: models.CustomUser, user_data: FederatedUserData) -> None:
        super().automap_user_attrs(user, user_data)

        if settings.OPENID_ANY_USER_IS_ADMIN:
            user.is_superuser = True
            user.is_staff = True

        elif hasattr(user_data, "roles") and isinstance(user_data.roles, list):
            if any(i_role in user_data.roles for i_role in settings.OPENID_SUPERUSER_ROLES):
                user.is_superuser = True
                user.is_staff = True
