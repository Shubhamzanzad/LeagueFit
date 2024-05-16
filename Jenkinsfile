pipeline {
    agent any
    environment {
        DATASET_IMAGE_NAME = 'dataset'
        BACKEND_IMAGE_NAME = 'backend'
        FRONTEND_IMAGE_NAME = 'frontend'
        GITHUB_REPO_URL = 'https://github.com/Shubhamzanzad/LeagueFit.git'
        PATH = ""
        DOCKERHUB_CREDENTIALS = credentials('LeagueFit-DockerHub')
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
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

        stage('Dockerhub Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Docker Images') {
            steps {
                script{
                    sh 'docker tag dataset zanzadshubham25/dataset:latest'
                    sh 'docker push zanzadshubham25/dataset'

                    sh 'docker tag backend zanzadshubham25/backend:latest'
                    sh 'docker push zanzadshubham25/backend'

                    sh 'docker tag frontend zanzadshubham25/frontend:latest'
                    sh 'docker push zanzadshubham25/frontend'
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
            sh 'docker logout'
        }
    }
}
