# CRUD Project Setup Instructions

## Setting Up Django Environment

### 1. Set Up a Virtual Environment

To create a virtual environment, navigate to your project directory and run:
```bash
python3 -m venv myenv
```

### 2. Activate the Virtual Environment

To activate the virtual environment, use:
- On Windows:
  ```bash
  myenv\Scripts\activate
  ```
- On macOS and Linux:
  ```bash
  source myenv/bin/activate
  ```

### 3. Install Django

Once the virtual environment is activated, install Django by running:
```bash
pip install django
```

### 4. Create a New Django Project

To create a new Django project, run:
```bash
django-admin startproject myproject
```

### 5. Database Migration

Before running the server, apply the initial migrations with the following command:
```bash
python manage.py migrate
```

### 6. Run the Development Server

To start the development server, execute:
```bash
python manage.py runserver
``` 

Now, you're set up to start developing your CRUD application!