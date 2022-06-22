pipeline {
    agent { dockerfile true }
    environment {DOCKERHUB_CREDENTIALS = credentials('klimovichevgeniy-docker-hub')}
    stages {
        stage('run linters and tests') {
            steps {
                sh 'python --version '
                sh 'flake8 . '
                sh 'pytest'
            }
        }
        stage('login dockerhub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push docker image') {
            steps {
                sh 'docker push fastapi/ci-cd:$BUILD_NUMBER'
            }
        }
    }
}