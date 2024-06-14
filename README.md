# Django: Create Applications in Python

This repository contains a Django project developed during the "Django: Create Applications in Python" training on Alura. The project is a website called Alura Space, designed to showcase space images such as photographs of galaxies and nebulae. Users can create accounts, upload, and delete images. The CRUD operations can be performed either through the provided templates or the Django admin interface.

This project was developed by the student during the "Django: Create Applications in Python" training, which can be accessed at [Alura](https://cursos.alura.com.br/formacao-django).

## Project Overview
Django is a high-level Python web framework that enables the rapid development of secure and easy-to-maintain websites. Built by experienced developers, Django handles much of the web development workload, allowing you to focus on writing your application without reinventing the wheel. It is free, open-source, and boasts an active community, excellent documentation, and various support options.

In this training, you will learn:
- How to use Django templates and best programming practices.
- How to work with databases and create forms using Django's native tools.
- How to create user registrations and implement authentication mechanisms.
- How to create a photograph management system (CRUD) and use services like AWS S3 for cloud image storage.

## Technologies Used
- Python 3.11.4
- Django 4.1
- Additional libraries (listed in `requirements.txt`)

## Environment Variables
Create a `.env` file in the root directory of the project and define the following variables:
```
SECRET_KEY=your_secret_key
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_STORAGE_BUCKET_NAME=your_aws_storage_bucket_name
```

Replace `your_secret_key`, `your_aws_access_key_id`, `your_aws_secret_access_key`, and `your_aws_storage_bucket_name` with your actual values.

## Project Structure
The directory structure of the project is as follows:
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

## How to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/django-create-applications-python.git
   ```
2. Navigate to the project directory:
   ```sh
   cd django-create-applications-python
   ```
3. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
5. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. Set up the environment variables by creating a `.env` file in the project root and adding the necessary variables.

7. Apply migrations to set up the database:
   ```sh
   python manage.py migrate
   ```
8. Create a superuser to access the Django admin:
   ```sh
   python manage.py createsuperuser
   ```
9. Run the Django development server:
   ```sh
   python manage.py runserver
   ```

## Learn More
To learn more about Django and how to develop web applications with Python, visit the [Django documentation](https://docs.djangoproject.com/).

Feel free to explore, modify, and use this project as a foundation for your own Django applications!
