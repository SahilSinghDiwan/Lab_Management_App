# SortlyClone - Flask Backend

## Overview

This is the Flask backend for the SortlyClone app, a mobile app that allows users to manage inventory items within a lab environment.

## Requirements

- Python 3.10+
- Flask
- Flask-RESTful
- Flask-SQLAlchemy

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/sortly-backend.git
   cd sortly-backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```
   flask run
   ```

4. The API will be available at `http://127.0.0.1:5000/`

### Endpoints

- `POST /items`: Add a new items to the inventory. Note Add a method to import multiple items.

- `GET /items` : Get a list of all items in the inventory. Note add a method to get specific object.
