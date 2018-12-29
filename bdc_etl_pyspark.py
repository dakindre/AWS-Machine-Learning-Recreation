import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)



## @type: DataSource
## @args: [database = "generating-lead-data", table_name = "bdc_generated_leads_2018_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "generating-lead-data", table_name = "bdc_generated_leads_2018_csv", transformation_ctx = "datasource0")





## @type: ApplyMapping
## @args: [mapping = [("col1", "string", "BAC", "string"), ("col2", "string", "Region", "string"), ("col3", "string", "Month", "string"), ("col4", "string", "VDPViews", "int"), ("col5", "string", "Visitors", "int"), ("col6", "string", "LeadVolume", "int"), ("col7", "string", "VisitorConversion", "int"), ("col8", "string", "Sales", "int")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("col1", "string", "BAC", "string"), ("col2", "string", "Region", "string"), ("col3", "string", "Month", "string"), ("col4", "string", "VDPViews", "int"), ("col5", "string", "Visitors", "int"), ("col6", "string", "LeadVolume", "int"), ("col7", "string", "VisitorConversion", "int"), ("col8", "string", "Sales", "int")], transformation_ctx = "applymapping1")


## @type: Filter
## @args: [f = <function>, transformation_ctx = "<transformation_ctx>"]
## @return: applytransform1
## @inputs: [frame = applymapping1]
applytransform1 = Filter.apply(frame = applymapping1, f = lambda x: x['VDPViews'] >= 0 and x['Visitors'] >= 0 and x['LeadVolume'] >= 0 and x['VisitorConversion'] >= 0 and x['Sales'] >= 0, transformation_ctx = "applytransform1")

## @type: Filter
## @args: [f = <function>, transformation_ctx = "<transformation_ctx>"]
## @return: applytransform2
## @inputs: [frame = applytransform1]
applytransform2 = Filter.apply(frame = applytransform1, f = lambda x: x['VDPViews'] >= x['Visitors'] and x['Visitors'] >= x['VisitorConversion'] and ['LeadVolume'] >= x['Sales'], transformation_ctx = "applytransform2")



## @type: DataSink
## @args: [connection_type = "s3", connection_options = {"path": "s3://lead-data-bdc"}, format = "csv", transformation_ctx = "datasink2"]
## @return: datasink2
## @inputs: [frame = applymapping1]
datasink2 = glueContext.write_dynamic_frame.from_options(frame = applytransform2, connection_type = "s3", connection_options = {"path": "s3://lead-data-bdc"}, format = "csv", transformation_ctx = "datasink2")
job.commit()