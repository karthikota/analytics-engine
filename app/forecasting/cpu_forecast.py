import numpy as np

from sklearn.linear_model import LinearRegression


def forecast_cpu():

    cpu_history = [45, 52, 48, 60, 67, 74, 80]

    X = np.array(range(len(cpu_history))).reshape(-1, 1)

    y = np.array(cpu_history)

    model = LinearRegression()

    model.fit(X, y)

    next_time = np.array([[len(cpu_history)]])

    prediction = model.predict(next_time)

    return {
        "predicted_cpu": round(float(prediction[0]), 2)
    }


if __name__ == "__main__":

    result = forecast_cpu()

    print(result)