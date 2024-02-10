pipeline {
    agent {  
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged'
            args  '--net="my-network"'
        }
    }
    tools {
        jfrog 'jfrog-cli-latest'
    }
    stages {
        stage ('Testing') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                jf '-v' 
                jf 'c show'
                jf 'rt ping'
                sh 'touch test-file'
                jf 'rt u a_1.2.0.zip generic-local/'
                jf 'rt bp'
                //jf 'rt dl my-repo/test-file'
            }
        }
    }
}

