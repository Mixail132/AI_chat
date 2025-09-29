# About
This is a simple AI chat powered by the `Gemini` `AI` model.\
Clone the repository using `Git` and enjoy chatting with `AI`.

## Technologies used:
- Python
- FastAPI
- Docker
- CSS
- HTML
- JS

## Configuration`.env` file
- Get your own `API_KEY` via the
 `Google AI Studio` [app](https://aistudio.google.com/api-keys).
- Create a `.env` file in the root directory of the repository. 
- Add the following lines to the file:
```commandline
GEMINI_API_KEY=your_api_key
SERVER_NAME=http://localhost:8000
```

## Running locally
- Create a virtual environment.
- Install project dependencies:
```commandline
pip install -r requirements.txt
```
- Launch FastAPI:
```commandline
uvicorn main:app --reload
```
- Open your browser and navigate to: 
```commandline
http://127.0.0.1:8000
```

## Running with `Docker`:
- Download and install the `Docker desktop` app.
- Build the `Docker` image:
```commandline
docker build --build-arg SERVER_NAME="https://api.myserver.com" -t aichat .
```
- Run the `Docker` container:
```commandline
docker run -d -p 8000:8000 aichat
```
- Open your browser and go to: 
```commandline
http://127.0.0.1:8000
```
