import pytest

import homepage.webmention


@pytest.mark.asyncio
async def test_webmention_discovery(http_session):
    KNOWN_ENDPOINTS = {
        "https://webmention.rocks/test/1": "https://webmention.rocks/test/1/webmention",
        "https://webmention.rocks/test/2": "https://webmention.rocks/test/2/webmention",
        "https://webmention.rocks/test/3": "https://webmention.rocks/test/3/webmention",
        "https://webmention.rocks/test/4": "https://webmention.rocks/test/4/webmention",
        "https://webmention.rocks/test/5": "https://webmention.rocks/test/5/webmention",
        "https://webmention.rocks/test/6": "https://webmention.rocks/test/6/webmention",
        "https://webmention.rocks/test/7": "https://webmention.rocks/test/7/webmention",
        "https://webmention.rocks/test/8": "https://webmention.rocks/test/8/webmention",
        "https://webmention.rocks/test/9": "https://webmention.rocks/test/9/webmention",
        "https://webmention.rocks/test/10": "https://webmention.rocks/test/10/webmention",
        "https://webmention.rocks/test/11": "https://webmention.rocks/test/11/webmention",
        "https://webmention.rocks/test/12": "https://webmention.rocks/test/12/webmention",
        "https://webmention.rocks/test/13": "https://webmention.rocks/test/13/webmention",
        "https://webmention.rocks/test/14": "https://webmention.rocks/test/14/webmention",
        "https://webmention.rocks/test/15": "https://webmention.rocks/test/15",
        "https://webmention.rocks/test/16": "https://webmention.rocks/test/16/webmention",
        "https://webmention.rocks/test/17": "https://webmention.rocks/test/17/webmention",
        "https://webmention.rocks/test/18": "https://webmention.rocks/test/18/webmention",
        # "https://webmention.rocks/test/19": "https://webmention.rocks/test/19/webmention",
        "https://webmention.rocks/test/20": "https://webmention.rocks/test/20/webmention",
        "https://webmention.rocks/test/21": "https://webmention.rocks/test/21/webmention?query=yes",
        "https://webmention.rocks/test/22": "https://webmention.rocks/test/22/webmention",
        # "https://webmention.rocks/test/23": "https://webmention.rocks/test/23/webmention",
    }
    for test_url, known_endpoint_url in KNOWN_ENDPOINTS.items():
        discovered_endpoint = await homepage.webmention.find_webmention_endpoint(http_session, test_url)
        assert discovered_endpoint == known_endpoint_url
