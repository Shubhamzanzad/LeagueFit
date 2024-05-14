pipeline {
    agent any
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
        
            
    stage('Build Docker Images') {
            steps {
                dir('/dataset') {
                     script {
                        docker.build("${DATASET_IMAGE_NAME}")
                    }       
                }
                dir('/backend') {
                     script {
                        docker.build("${BACKEND_IMAGE_NAME}")
                    }       
                }
                dir('/frontend') {
                     script {
                        docker.build("${FRONTEND_IMAGE_NAME}")
                    }       
                }
            }
        }
        
        stage('Push Docker Images') {
            steps {
                script {
                    docker.image("${DATASET_IMAGE_NAME}").push()
                }
                script {
                    docker.image("${BACKEND_IMAGE_NAME}").push()
                }
                script {
                    docker.image("${FRONTEND_IMAGE_NAME}").push()
                }
            }
        }
        
        stage('Deploy with Docker Compose') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }
    }
}
