pipeline {
    agent {
        label 'python-agent'
    }

    stages {

        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

    }
}
