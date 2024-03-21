pipeline {
    agent any // Use a Docker agent or any other agent depending on your needs

    environment {
        PYTHON = '/usr/bin/python3' // Specify the path to the Python interpreter
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                
                // Create a virtual environment
                sh '${PYTHON} -m venv venv'
                // Directly use pip from the virtual environment to install dependencies
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Check all requirements are met
                sh 'venv/bin/python check_requirements.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Ensure any necessary environment setup for deployment
                // Directly use python from the virtual environment if needed
                // For example, if deploying with a Python script: sh 'venv/bin/python deploy_script.py'
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
