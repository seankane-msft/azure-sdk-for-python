# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_query_table_async.py

DESCRIPTION:
    These samples demonstrate the following: querying a table for entities.

USAGE:
    python sample_query_table_async.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_STORAGE_CONNECTION_STRING - the connection string to your storage account
"""

import asyncio
from dotenv import find_dotenv, load_dotenv


class SampleTablesQuery(object):
    def __init__(self):
        load_dotenv(find_dotenv())

    async def insert_random_entities(self):
        import os

        from azure.data.tables.aio import TableClient
        from azure.core.exceptions import ResourceExistsError

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )
        table_name = "OfficeSupplies"

        brands = ["Crayola", "Sharpie", "Chameleon"]
        colors = ["red", "blue", "orange", "yellow"]
        names = ["marker", "pencil", "pen"]
        entity_template = {
            "PartitionKey": "pk",
            "RowKey": "row",
        }

        table_client = TableClient.from_connection_string(connection_string, table_name)
        async with table_client:
            try:
                await table_client.create_table()
            except ResourceExistsError:
                print("Table already exists")

            for i in range(25):
                e = copy.deepcopy(entity_template)
                e["RowKey"] += str(i)
                e["Name"] = random.choice(names)
                e["Brand"] = random.choice(brands)
                e["Color"] = random.choice(colors)
                e["Value"] = random.randint(0, 100)
                await table_client.create_entity(entity=e)

    async def sample_query_entities(self):
        import os

        from azure.data.tables.aio import TableClient
        from azure.core.exceptions import HttpResponseError

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )
        table_name = "OfficeSupplies"

        print("Entities with name: marker")
        # [START query_entities]
        async with TableClient.from_connection_string(connection_string, table_name) as table_client:
            try:
                parameters = {u"name": u"marker"}
                name_filter = u"Name eq @name"
                queried_entities = table_client.query_entities(
                    query_filter=name_filter, select=[u"Brand", u"Color"], parameters=parameters
                )
                async for entity_chosen in queried_entities:
                    print(entity_chosen)

            except HttpResponseError as e:
                pass
            # [END query_entities]

    async def sample_query_entities_multiple_params(self):
        import os

        from azure.data.tables.aio import TableClient

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )
        table_name = "OfficeSupplies"

        print("Entities with name: marker and brand: Crayola")
        # [START query_entities]
        async with TableClient.from_connection_string(connection_string, table_name) as table_client:
            parameters = {u"name": u"marker", u"brand": u"Crayola"}
            name_filter = u"Name eq @name and Brand eq @brand"
            queried_entities = table_client.query_entities(
                query_filter=name_filter, select=[u"Brand", u"Color"], parameters=parameters
            )

            async for entity_chosen in queried_entities:
                print(entity_chosen)
        # [END query_entities]

    async def sample_query_entities_values(self):
        import os
        from azure.data.tables.aio import TableClient
        from azure.core.exceptions import HttpResponseError

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )
        table_name = "OfficeSupplies"

        print("Entities with 25 < Value < 50")
        # [START query_entities]
        async with TableClient.from_connection_string(connection_string, table_name) as table_client:
            parameters = {u"lower": 25, u"upper": 50}
            name_filter = u"Value gt @lower and Value lt @upper"
            queried_entities = table_client.query_entities(
                query_filter=name_filter, select=[u"Value"], parameters=parameters
            )

            async for entity_chosen in queried_entities:
                print(entity_chosen)
        # [END query_entities]

    async def clean_up(self):
        import os
        from azure.data.tables.aio import TableClient

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )
        table_name = "OfficeSupplies"
        from azure.data.tables.aio import TableClient

        async with TableClient.from_connection_string(connection_string, table_name) as table_client:
            await table_client.delete_table()


async def main():
    stq = SampleTablesQuery()
    await stq.insert_random_entities()
    await stq.sample_query_entities()
    await stq.sample_query_entities_multiple_params()
    await stq.sample_query_entities_values()
    await stq.clean_up()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
