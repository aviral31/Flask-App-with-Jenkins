````
# Flask CI/CD Pipeline with Jenkins

## 📌 Project Overview
This project sets up a **CI/CD pipeline** for a simple Flask web application using **Jenkins**.  
The pipeline automates the following:
1. **Build** – Install Python dependencies inside a virtual environment.
2. **Test** – Run unit tests with `pytest`.
3. **Deploy** – Deploy the Flask app to a staging environment if tests pass.
4. **Notify** – Send email notifications on success or failure.

The pipeline is defined in a `Jenkinsfile` stored at the root of this repository.

## ⚙️ Prerequisites
Before running the pipeline, ensure the following are installed and configured:

- **Jenkins** (with the following plugins):
  - Pipeline
  - GitHub plugin
  - Git plugin
  - Email Extension (optional, for notifications)
- **Python 3.x** with `venv` support on the Jenkins agent
- **GitHub repository** forked and connected to Jenkins
- **GitHub webhook** configured for push events:
  - URL: `https://jenkinsacademics.herovired.com//github-webhook/`
  - Content type: `application/json`

## 🏗️ Pipeline Stages

### 1. Checkout
- Jenkins checks out the latest code from the GitHub repository.

### 2. Build
- Creates a Python virtual environment (`venv`).
- Installs required dependencies from `requirements.txt`:
  ```bash
  python3 -m venv venv
  ./venv/bin/pip install -r requirements.txt
````

### 3. Test

* Runs unit tests with `pytest`:

  ```bash
  ./venv/bin/pytest
  ```

### 4. Deploy

* Starts the Flask application in the background:

  ```bash
  nohup ./venv/bin/python flask_app.py > flask.log 2>&1 &
  echo $! > flask.pid
  ```
* Performs a smoke test using `curl` to ensure the app responds:

  ```bash
  curl -f http://127.0.0.1:5000/
  ```

### 5. Post Actions

* **On Success**: Email notification sent with job details.
* **On Failure**: Email notification sent with error details, Flask app stopped.
* **Always**: Archive logs (`flask.log`) as build artifacts.

## 📂 Repository Structure

```
├── flask_app.py         # Main Flask application
├── requirements.txt     # Python dependencies
├── test_flask_app.py    # Unit tests (pytest)
├── Jenkinsfile          # CI/CD pipeline definition
└── README.md            # Project documentation
```

## 📸 Screenshots

Please replace the placeholders below with your actual Jenkins pipeline screenshots before submission:

1. **Pipeline Overview (all stages visible)**
   ![Pipeline Overview](https://github.com/aviral31/Flask-App-with-Jenkins/blob/f4c3ed125cf257e8f85f079b37589e6652fc5253/JF1.png)
![Image Alt](https://github.com/aviral31/Flask-App-with-Jenkins/blob/f4c3ed125cf257e8f85f079b37589e6652fc5253/JF2.png)
![Image Alt](https://github.com/aviral31/Flask-App-with-Jenkins/blob/f4c3ed125cf257e8f85f079b37589e6652fc5253/JF3.png)

2. **Build & Test stage success**
   ![Build and Test Stage](https://github.com/aviral31/Flask-App-with-Jenkins/blob/f4c3ed125cf257e8f85f079b37589e6652fc5253/test.png)
![Image Alt](https://github.com/aviral31/Flask-App-with-Jenkins/blob/f4c3ed125cf257e8f85f079b37589e6652fc5253/Deploy.png)

3. **Deploy stage (Flask app running)**
   ![Flask App](https://github.com/aviral31/Flask-App-with-Jenkins/blob/2eaf9b1bafc97f4fbc7844a6ca4b2cd71b34b6f1/app_running.png)

4. **Email notification (success/failure)**
   ![Email Notification](https://github.com/aviral31/Flask-App-with-Jenkins/blob/f4c3ed125cf257e8f85f079b37589e6652fc5253/Jenkinsemailnotification.png)

---

## 🎯 Conclusion

This project demonstrates how to implement a **Jenkins CI/CD pipeline** for a Flask application using **virtual environments, pytest, and Jenkins declarative pipelines**.
The setup ensures reliable builds, automated testing, and deployment with minimal manual intervention.

---
