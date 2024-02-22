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
        else:
            user_roles = (
                getattr(user_data, "resource_access", {}).get(settings.OPENID_CLIENT_ID, {}).get("roles", [])
            )
            if any(i_role in user_roles for i_role in settings.OPENID_SUPERUSER_ROLES):
                user.is_superuser = True
                user.is_staff = True
