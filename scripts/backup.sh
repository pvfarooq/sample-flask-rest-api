#!/bin/bash

# Define the paths
DATABASE_PATH="/path/to/your/database.db"
BACKUP_PATH="/path/to/backup/shop_db_backup.sql"

# Run SQLite commands to backup the database
sqlite3 "$DATABASE_PATH" <<EOF
.output "$BACKUP_PATH"
.dump
.quit
EOF

echo "Backup complete"
