# Ecommerce Backend Design (Django learning progression)

A progressive, step-by-step implementation of an E-commerce backend using Django, showing the evolution from static mockups to a fully dynamic web application.

---

## 📁 Repository Structure

The project is structured into three progressive weeks:

1. **`week-1-static/`**:
   - Initial implementation of the e-commerce layout.
   - Core pages (Home, Product Listing, and Product Details).
   - Utilizes static dummy data (`SAMPLE_PRODUCTS`) inside views.

2. **`week-2-dynamic/`**:
   - Integration with a database (SQLite) using Django Models.
   - Dynamically renders product catalog pages.
   - Includes custom Search functionality filtering products by name or category.

3. **`week-3-final/`**:
   - Complete, feature-rich Django application.
   - Adds Pagination (displays 2 products per page for streamlined manual testing).
   - User authentication flows (User Signup, Login, and Logout).
   - Restricted authorization: Adding new products is protected via the `@login_required` decorator.

---

## ✨ Features

- **Product Catalog**: Beautiful presentation of products with images, description, pricing, and category.
- **Search System**: Direct query support matching name and category (`Q` object lookup).
- **Pagination**: Easy navigation through product listings.
- **User Authentication**: Secure signup and login/logout pages.
- **Product Management**: A secure dashboard/form to add products dynamically directly into the system database.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have Python installed on your system.

### 2. Installation
Install Django using pip:
```bash
pip install django
```

### 3. Running the Server (e.g., Week 3 - Final)
Navigate into any of the project directories to run the server:

```bash
# Go to the final folder
cd week-3-final

# Run migrations to set up the database
python manage.py migrate

# Create a superuser to access the Django admin dashboard and add products
python manage.py createsuperuser

# Start the local development server
python manage.py runserver
```

Once the server is running, visit:
- **Main App**: `http://127.0.0.1:8000/`
- **Django Admin**: `http://127.0.0.1:8000/admin/`

---

## 🛠️ Technology Stack
- **Backend**: Django (Python Web Framework)
- **Database**: SQLite3 (Local file-based SQL DB)
- **Frontend**: Django Templates with HTML and CSS

---

## 📬 Push Info
Pushed to Github Remote: [ecomerce-backend-design](https://github.com/ar6327699-cpu/ecomerce-backend-design.git)
