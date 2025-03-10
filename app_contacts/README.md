# Contact Manager Application (Carnet d'adresse)

A simple yet powerful contact management application built with Django and TinyDB. This application allows users to manage their contacts with a clean and responsive interface.

## Features

- Add new contacts with:
  - First name and last name
  - Phone number (with validation)
  - Address information
- View all contacts in a responsive table layout
- Mobile-friendly interface with Bootstrap 5
- Delete existing contacts with one click
- No SQL database required (uses TinyDB for data storage)
- Input validation for names and phone numbers

## Technical Stack

- **Backend:**
  - Python 3.13
  - Django 5.1.6
  - TinyDB (lightweight document database)
  - Custom validation for phone numbers and names

- **Frontend:**
  - Bootstrap 5.3.3
  - Responsive design
  - Mobile-first approach
  - Clean and intuitive UI

## Project Structure

```
app_contacts/
├── api/
│   ├── crm.py          # Business logic and TinyDB integration
│   └── db.json         # TinyDB database file
├── webapp/
│   ├── contacts/       # Main Django app
│   │   ├── templates/  # HTML templates
│   │   ├── static/     # CSS, JS files
│   │   └── views.py    # View functions
│   └── webapp/         # Django project settings
└── README.md          # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DzmitryiKorjik/Contact-Manager-Application.git
cd Contact-Manager-Application
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install django tinydb
```

4. Run migrations:
```bash
cd webapp
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Usage

1. **Adding a Contact:**
   - Fill in the contact form with required details
   - Click "Ajouter" to save the contact
   - All fields are validated before saving

2. **Viewing Contacts:**
   - All contacts are displayed in a responsive table
   - Table adapts to different screen sizes
   - Contact information is clearly organized

3. **Deleting a Contact:**
   - Click "Supprimer" button next to the contact
   - Contact is immediately removed from the database

## Validation Rules

- **Names:**
  - Cannot be empty
  - Cannot contain special characters or numbers
  - Both first name and last name are required

- **Phone Numbers:**
  - Must be at least 10 digits
  - Can contain spaces, parentheses, and plus sign
  - All non-digit characters are stripped during validation

## Security Features

- CSRF protection enabled
- Debug mode configurable
- Security middleware enabled

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

## Auteur
- **Name :** Mardovitch Dzmitryi
- **Formation :** Développement Web et Web Mobile.
- **Objective :** Validation des compétences en création et déploiement d'applications web.

## Acknowledgments

- Django documentation
- TinyDB project
- Bootstrap team
