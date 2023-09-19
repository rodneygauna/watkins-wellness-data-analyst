# Watkins Wellness - Data Analyst Project

## Project Overview

Create a simulated sales data environment, perform Extract, Transform, Load (ETL) operations on the data, and create interactive dashboards to visualize the insights using Streamlit.

## Project Steps

1. Database Creation:

Set up three SQLite3 databases, each representing a different source of sales data. You can use libraries like SQLite or SQLAlchemy in Python to create these databases.
Populate each database with random sales data. You can use Python's random library to generate realistic data.

2. Data Schema Design:

Define a clear schema for each database that includes tables for sales transactions, products, customers, dates, etc. Ensure that the schema of all three databases is similar for ease of ETL.

3. ETL Process:

Write Python scripts to perform the ETL process. This involves:
Extracting data from the three source databases.
Transforming and cleaning the data as needed (e.g., handling missing values, data type conversions).
Loading the transformed data into a new SQLite3 database, which will serve as your data warehouse.

4. Data Warehouse Design:

Create tables in the data warehouse to hold the integrated data.
Ensure that the data warehouse schema aligns with the structure of the source databases.

5. Streamlit Dashboard:

Use the Streamlit library in Python to build interactive dashboards.
Connect the dashboard to your data warehouse (SQLite3 database) to fetch and display insights.
Create multiple dashboards or tabs within the Streamlit app to showcase different aspects of the data, such as sales trends, product performance, customer segmentation, etc.
Implement filters, charts, and tables to allow users to interact with the data.

6. Documentation:

Document your project thoroughly, including the data schema, ETL process, and how to run the Streamlit dashboard.
Include comments in your code to explain the logic and any important decisions.

7. Testing and Validation:

Test your ETL process to ensure data accuracy and integrity.
Verify that the dashboards display accurate information and that the filters and interactivity work as expected.

8. Presentation:

Prepare a brief presentation or demo to showcase your project, highlighting your skills and the value it can bring to potential employers like Watkins Wellness.

9. Future Enhancements:

Consider adding more features or complexity to the project, such as implementing advanced data analytics, predictive modeling, or connecting to a live data source.
Completing this project will not only demonstrate your proficiency in Python, SQL, and data analysis but also provide you with a practical portfolio piece that you can showcase when applying for the Data Analyst position at Watkins Wellness or other similar roles.

## Run The Project

### Generate the Databases

Run the following to generate the databases:

```python
python3 src/db-generate/db-generate.py
```
