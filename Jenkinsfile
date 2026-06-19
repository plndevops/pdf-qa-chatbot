pipeline {
    agent {
        label 'python-agent'
    }

    stages {

        stage('Environment Info') {
            steps {
                echo "Build Number: ${env.BUILD_NUMBER}"
                echo "Job Name: ${env.JOB_NAME}"
                echo "Node Name: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
            }
        }

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
                 subject: "✅ Build Success - ${env.JOB_NAME}",
                 body: """
Build completed successfully.

Build Number : ${env.BUILD_NUMBER}
Job Name     : ${env.JOB_NAME}
Node Name    : ${env.NODE_NAME}
Workspace    : ${env.WORKSPACE}
"""
        }

        failure {
            mail to: 'testing0003099@gmail.com',
                 subject: "❌ Build Failed - ${env.JOB_NAME}",
                 body: """
Build failed.

Build Number : ${env.BUILD_NUMBER}

Please check Jenkins console logs.
"""
        }
    }
}
