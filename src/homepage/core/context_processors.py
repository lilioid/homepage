from homepage.core import models


def friends(request):
    """
    A django context processor which adds all known friends
    """
    return {"friends": models.Friend.objects.filter(is_shown=True)}
