pipeline {
    agent {
        label 'python-agent'
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
    }
}
