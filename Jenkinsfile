pipeline {
    agent any
      /*  docker {
            image 'python:3.10' // Specify your desired Python version
            args '-u root:root' // Run as root if necessary
        }
    }  /*

    stages {
        stage('Build') {
            steps {
                echo 'Building...'

                // Now, Python and pip are available from the Docker image
                // No need for diagnostic commands; Python is guaranteed to be available
                
                // If you still want to use a virtual environment
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Your testing steps go here
                // Remember to activate the virtual environment if you're using one
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Your deployment steps go here
                // Ensure the necessary environment or tools are available
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            // Cleanup is simplified since Docker handles most isolation
            sh 'rm -rf venv' // Optional: Clean up the virtual environment directory if used
        }
    }
}
