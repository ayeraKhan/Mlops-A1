pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/ayeraKhan/Mlops-A1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('ayerakhan/ml-api')
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image('ayerakhan/ml-api').push('latest')
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 ayerakhan/ml-api'
                }
            }
        }
    }
}
