pipeline {
    agent any

    environment {
        UPLOADS_DIR = 'uploads'
        REPORTS_DIR = 'reports'
        EMAIL_RECIPIENT = 'ananya.aithal@healthedge.com'
    }

    stages {

        /* 2️⃣ Clone source repo with credentials */
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                git credentialsId: 'github-creds', url: 'https://github.com/your-username/streamlit-analyzer.git'
            }
        }

        /* 3️⃣ Build the Docker image for the app */
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t streamlit-analyzer .'
            }
        }

        /* 4️⃣ Run CSV Clean + Report Generation in Docker container */
        stage('Run Clean + Report Inside Docker') {
            steps {
                script {
                    echo 'Preparing folders...'
                    sh """
                        mkdir -p ${UPLOADS_DIR} ${REPORTS_DIR}
                        echo "name,age
Alice,25
Bob,30" > ${UPLOADS_DIR}/sample.csv
                    """

                    echo 'Running clean_csv.sh inside Docker...'
                    sh """
                        docker run --rm \
                          -v $PWD/${UPLOADS_DIR}:/app/uploads \
                          -v $PWD/${REPORTS_DIR}:/app/reports \
                          streamlit-analyzer bash scripts/clean_csv.sh uploads/sample.csv
                    """

                    echo 'Running generate_report.sh inside Docker...'
                    sh """
                        docker run --rm \
                          -v $PWD/${UPLOADS_DIR}:/app/uploads \
                          -v $PWD/${REPORTS_DIR}:/app/reports \
                          streamlit-analyzer bash scripts/generate_report.sh uploads/sample.csv
                    """
                }
            }
        }

        /* 5️⃣ Archive all generated reports, regardless of name */
        stage('Archive Reports') {
            steps {
                echo 'Archiving all reports...'
                archiveArtifacts artifacts: "${REPORTS_DIR}/*", fingerprint: true
            }
        }

        /* 6️⃣ Send notification email with artifact link */
        stage('Send Email') {
            steps {
                script {
                    def reportLink = "${env.BUILD_URL}artifact/${REPORTS_DIR}/"
                    mail to: "${env.EMAIL_RECIPIENT}",
                         subject: "✅ Jenkins Build Complete - CSV Report Available",
                         body: """Hi,

Your Jenkins job completed successfully.

You can download the generated report here:
${reportLink}

– Jenkins"""
                }
            }
        }
    }

    /* 7️⃣ Post actions regardless of success/failure */
    post {
        always {
            echo 'Build completed.'
            cleanWs()
        }
    }
}
