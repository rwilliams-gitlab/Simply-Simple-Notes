pipeline {
  
  agent {
    kubernetes {
        yaml """
            apiVersion: v1
            kind: Pod
            spec:
                containers:
                - name: jnlp
                    image: jnlp-slave:latest
                    volumeMounts:
                    - name: docker
                        mountPath: /var/run/docker.sock
                volumes:
                - name: docker
                    hostPath: { path: /var/run/docker.sock }
        """
    //   yaml '''
    //     apiVersion: v1
    //     kind: Pod
    //     spec:
    //       containers:
    //       - name: docker
    //         image: docker:latest
    //         command:
    //         - cat
    //         tty: true
    //         volumeMounts:
    //          - mountPath: /var/run/docker.sock
    //            name: docker-sock
    //       volumes:
    //       - name: docker-sock
    //         hostPath:
    //           path: /var/run/docker.sock
    //     '''
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
                docker.build('ssn-docker-local' + '/ssn:latest', './')
            }
            rtDockerPush(
                serverId: "ARTIFACTORY_SERVER",
                image: 'ssn-docker-local' + '/ssn:latest',
                targetRepo: 'ssn-docker-local',
            )
        }
      }
    }
  }
}