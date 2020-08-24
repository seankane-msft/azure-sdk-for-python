import os
import copy
import random
import asyncio

class SampleTablesQuery(object):
    connection_string = os.getenv("AZURE_TABLES_CONNECTION_STRING")
    access_key = os.getenv("AZURE_TABLES_KEY")
    account_url = os.getenv("AZURE_TABLES_ACCOUNT_URL")
    account_name = os.getenv("AZURE_TABLES_ACCOUNT_NAME")
    table_name = "OfficeSupplies"

    entity_name = "marker"

    name_filter = "Name eq '{}'".format(entity_name)

    async def _insert_random_entities(self):
        from azure.data.tables.aio import TableClient
        brands = ["Crayola", "Sharpie", "Chameleon"]
        colors = ["red", "blue", "orange", "yellow"]
        names = ["marker", "pencil", "pen"]
        entity_template = {
            "PartitionKey": "pk",
            "RowKey": "row",
        }

        table_client = TableClient.from_connection_string(self.connection_string, self.table_name)

        for i in range(10):
            e = copy.deepcopy(entity_template)
            e["RowKey"] += str(i)
            e["Name"] = random.choice(names)
            e["Brand"] = random.choice(brands)
            e["Color"] = random.choice(colors)
            try:
                await table_client.create_entity(entity=e)
            except:
                # If the value is already in the table, skip and try again
                i -= 1
                pass


    async def sample_query_entities(self):
        await self._insert_random_entities()
        from azure.data.tables.aio import TableClient
        from azure.core.exceptions import HttpResponseError

        table_client = TableClient.from_connection_string(self.connection_string, self.table_name)

        try:
            queried_entities = table_client.query_entities(filter=self.name_filter, select=["Brand","Color"])

            for entity_chosen in queried_entities:
                print(entity_chosen)

        except HttpResponseError as e:
            print(e.message)

        finally:
            await table_client.delete_table()


async def main():
    stq = SampleTablesQuery()
    await stq.sample_query_entities()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())