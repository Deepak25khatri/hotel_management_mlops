pipeline {
  agent any
  environment {
    VENV_DIR = '/tmp/venv'
    GCP_PROJECT = "silent-venture-455019-b5"
    GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
  }
  
  stages {
   

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
    stage('Building and Pushing Docker Image to GCR') {
    steps {
        withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
            script {
                echo 'Building and Pushing Docker Image to GCR.............'
                sh '''
                # Set the path explicitly
                export PATH=${GCLOUD_PATH}:$PATH
                
                # Verify gcloud is available
                which gcloud
                
                # Activate service account with full path to key file
                gcloud auth activate-service-account --key-file="${GOOGLE_APPLICATION_CREDENTIALS}" --project=${GCP_PROJECT}
                
                # Verify authentication
                gcloud auth list
                
                # Configure Docker
                gcloud auth configure-docker --quiet
                
                # Build and push
                docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
                docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                '''
            }
        }
    }
}
  }
}
