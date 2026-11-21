
import os
import json
import calendar
import shutil
import logging

from datetime import datetime, timezone

# Must point to the same data directory used by EventSnap
BASE_DATA_DIR = "../data"

# Delete events inactive for six calendar months
RETENTION_MONTHS = 6

logging.basicConfig(
    filename="retention.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def subtract_months(date, months):

    month_index = date.month - months - 1
    year = date.year + month_index // 12
    month = month_index % 12 + 1

    day = min(
        date.day,
        calendar.monthrange(year, month)[1]
    )

    return date.replace(
        year=year,
        month=month,
        day=day
    )


def cleanup_inactive_events():

    current_time = datetime.now(timezone.utc)

    retention_cutoff = subtract_months(
        current_time,
        RETENTION_MONTHS
    )

    if not os.path.isdir(BASE_DATA_DIR):
        logging.error(
            f"Data directory not found: {BASE_DATA_DIR}"
        )
        return

    deleted_count = 0

    for folder_name in os.listdir(BASE_DATA_DIR):

        if not folder_name.startswith("event_"):
            continue

        event_folder = os.path.join(
            BASE_DATA_DIR,
            folder_name
        )

        if not os.path.isdir(event_folder):
            continue

        metadata_file = os.path.join(
            event_folder,
            "event_metadata.json"
        )

        # Never delete an event if its activity date is unknown
        if not os.path.exists(metadata_file):
            logging.warning(
                f"Skipped {folder_name}: metadata missing"
            )
            continue

        try:

            with open(metadata_file, "r") as f:
                metadata = json.load(f)

            last_accessed = datetime.fromisoformat(
                metadata["last_accessed_at"]
            )

            if last_accessed.tzinfo is None:
                last_accessed = last_accessed.replace(
                    tzinfo=timezone.utc
                )

            # Delete only if inactive for more than six months
            if last_accessed < retention_cutoff:

                logging.info(
                    f"Deleting inactive event: {folder_name}"
                )

                shutil.rmtree(event_folder)

                deleted_count += 1

                logging.info(
                    f"Successfully deleted: {folder_name}"
                )

        except Exception as e:

            logging.exception(
                f"Error processing {folder_name}: {e}"
            )

    logging.info(
        f"Cleanup completed. Deleted events: {deleted_count}"
    )

    print(
        f"Cleanup completed. "
        f"Deleted {deleted_count} inactive events."
    )


if __name__ == "__main__":
    cleanup_inactive_events()
