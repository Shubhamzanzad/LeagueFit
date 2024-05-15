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
        
        stage("Prune Docker Container") {
            steps {
                script {
                    sh 'docker system prune -a --volumes -f'
                    sh 'ls'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                dir('/dataset') {
                    sh "docker build -t ${DATASET_IMAGE_NAME} ."
                }
                dir('/backend') {
                    sh "docker build -t ${BACKEND_IMAGE_NAME} ."
                }
                dir('/frontend') {
                    sh "docker build -t ${FRONTEND_IMAGE_NAME} ."
                }
            }
        }

            
        stage('Build Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
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
    post {
        always {
            sh 'docker-compose down --remove-orphans -v'
            sh 'docker-compose ps'
        }
    }
}
