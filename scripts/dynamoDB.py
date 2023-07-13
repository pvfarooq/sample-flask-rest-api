import boto3
import logging
from typing import List

field_mapping = {
    "INTEGER": "N",
    "VARCHAR": "S",
    "FLOAT": "N",
    "TEXT": "S",
    "BOOLEAN": "N",
    "DATETIME": "S",
    "DATE": "S",
    "TIME": "S",
}


def get_field_type(field: str):
    field = field.split("(")[0]
    if field.upper() in field_mapping:
        dynamo_field = field_mapping[field]
        return dynamo_field


class DynamoDB:
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
    def __init__(self):
        self.db_resource = boto3.resource(
            "dynamodb",
            aws_access_key_id="******",
            aws_secret_access_key="******",
            region_name="ap-south-1",
        )

    def get_table(self, table_name: str):
        return self.db_resource.Table(table_name)

    def update_table(self, table_name: str):
        table = self.get_table(table_name)
        # Update the table

    def create_table(
        self,
        table_name: str,
        primary_key: str,
        primary_key_type: str,
        **kwargs,
    ):
        key_schema = [
            {"AttributeName": primary_key, "KeyType": "HASH"},
        ]
        attribute_definitions = [
            {
                "AttributeName": primary_key,
                "AttributeType": get_field_type(primary_key_type),
            },
        ]
        table = self.db_resource.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={"ReadCapacityUnits": 3, "WriteCapacityUnits": 3},
            BillingMode="PROVISIONED",
        )
        table.wait_until_exists()
        logging.info(f"Table {table_name} created successfully")
        return table

    def batch_write(self, table_name: str, items: list, force_write: bool = False):
        table = self.get_table(table_name)
        total_items: int = len(items)

        max_batch_size = 25
        max_batch_size_bytes = 1024 * 1024 * 16

        # Split items into multiple batches if necessary
        for start_index in range(0, total_items, max_batch_size):
            end_index = min(start_index + max_batch_size, total_items)
            batch_items = items[start_index:end_index]

            # Check if the total size of items in the batch exceeds the limit
            if self._get_items_size(batch_items) > max_batch_size_bytes:
                logging.warning(
                    "Batch size exceeds the maximum limit. Splitting into smaller batches."
                )
                self.batch_write(
                    table_name, batch_items
                )  # Recursive call to handle the split batch
                continue

            # Check if provisioned throughput is sufficient
            if not self._check_provisioned_throughput(table, len(batch_items)):
                logging.error(
                    "Insufficient provisioned throughput. Aborting batch write."
                )
                return

        # Perform the batch write operation
        with table.batch_writer() as batch:
            for item in items:
                try:
                    batch.put_item(Item=item)
                except Exception as e:
                    logging.error(f"Failed to put item in batch write: {e}")

        logging.info(f"Batch write to table {table_name} successful")

    def _get_items_size(self, items: List[dict]) -> int:
        # Calculate the total size of items in bytes
        total_size = sum(len(str(item)) for item in items)
        return total_size

    def _check_provisioned_throughput(self, table, num_items: int) -> bool:
        write_capacity = self._get_write_capacity(table.table_name)

        # Check if provisioned throughput is sufficient for the batch write operation
        if num_items > write_capacity:
            logging.warning("Insufficient write capacity units for batch write.")
            return False

        return True

    def _get_write_capacity(self, table_name: str) -> int:
        response = self.db_resource.meta.client.describe_table(TableName=table_name)
        write_capacity = response["Table"]["ProvisionedThroughput"][
            "WriteCapacityUnits"
        ]
        return write_capacity
