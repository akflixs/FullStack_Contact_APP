# FullStack Contacts App

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/version-1.0.0-success.svg" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/python-3.10+-informational.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/flask-2.0+-informational.svg" alt="Flask 2.0+">
  <img src="https://img.shields.io/badge/react-18.0+-informational.svg" alt="React 18.0+">
</p>

A minimal yet functional full-stack CRUD (Create, Read, Update, Delete) application for managing contacts. Built with a Python/Flask backend, React (via Vite) frontend, and SQLite for data persistence. This repository demonstrates a simple but complete workflow—from database modeling to dynamic user interfaces.


## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)
   - [Backend Component](#backend-component)
   - [Frontend Component](#frontend-component)
5. [File Structure](#file-structure)
6. [API Endpoints](#api-endpoints)
7. [License](#license)
8. [Contact](#contact)
9. [Future Enhancements](#future-enhancements)

## Overview

This project serves as a practical example of a full-stack application implementing all CRUD operations. It's designed to showcase modern development practices while maintaining simplicity and clarity—ideal for educational purposes, portfolio demonstrations, or as a starting point for more complex applications.

## Features

- **Contact Management**: Add, view, update, and delete contact information
- **Responsive Design**: Functional on both desktop and mobile devices
- **Form Validation**: Client and server-side validation for data integrity
- **REST API**: Well-structured API endpoints for all operations
- **Data Persistence**: SQLite database for storing contact information
- **Modern Frontend**: React components with hooks for state management
- **Clean Architecture**: Separation of concerns between frontend and backend

## Tech Stack

### Backend
- **Python**: Core programming language
- **Flask**: Lightweight web framework
- **SQLAlchemy**: ORM for database operations
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **SQLite**: Embedded relational database

### Frontend
- **React**: UI library for building component-based interfaces
- **Vite**: Next-generation frontend tooling
- **JavaScript/ES6+**: Modern JavaScript syntax
- **Node.js**: JavaScript runtime environment
- **Fetch API**: For making HTTP requests to the backend

## Getting Started

### Backend Component

- **RESTful API Design**: Implemented a Flask-based REST API with proper HTTP methods for CRUD operations
- **Database Integration**: Utilized SQLAlchemy ORM for abstracting database operations
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **Data Validation**: Server-side validation ensuring data integrity
- **Resource Organization**: Structured routes by resource for maintainability
- **Cross-Origin Configuration**: Configured CORS to allow secure cross-origin requests

### Frontend Component

- **Component Architecture**: Built reusable React components for contacts management
- **State Management**: Utilized React hooks (useState, useEffect) for efficient state management
- **API Integration**: Implemented fetch API calls to interact with backend endpoints
- **Responsive Design**: Created mobile-friendly UI with CSS
- **Form Handling**: Developed controlled components for form submissions with validation
- **Event Handling**: Implemented event handlers for user interactions

## File Structure

```
FullStack_Contacts_App/
├── backend/
│   ├── instance/
│   │   └── mydatabase.db
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.css
    │   ├── App.jsx
    │   ├── ContactForm.jsx
    │   ├── ContactList.jsx
    │   ├── index.css
    │   └── main.jsx
    ├── index.html
    ├── package-lock.json
    ├── package.json
    ├── README.md
    └── vite.config.js
```

## API Endpoints

| Method | Endpoint                      | Description                 |
|--------|-------------------------------|-----------------------------|
| GET    | `/contacts`                   | Retrieve all contacts       |
| POST   | `/create_contact`             | Create a new contact        |
| PATCH  | `/update_contact/<user_id>`   | Update an existing contact  |
| DELETE | `/delete_contact/<user_id>`   | Delete a contact            |

## Response Codes

| Code | Description           |
|------|-----------------------|
| 200  | Success               |
| 201  | Created               |
| 400  | Bad Request           |
| 404  | Not Found             |
| 500  | Internal Server Error |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Email**: akflixs@gmail.com
- **LinkedIn**: [linkedin.com/in/akflixs](https://www.linkedin.com/in/akflixs/)
- **GitHub**: [github.com/akflixs](https://github.com/akflixs)

## Future Enhancements

- User authentication and authorization
- Contact categorization/grouping
- Search and filter functionality
- Cloud deployment configuration
- Contact import/export features
- Image upload for contact avatars
- Dark mode theme support
- Pagination for large contact lists
- Comprehensive test suite
