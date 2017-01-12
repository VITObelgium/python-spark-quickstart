PyCharm integration: http://stackoverflow.com/a/34714207/1158374 (note: use absolute paths in PYTHONPATH)

package: python setup.py sdist --format=zip

submit: spark-submit --master local[*] --py-files dist/python-spark-quickstart-0.1.zip spark.py
