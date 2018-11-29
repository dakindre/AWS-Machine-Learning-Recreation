# AWS-Machine-Learning-Recreation

### Business Case

Develop four models which predict dealerships expected sales and service RO's based on digital lead traffic data. The predicted output of these models are compared against the actuals for both sales and service to determine the index scores which effectively rate the dealers performance monthly. The scores are broken out into the four categories below:

```
Generating Sales
Managing Sales
Generating Service
Managing Service
```
The below implementation is a recreation of a process done in AWS and only shows the results of mock degerated data for Generating Sales. The process was the same for all four created models. 

## Architecture

The following diagram shows the general architecture used to create the models. The following is a more descriptive overview"

1. The mock data was created by a jupyter script running on an EC2 [script] (generateData.ipynb)
2. Using the AWS SDK Boto3 the data was sent to S3
3. The AWS Machine Learning Service created a model based on the data provided in S3 
4. The output of future batch data is sent to S3 for storage
5. [Not Included] File would be downloaded and imported into On Premise MS SQL Server DB where the index scores would be computed


![alt text](/Images/GeneratingSalesMockMLFlow.png)


## Data Recreation

The data file used as input was created to mock to normalized distribution seen in actual data. Due to PII and data restriction laws I was not allowed to use the actual data set. The actual sales numbers used were randomly generated but roughly followed a normal distribution. The file structure is as shown below:

```
VDP Views | Unique Visitors | Lead Volume | Visitor Conversions | Actual Sales
```

## Regression Results

The following shows the results of predictive model created by AWS ML
