podTemplate(
    inheritFrom: "maven",
    label: "myJenkins",
    cloud: "openshift",
    volumes: [
        persistentVolumeClaim(claimName: "m2repo", mountPath: "/home/jenkins/.m2/")
    ]) {

    node("myJenkins") {

        @Library('github.com/mikeintoch/jenkins-library@master') _

        stage ('SCM checkout'){
            echo 'Checking out git repository'
            checkout scm
        }

        stage ('DEV - Image build'){
            echo 'Building docker image and deploying to Dev'
            buildApp('atmmovil-dev', "atmmovil", '8001')
            echo "This is the build number: ${env.BUILD_NUMBER}"
        }

        stage ('QA - Promote image'){
            echo 'Deploying to QA'
            promoteImage('atmmovil-dev', 'atmmovil-qa', 'atmmovil', '8001','latest')
        }

        stage ('Wait for approval'){
            input 'Approve to production?'
        }

        stage ('PRD - Promote image'){
            echo 'Deploying to production'
            promoteImage('atmmovil-qa', 'atmmovil', 'atmmovil', '8001' ,env.BUILD_NUMBER)
        }

        stage ('PRD - Canary Deploy'){
            echo 'Performing a canary deployment'
            canaryDeploy('atmmovil', 'atmmovil', env.BUILD_NUMBER)
        }

    }
}
