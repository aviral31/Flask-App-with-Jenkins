pipeline{
    agent any
    environment{    
        FLASK_APP='flask_app.py'
        FLASK_ENV='development'
    }   
    stages{
        stage ('Build')
        {
            sh 'apt-get update'
            sh 'apt-get install python3-pip -y'
            sh 'pip install -r requirements.txt'
        }
         stage('Test')
         {
            sh 'pytest'
         }
         stage('Deploy')
         {
            FLASK_ENV='development'
            sh 'python flask_app.py'
         }
    }

} 
