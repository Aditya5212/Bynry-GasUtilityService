# Gas Utility Service

## Overview

Gas Utility Service is a Django web application designed to help users manage their gas utility needs. It allows users to register, submit service requests, track their requests, and manage their profiles.

## Problem Statement

A gas utility company is experiencing a high volume of customer service requests. The company's current system is not able to handle the volume of requests, leading to long wait times and poor service for customers. This project aims to develop a Django application that provides consumer services for gas utilities, allowing customers to submit service requests online, track the status of their requests, and view their account information. Additionally, the application will provide customer support representatives with tools to manage requests and assist customers effectively.

## Features

- User Registration and Authentication
- Submit Service Requests
- Track Service Requests
- Modify and Delete Service Requests
- User Profile Management

## Technologies Used

- Django 5.1.3
- Bootstrap
- SQLite (for development)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd GasUtilityService
2. Create a virtual environment:
   ```bash
   python -m venv venv
3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
4. Run migrations:
   ```bash
   python manage.py migrate
5. Start the development server:
   ```bash
   python manage.py runserver

## Configuration

The settings.py file contains all the configuration settings for the Django project.

## Directory Structure
    ```bash
    gas-utility-service/
    │
    ├── GasUtilityService/           # Project settings and configuration
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── customer_service/            # Application for handling customer service requests
    │   ├── migrations/              # Database migrations for the app
    │   ├── templates/               # HTML templates for rendering views
    │   ├── static/                  # Static files (CSS, JavaScript)
    │   ├── admin.py                 # Admin interface configuration
    │   ├── apps.py                  # App configuration
    │   ├── models.py                # Database models
    │   ├── forms.py                 # Forms for handling user input
    │   ├── views.py                 # Views for handling requests and responses
    │   ├── urls.py                  # URL routing for the app
    │   └── tests.py                 # Test cases for the app
    │
    ├── theme/                       # Tailwind CSS and custom styles
    │   ├── static_src/
    │   ├── templates/
    │   └── ...
    │
    ├── manage.py                    # Command-line utility for administrative tasks
    └── requirements.txt             # Python dependencies

## Super user - admin
- username-aditya
- password-Pass@123


## Usage
- Users can register an account and log in to the application.
- Once logged in, users can submit service requests by filling out the provided form.
- Users can track their service requests, view their status, and modify or delete them as necessary.

## Snapshots
Here are some snapshots of the Gas Utility Service application:

### Home Page
![Home Page](https://github.com/user-attachments/assets/d64987e6-b34b-4afb-845f-0c1b0762ca4e)

### Login/Register Page
![Login](https://github.com/user-attachments/assets/112b346e-7362-4fd8-bcce-697fe0083dda)
![Register Page](https://github.com/user-attachments/assets/14ad17d5-69ab-486c-95fd-4d7d97a0a5e9)

### Service Request Form
![Service Request Form](https://github.com/user-attachments/assets/02adc25c-a9c5-463d-8ea1-14faf0135f53)

### Request Tracking
![Request Tracking](https://github.com/user-attachments/assets/bc7f008c-eb0d-4fdc-b9b3-96189a2561fa)

### Modify Request
![Modify Request](https://github.com/user-attachments/assets/5e46106b-57c0-4c12-82a6-f4d8ab7d0e02)

### Admin Dashboard
![Admin Dashboard](https://github.com/user-attachments/assets/3e4261ba-2b99-490f-a573-fdc188054192)
![Admin Dashboard](https://github.com/user-attachments/assets/d0c6427e-fe5e-453c-8bf4-22d722e2a9f1)
![Admin Dashboard](https://github.com/user-attachments/assets/eb8821b5-bab8-4312-b9d3-15fa8c4e63ef)


