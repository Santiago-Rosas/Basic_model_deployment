FROM python:3.10

WORKDIR /app

COPY requirements.txt /app

RUN pip install -U pip && pip install -r requirements.txt

COPY main.py /app
COPY model /app/model
COPY basemodels /app/basemodels
COPY ms /app/ms

# Run
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

## docker build . -t model_v1
## docker run -d -p 8000:8000 model_v1 --name mdel_v1_test