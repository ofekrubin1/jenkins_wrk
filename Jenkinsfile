pipeline {
    agent {  
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged'
            args  '--net="my-network"'
            //network 'my-network'
        }
    }
    tools {
        jfrog 'jfrog-cli-latest'
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                sh 'curl -u admin:password -T a_1.2.0.zip "http://172.19.0.3/artifactory/generic-local/a_1.2.0.zip"'
            }
        }
    }
}
