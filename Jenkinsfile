pipeline {
    agent any
    environment {
        DATASET_IMAGE_NAME = 'dataset'
        BACKEND_IMAGE_NAME = 'backend'
        FRONTEND_IMAGE_NAME = 'frontend'
        GITHUB_REPO_URL = 'https://github.com/Shubhamzanzad/LeagueFit.git'
        ANSIBLE_SUDO_PASS = credentials('ansible-sudo-password') 
        PATH = ""
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        stage('Unit Testing'){
            steps{
                dir('./backend'){
                    sh 'sudo apt-get install -y python3-numpy python3-pandas python3-sklearn'
                    sh 'python3 -m unittest test.py'
                }
            }
        }
        stage("Prunning") {
            steps {
                script {
                    sh 'docker system prune -a --volumes -f'
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                dir('./dataset') {
                    sh "docker build -t ${DATASET_IMAGE_NAME} ."
                }
                dir('./backend') {
                    sh "docker build -t ${BACKEND_IMAGE_NAME} ."
                }
                dir('./frontend') {
                    sh "docker build -t ${FRONTEND_IMAGE_NAME} ."
                }
            }
        }
        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'LeagueFit-DockerHub') {
                    sh ''' 
                        docker tag dataset zanzadshubham25/dataset:latest
                        docker push zanzadshubham25/dataset
                        docker tag backend zanzadshubham25/backend:latest
                        docker push zanzadshubham25/backend
                        docker tag frontend zanzadshubham25/frontend:latest
                        docker push zanzadshubham25/frontend
                    '''
                    }
                }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                script {
                    sh '''
                    ansible-playbook deploy.yml -i inventory --become --become-user=root --extra-vars "ansible_become_pass=${ANSIBLE_SUDO_PASS}"
                    '''
                }
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}