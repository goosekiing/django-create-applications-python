# Django: Creating Web Applications in Python

This repository contains a Django project developed during the "Django: Creating Applications in Python" training at Alura. Throughout the course, which involves multiple modules, a site is built using best programming practices. The project is a website called Space, designed to display space images such as photographs of galaxies and nebulas. Users can create accounts, upload, and delete images. CRUD operations can be performed through the provided models or the Django admin interface.

## Project Overview

Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django handles much of the web development workload, allowing you to focus on writing your application without reinventing the wheel. It is free and open-source, has an active community, excellent documentation, and many support options.

### Learning Objectives
- Understand how Django works in a practical way
- Learn how templates and page rendering work in Django
- Maintain good programming practices in Django projects
- Create your own web applications using Python
- Manage data in a Django application using databases
- Get familiar with Django Admin, a native administrative route of the framework
- Create forms with Django's native tools
- Handle media files in Django
- Utilize Django's internal modules for form creation
- Access Django's internal database
- Validate form data
- Create dynamic alert messages
- Structure partials to avoid code duplication
- Advance your knowledge of the MTV (Model-Template-View) architecture
- Refactor and organize a Django project
- Get to know AWS S3
- Persist photographs in an S3 Bucket

This project is part of the "Django: Create Applications in Python" course at Alura, available at [Alura Django Course](https://cursos.alura.com.br/formacao-django).

## Project Structure
```
django-create-applications-python/
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
├── templates/
│   └── ... (HTML files, organized by app directories)
├── setup/
│   └── ... (configuration .py files)
├── apps/
│   ├── galeria/
│   │   └── ... (Python files for gallery app)
│   └── usuarios/
│       └── ... (Python files for users app)
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.11.4
- Virtual environment
- Django 4.1

### Steps to Run the Project

1. **Clone the repository**
    ```sh
    git clone https://github.com/goosekiing/django-create-applications-python.git
    cd django-create-applications-python
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the requirements**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**
    - Create a `.env` file in the root directory with the following variables:
      ```env
      SECRET_KEY=your_secret_key
      AWS_ACCESS_KEY_ID=your_aws_access_key_id
      AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
      AWS_STORAGE_BUCKET_NAME=your_aws_bucket_name
      ```

5. **Apply migrations**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**
    ```sh
    python manage.py runserver
    ```

## Language
The language used in this project is Brazilian Portuguese (pt-br).

## Author
GitHub Username: [goosekiing](https://github.com/goosekiing)