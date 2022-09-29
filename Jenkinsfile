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
    registry = "https://gitlabroadshow.jfrog.io/"
    registryCredential = 'jfrog-secret'
    dockerImage = ''
  }

  stages {
    stage('Build-Docker-Image') {
      steps {
        container('docker') {
          script {
            docker.build('ssn-docker', './')
            artServer = Artifactory.newServer(url: registry, credentialsId: registryCredential)
            artDocker = Artifactory.docker(server: artServer)
            artDocker.push('https://gitlabroadshow.jfrog.io/latest', 'ssn-docker')
          }
        }
      }
    }
  }
}