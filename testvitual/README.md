# README for Flask App with Database Migration

This README provides an overview and basic instructions for a Flask web application that includes database migration using Flask-Migrate. This example assumes you have a Flask application for managing restaurants and their pizza menus

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Database Migration](#database-migration)
- [Running the Application](#running-the-application)
- [Using the Flask Shell](#using-the-flask-shell)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you get started, ensure you have the following prerequisites installed:

- Python (3.6 or later)
- Flask
- Flask-Script
- Flask-Migrate
- SQLAlchemy (for database management)
- Your preferred database system (e.g., PostgreSQL, MySQL, SQLite)

You can install these dependencies using pip:

```bash
pip install Flask Flask-Script Flask-Migrate SQLAlchemy
```

## Getting Started

1. Clone or download the project repository to your local machine.

2. Navigate to the project directory:

```bash
cd your-project-directory
```

3. Create a virtual environment to isolate project dependencies:

```bash
python -m venv venv
```

4. Activate the virtual environment:

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install project-specific packages:

```bash
pip install -r requirements.txt
```

6. Customize the Flask application in the `create_app()` function in `app.py` to match your project's requirements.

## Database Migration

This project uses Flask-Migrate for managing database migrations. Follow these steps to set up and apply database migrations:

1. Initialize the database migration environment:

```bash
flask db init
```

2. Create an initial migration:

```bash
flask db migrate -m "Initial migration"
```

3. Apply the migration to the database:

```bash
flask db upgrade
```

## Running the Application

You can run the Flask application using the Flask-Script manager. In your project directory, run:

```bash
python manage.py runserver
```

The application will be accessible at `http://localhost:5000` by default. You can customize the host and port in the `manage.py` file if needed.

## Using the Flask Shell

You can use the Flask shell to interact with the database and perform various tasks. To start the Flask shell, run:

```bash
python manage.py shell
```

This will provide you with access to the database and application context. You can use the pre-defined objects and functions set up in the `make_shell_context()` function in `manage.py`.

## Contributing

If you'd like to contribute to this project, please follow the standard open-source practices:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Create a pull request to the original repository.

## License
This project is licensed under the [License Name Here] License - see the LICENSE.md file for details.
Contributions are welcome! If you find any issues or improvements, feel free to create a pull request.

You can reach me on : Email: shadrackkibet100@@gmail.com Mattermost: @Shadrack Kibet: @kibet-shadrack License This project is licensed under the MIT License.

Copyright (c) [2023] [Shadrack Kibet]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.