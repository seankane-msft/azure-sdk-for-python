# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from azure.data.tables.aio._table_client_async import TableClient
from azure.data.tables.aio._table_service_client_async import TableServiceClient

# from ._azure.data.tables_async import AzureTable
__all__ = [
    'TableClient',
    'TableServiceClient',
    # 'AzureTable'
]

