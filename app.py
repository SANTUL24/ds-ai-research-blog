from flask import Flask, render_template

app = Flask(__name__)
projects = [
    {
    "slug": "credit-risk-pd-modelling",
    "title": "Credit Risk & PD Modelling",
    "category": "MACHINE LEARNING",
    "description": "Predictive modelling for probability of default and credit risk assessment.",
    "tools": "Python · XGBoost · Pandas · Scikit-learn",
    "problem": "Build a machine learning model to identify customers with higher probability of default.",
    "data": "Customer-level credit bureau and behavioural information used for risk modelling.",

    "features": [
        "Credit bureau score",
        "Current outstanding balance",
        "Total indebtedness",
        "Number of active loans",
        "Loan default rate",
        "Recent enquiries",
        "Delinquency history",
        "Customer vintage"
    ],

    "target_definition": "Ever Max DPD > 60",

    "eda": [
        "Examine target distribution and default rate",
        "Analyse missing values and data quality",
        "Study relationships between risk variables and the target",
        "Identify outliers and unusual observations",
        "Compare risk behaviour across customer segments"
    ],
    "methodology": "Data preparation → EDA → feature engineering → model development → validation → risk segmentation.",
    "result": "A structured credit-risk modelling framework with model evaluation and risk-based decisioning.",

    "metrics": [
                    {
                        "name": "AUC",
                        "value": "0.68"
                    },
                    {
                        "name": "KS",
                        "value": "0.27"
                    },
                    {
                        "name": "Model",
                        "value": "XGBoost"
                    },
                    {
                        "name": "Target",
                        "value": "Ever Max DPD > 60"
                    }
               ]
    },
    {
        "slug": "customer-risk-segmentation",
        "title": "Customer Risk Segmentation",
        "category": "DATA SCIENCE",
        "description": "Customer segmentation and behavioural risk analysis using machine learning.",
        "tools": "Python · Pandas · Scikit-learn",
        "problem": "Identify meaningful customer segments based on behavioural and risk characteristics.",
        "methodology": "Data preparation → feature selection → clustering → segment profiling → interpretation.",
        "result": "Customer groups differentiated by behavioural and risk characteristics."
    },
    {
        "slug": "ai-research",
        "title": "AI Research Projects",
        "category": "ARTIFICIAL INTELLIGENCE",
        "description": "Experiments with modern AI, deep learning and intelligent applications.",
        "tools": "Python · PyTorch · Transformers",
        "problem": "Explore practical applications of modern artificial intelligence techniques.",
        "methodology": "Research → experimentation → model development → evaluation → application.",
        "result": "A collection of experiments exploring modern AI systems."
    }
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/blog")
def blog():

    posts = [
        {
            "title": "What is a PD Model?",
            "category": "Machine Learning",
            "description": "Understanding probability of default models and their role in credit risk."
        },
        {
            "title": "Introduction to XGBoost",
            "category": "Machine Learning",
            "description": "Understanding gradient boosting and why XGBoost is powerful for predictive modelling."
        },
        {
            "title": "From Machine Learning to AI",
            "category": "Artificial Intelligence",
            "description": "Exploring the evolution from traditional machine learning to modern AI systems."
        }
    ]

    return render_template("blog.html", posts=posts)

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/projects/<slug>")
def project_detail(slug):

    project = next(
        (p for p in projects if p["slug"] == slug),
        None
    )

    if project is None:
        return "Project not found", 404

    return render_template(
        "project_detail.html",
        project=project
    )
    
if __name__ == "__main__":
    app.run(debug=True)