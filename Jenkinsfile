pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "manaswini6i/cloudml-sentinel"
        DOCKER_TAG   = "v4"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/CodebyManaswini/cloudml-sentinel.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
        
        stage('Deploy to EC2') {
            steps {
                sh '''
                    docker pull ${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker stop cloudml-sentinel || true
                    docker rm cloudml-sentinel || true
                    docker run -d -p 8000:8000 --name cloudml-sentinel ${DOCKER_IMAGE}:${DOCKER_TAG}
                '''
            }
        }
    }
    
    post {
        success {
            echo ' Pipeline completed successfully!'
        }
        failure {
            echo ' Pipeline failed!'
        }
    }
}