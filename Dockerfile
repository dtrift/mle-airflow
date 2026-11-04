FROM apache/airflow:3.3.2

COPY requirements.txt /tmp/requirements.txt

# Версии транзитивных зависимостей подбирает constraints-файл Airflow
# (python базового образа — 3.13, проверено `python --version` в образе).
RUN pip install --no-cache-dir \
    -r /tmp/requirements.txt \
    -c https://raw.githubusercontent.com/apache/airflow/constraints-3.3.2/constraints-3.13.txt
