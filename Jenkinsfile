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
            image: codefresh/kubectl
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
    stage('Build and Publish') {
        steps {
            container('docker') {
                rtServer (
                    id: "Roadshow Artifactory",
                    url: "https://gitlabroadshow.jfrog.io/",
                )
                script {
                    docker.build('gitlabroadshow.jfrog.io/ssn-docker-local' + '/ssn:latest', './')
                }
                rtDockerPush(
                    serverId: "Roadshow Artifactory",
                    image: 'gitlabroadshow.jfrog.io/ssn-docker-local' + '/ssn:latest',
                    targetRepo: 'ssn-docker-local',
                )
            }
        }
    }
    stage('Deploy to k8s') {
        steps {
            container('kctl') {
                sh 'kubectl apply -f Manifests/deployment.yaml'
                sh 'kubectl -n devops-tools rollout restart deployments/ssn-app'
                sh "kubectl get services --namespace devops-tools ssn-service --output jsonpath='{.status.loadBalancer.ingress[0].ip}'"
            }
        }
    }
  }
}