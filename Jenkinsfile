pipeline {
    agent any // Use a Docker agent or any other agent depending on your needs

    environment {
        PYTHON = '/usr/bin/python3'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'

                // If you still want to use a virtual environment
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Remember to activate the virtual environment if you're using one
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
            // Cleanup the virtual environment directory if used
            sh 'rm -rf venv'
        }
    }
}
