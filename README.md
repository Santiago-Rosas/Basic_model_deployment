# Basic model deployment

Deployment of SVC model using FastAPI:

- Sacling features with StandardScale 
- Model selection using  GridSearchCV
- app construction with FastAPI
- Containerization of the app using Docker 

## For running app 
1. Clone the repository: 
```bash
git clone https://github.com/Santiago-Rosas/Basic_model_deployment.git
```
2. Create the docker image: 
```bash
docker build . -t model_v1
```
3. Build the docker container: 

```bash
docker run -d --rm -p 8000:8000 model_v1
```

## Usage
Request prediction (example):
```bash
curl -d '{"CreditScore": 608, "Geography": "Spain", "Gender": "Female", "Age": 41, "Tenure": 1, "Balance": 83807.86, "NumOfProducts": 1, "HasCrCard": 0, "IsActiveMember": 1, "EstimatedSalary": 112542.58}' \
     -H "Content-Type: application/json" \
     -X POST http://0.0.0.0:8000/predict
```
Get information about model 

```bash
curl -XGET http://localhost:8000/info_model
```

## To visit documentation of the app 

http://localhost:8000/docs

## License

[MIT](https://choosealicense.com/licenses/mit/)
