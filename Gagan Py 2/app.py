from flask import Flask, render_template

app = Flask(__name__)

# Portfolio data
portfolio_data = {
    'name': 'Gagan Goyal',
    'title': 'Data Engineer',
    'description': 'Experienced, self-motivated, result-oriented, problem-solving Data Engineer with expertise in modern technologies.',
    'location': 'Noida, Uttar Pradesh',
    'phone': '+91 8561920884',
    'email': 'gagangoyal.cs@gmail.com',
    'linkedin': 'https://linkedin.com/in/gagan-goyal',
    'about': 'I am an experienced Data Engineer with 5.10 years of expertise in modern technologies like PySpark, ADF, Databricks, Delta Lake, Cosmos DB, Hadoop, SQL, and Python. I hold a B1/B2 USA VISA valid till 2028.',
    'skills': {
        'Microsoft Cloud Services': [
            'Azure Databricks',
            'Azure Data Factory',
            'Azure SQL Database',
            'Azure Storage Explorer',
            'Azure Data Lake Storage',
            'Azure Blob Storage',
            'Cosmos DB',
            'Azure DevOps'
        ],
        'Programming & Databases': [
            'PySpark',
            'Python',
            'MS SQL Server',
            'Cosmos DB',
            'SQL'
        ],
        'Tools & Frameworks': [
            'ADF',
            'Procfwk',
            'Git'
        ]
    },
    'experience': [
        {
            'company': 'WNS',
            'project': 'Global Canvas MDR Build',
            'period': 'Jan 2024 - Sept 2024',
            'responsibilities': [
                'Migrated datasets from Dataroma to Azure Databricks',
                'Analyzed 22+ datasets and created gold tables',
                'Developed workflow jobs and monitoring systems',
                'Built Power BI reports and validation systems'
            ]
        },
        {
            'company': 'WNS',
            'project': 'Abacus Migration',
            'period': 'Jun 2023 - Dec 2023',
            'responsibilities': [
                'Migrated IBM Abacus SQL scripts to Databricks',
                'Created workflow jobs and monitoring systems',
                'Updated Power BI reports and connections',
                'Developed data transfer solutions'
            ]
        }
    ],
    'education': {
        'degree': 'B.Tech (Computer Science)',
        'institution': 'JECRC Foundation, Jaipur',
        'year': 'May 2019'
    }
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True) 