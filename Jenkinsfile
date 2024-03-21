pipeline {
    agent any // Use a Docker agent or any other agent depending on your needs

    environment {
        PYTHON = '/usr/bin/python3' // Specify the path to the Python interpreter
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                
                // Use the PYTHON environment variable to specify the Python interpreter
                sh '${PYTHON} -m venv venv' // Create a virtual environment
                sh '. venv/bin/activate' // Activate the virtual environment
                sh 'pip3 install -r requirements.txt' // Install dependencies
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Ensure the virtual environment is activated before testing
                sh '. venv/bin/activate' // Make sure to activate the virtual environment
                // Insert your testing commands here, e.g., `sh 'python -m unittest discover'`
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Ensure any necessary environment setup for deployment
                // Insert your deployment commands here
                // Example: sh './deploy.sh'
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
