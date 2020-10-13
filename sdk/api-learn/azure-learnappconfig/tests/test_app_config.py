import pytest
import os

from _shared.testcase import AppConfigTestCase
from devtools_testutils import ResourceGroupPreparer
from appconfig_preparer import AppConfigPreparer

from azure.learnappconfig import AppConfigurationClient
from azure.core.exceptions import ResourceNotFoundError

class AppConfigurationClientTest(AppConfigTestCase):
    def setUp(self):
        super(AppConfigurationClientTest, self).setUp()

    def test_get_key_value(self):
        client = self.create_basic_client(AppConfigurationClient, account_url=self.app_config_url)
        assert client is not None

        assert self.env_color == client.get_configuration_setting(self.env_color_key)
        assert self.env_greeting == client.get_configuration_setting(self.env_greeting_key)

    def test_get_invalid_key(self):
        client = self.create_basic_client(AppConfigurationClient, account_url=self.app_config_url)
        assert client is not None

        with pytest.raises(ResourceNotFoundError):
            client.get_configuration_setting("KEY_THAT_DOES_NOT_EXIST")

    def test_create_client_invalid_url(self):
        url = os.environ.get('APP_CONFIG_URL_DOES_NOT_EXIST')
        with pytest.raises(ValueError):
            client = self.create_basic_client(AppConfigurationClient, account_url=url)