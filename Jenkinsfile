pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                
                // Diagnostic commands to check Python availability and version
                sh 'which python3 || true'
                sh '/usr/bin/python3 --version || true'
                
                // The original command to create a virtual environment
                sh '/usr/bin/python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
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
            sh 'rm -rf venv' // Clean up the virtual environment directory
        }
    }
}
