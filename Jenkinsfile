pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                sh '/usr/bin/python3 -m JenkinsPractice venv'
                #python3 -m JenkinsPractice venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Your testing steps go here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Your deployment steps go here
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf JenkinsPractice'
        }
    }
}


