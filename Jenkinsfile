pipeline {
    agent {
        docker { image 'zip_job_image:latest'}
	}
    stages {
        stage('Build') {
            steps {
                sh 'python3 /tmp/zip_job.py'
            }
        }
    }
}
