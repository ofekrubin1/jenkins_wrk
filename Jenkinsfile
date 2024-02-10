pipeline {
    agent {  
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged --net="my-network"'
            volumes ['/tmp/jfrog/:/tmp/jfrog/']
        }
    }
    stages {
        stage ('Testing') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                sh '/tmp/jfrog/jf -v' 
                sh '/tmp/jfrog/jf c show'
                sh '/tmp/jfrog/jf rt ping'
                sh '/tmp/jfrog/jf rt u a_1.2.0.zip generic-local/'
                sh '/tmp/jfrog/jf rt bp'
                //jf 'rt dl my-repo/test-file'
            }
        }
    }
}
