FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy --ignore-pipfile

COPY ["predict.py", "model1.bin", "./"]

EXPOSE 9696

RUN pipenv install gunicorn

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]