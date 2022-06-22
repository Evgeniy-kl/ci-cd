pipeline {
  environment {
    imagename = "evgeniypython123/evgeniy"
    registryCredential = 'klimovichevgeniy-docker-hub'
    dockerImage = ''
  }
  agent any
  stages {

  stage('Lint and Test')
        {
        agent { dockerfile true }
            steps
            {
                sh 'black .'
                sh 'flake8 . '
                sh 'pytest'
            }

        }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script

        {
          docker.withRegistry( '', registryCredential )
          {
            dockerImage.push()
             dockerImage.push('latest')
          }
        }
      }
    }
  }
}