FROM apache/spark-py:latest
USER root
RUN pip install numpy pyarrow scikit-learn ipython