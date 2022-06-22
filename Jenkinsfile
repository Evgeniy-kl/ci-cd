pipeline {
    agent { label "linux" }
    environment {DOCKERHUB_CREDENTIALS = credentials('klimovichevgeniy-docker-hub')}
    stages
    {
        stage('test build and push')
        {
            steps
            {
                sh 'docker build -t fast_api .'
                sh 'mypy .'
                sh 'flake8 . '
                sh 'pytest'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push fastapi:$BUILD_NUMBER'

            }

        }
    }
}