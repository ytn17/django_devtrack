# DevTrack — Issue Tracking API

A Django REST Framework API for tracking issues and reporters. Data is persisted to JSON files (no database migrations required).

---

## Prerequisites

- Python 3.14+
- pip

---

## Setup & Run

**1. Clone / navigate to the project directory:**

```bash
cd django_devtrack
```

**2. Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

**3. Install dependencies:**

```bash
pip install django djangorestframework
```

**4. Start the development server:**

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoints

Base path: `/devtrack/api/`

### Reporters

#### Create a reporter

```
POST /devtrack/api/create-reporter/
```

**Request body:**

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "team": "Backend"
}
```

**Responses:**
- `201 Created` — reporter created successfully
- `400 Bad Request` — validation error or duplicate ID

---

#### Get all reporters

```
GET /devtrack/api/reporters/
```

**Response:** `200 OK` — list of all reporters

---

#### Get reporter by ID

```
GET /devtrack/api/reporters/<id>
```

**Example:** `GET /devtrack/api/reporters/1`

**Responses:**
- `200 OK` — reporter object
- `404 Not Found` — no reporter with that ID

---

### Issues

#### Create an issue

```
POST /devtrack/api/create-issue/
```

**Request body:**

```json
{
  "id": 1,
  "title": "Login page crashes on submit",
  "description": "Clicking submit on the login form throws a 500 error.",
  "status": "open",
  "priority": "high",
  "reporter_id": 1
}
```

**Allowed values:**
- `status`: `open`, `in_progress`, `resolved`, `closed`
- `priority`: `low`, `medium`, `high`, `critical`

**Responses:**
- `201 Created` — issue created successfully
- `400 Bad Request` — validation error or duplicate ID

---

#### Get all issues

```
GET /devtrack/api/issues/
```

**Response:** `200 OK` — list of all issues

To fetch a single issue by ID, pass a query parameter:

```
GET /devtrack/api/issues/?id=1
```

**Responses:**
- `200 OK` — issue object or list
- `404 Not Found` — no issue with that ID

---

#### Get issues by status

```
GET /devtrack/api/issues/status/?status=<status>
```

**Example:** `GET /devtrack/api/issues/status/?status=open`

Filtering is case-insensitive.

**Responses:**
- `200 OK` — list of matching issues
- `404 Not Found` — no issues with that status

---

## Data Storage

All data is stored as JSON files — no database setup or migrations are needed:

| Data      | File                              |
|-----------|-----------------------------------|
| Reporters | `issues/resources/reporters.json` |
| Issues    | `issues/resources/issues.json`    |

---

## Project Structure

```
django_devtrack/
├── manage.py
├── devtrack/              # Project configuration
│   ├── settings.py
│   └── urls.py
└── issues/                # Issues & reporters app
    ├── models.py          # Domain models (plain Python classes)
    ├── views.py           # API view functions
    ├── urls.py            # App URL routes
    └── resources/         # JSON data files
        ├── issues.json
        └── reporters.json
```

API test eveidences via Postman:

1) Create issues API -
   <img width="2226" height="600" alt="image (1)" src="https://github.com/user-attachments/assets/fc437726-6e87-496d-aa75-f063d57cccdc" />

   <img width="2248" height="674" alt="image (2)" src="https://github.com/user-attachments/assets/cb02545b-afad-442a-b38e-e699aae74104" />

   <img width="2246" height="740" alt="image (3)" src="https://github.com/user-attachments/assets/38b61b56-393f-4e96-8cfb-e033273739bb" />


   
   


