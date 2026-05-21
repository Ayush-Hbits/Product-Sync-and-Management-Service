# FastAPI Product Sync Service

## Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

## Swagger
Open: http://127.0.0.1:8000/docs

## Test Headers
Use:
- `X-User-Id: 1` for Admin
- `X-User-Id: 2` for Subscriber
