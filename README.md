# Security Guard Ordering System

A modern web-based platform for ordering security guards from various organizations with ease and efficiency.

## Project Overview

The Security Guard Ordering System is designed to bridge the gap between security service providers and clients by introducing a digital platform that simplifies the ordering process. Clients can easily select their preferred security office, specify their needs (such as the number of guards, age, gender, and status), and place orders in real-time.

**Key Benefits:**
- Reduces inefficiencies in traditional guard hiring processes
- Improves customer satisfaction
- Modernizes security service delivery
- Provides transparency and real-time updates

## Features

### User Features
- User registration and authentication
- Place and track orders in real-time
- View order history

### Admin Features
-  Manage organizations,security office and guard profiles
-  Approve/reject orders
-  Monitor system performance

## Technology Stack

### Frontend
- **Framework**: React.js
- **Styling**: CSS
- **Routing**: React Router

### Backend
- **Framework**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)

### DevOps
- **Version Control**: Git & GitHub

## Installation

### Prerequisites
- Node.js 
- Python 
- PostgreSQL
- Git

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/security-guard-ordering-system.git
   cd security-guard-ordering-system/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## System Architecture

The system follows a three-tier architecture:

1. **Frontend**: React.js application that provides the user interface
2. **Backend**: Django REST API that processes business logic
3. **Database**: PostgreSQL for data persistence

**Developed by**:
- Hafidh Mwita Haji ([hafidhmwita30@hafidhmwita](https://github.com/hafidhmwita))
- Issa Kassim Moh'd ([issakassim9999@issakassim](https://github.com/WAKASSIMU))

**Supervisor**: Masoud Mmanga Hamad

**Institution**: The State University of Zanzibar

```
BITAM/11/23/099/TZ | BITAM/11/23/033/TZ
```
