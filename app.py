
import streamlit as st

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------
# TRAVEL DATABASE
# -----------------------------

places = {
    "Jaipur": {
        "Nature": ["Jal Mahal", "Central Park"],
        "History": ["Hawa Mahal", "Amber Fort", "City Palace"],
        "Shopping": ["Johari Bazaar", "Bapu Bazaar"],
        "Adventure": ["Nahargarh Fort", "Hot Air Balloon Ride"],
        "Food": ["Chokhi Dhani", "Local Food Market"]
    },

    "Goa": {
        "Nature": ["Baga Beach", "Dudhsagar Falls"],
        "History": ["Aguada Fort", "Old Goa Churches"],
        "Shopping": ["Anjuna Flea Market", "Mapusa Market"],
        "Adventure": ["Water Sports", "Scuba Diving"],
        "Food": ["Goan Food Market", "Beachside Cafes"]
    },

    "Agra": {
        "Nature": ["Mehtab Bagh", "Taj Nature Walk"],
        "History": ["Taj Mahal", "Agra Fort", "Fatehpur Sikri"],
        "Shopping": ["Sadar Bazaar", "Kinari Bazaar"],
        "Adventure": ["Heritage Walking Tour"],
        "Food": ["Local Street Food", "Petha Shops"]
    },

    "Delhi": {
        "Nature": ["Lodhi Garden", "Garden of Five Senses"],
        "History": ["Red Fort", "India Gate", "Qutub Minar"],
        "Shopping": ["Sarojini Nagar", "Connaught Place"],
        "Adventure": ["Adventure Island"],
        "Food": ["Chandni Chowk", "Delhi Food Streets"]
    }
}

# -----------------------------
# WEBSITE DESIGN
# -----------------------------

st.title("✈️ AI TRIP PLANNER BY ISHANT, DIVISHA, PIYUSH, KHETAN, AANYA")
st.subheader("Your Personal Smart Travel Assistant")

st.write(
    "Plan your dream trip according to your "
    "destination, budget and interests."
)

st.divider()

# -----------------------------
# USER INPUT
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    starting_city = st.text_input(
        "Starting City", "Greater Noida"
    )

    destination = st.selectbox(
        "Choose Destination",
        list(places.keys())
    )

    days = st.slider(
        "Number of Days", 1, 7, 3
    )

with col2:
    budget = st.number_input(
        "Total Budget (₹)",
        min_value=1000,
        max_value=200000,
        value=10000,
        step=1000
    )

    travellers = st.number_input(
        "Number of Travellers",
        min_value=1,
        max_value=20,
        value=2
    )

    interest = st.selectbox(
        "Your Travel Interest",
        ["Nature", "History", "Shopping",
         "Adventure", "Food"]
    )

st.divider()

# -----------------------------
# TRIP GENERATION ALGORITHM
# -----------------------------

if st.button("✨ Generate My Trip", use_container_width=True):

    selected_places = places[destination][interest]

    # Calculate estimated expenses
    food_cost = days * travellers * 500
    travel_cost = days * travellers * 400
    hotel_cost = days * travellers * 1000

    total_cost = food_cost + travel_cost + hotel_cost

    st.success("Your trip plan is ready!")

    # Show trip details
    st.header("📍 Your Trip Overview")

    a, b, c = st.columns(3)

    a.metric("Destination", destination)
    b.metric("Trip Duration", f"{days} Days")
    c.metric("Travellers", travellers)

    st.subheader("🗓️ Your Day-Wise Itinerary")

    for day in range(days):
        place = selected_places[day % len(selected_places)]

        with st.expander(f"Day {day + 1}"):
            st.write(f"📍 Visit: **{place}**")
            st.write("🍽️ Enjoy local food and explore nearby areas.")
            st.write("📸 Take pictures and enjoy your trip!")

    # Budget breakdown
    st.subheader("💰 Estimated Budget")

    st.write(f"🍽️ Food: ₹{food_cost}")
    st.write(f"🚕 Local Travel: ₹{travel_cost}")
    st.write(f"🏨 Accommodation: ₹{hotel_cost}")

    st.metric("Estimated Total Cost", f"₹{total_cost:,}")

    if total_cost <= budget:
        st.success("Your estimated trip cost is within your budget!")
    else:
        st.warning(
            "Your estimated trip cost exceeds your budget. "
            "Consider reducing expenses."
        )

    st.info(
        "Note: These are illustrative estimates, not live travel prices."
    )

    st.balloons()

st.divider()

st.caption(
    "AI Trip Planner | BTech CSE Computational Thinking Project"
)
