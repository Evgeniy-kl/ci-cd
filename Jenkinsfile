pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'python --version '
                sh 'flake8 . '
            }
        }
    }
}