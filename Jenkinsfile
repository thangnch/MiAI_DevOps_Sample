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
                echo 'Build not need.Zip'
                sh 'zip -r main.zip main.py'
            }
        }

        // Stage2 : Testing
        stage ('Test'){
            steps {
                echo 'testing......'

            }
        }

        stage ('Send to Nexus'){
            steps {
                nexusArtifactUploader artifacts: [[artifactId: 'main', classifier: '', 
                file: 'main.zip', type: 'zip']], credentialsId: '948b1271-9a5c-4e21-bc0d-c8b27335d244',
                 groupId: 'FlaskApp', nexusUrl: '192.168.1.95:8081',
                 nexusVersion: 'nexus3', protocol: 'http',
                 repository: 'PythonDeploy', version: "${Version}"

            }
        }

        stage ('Deploy to docker'){
            steps {
                echo ' Deploy......'
                sshPublisher(publishers: [sshPublisherDesc(configName: 'Ansible_ControlNode', 
                transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'ansible-playbook /home/ansibleadmin/deploydocker.yaml -i /etc/ansible/hosts',
                execTimeout: 120000, flatten: false, 
                makeEmptyDirs: false, noDefaultExcludes: false, 
                patternSeparator: '[, ]+', remoteDirectory: '', 
                remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], 
                usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])

            }
        }

       




    }

}