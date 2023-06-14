def img

pipeline
{

   /* environment
    {

        registry = "Shantanu-2001/EMP-Portal-Project-DevOps"

        registryCredential = 'DOCKERHUB'

        githubCredential = 'none'

        dockerImage = ' '

        scannerHome = tool 'sonar 2.15'
    }*/

    agent any

    parameters
    {

        choice(

            choices: ['Dev', 'Prod'],

            description: 'Select the target cluster',

            name: 'TARGET CLUSTER'

        )

    }


    stages
    {

        stage('Checkout project')

        {

            steps

            {

                script

                {

                    //Checkout the project from GitHub

                    git branch: 'Dev',

                    credentialsId: 'none',

                    url: 'https://github.com/Shantanu-2001/EMP-Portal-Project-DevOps.git'

                }

            }

        }

        stage('Installing packages')

        {

            steps

            {

                script

                {

                    //Install required python packages

                    sh 'pip install -r requirements.txt'

                }

            }

        }

		/*stage('Static Code Checking')
		{
			steps
			{
				script
				{
					//Run pylint on Python files and generate a report
					sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
					recordIssues(
						tool: pyLint(pattern: 'pylint.log'),
						unstableTotalHigh: 100
					)
				}
			}
		}*/
	    stage('Static Code Checking') {
            steps {
                script {
                    sh 'find . -name \\*.py | xargs pylint --load-plugins=pylint_django -f parseable | tee pylint.log'
                    recordIssues(
                        tool: pyLint(pattern: 'pylint.log'),
                        failTotalHigh: 10,
                    )
                }
            }
        }

		stage('SonarQube Analysis')
		{
			steps
			{
				script
				{
					withSonarQubeEnv('sonar')
					{
						// Run SonarQube scanner for code Analysis
						sh '''${sonar 2.15}/bin/sonar-scanner \
					        -Dsonar.projectKey=DevOps-project \
							-Dsonar.sources=. '''
					}
				}
			}
		}
	}
}
stage("Testing with pytest"){
                     steps{
                        script{
                          withPythonEnv('python3'){
                             sh 'pip install pytest'
                             sh 'pip install flask_sqlalchemy'
                             sh 'pytest test_app.py'
                           }
                     }     
                  }   
          }

            stage('Clean Up'){
                steps {
                  sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${JOB_NAME} | awk \'{print $1}\')'
                  sh returnStatus: true, script: 'docker rmi $(docker images | grep ${registry} | awk \'{print $3}\') --force'
                  sh returnStatus: true, script: 'docker rmi -f ${JOB_NAME}'
                 }
            }
          stage('Build image'){
                steps {
                   script{
                       img = registry + ":${env.BUILD_ID}"
                       println("${img}")
                       dockerImage = docker.build("${img}")
                      }
                  }
                }













