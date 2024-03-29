This code sample shows how to use Spark (http://spark.apache.org/) for distributed processing on the PROBA-V Mission Exploitation Platform. (https://proba-v-mep.esa.int/)
The sample intentionally implements a very simple computation:
for each PROBA-V tile in a given bounding box and time range, a histogram is computed. The results are then summed and printed. Computation of the histograms runs in parallel.

# Development environment setup

PyCharm integration: http://stackoverflow.com/a/34714207/1158374

Note: at least PyCharm Community Edition 2016.2.3 requires that you expand `SPARK_HOME` yourself, so `PYTHONPATH` becomes:

`/path/to/the/spark/directory/python:/path/to/the/spark/directory/python/lib/py4j-some-version.src.zip`

# Running the code
## Locally
Run the `spark.py` script directly in your development environment. This allows for debugging your script.
Run the `run-local` bash script on the command line for a local test run.

Both methods will use the local cpu's of your system. 
## On the Hadoop cluster
### Log into Hadoop
Run `kinit` and provide your MEP password. (Same as VM/portal.)

### Submit your job on Hadoop
Run the `run-cluster` script. It will package your project and submit it to the Hadoop cluster.

Inside this script, you can adjust options such as `--num-executors` to specify the number of parallel executors to use.

Additional Python dependencies as `.zip`, `.egg` or `.py` files can be appended to the `--py-files` argument.

### View job logs Hadoop
As your job now runs on remote servers, the output generated there is not directly visible. You can retrieve the full logs like this:

Find the application ID: it is printed in the console output of the Spark job, for example `application_1484394506558_0055`. Then run:
`yarn logs  -log_files_pattern std.*  -applicationId application_1484394506558_0055`

### Using the Spark UI to inspect the running job
Use X2Go Client to start a remote desktop session with your VM; run Firefox and navigate to the job's tracking URL printed in
Spark's console output, e.g:
[http://epod-master1.vgt.vito.be:8088/proxy/application_1484394506558_0055](http://epod-master1.vgt.vito.be:8088/proxy/application_1484394506558_0055).

An overview of the jobs submitted to the cluster is available at
[http://epod-master1.vgt.vito.be:8088/cluster](http://epod-master1.vgt.vito.be:8088/cluster).

# Spark 3 support
## Python3.8
Python3.8 no longer supports spark 2.4. This means if you have python3.8 code, Spark 3 will have to be used.
Spark 3.2 is available under `/opt/spark3_2_0/` on your userVM.

## Getting an environment
Since the Hadoop cluster does not have Python 3.8 installed by default, your own environment will have to be created. This environment will need to have the Python 3.8 binaries as well as the required libraries installed (as those are also not available on the epods).
The preferred way to achieve this is by using conda and conda-pack to package your environment as venv and venv-pack will not package Python 3.8 binaries and only install the Python 3.8 packages you install inside the virtual environment.
More information on how to get a conda environment packages for Spark [can be found here](https://conda.github.io/conda-pack/spark.html)

For our example, a simple environment where only numpy is installed as an extra package is used. The package is located on HDFS at `hdfs://hacluster/spark3_sample/spark3_example.tar.gz`. This package was created by performing:
`conda create -y -n spark3_example python=3.8 numpy`
`conda activate spark3_example`
`conda pack -o spark3_example.tar.gz`

The spark-submit command is located at `run-cluster-spark3`.
The configuration of note is:
* Setting `SPARK_HOME`
* Setting `PYSPARK_PYTHON`
* Adding the environment using `--archives`
