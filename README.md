# Digital Traffic Scoring Solution

### Business Case

Create a sustainable and scalable method in which to track dealer conversion performance through meaningful KPI's and calculated scoring based off of predictive models created with the purpose of learning dealerships expected sales and service figures.

Whereas traditional models look to define expected performance based on geographical comparison and industry standards, this model aims to understand fluctuation in volume based on seasonality and similarly sized dealerhsips. Metrics pertaining to lead suppliers and breakdowns by lead type are future considerations.

The two main areas of focus are listed below and their respective KPI's that were proven to have strong correlation to the target metric, which in this case is actual sales. Service has no yet been implemented and is therefore left out. It follows a similar structure to the sales methodology.

```
Generating Sales:   VDP Views | Unique Visitors | Lead Volume | Visitor Conversions | Actual Sales

Managing Sales:     Close Rate | SDSV Close Rate | Sales Loyalty | % of Leads Responded to Within 30 Minutes

```

The below implementation was developed using AWS, Python, PySpark, and Tableau. The dack is a mock representation of data seen in the field due to PPI and data rights. It is intended as a mock representation of the process.

## Architecture

The following diagram shows the general architecture used to create the models. The following is a more descriptive overview"

1. The mock data was created using a Jupyter Notebook running on EC2
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

The mock data for training the model was created using the two scripts below:

[Generating](/bdc_generating_data_generator.ipynb)

[Managing](/bdc_managing_data_generator_training.ipynb)

The batch prediction set of which the the report data is comprised is altered slightly both up and down for metrics to show enough variance that would simulate normal changes in dealerships. An example of this can be seen in modifying slight the mu and sigma of the normalized distribution in the sample file below:

[Managing Sample](/bdc_managing_data_generator_altered.ipynb)



## Regression Results

The log results of the ML training can be found [here](/MLOutput.txt) 

## Visualization
In order to visualize the results of the scoring system a Tableau dashboard was created to see how the process works with mock data. A sample image is shown below and the full hosted report can be found on Tableau public here. 

![alt_text](/Images/DigitalTrafficDashboard.png)

