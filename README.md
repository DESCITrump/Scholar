# DESCITRUMP SCHOLAR

**DeSciTrump Scholar** is a web application designed to support the scientific community with features like a scientific document library, intelligent search, scholarship management, and a science-focused chatbot.

## Main Features

- **Scientific Document Library:** Manage and share research documents.
- **Intelligent Search:** Use full-text search to find relevant documents.
- **Scholarship Management:** Post and search for scholarship opportunities.
- **Q&A Chatbot:** Provide answers to scientific inquiries (future feature or using an external service).
- **User Authentication & Management:** Registration, login with JWT.

## Installation

### System Requirements
- Python 3.8+
- SQLite (or another SQL database if you prefer to change)

### Software Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DeSciTrump/DeSciTrump-Scholar.git
   cd DeSciTrump-Scholar

Install dependencies:
bash
pip install -r requirements.txt
Configuration:
Copy config.py.example to config.py and configure environment variables if necessary.
Initialize the database:
Run the following command to create the database tables:
bash
python run.py db init
python run.py db migrate
python run.py db upgrade
Run the application:
bash
python run.py

Project Structure
app/: Contains the main Flask application code.
__init__.py: Application initialization.
models.py: Data model definitions.
routes.py: Main route handlers.
auth.py: User authentication.
api/: APIs for documents, search, scholarship.
services/: Services like the chatbot.
templates/: HTML files for the frontend.
config.py: Application configuration.
run.py: Script to run the application.
requirements.txt: List of required Python libraries.
migrations/: Directory containing database migrations.
static/: Static resources like CSS and JavaScript.

Contributing
We welcome contributions! If you have ideas, bug reports, or want to add new features:

Open an issue to discuss.
Fork the repository, make changes, and submit a pull request.