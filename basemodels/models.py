
from pydantic import BaseModel, Field


# Input for data validation
class Input(BaseModel):
    CreditScore: float = Field(gt=0)
    Geography: str = Field(min_length=1, max_length=20)
    Gender: str = Field(min_length=4, max_length=6)
    Age: int = Field(gt=0)
    Tenure: int = Field(ge=0)
    Balance: float = Field(ge=0)
    NumOfProducts: int = Field(gt=0)
    HasCrCard: int = Field(le=1)
    IsActiveMember: int = Field(le=1)
    EstimatedSalary: float = Field(gt=0)

    class Config:
        schema_extra = {
            "example":{
            "CreditScore": 608,
            "Geography": "Spain",
            "Gender": "Female",
            "Age": 41,
            "Tenure": 1,
            "Balance": 83807.86,
            "NumOfProducts": 1,
            "HasCrCard": 0,
            "IsActiveMember": 1,
            "EstimatedSalary": 112542.58,
            }
}

# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int
