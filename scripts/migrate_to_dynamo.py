import sqlite3
from dynamoDB import DynamoDB
from decimal import Decimal


def migrate_to_dynamo():
    connection = sqlite3.connect("../shopapp.sqlite3")
    cursor = connection.cursor()

    tables = ["product"]
    for table in tables:
        # Execute a SELECT query to get the table definition
        cursor.execute(
            f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table}'"
        )
        table_definition = cursor.fetchone()[0]

        # Extract the primary key information from the table definition
        primary_key = None
        if "PRIMARY KEY" in table_definition:
            primary_key_start = table_definition.index("PRIMARY KEY") + len(
                "PRIMARY KEY"
            )
            primary_key_end = table_definition.index(")", primary_key_start)
            primary_key = table_definition[primary_key_start:primary_key_end].strip()
            primary_key = primary_key.replace("(", "")

        # Execute PRAGMA statement to get column information
        cursor.execute(f"PRAGMA table_info({table})")
        columns = cursor.fetchall()

        # Extract column names and types
        columns_and_datatypes = {}
        for column in columns:
            column_name = column[1]
            column_type = column[2]
            columns_and_datatypes[column_name] = column_type

        primary_key_type = columns_and_datatypes[primary_key]

        dynamo_db = DynamoDB()
        # dynamo_db.create_table(table, primary_key, primary_key_type)

        # Execute a SELECT query to get the table data
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        items = []
        for row in rows:
            item = {}
            for index, column in enumerate(columns):
                column_name = column[1]
                column_value = row[index]
                if isinstance(column_value, float):
                    column_value = Decimal(str(column_value))
                item[column_name] = column_value
            items.append(item)

        # Write the data to DynamoDB
        dynamo_db.batch_write(table, items)

    # Close the database connection
    connection.close()


if __name__ == "__main__":
    migrate_to_dynamo()

# --- some useful code snippets ---

# tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
# Fetch all rows
# rows = cursor.fetchall()
# Convert data to JSON format
# table_data = []
# for row in rows:
#     table_data.append(dict(zip(table_columns, row)))
# json_data[table_name] = table_data

# Save data to a JSON file
# with open("output.json", "w") as file:
#     json.dump(json_data, file, indent=4)
