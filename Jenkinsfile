pipeline{
    agent any  
    stages{
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aviral31/Flask-App-with-Jenkins.git'
            }
        }
        stage ('Build')
        {
            steps{
            sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
        }
        }
         stage('Test')
         {
             steps{
            sh 'sudo pytest'
         }
         }
         stage('Deploy')
         {
             steps{
            sh 'sudo python flask_app.py'
         }
         }
    }
} 
