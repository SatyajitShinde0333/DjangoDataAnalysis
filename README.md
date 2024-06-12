# DjangoDataAnalysis


This project is a Django-based web application for uploading CSV files and performing data analysis, including generating histograms. The application is styled to provide an attractive user interface and clear visualization of data.

**1 Features**

- Upload CSV files
- Generate histograms and pie charts
- Display missing values in the dataset
- Attractive and responsive UI

**2 Prerequisites**

Before you begin, ensure you have met the following requirements:
- Python 3.8 or later
- Django 3.2 or later
- pip (Python package installer)

**3 Installation**

To get started with the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SatyajitShinde0333/DjangoDataAnalysis
   ```

2. **Navigate to the project directory:**
   ```bash
   cd data_analysis_project
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply the migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000/
   ```
**4 Project Structure**

```plaintext
data_analysis_project/
│
├── analysis/
│   ├── migrations/
│   ├── templates/
│   │   └── analysis/
│   │       ├── upload.html
│   │       ├── success.html
│   │       └── result.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── data_analysis_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
│   └── csv_files/
│       └── (uploaded CSV files)
│
├── manage.py
└── requirements.txt

```


**5 Usage**

1. Navigate to the home page and upload a CSV file.
2. After uploading, you will be redirected to a success page.
3. Click on the link to view the analysis results, which include histograms.

**6 CSV Files**

- Uploaded CSV files are stored in the `media/csv_files/` directory.
- Ensure the `media` directory exists and is writable by the web server.

 Sample CSV File: Crop Production

A sample CSV file `crop_production.csv` is included in the `media/csv_files/` directory. This file contains data on crop production, with columns such as `Year`, `State`, `Crop`, `Area`, and `Production`. 

**7 Customization**
Views
The main logic for generating the histograms and pie charts is in analysis/views.py. You can customize the charts by modifying the Seaborn and Matplotlib settings.

Templates
The HTML templates are located in analysis/templates/analysis/. You can customize the appearance by editing these templates and the associated HTML file in analysis/templates/analysis/result.html.

**8 Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature).
4. Push to the branch (git push origin feature-branch).
5. Create a pull request.

**9 Acknowledgements**

- [Django](https://www.djangoproject.com/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Poppins Font](https://fonts.google.com/specimen/Poppins)


**10 Explanation**

- Project Features: A brief overview of what the project does.
- Prerequisites: Requirements for running the project.
- Installation: Step-by-step instructions to set up the project.
- Running the Server: Instructions to start the development server.
- Project Structure: An overview of the project's directory structure.
- Usage: How to use the application.
- Customization: Guidance on how to customize the views and templates.
- Contributing: Instructions for contributing to the project.
- License: Information about the project's license.
- Acknowledgements: Recognition of the tools and resources used in the project.



