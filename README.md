# FlavorVault-A_Recipe_Management_System
FlavorVault: Recipe Management System
Welcome to **FLAVORVAULT**, a versatile recipe management system built using Django, Bootstrap, and SQLite. This application helps you efficiently store, organize, and explore your favorite recipes with a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
<!-- - [License](#license)
- [Contact](#contact) -->

## Features

- **Recipe Storage:** Save and categorize your recipes.
- **Ingredient Management:** Manage and customize your ingredient list.
- **Meal Planning:** Plan your meals and generate shopping lists.
- **Search and Filter:** Easily find recipes by ingredients, tags, or categories.
- **User Accounts:** Create and manage user profiles for a personalized experience.
- **Responsive Design:** A modern and responsive user interface using Bootstrap.

## Getting Started

To get started with FLAVORVAULT, follow these steps to set up the project on your local machine.

### Prerequisites

- [Python](https://www.python.org/) (version 3.8 or higher)
- [Django](https://www.djangoproject.com/) (version 4.x or higher)
- [SQLite](https://www.sqlite.org/) (included with Django by default)
- [Bootstrap](https://getbootstrap.com/) (included via CDN in HTML)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Bhushan-3000/FLAVORVAULT-RECIPE-MANAGEMENT-SYSTEM.git



Navigate to the Project Directory

bash
cd FLAVORVAULT-RECIPE-MANAGEMENT-SYSTEM
Create a Virtual Environment

bash
python -m venv venv
Activate the Virtual Environment

On Windows:

bash
venv\Scripts\activate
On macOS/Linux:

bash
source venv/bin/activate
Install Dependencies

bash
pip install -r requirements.txt
Apply Migrations

bash
python manage.py migrate
Create a Superuser (optional but recommended for admin access)

bash
python manage.py createsuperuser
Run the Development Server

bash
python manage.py runserver

The application will be available at http://127.0.0.1:8000.


## Usage

After setting up the project, you can access FLAVORVAULT at http://127.0.0.1:8000.

Register/Login: Create an account or log in to start using the system.

Add Recipes: Use the form to add new recipes.

Search & Filter: Use the search functionality to find recipes by ingredients or categories.

Plan Meals: Use the meal planning feature to organize your meals and generate shopping lists.

Admin Interface: Access the Django admin interface at http://127.0.0.1:8000/admin for managing users and recipes.

## Contributing

We welcome contributions to FLAVORVAULT! To contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes and commit them (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Open a pull request with a clear description of your changes.
