pipeline {
    agent any

    stages {

        stage('Pull Latest Code') {
            steps {
                dir('/var/lib/jenkins/pdf-qa-chatbot') {
                    sh 'git pull origin main'
                }
            }
        }

        stage('Install Dependencies') {
    steps {
        dir('/var/lib/jenkins/pdf-qa-chatbot') {
            sh '''
            ./venv/bin/pip install -r requirements.txt
            '''
        }
    }
}
