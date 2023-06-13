pipeline

{

    environment

    {

        registry = "Shantanu-2001/EMP-Portal-Project-DevOps"

        registryCredential = 'DOCKERHUB'

        githubCredential = 'Github-Creds'

        dockerImage = ' '

    }   scannerHome = tool 'sonar4.8'




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

    }

}


