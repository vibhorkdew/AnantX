pipeline {

```
agent any

stages {

    stage('Checkout') {
        steps {
            git branch: 'master',
            url: 'https://github.com/vibhorkdew/KavachOps.git'
        }
    }

    stage('SonarQube Analysis') {
        steps {
            withSonarQubeEnv('SonarQube') {
                sh '''
                docker run --rm \
                --network kavachops-net \
                -e SONAR_HOST_URL=$SONAR_HOST_URL \
                -e SONAR_TOKEN=$SONAR_AUTH_TOKEN \
                -v $WORKSPACE:/usr/src \
                sonarsource/sonar-scanner-cli
                '''
            }
        }
    }

    stage('Quality Gate') {
        steps {
            timeout(time: 5, unit: 'MINUTES') {
                waitForQualityGate abortPipeline: true
            }
        }
    }

    stage('Docker Build') {
        steps {
            sh 'docker compose build'
        }
    }

    stage('Trivy Scan') {
        steps {
            sh '''
            trivy image \
            --format json \
            -o trivy-report.json \
            postgres:15
            '''
        }
    }

    stage('Archive Trivy Report') {
        steps {
            archiveArtifacts artifacts: 'trivy-report.json'
        }
    }

}
```

}
