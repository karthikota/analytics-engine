from pydantic import BaseModel
from typing import List


class SnapshotReference(BaseModel):
    snapshot_id: str


class SnapshotList(BaseModel):
    snapshots: List[SnapshotReference]