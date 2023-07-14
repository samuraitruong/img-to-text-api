## get started
```
docker-compose up 
// or
docker-compose up --build
```

Or

```
python3 -m .venv
pip3 install -r requirements.txt
cd app

python3 main.py
```


## run test
```
cd app
pytest
```

## Build production

```
docker build -t img-to-text .
```