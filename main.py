# main_simple.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
import joblib
import logging
from pydantic import BaseModel, Field, field_validator



# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from pydantic import BaseModel, Field, field_validator

class SalaryInput(BaseModel):
    # Use the exact field names that your frontend is sending
    AGENCY_NAME: str = Field(..., description="Name of the agency")
    CLASS_TITLE: str = Field(..., description="Title of the class")
    ETHNICITY: str = Field(..., description="White, Black, Hispanic, Other")
    GENDER: str = Field(..., description="Male or Female")
    STATUS: str = Field(..., description="Employment status:Full-Time or Part-Time")
    
    # ✅ automatically convert all string fields to uppercase
    @field_validator("AGENCY_NAME", "CLASS_TITLE", "ETHNICITY", "GENDER", "STATUS", mode="before")
    def ensure_uppercase(cls, v):
        if isinstance(v, str):
            return v.upper()
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "AGENCY_NAME": "TEXAS DEPARTMENT OF CRIMINAL JUSTICE",
                "CLASS_TITLE": "CORREC OFFICER IV",
                "ETHNICITY": "HISPANIC",
                "GENDER": "FEMALE",
                "STATUS": "CRF - CLASSIFIED REGULAR FULL-TIME"
            }
        }

app = FastAPI(title="Texas Salary Estimator API")

# Load the simplified model
model = None
try:
    model = joblib.load('model_simple.pkl')
    logger.info("✅ Simplified model loaded successfully!")
except Exception as e:
    logger.error(f"❌ Model loading failed: {e}")

@app.get("/")
def home():
    return {"message": "Texas Salary Estimator API (Simplified)"}

@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "healthy"}

@app.post("/predict")
def predict_salary(user_input: SalaryInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert input to DataFrame with cleaned column names
        input_data = {
            "AGENCY_NAME": user_input.AGENCY_NAME,  # Use cleaned name
            "CLASS_TITLE": user_input.CLASS_TITLE,  # Use cleaned name  
            "ETHNICITY": user_input.ETHNICITY,
            "GENDER": user_input.GENDER,
            "STATUS": user_input.STATUS
        }

        input_df = pd.DataFrame([input_data])
        
        logger.info(f"Input DataFrame columns: {list(input_df.columns)}")
        logger.info(f"Input data: {input_data}")

        prediction = model.predict(input_df)
        predicted_salary = float(prediction[0])
        
        logger.info(f"✅ Prediction successful: ${predicted_salary:,.2f}")
        
        return JSONResponse(
            content={
                "Estimated_Annual_Salary": predicted_salary,
                "currency": "USD",
                "message": "Prediction successful"
            }, 
            status_code=200
        )
    except Exception as e:
        logger.error(f"❌ Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")