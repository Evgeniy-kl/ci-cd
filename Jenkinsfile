pipeline {
    agent { dockerfile true }
    environment {DOCKERHUB_CREDENTIALS = credentials('klimovichevgeniy-docker-hub')}
    stages
    {
        stage('test build and push')
        {
            steps
            {
                sh 'python --version '
                sh 'flake8 . '
                sh 'pytest'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push fastapi/ci-cd:$BUILD_NUMBER'

            }

        }
    }
}