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
    stage('Building and Pushing Docker Image to GCR'){
            steps{
              
                withCredentials([file(credentialsId: 'gcp-key' , variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                      sh 'rm -rf venv'
                        echo 'Building and Pushing Docker Image to GCR.............'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}


                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest 

                        '''
                    }
                }
            }
        }
  }
}
