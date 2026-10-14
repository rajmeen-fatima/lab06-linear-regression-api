
pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        set +x
                        echo "$DOCKER_PASS" | docker login \
                            -u "$DOCKER_USER" --password-stdin
                        docker push rajmeenfatima/linear-regression-api:latest
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy API') {
            steps {
                sh '''
                    docker-compose down
                    docker-compose up -d
                '''
            }
        }
    }
}

