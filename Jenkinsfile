pipeline {
  agent any
  environment {
    VENV_DIR = '/tmp/venv'
  }
  
  stages {
    stage('Check Python Version') {
      steps {
        script {
          echo 'Checking Python version...'
          sh '''
          python3 --version || echo "Python3 is not installed"
          python --version || echo "Python is not installed"
          which python3 || echo "Python3 not found in PATH"
          which python || echo "Python not found in PATH"
          '''
        }
      }
    }

    stage('Cloning the GitHub Repo') {
      steps {
        script {
          echo 'Cloning the GitHub repo...'
          checkout scmGit(branches: [[name: '*/main']], extensions: [], 
            userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Deepak25khatri/hotel_management_mlops.git']])
        }
      }
    }

    stage('Setting up Virtual Environment and Installing Dependencies') {
      steps {
        script {
          echo 'Setting up virtual environment and installing dependencies...'
          sh '''
          python3 -m venv ${VENV_DIR} || python -m venv ${VENV_DIR}
          . /tmp/venv/bin/activate
          pip install --upgrade pip
          pip install -e .
          '''
        }
      }
    }
  }
}
