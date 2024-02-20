# python concurrency

## flask_app

```
gunicorn --bind 0.0.0.0 --workers 1 --threads 1 flask_app:app
```

## fastapi_app
```
python fastapi_app.py --workers 1
```

## request_test
```
python request_test.py sleep --num_users=10 --num_requests=10
python request_test.py count --num_users=10 --num_requests=10
```