#scoring.py
def predict_price(surface_area: float, bedrooms: int) -> float:
    """
    The core scoring algorithm. 
    Separated from the API logic.
    Example formula used only for reference to calculate price
    """
    base_price = 50000
    area_rate = 3000  
    bedrooms_rate = 15000
    
    # Apply formula
    price = (base_price + (surface_area * area_rate) + (bedrooms * bedrooms_rate)
    )
    
    return price

