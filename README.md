This code sample shows how to use Spark (http://spark.apache.org/) for distributed processing on the PROBA-V Mission Exploitation Platform. (https://proba-v-mep.esa.int/)
The sample intentionally implements a very simple computation:
For each PROBA-V tile in a given bounding box and time range, a histogram is computed, the results are then printed. Computation of the histograms runs in parallel.

# Development environment setup

PyCharm integration: http://stackoverflow.com/a/34714207/1158374 (note: use absolute paths in PYTHONPATH)

# Running the code
## Locally
Run the spark.py script directly in your development environment. This allows for debugging your script.
Run the 'run-local' bash script on the command line for a local test run.

Both methods will use the local cpu's of your system. 
## On the Hadoop cluster
### Log into Hadoop
kinit
### Submit your job on Hadoop
(TODO)
### Using the Spark UI to inspect the running job
### View job logs Hadoop
(TODO)


