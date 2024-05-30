# Sports Betting Backend API with Flask

## Description
A flask app to interact with the Sports Betting. This api will expose endpoints that will be used from a frontend app to help the user use the Sports Betting from a ui.

## Installation
#### Clone the repository
```bash
git clone https://github.com/gmoraitis/sb_backend.git
```
#### Create a Python Virtual Env
```bash
cd sb_backend
python3 -m venv venv
source venv/bin/activate
```
#### Using the venv, install the dependencies
```bash
pip3 install -r requirements.txt
```

## Usage
#### Run the app
```bash
python3 app.py
```

## API Endpoints
Open a new terminal window
```bash
curl -X POST http://127.0.0.1:5000/init_dataloader -H "Content-Type: application/json" -d '{"leagues": ["England", "Germany"], "years": [2020, 2021]}'
```
You should get this:
```bash
{
  "message": "Dataloader initialized successfully"
}
```


## Testing
Information on how to run the tests for the application.
...