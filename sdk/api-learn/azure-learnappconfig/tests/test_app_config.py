import os
import pytest

from devtools_testutils import AzureTestCase

from azure.learnappconfig import AppConfigurationClient
from azure.core.exceptions import ResourceNotFoundError

APP_CONFIG_URL = "https://fake-app-config-url.azconfig.io"

class AppConfigurationClientTest(AzureTestCase):
    def __init__(self, *args, **kwargs):
        super(AppConfigurationClientTest, self).__init__(*args, **kwargs)
        self.env_color = os.environ.get('API-LEARN_SETTING_COLOR_VALUE', "Green")
        self.env_color_key = os.environ.get('API-LEARN_SETTING_COLOR_KEY', "FontColor")
        self.env_greeting = os.environ.get('API-LEARN_SETTING_TEXT_VALUE', "Hello World!")
        self.env_greeting_key = os.environ.get('API-LEARN_SETTING_TEXT_KEY', "Greeting")

    def setUp(self):
        super(AppConfigurationClientTest, self).setUp()
        # Set the env variable AZURE_APP_CONFIG_URL or put APP_CONFIG_URL in your "mgmt_settings_real.py" file
        self.app_config_url = self.set_value_to_scrub('APP_CONFIG_URL', APP_CONFIG_URL)

    def test_get_key_value(self):
        client = self.create_basic_client(AppConfigurationClient, account_url=self.app_config_url)
        assert client is not None

        assert self.env_color == client.get_configuration_setting(self.env_color_key)['value']
        assert self.env_greeting == client.get_configuration_setting(self.env_greeting_key)['value']

    def test_get_invalid_key(self):
        client = self.create_basic_client(AppConfigurationClient, account_url=self.app_config_url)
        assert client is not None

        with pytest.raises(ResourceNotFoundError):
            client.get_configuration_setting("KEY_THAT_DOES_NOT_EXIST")