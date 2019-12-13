pipeline {
agent any

stages {
    stage('envsetup'){
        steps{
            sh '''#!/bin/bash
            which python3
            #python3 -m venv tempenv
            source /home/abhilash/Desktop/Avenger/marvel/bin/activate
            pip3 install -r requirements.txt
            '''
        }
    }
    stage('email-notification'){
        steps{
             emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
             recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
             subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
        }
    }
}

}
