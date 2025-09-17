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
            sh 'sudo apt-get update'
            sh 'sudo apt-get install python3-pip -y'
            sh 'sudo pip install -r requirements.txt'
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
