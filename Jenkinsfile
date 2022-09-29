pipeline {
  
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: docker
            image: docker:latest
            command:
            - cat
            tty: true
            volumeMounts:
             - mountPath: /var/run/docker.sock
               name: docker-sock
          volumes:
          - name: docker-sock
            hostPath:
              path: /var/run/docker.sock
        '''
    }
  }
  
  environment {
    registry = "gitlabroadshow.jfrog.io/ssn-docker-local"
    registryCredential = 'jfrog-secret'
    dockerImage = ''
  }

  stages {
    stage('Build-Docker-Image') {
      steps {
        container('docker') {
          script {
            script {
                def customImage = docker.build("my-image:${env.BUILD_ID}")
                customImage.push()
            }
          }
        }
      }
    }
  }
}