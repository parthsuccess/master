import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Energy Consumption Calculator",
    page_icon="⚡",
    layout="centered"
)

# Main title
st.title("⚡ Energy Consumption Calculator")
st.markdown("Calculate your daily energy consumption based on your housing and appliances")

# Create two columns for better layout
col1, col2 = st.columns(2)

# Personal Information Section
st.header("📋 Personal Information")
with col1:
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)

with col2:
    city = st.text_input("Enter your city:")
    area = st.text_input("Enter your area name:")

# Housing Information Section
st.header("🏠 Housing Information")
with col1:
    flat_tenament = st.selectbox(
        "Are you living in Flat or Tenement?",
        ["Select", "Flat", "Tenement"]
    )

with col2:
    facility = st.selectbox(
        "What type of accommodation?",
        ["Select", "1BHK", "2BHK", "3BHK"]
    )

# Appliances Section
st.header("🔌 Appliances")
col3, col4, col5 = st.columns(3)

with col3:
    ac = st.radio("Are you using AC?", ["No", "Yes"])

with col4:
    fridge = st.radio("Are you using Fridge?", ["No", "Yes"])

with col5:
    wm = st.radio("Are you using Washing Machine?", ["No", "Yes"])

# Calculate button
if st.button("Calculate Energy Consumption", type="primary"):
    # Validation
    if not name:
        st.error("Please enter your name")
    elif flat_tenament == "Select":
        st.error("Please select Flat or Tenement")
    elif facility == "Select":
        st.error("Please select your accommodation type")
    else:
        # Energy calculation using your original logic
        cal_energy = 0
        
        facility_lower = facility.lower()
        if facility_lower == "1bhk":
            cal_energy += 2 * 0.4 + 2 * 0.8  # 2.4 kWh
        elif facility_lower == "2bhk":
            cal_energy += 3 * 0.4 + 3 * 0.8  # 3.6 kWh
        elif facility_lower == "3bhk":
            cal_energy += 4 * 0.4 + 4 * 0.8  # 4.8 kWh
        
        # Add appliance consumption
        if ac == "Yes":
            cal_energy += 3
        
        if fridge == "Yes":
            cal_energy += 3
            
        if wm == "Yes":
            cal_energy += 3
        
        # Display results
        st.success("✅ Calculation Complete!")
        
        # Create results section
        st.header("📊 Energy Consumption Report")
        
        # Display in a nice format
        col_result1, col_result2 = st.columns(2)
        
        with col_result1:
            st.metric(
                label="Daily Energy Consumption",
                value=f"{cal_energy:.1f} kWh"
            )
            st.metric(
                label="Monthly Energy Consumption",
                value=f"{cal_energy * 30:.1f} kWh"
            )
        
        with col_result2:
            st.metric(
                label="Estimated Monthly Cost",
                value=f"₹{cal_energy * 30 * 6:.0f}",
                help="Assuming ₹6 per kWh"
            )
            st.metric(
                label="Annual Energy Consumption",
                value=f"{cal_energy * 365:.0f} kWh"
            )
        
        # Detailed breakdown
        st.subheader("🔍 Detailed Breakdown")
        
        # Base consumption
        base_consumption = 0
        if facility_lower == "1bhk":
            base_consumption = 2.4
        elif facility_lower == "2bhk":
            base_consumption = 3.6
        elif facility_lower == "3bhk":
            base_consumption = 4.8
        
        breakdown_data = {
            "Item": ["Base Consumption (" + facility + ")", "Air Conditioner", "Refrigerator", "Washing Machine"],
            "Usage": ["Yes", ac, fridge, wm],
            "Energy (kWh)": [base_consumption, 3 if ac == "Yes" else 0, 3 if fridge == "Yes" else 0, 3 if wm == "Yes" else 0]
        }
        
        st.table(breakdown_data)
        
        # Personal details summary
        st.subheader("👤 Personal Details")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age} years")
        st.write(f"**Location:** {area}, {city}")
        st.write(f"**Accommodation:** {facility} {flat_tenament}")
        
        # Energy saving tips
        st.subheader("💡 Energy Saving Tips")
        tips = [
            "🌡️ Set AC temperature to 24°C for optimal efficiency",
            "🔌 Unplug devices when not in use",
            "💡 Use LED bulbs instead of incandescent bulbs",
            "🌞 Use natural light during daytime",
            "🔄 Regular maintenance of appliances improves efficiency"
        ]
        
        for tip in tips:
            st.write(tip)

# Footer
st.markdown("---")
st.markdown("*Energy consumption values are estimates based on typical usage patterns*")