pipeline {
    agent any // Use a Docker agent or any other agent depending on your needs

    environment {
        PYTHON = '/usr/bin/python3'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'

                // Use the PYTHON environment variable to specify the Python interpreter
                sh '${PYTHON} -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Ensure the virtual environment is activated before testing
                sh '. venv/bin/activate'
                // Insert your testing commands here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Ensure any necessary environment setup for deployment
                // Insert your deployment commands here
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
