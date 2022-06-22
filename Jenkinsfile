#!groovy

pipeline {
  agent none
  stages {
    stage('Maven Install') {
      agent {
        docker {
          image 'maven:3.5.0'
        }
      }
    }
    stage('Linters and tests')
        {
            agent { dockerfile true }
            steps
            {
                sh 'mypy .'
                sh 'flake8 . '
                sh 'pytest'
            }

    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t fastapi/ci-cd:latest .'
      }
    }
  }
}