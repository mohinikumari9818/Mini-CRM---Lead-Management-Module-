🧩 Mini CRM – Lead Management Module

A simple full-stack Mini CRM application built to manage leads with secure authentication and basic CRUD functionality.
The project focuses on clean architecture, API design, and functionality, keeping the UI minimal as per assessment guidelines.

🚀 Tech Stack
Frontend

React

Axios

Basic CSS

Backend

Django

Django REST Framework

JWT Authentication (SimpleJWT)

Database

SQLite

Tools

Postman (API testing)

✨ Features

JWT-based user authentication

Lead management:

Create leads

View leads

Update lead status

Delete leads

Lead status tracking:

New

Contacted

Qualified

Protected REST APIs

Simple, clean, and functional UI

Separate frontend and backend structure

📂 Project Structure
Mini CRM – Lead Management Module/
├── crm_backend/
│   ├── crm_backend/
│   ├── leads_app/
│   ├── manage.py
│   └── db.sqlite3
├── crm-frontend/
│   ├── src/
│   ├── public/
│   └── package.json
└── .gitignore

🔐 Authentication

Authentication is handled using JWT

After login, the access token must be sent in request headers:

Authorization: Bearer <access_token>


All lead-related APIs are protected.

📡 API Endpoints
Method	Endpoint	Description
POST	/api/token/	Generate JWT token
GET	/api/leads/	Fetch all leads
POST	/api/leads/	Create a new lead
PATCH	/api/leads/{id}/	Update lead status
DELETE	/api/leads/{id}/	Delete a lead
🛠 Backend Setup
cd crm_backend
py -m pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver


Backend runs at:

http://localhost:8000

🎨 Frontend Setup
cd crm_backend/crm-frontend
npm install
npm start


Frontend runs at:

http://localhost:3000

🧪 Testing

APIs were tested using Postman

Frontend communicates with backend using Axios

JWT token is stored in browser localStorage after login

📝 Notes

UI is intentionally kept minimal as per assessment requirements

Focus is on backend logic, API security, and frontend-backend integration

SQLite is used for simplicity and ease of setup

CORS configured for local development
