pipeline {
    agent { dockerfile true }
    environment {DOCKERHUB_CREDENTIALS = credentials('evgeniyklimovich4-docker-hub')}
    stages {
        stage('run linters and tests') {
            steps {
                sh 'python --version '
                sh 'flake8 . '
                sh 'pytest'
            }
        }
        stage('build docker image') {
            steps {
                sh 'docker build backend/Dockerfile'
            }
        }
    }
}