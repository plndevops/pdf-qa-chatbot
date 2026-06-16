pipeline {
    agent {
        label 'python-agent'
    }

    stages {

        stage('Build') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

    }
}
