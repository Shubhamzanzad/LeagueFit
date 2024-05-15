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
        
            
        stage('Build Docker Compose') {
            steps {
                script {

                    sh 'docker rm backend'
                    sh 'echo "1"'
                    // sh 'docker rm frontend'
                    // sh 'echo "2"'
                    sh 'docker rm dataset'
                    sh 'echo "3"'
                    sh 'docker-compose up'
                    sh 'echo 4"'
                }
            }
        }
        
        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'DockerHubCred') {
                        sh 'docker tag dataset zanzadshubham/dataset:latest'
                        sh 'docker push zanzadshubham/dataset'

                        sh 'docker tag backend zanzadshubham/backend:latest'
                        sh 'docker push zanzadshubham/backend'

                        sh 'docker tag frontend zanzadshubham/frontend:latest'
                        sh 'docker push zanzadshubham/frontend'
                    }
                 }
            }
        }
        
        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }
        // stage('Run Tests') {
        //     steps {
        //         script{
        //             sh 'python3 test.py'
        //         }
        //     }    
        // }
    }
}
