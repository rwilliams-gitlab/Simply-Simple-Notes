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
    stage ('Artifactory configuration') {
        steps {
            rtServer (
                id: "ARTIFACTORY_SERVER",
                url: "https://gitlabroadshow.jfrog.io/",
                credentialsId: "jfrog-secret"
            )
        }
    }

    stage ('Build docker image') {
        steps {
            script {
                docker.build('ssn-docker' + '/ssn:latest', './')
            }
        }
    }

    stage ('Push image to Artifactory') {
        steps {
            rtDockerPush(
                serverId: "ARTIFACTORY_SERVER",
                image: 'ssn-docker' + '/ssn:latest',
                // Host:
                // On OSX: "tcp://127.0.0.1:1234"
                // On Linux can be omitted or null
                host: HOST_NAME,
                targetRepo: 'docker-local',
                // Attach custom properties to the published artifacts:
                properties: 'project-name=docker1;status=stable'
            )
        }
    }
  }
}