pipeline {
  agent {
    kubernetes {
      label 'ssn-demo'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  namespace: devops-tools
spec:
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
    - name: m2
      persistentVolumeClaim:
        claimName: m2
"""
}
   }
  stages {
    stage('Build') {
      steps {
        container('docker') {
          sh """
             docker build .
          """
        }
      }
    }
  }
}