podTemplate(label: 'ssn-node', cloud: 'kubernetes', serviceAccount: 'jenkins-admin',
  containers: [
    containerTemplate(name: 'docker', image: 'moby/buildkit:master', ttyEnabled: true, command: 'cat', privileged: true,
        envVars: [secretEnvVar(key: 'DOCKER_USERNAME', secretName: 'docker-hub-credentials', secretKey: 'username'),
    ]),
    containerTemplate(name: 'kubectl', image: 'roffe/kubectl', ttyEnabled: true, command: 'cat'),
  ]) {
    node('ssn-node') {
        stage('Prepare') {
            checkout scm
        }

        stage('Build Docker Image') {
            container('docker') {
                sh """
                  docker build .
                """
            }
        }
    }
}
