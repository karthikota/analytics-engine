import pandas as pd

from app.ingestion.telemetry_pipeline import build_telemetry


def build_dataframe():

    telemetry = build_telemetry()

    if not telemetry:
        print("No telemetry data available.")
        return pd.DataFrame()

    df = pd.DataFrame(telemetry)

    return df


if __name__ == "__main__":

    df = build_dataframe()

    print(df)