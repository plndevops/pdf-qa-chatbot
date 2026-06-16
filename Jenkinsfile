pipeline {
    agent {
        label 'python-agent'
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/plndevops/pdf-qa-chatbot.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                python -m py_compile app.py
                '''
            }
        }

    }
}
