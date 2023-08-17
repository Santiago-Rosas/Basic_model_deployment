import pandas as pd
import joblib

model = joblib.load("model/model.pk")
column_equivalence =joblib.load("model/column_equivalence.pk")
scaler=joblib.load("model/scaler.pk")

def convert_numerical(features):
    output = []
    for i, feat in enumerate(features):
        if i in column_equivalence:
            output.append(column_equivalence[i][feat])
        else:
            try:
                output.append(pd.to_numeric(feat))
            except:
                output.append(0)
    return output



def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction


def get_model_response(input):
    DF = pd.json_normalize(input.__dict__)
    numerical= convert_numerical(DF.values[0])
    X = scaler.transform([numerical]) 
    prediction = predict(X, model)
    if prediction == 1:
        label = " likely to churn"
    else:
        label = " likely to not churn"
    return {
        'label': label,
        'prediction': int(prediction)
    }
