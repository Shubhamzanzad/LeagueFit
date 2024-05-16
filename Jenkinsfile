pipeline {
    agent any
    environment {
        DATASET_IMAGE_NAME = 'dataset'
        BACKEND_IMAGE_NAME = 'backend'
        FRONTEND_IMAGE_NAME = 'frontend'
        GITHUB_REPO_URL = 'https://github.com/Shubhamzanzad/LeagueFit.git'
        PATH = ""
        // DOCKERHUB_CREDENTIALS = credentials('LeagueFit-DockerHub')
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
        

        // 
        

        // stage('Dockerhub Login') {
        //     steps {
        //         sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        //     }
        // }

        // stage('Push Docker Images') {
        //     steps {
        //         script{
        //             docker.withRegistry('', 'LeagueFit-DockerHub') {
        //             sh ''' 
        //                 docker tag dataset zanzadshubham25/dataset:latest
        //                 docker push zanzadshubham25/dataset
        //                 docker tag backend zanzadshubham25/backend:latest
        //                 docker push zanzadshubham25/backend
        //                 docker tag frontend zanzadshubham25/frontend:latest
        //                 docker push zanzadshubham25/frontend
        //                 docker ps
        //                 docker images
        //             '''
        //             }
        //         }
        //     }
        // }

        // stage("Deleted Docker Imgaes") {
        //     steps {
        //         script {
        //             sh '''
        //                 docker rmi -f backend
        //                 docker rmi -f frontend
        //                 docker rmi -f dataset
        //                 docker rmi -f zanzadshubham25/dataset
        //                 docker rmi -f zanzadshubham25/frontend
        //                 docker rmi -f zanzadshubham25/backend
        //             '''
        //         }
        //     }
        // }
        
        stage('Run Ansible Playbook') {
            steps {
                ansiblePlaybook becomeUser: null,
                colorized: true,
                credentialsId: 'localhost',
                disableHostKeyChecking: true,
                installation: 'Ansible',
                inventory: 'inventory',
                playbook: 'deploy.yml',
                sudoUser: null
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
            // sh 'docker logout'
        }
    }
}
