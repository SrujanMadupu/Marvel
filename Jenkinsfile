pipeline {
agent any

stages {
    stage('envsetup'){
        steps{
            sh '''#!/bin/bash
            which python
            python -m venv tempenv
            source tempenv/bin/activate
            pip3 install -r requirements.txt
            '''
        }
    }
    stage('runapp'){
        steps{
            sh '''
            python manage.py runserver 
            '''
        }
    }
}

}
