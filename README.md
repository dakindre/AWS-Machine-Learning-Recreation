# Digital Traffic Effectivness for Dealerships 

### Business Case

Create sustainable and scalable method in which to track dealer conversion performance through meaningful KPI's and calculated scoring based off of predictive models created with the purpose of learning dealerships expected sales and service figures.

Whereas traditional models look to define expected performance based on geography and realtive size, this model aims to understand fluctuation in volume based on seasonality and similarly sized dealerhsip. Metrics pertaining to lead suppliers and breakdowns by lead type are future considerations.

The four main areas of focus are listed below. Additionally there would be a filter for showing these below metrics by lead type and source vendor. 

```
Generating Sales
Managing Sales
Generating Service
Managing Service
```
The below implementation was developed using AWS, Python, PySpark, and Tableau. The dack is a mock representation of data seen in the field due to PPI and data rights. It is intended as a mock representation of the process.

## Architecture

The following diagram shows the general architecture used to create the models. The following is a more descriptive overview"

1. The mock data was created by a jupyter [script](/generateData.ipynb) running on an EC2
2. Mock data is sent to S3 using Boto3 SDK
3. Event trigger begins Glue's Pyspark ETL handling
4. Data is reloaded into S3 in a full form and newly created form with unique ID for ML process
5. Minimized data set load triggers the Machine Learning Batch process
6. Batch process returns data to S3 
7. Predictive results are combined with original file using PySpark data transformation
8. Results are stored in S3 and downloaded
9. Data imported into Tableau for visualization and further calculations


![alt text](/Images/AWS_Data_Flow.png)


## Data Recreation

The data file used as input was created to mock to normalized distribution seen in actual data. The generation created 60,000 random data entries. Due to PII and data restriction laws I was not allowed to use the actual data set. The actual sales numbers used were randomly generated but roughly followed a normal distribution. The file structure is as shown below:

```
VDP Views | Unique Visitors | Lead Volume | Visitor Conversions | Actual Sales
```

## Regression Results

The log results of the ML training can be found [here](/MLOutput.txt) 

