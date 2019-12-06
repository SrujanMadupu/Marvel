pipeline {
agent any

stages {
    stage('envsetup'){
        steps{
            sh '''#!/bin/bash
            which python3
            python3 -m venv tempenv
            source /home/abhilash/Desktop/Avenger/tempenv/bin/activate
            pip3 install -r requirements.txt
            '''
        }
    }
    stage('runapp'){
        steps{
            sh '''
            python3 manage.py runserver 
            '''
        }
    }
}

}
