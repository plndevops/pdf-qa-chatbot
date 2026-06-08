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
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Restart Service') {
            steps {
                sh '''
                sudo systemctl restart pdfchatbot
                '''
            }
        }
    }
}
