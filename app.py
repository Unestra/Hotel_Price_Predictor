import streamlit as st
import pickle
import pandas as pd

# โหลดโมเดล
with open('hotel_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🔮 Hotel Price Predictor")
st.title("🔮 Project2_Group4")

# ข้อมูลโรงแรม (description + location)
hotel_data = {
    "Grandview Hotel New York": (
        "Standard Queen Room with 1 queen bed and city view. Free Wi-Fi and daily housekeeping.",
        "New York, NY"
    ),
    "Gold Point Resort by Vacatia": (
        "Spacious condo with mountain views, fireplace, and full kitchen. Ideal for families.",
        "Breckenridge, CO"
    ),
    "Hotel Effie Sandestin": (
        "Deluxe king room with balcony, pool access, and luxurious amenities.",
        "Miramar Beach, FL"
    ),
    "Hilton Garden Inn San Diego": (
        "Modern room with work desk, microwave, and close to shopping districts.",
        "San Diego, CA"
    ),
    "The Venetian Resort Las Vegas": (
        "Luxury suite with marble bathroom and premium casino access.",
        "Las Vegas, NV"
    ),
    "Marriott Marquis Houston": (
        "Executive room with skyline view and access to rooftop pool.",
        "Houston, TX"
    ),
    "Waldorf Astoria Beverly Hills": (
        "Elegant suite with private terrace and personalized concierge service.",
        "Beverly Hills, CA"
    ),
    "The Ritz-Carlton Orlando": (
        "Golf view suite with large bathroom and fine dining on-site.",
        "Orlando, FL"
    ),
    "Hyatt Regency Maui Resort": (
        "Oceanfront room with lanai, ideal for honeymooners.",
        "Lahaina, HI"
    ),
    "Omni Boston Hotel at the Seaport": (
        "Premium room in Seaport District with business facilities.",
        "Boston, MA"
    ),
    "The Cosmopolitan of Las Vegas": (
        "City-view suite with terrace, soaking tub, and nightlife access.",
        "Las Vegas, NV"
    ),
    "The Langham Chicago": (
        "Club room with river view and spa access included.",
        "Chicago, IL"
    ),
    "Four Seasons Resort Maui": (
        "Beachfront bungalow with personal butler and private pool.",
        "Maui, HI"
    ),
    "Sheraton Waikiki": (
        "High-rise room with ocean view and daily cultural activities.",
        "Waikiki, HI"
    ),
    "Loews Miami Beach Hotel": (
        "Art deco room steps from the beach and vibrant nightlife.",
        "Miami Beach, FL"
    ),
    "InterContinental San Francisco": (
        "Business king room near convention center with city views.",
        "San Francisco, CA"
    ),
    "Park Hyatt New York": (
        "Luxury suite with floor-to-ceiling windows near Central Park.",
        "New York, NY"
    ),
    "Mandarin Oriental Boston": (
        "Modern suite with spa-style bathroom and afternoon tea service.",
        "Boston, MA"
    ),
    "The St. Regis Aspen Resort": (
        "Ski-in/ski-out suite with fireplace and heated bathroom floors.",
        "Aspen, CO"
    ),
    "Fairmont Pacific Rim Vancouver": (
        "Harbor-view room with digital concierge and yoga mat.",
        "Vancouver, BC"
    )
}

# UI Input
name = st.selectbox("🏨 Hotel Name", list(hotel_data.keys()))
default_description, default_location = hotel_data[name]

# Description (editable)
description = st.text_area("📝 Room Description", value=default_description)

# Location (editable)
location = st.text_input("📍 Location", value=default_location)

# Rating slider
rating = st.slider("⭐ Rating", min_value=5.0, max_value=10.0, step=0.1)

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame({
        'name': [name],
        'description': [description],
        'location': [location],
        'rating': [rating]
    })

    predicted_price = model.predict(input_df)[0]
    st.success(f"💰 Estimated Price: {predicted_price:.2f} ฿")
