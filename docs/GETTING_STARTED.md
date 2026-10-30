# Compass MVP

## Run the API

From `backend`:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`; interactive documentation is at `/docs`.

## Run the frontend

From `frontend` in a second terminal:

```powershell
python -m http.server 5173
```

Open `http://127.0.0.1:5173`. The page checks the API health endpoint automatically.

## Next MVP slice

## Configure Gemini

Before starting the backend, set `GEMINI_API_KEY` in the same PowerShell window:

```powershell
$env:GEMINI_API_KEY="your_gemini_api_key"
```

Compass uses Gemini for structured project analysis. If Gemini is unavailable or the key is invalid, the app stays usable and displays a clear fallback result instead of failing.
