import json
import boto3
from datetime import datetime, timedelta, tzinfo


def delete_rds_snapshots():
    # Setting retention period of 6 days
    retention_date = datetime.now(UTC) - timedelta(days=6)

    print("Connecting to AWS")
    rds = boto3.setup_default_session()
    clnt = boto3.client("rds")
    snapshots = clnt.describe_db_snapshots(SnapshotType="manual")
    print("Looking for snapshots older than {}".format(retention_date))

    for i in snapshots["DBSnapshots"]:
        if i["SnapshotCreateTime"] < retention_date:
            print("Deleting snapshot {}".format(i["DBSnapshotIdentifier"]))
            clnt.delete_db_snapshot(DBSnapshotIdentifier=i["DBSnapshotIdentifier"])
