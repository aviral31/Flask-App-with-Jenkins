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
<<<<<<< HEAD
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
=======
>>>>>>> 94253c9ea63ffcbf8cc52c1b8c7c773913313c91
            }
        }

        stage('Deploy') {
            steps {
<<<<<<< HEAD
                sh '''
=======
                 sh '''
>>>>>>> 94253c9ea63ffcbf8cc52c1b8c7c773913313c91
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
<<<<<<< HEAD
}
=======
}
>>>>>>> 94253c9ea63ffcbf8cc52c1b8c7c773913313c91
