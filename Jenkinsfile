pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                /usr/bin/python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Your testing steps go here, ensure the virtual environment is activated if needed
                sh '''
                . venv/bin/activate
                // Add your test commands here
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Your deployment steps go here, ensure the virtual environment is activated if needed
                sh '''
                . venv/bin/activate
                // Add your deployment commands here
                '''
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf venv' // Corrected to remove the 'venv' directory
        }
    }
}

