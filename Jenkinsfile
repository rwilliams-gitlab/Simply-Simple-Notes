pipeline {
  
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: docker
            image: npalm/dind-java:latest
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
                id: "JFrog SaaS",
                url: "https://gitlabroadshow.jfrog.io/",
            )
            script {
                docker.build('gitlabroadshow.jfrog.io/ssn-docker-local' + '/ssn:latest', './')
            }
            rtDockerPush(
                serverId: "JFrog SaaS",
                image: 'gitlabroadshow.jfrog.io/ssn-docker-local' + '/ssn:latest',
                targetRepo: 'ssn-docker-local',
            )
        }
      }
    }
  }
}