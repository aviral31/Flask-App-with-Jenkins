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
                sh 'sudo apt-get install python3-pip -y'
                sh 'sudo apt install python3-flask -y'
                sh 'sudo apt install python3-pytest -y'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
          python3 flask_app.py &
          FLASK_PID=$!
          echo "Flask running with PID $FLASK_PID"
          sleep 15   # simulate test time
          kill $FLASK_PID
          echo "Flask stopped"
        '''
            }
        }
    }
}