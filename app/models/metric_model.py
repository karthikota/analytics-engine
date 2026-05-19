from pydantic import BaseModel
from typing import List


class MetricPoint(BaseModel):
    timestamp: str
    value: float


class PodMetrics(BaseModel):
    pod_name: str
    cpu: List[MetricPoint]
    ram: List[MetricPoint]