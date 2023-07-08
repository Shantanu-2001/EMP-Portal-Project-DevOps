def img
def username = "shantanu2001"
def password = "shantanu@rana"

pipeline {
    environment {
        scannerHome = tool 'sonar'
    } 
    agent any

    parameters {
        choice(
            choices: ['Dev', 'Prod'],
            description: 'Select the target cluster',
            name: 'TARGET CLUSTER'
        )
    }

    stages {
        stage('Checkout project') {
            steps {
                script {
                    // Checkout the project from GitHub
                    git branch: 'Dev',
                    credentialsId: 'none',
                    url: 'https://github.com/Shantanu-2001/EMP-Portal-Project-DevOps.git'
                }
            }
        }

        stage('Installing packages') {
            steps {
                script {
                    // Install required python packages
                    sh 'pip install -r requirements.txt'
                }
            }
        }

      /*  stage('Static Code Checking') {
            steps {
                script {
                    // Run pylint on Python files and generate a report
                    sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
                    recordIssues(
                        tools: [pyLint(pattern: 'pylint.log')],
                        unstableTotalAll: 100
                    )
                }
            }
        }   */

    
        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('sonarqube_portal') {
                        // Run SonarQube scanner for code analysis
                        sh '''${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=DevOps-project-new \
                            -Dsonar.sources=. '''
                    }
                }
            }
        }
        

        stage('Testing with pytest') {
            steps {
                sh 'python3 -m pytest'
                sh 'python3 test_app.py'
            }
        }

        stage('Clean Up') {
            steps {
                sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force'
                sh returnStatus: true, script: 'docker rmi -f ${JOB_NAME}'
            }
        } 

        stage('Build image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Push To Dockerhub') {
            steps {
                sh "docker tag flask-app shantanu2001/new_flask_app:latest"
                sh "docker login -u ${username} -p ${password}"
                sh "docker push shantanu2001/new_flask_app"
            }
        }

        stage('Deploy to containers') {
            steps {
                sh "docker login -u ${username} -p ${password}"
                sh "docker run -it -p 5000:5000 -d flask-app"
            }
        }
    }
}
