from simple_openid_connect.integrations.django.user_mapping import UserMapper


class HomepageUserMapper(UserMapper):
    def automap_user_attrs(self, user, user_data):
        super().automap_user_attrs(user, user_data)
        user.is_superuser = True
        user.is_staff = True
