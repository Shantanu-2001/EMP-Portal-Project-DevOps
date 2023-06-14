def img

pipeline
{

    environment
    {

        registry = "Shantanu-2001/EMP-Portal-Project-DevOps"

        registryCredential = 'DOCKERHUB'

        githubCredential = 'none'

        dockerImage = ' '

        scannerHome = tool 'sonar 2.15'
    }

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

                    credentialsId: githubCredential,

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

		stage('Static Code Checking')
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
						sh '''${scannerHome}/bin/sonar-scanner \
					        -Dsonar.projectKey=DevOps-project \
							-Dsonar.sources=. '''
					}
				}
			}
		}
	}
}


