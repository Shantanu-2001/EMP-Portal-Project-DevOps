pipeline

{

    environment

    {

        registry = "shantanurana/emp-portal-project"

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

                    git branch: 'dev',

                    credentialsId: githubCredential,

                    url: 'insert url here.git'

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


