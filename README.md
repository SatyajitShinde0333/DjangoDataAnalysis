# DjangoDataAnalysis


This project is a Django-based web application for uploading CSV files and performing data analysis, including generating histograms and pie charts. The application is styled to provide an attractive user interface and clear visualization of data.

## Features

- Upload CSV files
- Generate histograms and pie charts
- Display missing values in the dataset
- Attractive and responsive UI

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or later
- Django 3.2 or later
- pip (Python package installer)

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/yourusername/data_analysis_project.git
   cd data_analysis_project
  

2. Create a virtual environment:
   bash
   python -m venv .venv
  

3. Activate the virtual environment:
   - On Windows:
     bash
     .venv\Scripts\activate
    
   - On macOS/Linux:
     bash
     source .venv/bin/activate
     

4. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

5. Apply the migrations:
   bash
   python manage.py migrate
   

## Running the Server

1. Start the Django development server:
   bash
   python manage.py runserver
   

2. Open your web browser and navigate to `http://127.0.0.1:8000` to access the application.

## Project Structure

# Data Analysis Project

This project is a Django-based web application for uploading data files, performing data analysis, and visualizing the results through histograms and pie charts.

## Project Structure

```plaintext
data_analysis_project/
│
├── analysis/
│   ├── migrations/
│   ├── templates/
│   │   └── analysis/
│   │       ├── index.html
│   │       ├── success.html
│   │       └── plot.html
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
├── manage.py
└── requirements.txt



## Usage

1. Navigate to the home page and upload a CSV file.
2. After uploading, you will be redirected to a success page.
3. Click on the link to view the analysis results, which include histograms and a pie chart.

## Customization

### Views

The main logic for generating the histograms and pie charts is in `analysis/views.py`. You can customize the charts by modifying the Seaborn and Matplotlib settings.

### Templates

The HTML templates are located in `analysis/templates/analysis/`. You can customize the appearance by editing these templates and the associated CSS file in `analysis/static/analysis/styles.css`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Poppins Font](https://fonts.google.com/specimen/Poppins)
```

### Explanation

- **Project Features:** A brief overview of what the project does.
- **Prerequisites:** Requirements for running the project.
- **Installation:** Step-by-step instructions to set up the project.
- **Running the Server:** Instructions to start the development server.
- **Project Structure:** An overview of the project's directory structure.
- **Usage:** How to use the application.
- **Customization:** Guidance on how to customize the views and templates.
- **Contributing:** Instructions for contributing to the project.
- **License:** Information about the project's license.
- **Acknowledgements:** Recognition of the tools and resources used in the project.

Make sure to replace `yourusername` with your actual GitHub username in the clone URL. This README should give anyone looking at your project a clear understanding of how to set it up, run it, and contribute to it.

