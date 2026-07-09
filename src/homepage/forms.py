from urllib.parse import urlparse

from django import forms
from django.conf import settings
from django.urls import is_valid_path


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


class WebmentionPayload(forms.Form):
    source = forms.CharField(max_length=256, strip=True)
    target = forms.CharField(max_length=256, strip=True)

    def clean_source(self):
        url = urlparse(self.data["source"])
        if url.scheme not in ["http", "https"]:
            raise forms.ValidationError("URL scheme must be http or https")

        return url

    def clean_target(self):
        url = urlparse(self.data["target"])
        if url.scheme not in ["http", "https"]:
            raise forms.ValidationError("URL scheme must be http or https")

        if not is_valid_path(url.path):
            raise forms.ValidationError("Path is not valid on this site")

        if url.netloc != settings.BASE_URI.netloc:
            raise forms.ValidationError(
                f"Webmentions can only be sent to canonical location {settings.BASE_URI.netloc}"
            )

        return url

