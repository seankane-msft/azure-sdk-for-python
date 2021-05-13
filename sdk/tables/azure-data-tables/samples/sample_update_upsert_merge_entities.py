# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_update_upsert_merge_entities.py

DESCRIPTION:
    These samples demonstrate the following: updating, upserting, and merging entities.

USAGE:
    python sample_update_upsert_merge_entities.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_STORAGE_CONNECTION_STRING - the connection string to your storage account
"""


from dotenv import find_dotenv, load_dotenv


class TableEntitySamples(object):
    def __init__(self):
        load_dotenv(find_dotenv())

    def create_and_get_entities(self):
        import os

        # Instantiate a table service client
        from azure.data.tables import TableClient

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )

        with TableClient.from_connection_string(connection_string, table_name="mytable3") as table:

            # Create the Table
            table.create_table()

            my_entity = {
                u"PartitionKey": u"color",
                u"RowKey": u"crayola",
                u"text": u"Marker",
                u"color": u"Purple",
                u"price": u"5",
            }
            try:
                # [START create_entity]
                created_entity = table.create_entity(entity=my_entity)
                print("Created entity: {}".format(created_entity))
                # [END create_entity]

                # [START get_entity]
                # Get Entity by partition and row key
                got_entity = table.get_entity(partition_key=my_entity["PartitionKey"], row_key=my_entity["RowKey"])
                print("Received entity: {}".format(got_entity))
                # [END get_entity]

            finally:
                # Delete the table
                table.delete_table()

    def list_all_entities(self):
        import os

        # Instantiate a table service client
        from azure.data.tables import TableClient

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )

        with TableClient.from_connection_string(connection_string, table_name="mytable4") as table:

            # Create the table
            table.create_table()

            entity = {
                u"PartitionKey": u"color2",
                u"RowKey": u"sharpie",
                u"text": u"Marker",
                u"color": u"Purple",
                u"price": u"5",
            }
            entity1 = {
                u"PartitionKey": u"color2",
                u"RowKey": u"crayola",
                u"text": u"Marker",
                u"color": u"Red",
                u"price": u"3",
            }

            try:
                # Create entities
                table.create_entity(entity=entity)
                table.create_entity(entity=entity1)
                # [START query_entities]
                # Query the entities in the table
                entities = list(table.list_entities())

                for i, entity in enumerate(entities):
                    print("Entity #{}: {}".format(entity, i))
                # [END query_entities]

            finally:
                # Delete the table
                table.delete_table()

    def update_entities(self):
        import os

        # Instantiate a table service client
        from azure.data.tables import TableClient
        from azure.data.tables import UpdateMode

        access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
        endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
        account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
        connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
            account_name, access_key, endpoint_suffix
        )

        with TableClient.from_connection_string(connection_string, table_name="mytable6") as table:

            # Create the table and Table Client
            table.create_table()

            entity = {
                u"PartitionKey": u"color2",
                u"RowKey": u"sharpie",
                u"text": u"Marker",
                u"color": u"Purple",
                u"price": u"5",
            }
            entity1 = {
                u"PartitionKey": u"color2",
                u"RowKey": u"crayola",
                u"text": u"Marker",
                u"color": u"Red",
                u"price": u"3",
            }

            try:
                # Create entities
                table.create_entity(entity=entity)
                created = table.get_entity(partition_key=entity["PartitionKey"], row_key=entity["RowKey"])

                # [START upsert_entity]
                # Try Replace and insert on fail
                insert_entity = table.upsert_entity(mode=UpdateMode.REPLACE, entity=entity1)
                print("Inserted entity: {}".format(insert_entity))

                created["text"] = "NewMarker"
                merged_entity = table.upsert_entity(mode=UpdateMode.MERGE, entity=entity)
                print("Merged entity: {}".format(merged_entity))
                # [END upsert_entity]

                # [START update_entity]
                # Update the entity
                created["text"] = "NewMarker"
                table.update_entity(mode=UpdateMode.REPLACE, entity=created)

                # Get the replaced entity
                replaced = table.get_entity(partition_key=created["PartitionKey"], row_key=created["RowKey"])
                print("Replaced entity: {}".format(replaced))

                # Merge the entity
                replaced["color"] = "Blue"
                table.update_entity(mode=UpdateMode.MERGE, entity=replaced)

                # Get the merged entity
                merged = table.get_entity(partition_key=replaced["PartitionKey"], row_key=replaced["RowKey"])
                print("Merged entity: {}".format(merged))
                # [END update_entity]

            finally:
                # Delete the table
                table.delete_table()


if __name__ == "__main__":
    sample = TableEntitySamples()
    sample.create_and_get_entities()
    sample.list_all_entities()
    sample.update_entities()
