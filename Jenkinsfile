pipeline {
    agent any
    parameters {
        string(
            name: 'GCP_VM_IP',
            defaultValue: '',
            description: 'External IP of the GCP VM'
        )
    }
    environment {
        DATASET_IMAGE_NAME = 'dataset'
        BACKEND_IMAGE_NAME = 'backend'
        FRONTEND_IMAGE_NAME = 'frontend'
        GITHUB_REPO_URL = 'https://github.com/Shubhamzanzad/LeagueFit.git'
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
                withCredentials([usernamePassword(credentialsId: 'docker-token', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
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
        stage('Run Ansible Playbook') {
            steps {
                script {
                    if (!params.GCP_VM_IP?.trim()) {
                        error 'GCP_VM_IP parameter is required. Provide the VM external IP before running the pipeline.'
                    }
                    sh """
                    printf '[leaguefit]\\n${params.GCP_VM_IP} ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/google_compute_engine ansible_ssh_common_args=\\'-o StrictHostKeyChecking=no\\'\\n' > inventory
                    ansible-playbook deploy.yml -i inventory
                    """
                }
            }
        }
    }
    post {
        always {
            node(null) {
                sh 'docker logout'
            }
        }
    }
}