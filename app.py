import streamlit as st
import pickle
import pandas as pd

# โหลดโมเดล
with open('hotel_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🔮 Hotel Price Predictor")

# ตัวอย่าง description สำหรับแต่ละโรงแรม
descriptions = {
    "Grandview Hotel New York": "Standard Queen Room with 1 queen bed and city view. Free Wi-Fi and daily housekeeping.",
    "Gold Point Resort by Vacatia": "Spacious condo with mountain views, fireplace, and full kitchen. Ideal for families.",
    "Hotel Effie Sandestin": "Deluxe king room with balcony, pool access, and luxurious amenities."
}

# Input from user
name = st.selectbox("🏨 Hotel Name", list(descriptions.keys()))
location = st.selectbox("📍 Location", ["Flushing, Queens", "Baldy Mountain, Breckenridge", "South Beach, Miami Beach"])
rating = st.slider("⭐ Rating", min_value=5.0, max_value=10.0, step=0.1)

# Auto-fill description ตามโรงแรม
default_description = descriptions.get(name, "")
description = st.text_area("📝 Room Description", value=default_description)

# ปุ่มทำนาย
if st.button("Predict Price"):
    # สร้าง DataFrame สำหรับส่งเข้าโมเดล
    input_df = pd.DataFrame({
        'name': [name],
        'description': [description],
        'location': [location],
        'rating': [rating]
    })

    # ทำนาย
    predicted_price = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: {predicted_price:.2f} ฿ ")
