pipeline {
    agent {
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                sh 'curl -u admin:password -T a_1.2.0.zip "https://172.18.0.2/artifactory/generic-local/a_1.2.0.zip"'
            }
        }
    }
}
