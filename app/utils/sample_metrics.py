import random
from datetime import datetime


def generate_sample_metrics(pod_name):

    if pod_name == "frontend":

        cpu_usage = round(random.uniform(80, 95), 2)

    else:

        cpu_usage = round(random.uniform(20, 60), 2)

    ram_usage = round(random.uniform(200, 900), 2)

    return {
        "timestamp": datetime.now().isoformat(),
        "pod_name": pod_name,
        "cpu": cpu_usage,
        "ram": ram_usage
    }