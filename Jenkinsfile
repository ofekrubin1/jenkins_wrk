pipeline {
    agent {  
        docker { 
            image 'zip_job_image:latest'
            label 'zip-job-docker'
            reuseNode true
            args '-u root:root --privileged --net="my-network" -v /tmp/jfrog:/tmp/jfrog'
        }
    }
  environment {
        ARTIFACTORY_URL = 'http://172.19.0.3:8082/artifactory/generic-local'
        API_KEY = 'eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJ0Tkhwc1oyc3pIUmxyN0RMTVJSSGpxNFpvdDJXWEFpS3FBYVhLTlRzTzNBIn0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxaHA5OXJxZTAwbnM5MG02MHcxbXIwYWo0XC91c2Vyc1wvYWRtaW4iLCJzY3AiOiJhcHBsaWVkLXBlcm1pc3Npb25zXC9hZG1pbiIsImF1ZCI6IipAKiIsImlzcyI6ImpmZmVAMDAwIiwiaWF0IjoxNzA3NTc4Nzk5LCJqdGkiOiI3ZDgzMmIzNC04YTg1LTQxMzAtOGI1Zi0wNzE3YmViNzJhYzIifQ.bzVhbWhXoButZtm-o4tm67-KKJx5tmabLFk05nqX_axkg9vTspGL5DvdY0F70glc04HzzlGbZUFIyz18hvZi-NXlaskBYmQMyoAeGFjYQa5HRJa7hXa2VD6iiuve7peSqB-t3INYqwnfpHjgSCJtylunGpNHTR-p4g0s4EBtXKSVNLOra3qwfGFIHYV01J4PLY2qv7cBurcYHYZ1SaWss780cMcMlyXPK2JTvq6Ze6cz1_hDLfQTK_-F9r-EnQdsIm1j2cUzvhu1pJpZhR_3FtvR285QkfL8EMO_-66d6P8RvOoPd-kPbN9WtRpleuz1BSr0Zc22xDHALIFvLF4WEA'
    }
    stages {
        stage ('Testing') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                sh "/tmp/jfrog/jf rt u a_1.2.0.zip ${env.ARTIFACTORY_URL} --apikey=${env.API_KEY}"
            }
        }
    }
}
