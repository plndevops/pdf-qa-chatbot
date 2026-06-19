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

    post {
        success {
            mail to: 'testing0003099@gmail.com',
                 subject: "Build Success - ${env.JOB_NAME}",
                 body: """
Build #${env.BUILD_NUMBER} completed successfully.

Job Name: ${env.JOB_NAME}
Node: ${env.NODE_NAME}
Workspace: ${env.WORKSPACE}
"""
        }

        failure {
            mail to: 'testing0003099@gmail.com',
                 subject: "Build Failed - ${env.JOB_NAME}",
                 body: """
Build #${env.BUILD_NUMBER} failed.

Please check Jenkins console logs.
"""
        }
    }
}
