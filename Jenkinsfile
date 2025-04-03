pipeline{
  agent any
  environment{
    VENV_DIR = 'venv'
  }
  stages{
    stage('cloning the github repo to jenkins'){
      steps{
        script{
          echo 'cloning the github repo..............'
          checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Deepak25khatri/hotel_management_mlops.git']])
        }
      }
    }
    stage('Setting up virtual environment and installing dependencies'){
      steps{
        script{
          echo 'Setting up virtual environment and installing dependencies..............'
          sh '''
          python -m venv ${VENV_DIR}
          . ${VENV_DIR}/bin/activate
          pip install --upgrade pip
          pip install -e .
          '''
        }
      }
    }
  }
}