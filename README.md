# 🧁 Django Webpage Project

This is a basic Django web application that demonstrates a small website setup with two Django apps: `chai` and `biscuit`. The project uses templates, static files, views, and URL routing.

---

## 📁 Project Structure

```
Django_webpage/
│
├── Django/                  # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── biscuit/                # Biscuit app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/biscuit/all_biscuit.html
│
├── chai/                   # Chai app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/chai/all_chai.html
│
├── templates/
│   └── index.html          # Main index template
│
├── static/
│   └── style.css           # Stylesheet
│
├── db.sqlite3              # SQLite database
└── manage.py               # Django management script
```

---

## 🚀 Features

- Two modular Django apps: **chai** and **biscuit**
- Template-based rendering for both apps
- Static file handling (CSS)
- Basic routing using `urls.py`
- Admin interface support
- SQLite database

---

## 🛠️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Django_webpage.git
   cd Django_webpage/Django
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install django
   ```

4. **Apply migrations and run the server:**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the site:**

   Open your browser and go to: `http://127.0.0.1:8000/`

---

## 🧩 App URLs

- Home Page: `/`
- Chai List: `/chai/`
- Biscuit List: `/biscuit/`

---

## 👨‍💻 Author

**YASH THAKUR**  
[GitHub Profile](https://github.com/ceYASH)
