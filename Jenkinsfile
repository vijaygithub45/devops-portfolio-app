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
