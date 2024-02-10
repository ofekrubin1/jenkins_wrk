pipeline {
    agent {  
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged --net="my-network" -v /tmp/jfrog:/tmp/jfrog'
        }
    }
    stages {
        stage ('Testing') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                // sh '/tmp/jfrog/jf -v' 
                // sh '/tmp/jfrog/jf c show'
                // sh '/tmp/jfrog/jf rt ping --url=http://172.19.0.3:8082'
                // sh '/tmp/jfrog/jf rt u a_1.2.0.zip generic-local/'
                sh '/tmp/jfrog/jf rt u a_1.2.0.zip generic-local/box/ --url=http://172.19.0.3:8082'
                // sh '/tmp/jfrog/jf rt bp'
                //jf 'rt dl my-repo/test-file'
            }
        }
    }
}
