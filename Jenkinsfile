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
                sh `sudo apt install python3 -y`
                sh 'sudo apt install python3-flask -y'
                sh 'sudo apt install python3-pytest -y'
            }
        }

        stage('Deploy') {
            steps {
                sh 'python flask_app.py'
            }
        }
    }
}
