pipeline {
    agent {
        docker {
            image 'zip_job_image:latest'
            args '-u root:root --privileged'
            label 'zip-job-docker'
            reuseNode true
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 /tmp/zip_job.py'
            }
        }
    }
}

