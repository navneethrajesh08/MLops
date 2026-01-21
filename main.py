from fastapi import FastAPI
from pydantic import BaseModel
from scoring import predict_price

app = FastAPI()

class PropertyItem(BaseModel):
    name: str
    surface_area: float
    bedrooms: int


@app.get("/")
def home():
    return {"message": "Property Price Predictor"}

@app.get("/properties/{property_id}")
def get_property(property_id: int, name: str,surface_area: float, bedrooms:int):
    # Adding data with the required fields
    response = {
        "property_id": property_id,
        "name": name,
        "surface_area": surface_area,  
        "bedrooms": bedrooms,
        "message": f"Details added for property ID {property_id}"
    }
    return response

@app.put("/properties/{property_id}")
def update_property(property_id: int, property_item: PropertyItem):
    # Predict price using our scoring algorithm
    predicted_price = predict_price(property_item.surface_area, property_item.bedrooms
    )
    return {
        "predicted_price_euros": round(predicted_price, 2),
    }