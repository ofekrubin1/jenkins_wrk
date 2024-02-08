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
            }
        }
    }
}
