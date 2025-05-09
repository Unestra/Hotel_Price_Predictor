import streamlit as st
import pickle
import pandas as pd

# โหลดโมเดล
with open('hotel_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🔮 Hotel Price Predictor")

# Input from user
name = st.selectbox("🏨 Hotel Name", ["Grandview Hotel New York", "Gold Point Resort by Vacatia", "Hotel Effie Sandestin"])  # เพิ่มตามชื่อใน dataset
location = st.selectbox("📍 Location", ["Flushing, Queens", "Baldy Mountain, Breckenridge", "South Beach, Miami Beach"])    # เพิ่มตาม location จริง
rating = st.slider("⭐ Rating", min_value=5.0, max_value=10.0, step=0.1)
# description = st.text_area("📝 Room Description", "Standard Queen Room1 queen bedOnly 1 room left at this price!")
st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ca.kayak.com%2Fnews%2Fwhat-do-hotel-stars-mean%2F&psig=AOvVaw3QQIpeIUIhVpyGBFjoXCJF&ust=1746858135964000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCLjbgOnflY0DFQAAAAAdAAAAABAE", caption="Hotel Front", use_column_width=True)


# ปุ่มทำนาย
if st.button("Predict Price"):
    # สร้าง DataFrame 1 แถวสำหรับส่งเข้าโมเดล
    input_df = pd.DataFrame({
        'name': [name],
        'description': [description],
        'location': [location],
        'rating': [rating]
    })

    # ทำนาย
    predicted_price = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: {predicted_price:.2f} บาท")
