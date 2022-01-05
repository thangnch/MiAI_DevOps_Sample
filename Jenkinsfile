pipeline{
    //Directives
    agent any
    environment{
       ArtifactId = "FlaskApp"
       Version = "1"
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
                nexusArtifactUploader artifacts: [[artifactId: 'FlaskApp', classifier: '', file: 'target/FlaskApp-1.py', type: 'py']], credentialsId: 'f42494d3-c5c8-4e49-a4d9-078f728e4155', groupId: 'PythonFlask', nexusUrl: 'http://192.168.1.144:8081', nexusVersion: 'nexus3', protocol: 'http', repository: 'FlaskApp', version: '1'

            }
        }

        stage ('Deploy'){
            steps {
                echo ' Dep[loy]......'

            }
        }

       




    }

}