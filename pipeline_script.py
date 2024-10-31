pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[credentialsId: 'b168e6c2-81aa-4f70-917b-3b21c7aa2688', url: 'https://github.com/Saunakm1270/DevopsAI.git']])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'b168e6c2-81aa-4f70-917b-3b21c7aa2688', url: 'https://github.com/Saunakm1270/DevopsAI.git'
                bat 'python sort.py'
                
            }
        }
        stage('Test') {
            steps {
                echo "Testing is done"
            }
        }
    }
}
