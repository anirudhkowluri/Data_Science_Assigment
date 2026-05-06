from fastapi import FastAPI
import joblib
import uvicorn

app = FastAPI()


@app.get('/')
def home():

    return {
        'message': 'Forecast API Running'
    }


@app.get('/predict/{state}')
def predict(state: str):

    results = joblib.load(
        'forecast_results.pkl'
    )

    state = state.title()

    available_states = list(results.keys())

    if state not in results:

        return {
            'error': 'State not found',
            'available_states': available_states
        }

    return {
        'state': state,
        'best_model': results[state]['best_model'],
        'rmse': results[state]['rmse']
    }


@app.get('/states')
def get_states():

    results = joblib.load(
        'forecast_results.pkl'
    )

    return {
        'available_states': list(results.keys())
    }


if __name__ == '__main__':

    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8000
    )