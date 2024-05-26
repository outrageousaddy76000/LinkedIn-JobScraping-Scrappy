# LinkedIn-JobScraping-Scrappy-

## Overview
This LinkedIn Job Scraper is a tool to fetch job listings from LinkedIn based on multiple job titles simultaneously. It extracts relevant job information such as job title, company name, and job description, and saves the results into CSV files.

## Features
- Scrapes multiple job titles at once.
- Extracts job title, company name, and job description.
- Saves output as CSV files.

## Prerequisites
- Python 3.6+
- Internet connection

## Setup and Installation
- Clone or Download the Project
- Download the project files to your local machine.
- Create a Virtual Environment
- Open a terminal and navigate to the project directory. Create a virtual environment with the following command:
```
python -m venv env
```
- Activate the Virtual Environment

###### On Windows:
```
env\Scripts\activate
```
###### On macOS/Linux:
```
source env/bin/activate
```
- Install Dependencies
Install the required dependencies by running:
```
pip install -r requirements.txt
```
Running the Scraper
```run.py``` 

Open the run.py file and run it or using the terminal:

python run.py

Output
The CSV files will be saved in the same directory where the script is run. Each file will be named based on the job title and the current date. For example:

These files will contain the scraped job listings with details such as job title, company name, and job description.

Notes
Ensure you have a stable internet connection while running the scraper.
If LinkedIn blocks requests due to too many requests in a short time, consider adding delays or using a proxy service.
This overview provides a simple guide on how to set up and run the LinkedIn Job Scraper using the provided script. No advanced technical knowledge is required.
