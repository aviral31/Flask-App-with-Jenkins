## Flask-App-with-Jenkins

This repository demonstrates a minimal Flask web application with a Jenkins pipeline for CI/CD automation.

### Project Structure
- `flask_app.py`: Main Flask application. Exposes a single route (`/`) returning "Hello, World!".
- `requirements.txt`: Python dependencies (only Flask required).
- `Jenkinsfile`: Jenkins pipeline configuration (add stages for install, test, deploy).

### Setup & Usage
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the app locally:**
   ```bash
   python flask_app.py
   ```
   The app runs on [http://localhost:5000](http://localhost:5000).

### CI/CD Pipeline
Use Jenkins to automate install, test, and deploy steps. Example pipeline stages:

### Notes
- All logic is in `flask_app.py`. Add new features or modules as needed.
- Update `requirements.txt` for new dependencies.