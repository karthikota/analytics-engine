import random

from app.anomaly.dataframe_builder import build_dataframe


def generate_dependencies():

    df = build_dataframe()

    if df.empty:
        return []

    pod_names = list(df["pod_name"])

    dependencies = []

    for pod in pod_names:

        targets = random.sample(
            [p for p in pod_names if p != pod],
            k=2
        )

        for target in targets:

            dependencies.append({
                "source": pod,
                "target": target,
                "influence_score": round(random.uniform(0.5, 1.0), 2)
            })

    return dependencies


if __name__ == "__main__":

    graph = generate_dependencies()

    for edge in graph:
        print(edge)