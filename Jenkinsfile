pipeline {
    agent any 
    stages {
        stage('Build Repo') { 
            steps {
                sh "git clone https://github.com/KennyIT3/Python_Scipts-Automating-Sysadmin.git " 
            }
        }
        stage('Testing Repo') { 
            steps {
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
