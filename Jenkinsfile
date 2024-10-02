pipeline {
    agent any
    stages {
        stage('Build Repo') {
            steps {
                //sh "git clone https://github.com/KennyIT3/Python_Scipts-Automating-Sysadmin.git"
                sh "mvn clean"
            }
        }
        stage('Testing Repo') {
            steps {
                echo "Testing Code"
                echo 'Testing Code'
                sh 'date'
            }
        }
        stage('Deploy Repo') {
            steps {
                echo "Done"
            }
        }
    }
}
