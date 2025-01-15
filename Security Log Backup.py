#!/usr/bin/env python3
# File: log_backup.py
# Title: Enhanced Security Log Backup Script
# Description: A script to backup security logs to a secure location with compression and retention policy.

import os
import shutil
import tarfile
from datetime import datetime
import logging
import sys

# Configuration
LOG_DIR = '/var/log'
BACKUP_DIR = '/backup/logs'
RETENTION_DAYS = 30  # Number of days to keep backups
LOG_FILE = '/var/log/log_backup.log'

# Set up logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_backup(log_dir, backup_dir, timestamp):
    """Create a compressed backup of the log directory."""
    try:
        backup_path = os.path.join(backup_dir, f'logs_backup_{timestamp}')
        compressed_backup_path = f'{backup_path}.tar.gz'

        # Create a compressed archive of the log directory
        with tarfile.open(compressed_backup_path, 'w:gz') as tar:
            tar.add(log_dir, arcname=os.path.basename(log_dir))

        logging.info(f"Logs backed up to {compressed_backup_path}")
        print(f"Logs backed up to {compressed_backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        print(f"Error: {e}")
        sys.exit(1)

def delete_old_backups(backup_dir, retention_days):
    """Delete backups older than the specified retention period."""
    try:
        now = datetime.now()
        for backup in os.listdir(backup_dir):
            backup_path = os.path.join(backup_dir, backup)
            if os.path.isfile(backup_path):
                backup_time = datetime.fromtimestamp(os.path.getmtime(backup_path))
                if (now - backup_time).days > retention_days:
                    os.remove(backup_path)
                    logging.info(f"Deleted old backup: {backup_path}")
                    print(f"Deleted old backup: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to delete old backups: {e}")
        print(f"Error: {e}")

def ensure_backup_dir_exists(backup_dir):
    """Ensure the backup directory exists; create it if it doesn't."""
    if not os.path.exists(backup_dir):
        try:
            os.makedirs(backup_dir)
            logging.info(f"Created backup directory: {backup_dir}")
        except Exception as e:
            logging.error(f"Failed to create backup directory: {e}")
            print(f"Error: {e}")
            sys.exit(1)

def main():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # Ensure the backup directory exists
    ensure_backup_dir_exists(BACKUP_DIR)

    # Create the backup
    create_backup(LOG_DIR, BACKUP_DIR, timestamp)

    # Delete old backups
    delete_old_backups(BACKUP_DIR, RETENTION_DAYS)

if __name__ == "__main__":
    main()