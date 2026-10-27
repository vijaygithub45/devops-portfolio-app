pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate Application') {
            steps {
                sh '''
                    echo "Checking project files..."
                    test -f app.py
                    test -f requirements.txt
                    test -f Dockerfile
                    test -f helm/devops-portfolio-app/Chart.yaml
                    echo "Project structure validation successful"
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Creating Python virtual environment..."
                    python3 -m venv .venv
                    .venv/bin/python --version
                    .venv/bin/pip --version
                    .venv/bin/pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running automated tests..."
                    .venv/bin/pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building application Docker image..."
                    docker build --pull=false -t devops-portfolio-app:1.0 .
                    echo "Verifying built image..."
                    docker image inspect devops-portfolio-app:1.0
                '''
            }
        }

        stage('Show Git Commit') {
            steps {
                sh 'git log -1 --oneline'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }

        failure {
            echo 'CI pipeline failed.'
        }
    }
}
