pipeline {
    agent {  
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged --net="my-network" -v /tmp/jfrog:/tmp/jfrog'
        }
    }
    envinronment{
        CI=true
        ACCESS_TOKEN=cradentials('artifactory_secret_token')
    }
    stages {
        stage ('Testing') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                sh "/tmp/jfrog/jf rt u a_1.2.0.zip generic-local/ --url=http://172.19.0.3:8082/artifactory --apikey=${apiKey}"
                            
          }
        }
    }
}
