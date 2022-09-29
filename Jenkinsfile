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
  
  stages {
    stage('Build-Docker-Image') {
      steps {
        container('docker') {
            rtServer (
                id: "ARTIFACTORY_SERVER",
                url: "https://gitlabroadshow.jfrog.io/",
                credentialsId: "jfrog-secret"
            )
            script {
                docker.build('ssn-docker' + '/ssn:latest', './')
            }
            rtDockerPush(
                serverId: "ARTIFACTORY_SERVER",
                image: 'ssn-docker' + '/ssn:latest',
                targetRepo: 'ssn-docker',
            )
        }
      }
    }
  }
}