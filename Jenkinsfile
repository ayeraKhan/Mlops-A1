pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'  // Jenkins credentials ID
        IMAGE_NAME = 'your-dockerhub-username/your-image-name'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "docker login -u $DOCKER_USER -p $DOCKER_PASS"
                        sh "docker push $IMAGE_NAME"
                    }
                }
            }
        }

        stage('Send Notification') {
            steps {
                mail to: 'admin@example.com',
                     subject: "Deployment Successful",
                     body: "The application has been successfully deployed and pushed to Docker Hub."
            }
        }
    }
}
