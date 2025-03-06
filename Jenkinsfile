pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'  // Jenkins credentials ID
        IMAGE_NAME = 'ayerakhan/MlopsJenkins'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/ayeraKhan/Mlops-A1.git'
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
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push $IMAGE_NAME"
                    }
                }
            }
        }
    }

    post {
        success {
            mail to: 'admin@example.com',
                 subject: "✅ Deployment Successful",
                 body: "The application has been successfully deployed and pushed to Docker Hub."
        }
        failure {
            mail to: 'admin@example.com',
                 subject: "❌ Deployment Failed",
                 body: "The deployment has failed. Please check the Jenkins logs for details."
        }
    }
}
