package: python setup.py sdist --format=zip

submit: spark-submit --master local[*] --py-files dist/python-spark-quickstart-0.1.zip spark.py
