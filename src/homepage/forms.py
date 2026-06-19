from django import forms


class GuestbookForm(forms.Form):
    public_handle = forms.CharField(
        label="Public Handle",
        required=False,
        max_length=32,
        strip=True,
        empty_value="anonymous",
        help_text="This handle will be displayed next to your guestbook entry to identify you (optional)",
    )
    contact = forms.CharField(
        label="Contact",
        required=False,
        max_length=64,
        strip=True,
        help_text="Your e-mail address, fedi handle or similar. If you want to contact me again to remove your comment "
        " or change something about it, do so via the way described here (optional)",
    )
    content = forms.CharField(
        label="Content",
        required=True,
        max_length=512,
        strip=True,
        empty_value="anonymous",
        help_text="The content of your guestbook entry",
    )
