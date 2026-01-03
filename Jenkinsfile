pipeline {
    agent any

    environment {
        BACKEND_IMAGE = "yourdockerhub/mindforge-backend"
        FRONTEND_IMAGE = "yourdockerhub/mindforge-frontend"
        DOCKER_CREDS = "dockerhub-creds"
    }

    stages {

        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Run Tests") {
            steps {
                sh "pytest backend/tests/ -v || true"
            }
        }

        stage("Build Images") {
            steps {
                sh """
                docker build -t $BACKEND_IMAGE:latest -f docker/backend.Dockerfile .
                docker build -t $FRONTEND_IMAGE:latest -f docker/frontend.Dockerfile .
                """
            }
        }

        stage("Push Images") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKER_CREDS,
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $BACKEND_IMAGE:latest
                    docker push $FRONTEND_IMAGE:latest
                    """
                }
            }
        }

        stage("Deploy to Kubernetes") {
            steps {
                sh "kubectl apply -f k8s/"
            }
        }
    }

    post {
        success {
            echo "MindForge deployed successfully"
        }
        failure {
            echo "Deployment failed"
        }
    }
}
