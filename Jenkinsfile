pipeline {
    agent any
    environment {
    image = "taskmanager"
    }

    stages {
        stage('clone') {
            steps {
                echo 'Cloning the Repo'
                git branch: 'main', url: 'https://github.com/VireshDhuri01/Jenkins-Docker-Project.git'
            }
        }
        stage('Image and Container') {
            steps {
                echo 'Building and Running the Image and Containers'
                sh 'docker compose up'
            }
        }
    }
}
