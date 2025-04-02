pipeline{
  agent any
  stages{
    stage('cloning the github repo to jenkins'){
      steps{
        script{
          echo 'cloning the github repo..............'
          checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Deepak25khatri/hotel_management_mlops.git']])
        }
      }
    }
  }
}