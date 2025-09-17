pipeline {
    agent any  

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aviral31/Flask-App-with-Jenkins.git'
            }
        }

        stage('Build') {
            steps {
                sh 'sudo pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'python flask_app.py'
            }
        }
    }
}