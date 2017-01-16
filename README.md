This code sample shows how to use Spark (http://spark.apache.org/) for distributed processing on the PROBA-V Mission Exploitation Platform. (https://proba-v-mep.esa.int/)
The sample intentionally implements a very simple computation:
For each PROBA-V tile in a given bounding box and time range, a histogram is computed, the results are then printed. Computation of the histograms runs in parallel.

# Development environment setup

PyCharm integration: http://stackoverflow.com/a/34714207/1158374

Note: at least PyCharm Community Edition 2016.2.3 requires that you expand `SPARK_HOME` yourself, so `PYTHONPATH` becomes:

`/path/to/the/spark/directory/python:/path/to/the/spark/directory/python/lib/py4j-some-version.src.zip`

# Running the code
## Locally
Run the spark.py script directly in your development environment. This allows for debugging your script.
Run the 'run-local' bash script on the command line for a local test run.

Both methods will use the local cpu's of your system. 
## On the Hadoop cluster
### Log into Hadoop
Run 'kinit' and provide your MEP password. (Same as VM/portal.)
kinit
### Submit your job on Hadoop
Run the run-cluster script.
Inside this script, you can adjust options such as '--num-executors' to specify the number of parallel executors to use.
### Using the Spark UI to inspect the running job
Use X2Go Client to start a remote desktop session with your VM; run Firefox and navigate to the job's tracking URL printed in
Spark's console output, e.g:
[http://epod6.vgt.vito.be:8088/proxy/application_1484394506558_0055](http://epod6.vgt.vito.be:8088/proxy/application_1484394506558_0055).

An overview of the jobs submitted to the cluster is available at
[http://epod6.vgt.vito.be:8088/cluster](http://epod6.vgt.vito.be:8088/cluster).

### View job logs Hadoop
As your job now runs on remote servers, the output generated there is not directly visible. You can retrieve the full logs like this:

Find the application id, it is printed in the console output of the Spark job.
Run:
yarn logs -applicationId application_xxxxx


