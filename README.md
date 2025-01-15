# Scritps
Python Script for Security Log Backup

### Example Usage:
1- Run the script: python3 "Security Log Backup.py"

2-Output:

A compressed backup file is created in /backup/logs (e.g., logs_backup_20240731153045.tar.gz).

Old backups older than 30 days are deleted.

Logs are written to /var/log/log_backup.log.

### Configuration Options:
LOG_DIR: The directory containing the logs to back up.

BACKUP_DIR: The directory where backups will be stored.

RETENTION_DAYS: The number of days to retain backups (older backups are deleted).

LOG_FILE: The file where script logs are stored.

This enhanced script is robust, efficient, and ready for production use. It ensures secure log backups while managing disk space and providing detailed logs for troubleshooting.


### Example Usage:
1. Run the script:
   ```bash
   ./log_backup.py
   ```

2. Output:
   - A compressed backup file is created in `/backup/logs` (e.g., `logs_backup_20240731153045.tar.gz`).
   - Old backups older than 7 days are deleted.
   - Logs are written to `/var/log/log_backup.log`.

---

### Configuration Options:
- `LOG_DIR`: The directory containing the logs to back up.
- `BACKUP_DIR`: The directory where backups will be stored.
- `RETENTION_DAYS`: The number of days to retain backups (older backups are deleted).
- `LOG_FILE`: The file where script logs are stored.
