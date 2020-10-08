import hashlib
import base64
import hmac
from datetime import datetime

from azure.core.pipeline.policies import SansIOHTTPPolicy


class AppConfigRequestsCredentialsPolicy(SansIOHTTPPolicy):

    def __init__(self, host, credential, secret):
        super(AppConfigRequestsCredentialsPolicy, self).__init__()
        self._host = host
        self._credential = credential
        self._secret = secret

    def _signed_request(self, request):
        verb = request.http_request.method.upper()

        # Get the path and query from url, which looks like https://host/path/query
        query_url = str(request.http_request.url[len(self._host) + 8 :])

        signed_headers = "x-ms-date;host;x-ms-content-sha256"

        utc_now = str(datetime.utcnow().strftime("%b, %d %Y %H:%M:%S ")) + "GMT"
        if request.http_request.body is None:
            request.http_request.body = ""
        content_digest = hashlib.sha256(
            (request.http_request.body.encode("utf-8"))
        ).digest()
        content_hash = base64.b64encode(content_digest).decode("utf-8")

        string_to_sign = (
            verb
            + "\n"
            + query_url
            + "\n"
            + utc_now
            + ";"
            + self._host
            + ";"
            + content_hash
        )

        # decode secret
        # decoded_secret = base64.b64decode(secret, validate=True)
        decoded_secret = base64.b64decode(self._secret)
        digest = hmac.new(
            decoded_secret, string_to_sign.encode("utf-8"), hashlib.sha256
        ).digest()
        signature = base64.b64encode(digest).decode("utf-8")
        signature_header = {
            "x-ms-date": utc_now,
            "x-ms-content-sha256": content_hash,
            "Authorization": "HMAC-SHA256 Credential="
            + self._credential
            + "&SignedHeaders="
            + signed_headers
            + "&Signature="
            + signature,
        }

        request.http_request.headers.update(signature_header)
        return request

    def on_request(self, request):
        self._signed_request(request)