pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git branch: 'main', url: 'https://github.com/Amneet10/flask-weather-services.git'
            }
        }


        stage('Build') {
            steps {
                // Build Docker image
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Check') {
            steps {
                // Start the Flask development server
                sh 'flask run --host=0.0.0.0 & sleep 10' // Start the server in the background
            }
        }




        // Add more stages as needed for your pipeline
    // }
    // // Optionally, you can define post actions like cleanup or notifications
    // post {
    //     always {
    //         // Clean up workspace
    //         cleanWs()
    //     }
    }
}