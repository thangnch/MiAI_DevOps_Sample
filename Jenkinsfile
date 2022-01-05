pipeline{
    //Directives
    agent any
    environment{
       ArtifactId = "FlaskApp"
       Version = "2"
       Name = "FlaskApp"
       GroupId = "PythonFlask"
    }
    stages {
        // Specify various stage with in stages

        // stage 1. Build
        stage ('Build'){
            steps {
                echo 'Build not need'
            }
        }

        // Stage2 : Testing
        stage ('Test'){
            steps {
                echo ' testing......'

            }
        }

        stage ('Send to Nexus'){
            steps {
                nexusArtifactUploader artifacts: [[artifactId: 'main', classifier: '', file: 'main', type: 'py']], credentialsId: '948b1271-9a5c-4e21-bc0d-c8b27335d244', groupId: 'FlaskApp', nexusUrl: '192.168.1.144:8081',
                 nexusVersion: 'nexus3', protocol: 'http', repository: 'PythonDeploy', version: "${Version}"

            }
        }

        stage ('Deploy'){
            steps {
                echo ' Dep[loy]......'

            }
        }

       




    }

}