
pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-python-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f my-python-app || true

                    docker run -d \
                    --restart unless-stopped \
                    --name my-python-app \
                    -p 8081:5000 \
                    my-python-app:${BUILD_NUMBER}
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh 'curl -f http://localhost:8081'
            }
        }
    }
}
