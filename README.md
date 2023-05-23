# Flask Demo
Playing around with Flask, SQLAlchemy, and React.

### Run API

Optionally create a virtual environment.

```
python -V
>> Python 3.7.6
python -m virtualenv venv
source venv/Scripts/activate
```

Install dependencies in requirements.txt.

```
pip install -r requirements.txt
```

Start the server.

```
python server.py
```

Server should be reachable at localhost:5001/canary

```
curl localhost:5001/test
```

### Run the Client

```
yarn --version
>> 1.3.2
yarn install
yarn start
```

Client should be running at localhost:3000.










