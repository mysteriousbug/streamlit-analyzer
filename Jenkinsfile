pipeline {
    agent any
    environment {
        REPORT_PATH = 'uploads/sample.csv'
        EMAIL_RECIPIENT = 'ananya.aithal@healthedge.com'
    }
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/mysteriousbug/streamlit-analyzer.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t streamlit-analyzer .'
            }
        }

        stage('Run Clean + Report Inside Docker') {
            steps {
                sh '''
                echo "name,age\nAlice,25\nBob,30" > uploads/movies.csv
                docker run --rm -v $PWD/uploads:/app/uploads -v $PWD/reports:/app/reports streamlit-analyzer bash scripts/clean_csv.sh $REPORT_PATH
                docker run --rm -v $PWD/uploads:/app/uploads -v $PWD/reports:/app/reports streamlit-analyzer bash scripts/generate_report.sh $REPORT_PATH
                '''
            }
        }

        stage('Send Email') {
            steps {
                script {
                    def latestReport = sh(script: "ls -t reports/*.txt | head -n1", returnStdout: true).trim()
                    mail to: "${env.EMAIL_RECIPIENT}",
                         subject: "CSV Report from Jenkins",
                         body: "Hi,\n\nHere is your latest CSV report.\n\n– Jenkins",
                         attachLog: false,
                         attachmentsPattern: latestReport
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.txt', fingerprint: true
        }
    }
}
