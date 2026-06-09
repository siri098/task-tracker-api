# Task Tracker API

A beginner-friendly **FastAPI** REST API for managing tasks. Data is stored **in memory** (no database), so tasks disappear when the server restarts.

## Features

- Full CRUD for tasks
- Pydantic validation on request bodies
- Clear 404 errors when a task is not found
- Interactive API docs at `/docs`
- Ready to deploy on [Render](https://render.com)

## Task model

| Field        | Type     | Description                    |
|-------------|----------|--------------------------------|
| `id`        | string   | Unique identifier (UUID)       |
| `title`     | string   | Task title (required)          |
| `description` | string | Optional details               |
| `completed` | boolean  | Whether the task is done       |
| `created_at` | datetime | When the task was created (UTC) |

## Endpoints

| Method | Path                      | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/health`                 | Health check             |
| GET    | `/tasks`                  | List all tasks           |
| GET    | `/tasks/{task_id}`        | Get one task             |
| POST   | `/tasks`                  | Create a task            |
| PUT    | `/tasks/{task_id}`        | Update a task (full)     |
| PATCH  | `/tasks/{task_id}/complete` | Mark task as completed |
| DELETE | `/tasks/{task_id}`        | Delete a task            |

## Project structure

```
task-tracker-api/
├── app/
│   ├── __init__.py
│   ├── main.py       # Routes and FastAPI app
│   ├── models.py     # Pydantic models
│   └── storage.py    # In-memory storage
├── requirements.txt
└── README.md
```

## Local setup

### 1. Create a virtual environment (recommended)

```bash
python -m venv venv
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Example requests

### Health check

```bash
curl http://127.0.0.1:8000/health
```

### Create a task

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Buy groceries\", \"description\": \"Milk and eggs\"}"
```

### List all tasks

```bash
curl http://127.0.0.1:8000/tasks
```

### Get one task

```bash
curl http://127.0.0.1:8000/tasks/{task_id}
```

### Update a task

```bash
curl -X PUT http://127.0.0.1:8000/tasks/{task_id} \
  -H "Content-Type: application/json" \
  -d "{\"title\": \"Buy groceries\", \"description\": \"Milk, eggs, bread\", \"completed\": false}"
```

### Mark as completed

```bash
curl -X PATCH http://127.0.0.1:8000/tasks/{task_id}/complete
```

### Delete a task

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/{task_id}
```

## Deploy on Render

[Render](https://render.com) can host this API for free (with limitations).

### Option A: Deploy from GitHub

1. Push this project to a GitHub repository.
2. Sign in to [Render](https://dashboard.render.com) and click **New +** → **Web Service**.
3. Connect your GitHub account and select the repository.
4. Configure the service:
   - **Name:** `task-tracker-api` (or any name you like)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Click **Create Web Service**.

Render sets the `PORT` environment variable automatically. Using `--host 0.0.0.0` lets the server accept external connections.

### Option B: Use a `render.yaml` blueprint (optional)

You can add a `render.yaml` at the repo root and deploy via **New +** → **Blueprint**. Example:

```yaml
services:
  - type: web
    name: task-tracker-api
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    healthCheckPath: /health
```

### After deployment

- Your API URL will look like: `https://task-tracker-api.onrender.com`
- Test health: `https://your-app.onrender.com/health`
- Open docs: `https://your-app.onrender.com/docs`

> **Note:** In-memory storage resets when Render restarts or redeploys your service. For persistent data, you would add a database later.

## License

MIT — use freely for learning and projects.
