pipeline {
    agent {
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged'
            //network 'my-network'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh "docker network connect my-network ${env.BUILD_TAG}"
                sh 'python3 /tmp/zip_job.py'
                sh 'curl -u admin:password -T a_1.2.0.zip "http://172.19.0.3/artifactory/generic-local/a_1.2.0.zip"'
            }
        }
    }
}
