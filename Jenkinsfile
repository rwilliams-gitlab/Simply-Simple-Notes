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
          - name: kctl
            image: bitnami/kubectl
            command:
            - cat
            tty: true
          volumes:
          - name: docker-sock
            hostPath:
              path: /var/run/docker.sock
        '''
    }
  }

  stages {
    container('docker') {
        stage('Build-Docker-Image') {
            steps {
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
    container('kctl') {
        stage('Deploy to k8s') {
            steps {
                sh 'kubectl apply -f Manifests/deployment.yaml'
                sh 'kubectl version'
                sh 'kubectl -n devops-tools rollout restart deployments/ssn-app'
            }
        }
    }
  }
}