import streamlit as slt
slt.set_page_config(layout="wide")
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime
import csv


# Load bus route lists from CSV files
def load_route_lists():
    df_AP = pd.read_csv(r"C:/streamlit_day2/myappr/AP_data.csv")
    df_TS = pd.read_csv(r"C:/streamlit_day2/myappr/tsrtc_data2.csv")
    df_KL = pd.read_csv(r"C:/streamlit_day2/myappr/ksrtc_data3.csv")
    df_RS = pd.read_csv(r"C:/streamlit_day2/myappr/rsrtc_data4.csv")
    df_HR = pd.read_csv(r"C:/streamlit_day2/myappr/hrtc_data5.csv")
    df_CTU = pd.read_csv(r"C:/streamlit_day2/myappr/ctu_data6.csv")
    df_SB = pd.read_csv(r"C:/streamlit_day2/myappr/sbstc_data6.csv")
    df_UP = pd.read_csv(r"C:/streamlit_day2/myappr/upsrtc_data.csv")
    df_PE = pd.read_csv(r"C:/streamlit_day2/myappr/pepsu_data.csv")
    df_WB = pd.read_csv(r"C:/streamlit_day2/myappr/wbtc_data.csv")
    df_BS = pd.read_csv(r"C:/streamlit_day2/myappr/bsrtc_data01.csv")
    df_AS = pd.read_csv(r"C:/streamlit_day2/myappr/astc_data.csv")

    lists_AP = df_AP["Route_name"].tolist()
    lists_TS = df_TS["Route_name"].tolist()
    lists_KL = df_KL["Route_name"].tolist()
    lists_RS = df_RS["Route_name"].tolist()
    lists_HR = df_HR["Route_name"].tolist()
    lists_CTU = df_CTU["Route_name"].tolist()
    lists_SB = df_SB["Route_name"].tolist()
    lists_UP = df_UP["Route_name"].tolist()
    lists_PE = df_PE["Route_name"].tolist()
    lists_WB = df_WB["Route_name"].tolist()
    lists_BS = df_BS["Route_name"].tolist()
    lists_AS = df_AS["Route_name"].tolist()

    return lists_AP, lists_TS, lists_KL, lists_RS, lists_HR, lists_CTU, lists_SB, lists_UP, lists_PE, lists_WB, lists_BS, lists_AS


lists_AP, lists_TS, lists_KL, lists_RS, lists_HR, lists_CTU, lists_SB, lists_UP, lists_PE, lists_WB, lists_BS, lists_AS = load_route_lists()


def get_routes(state):
    if state == "Andhra Pradesh":
        return lists_AP
    elif state == "Telangana":
        return lists_TS
    elif state == "Kerala":
        return lists_KL
    elif state == "Rajasthan":
        return lists_RS
    elif state == "Himachal":
        return lists_HR
    elif state == "Chandigarh":
        return lists_CTU
    elif state == "South Bengal":
        return lists_SB
    elif state == "Uttar Pradesh":
        return lists_UP
    elif state == "Punjab":
        return lists_PE
    elif state == "West Bengal":
        return lists_WB
    elif state == "Bihar":
        return lists_BS
    elif state == "Assam":
        return lists_AS

def load_csv_data():
    try:
        return pd.read_csv(r"C:/streamlit_day2/myappr/redbusdata12.csv")
    except Exception as e:
        slt.error(f"Error loading data: {e}")
        return pd.DataFrame()

df_redbus = load_csv_data()

df_redbus['Price'] = pd.to_numeric(df_redbus['Price'], errors='coerce')

df_redbus = df_redbus.dropna(subset=['Price'])


# Navigation menu:
web = option_menu(menu_title="Welcome to Redbus",
                  options=["Home", "About us", "Bus details", "Bus Booking", "Terms and Conditions", "FAQ"],  # Add "FAQ"
                  icons=["house", "info-circle", "bus", "ticket", "file-text", "question-circle"],  # Added relevant icon
                  orientation="horizontal")


# Home page:

if web == "Home":
    slt.image("C:/Users/Shalini/Downloads/WhatsApp Image 2024-09-26 at 8.40.12 PM.jpeg", width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":blue[Domain:] Transportation")
    slt.image("C:/Users/Shalini/Downloads/WhatsApp Image 2024-09-26 at 8.43.07 PM.jpeg", width=400)
    slt.subheader(":blue[Objective:]")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data.")
    slt.subheader(":blue[Overview:]")
    slt.markdown('''Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites.
                    Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    MySQL: The extracted data is stored in MySQL for further querying and filtering.
                    Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.''')


# About us page:

if web == "About us":
    slt.title("About Us")
    slt.subheader("Welcome to Redbus Data Scraping and Filtering Application")
    slt.markdown(
        """
        **Objective**: 
        Our primary goal is to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. This application allows users to easily filter and find relevant bus travel information across various states in India.

        **What We Do**:
        - We scrape data from multiple state-run bus services to provide a centralized platform for bus route and fare information.
        - Users can filter bus details based on criteria like bus type, fare range, and time of travel, making it easier to plan their journeys.
        
        **Technologies Used**:
        - **Selenium**: A powerful tool for web scraping, allowing us to automate the extraction of data from websites.
        - **Pandas**: A robust library for data manipulation and analysis, enabling us to handle large datasets efficiently.
        - **MySQL**: Used for storing the scraped data for further querying and analysis.
        - **Streamlit**: A user-friendly framework that facilitates the creation of interactive web applications for data visualization.

        **Our Vision**:
        We aim to provide an intuitive and efficient platform for travelers to access bus travel information, thus enhancing their travel planning experience. 

        **Developed By**: Shalini Raju
        """
    )



# Bus details page:

elif web == "Bus details":
    slt.header("📋 Bus Details")
    state = slt.selectbox("🗺️ Select State" , ["Andhra Pradesh", "Telangana", "Kerala", "Rajasthan", "Himachal", 
                                                 "Chandigarh", "South Bengal", "Uttar Pradesh", 
                                                 "Punjab", "West Bengal", "Bihar", "Assam"])

    
    route = slt.selectbox("📍 List of routes", get_routes(state))

    
    filtered_data_by_route = df_redbus[df_redbus['Route_name'] == route].copy()

    bus_names = filtered_data_by_route['Bus_name'].unique()
    selected_bus_name = slt.selectbox("🚌 Select Bus Name", ["All"] + bus_names.tolist())

    
    bus_types = filtered_data_by_route['Bus_type'].unique()
    selected_bus_type = slt.selectbox("🚌 Select Bus Type", ["All"] + bus_types.tolist())

    
    filtered_data_by_route['Start_time'] = pd.to_datetime(filtered_data_by_route['Start_time'], format='%H:%M', errors='coerce')
    filtered_data_by_route.dropna(subset=['Start_time'], inplace=True)  
    start_times = filtered_data_by_route['Start_time'].dt.strftime('%I:%M %p').unique()
    selected_start_time = slt.selectbox("⏰ Select Start Time", ["All"] + start_times.tolist())

    
    min_price = filtered_data_by_route['Price'].min()
    max_price = filtered_data_by_route['Price'].max()

    if pd.isna(min_price):
        min_price = 0  
    if pd.isna(max_price):
        max_price = 1000  

    if min_price == max_price:
        max_price = min_price + 1  

    selected_price_range = slt.slider("💰 Select Price Range", 
                                      min_value=int(min_price), 
                                      max_value=int(max_price), 
                                      value=(int(min_price), int(max_price)))

    
    ratings = filtered_data_by_route['Ratings'].unique()
    selected_rating = slt.selectbox("⭐ Select Rating", ["All"] + ratings.tolist())

    if slt.button("🔍 Submit"):
        def query_bus_details(route_name, bus_name, bus_type, start_time, price_range, rating):
            filtered_data = df_redbus[df_redbus['Route_name'] == route_name].copy()

            if bus_name != "All":
                filtered_data = filtered_data[filtered_data['Bus_name'] == bus_name]

            if bus_type != "All":
                filtered_data = filtered_data[filtered_data['Bus_type'] == bus_type]
            
            if start_time != "All":
                filtered_data['Start_time'] = pd.to_datetime(filtered_data['Start_time'], format='%H:%M', errors='coerce')
                filtered_data.dropna(subset=['Start_time'], inplace=True)
                filtered_data['Start_time'] = filtered_data['Start_time'].dt.strftime('%I:%M %p')
                filtered_data = filtered_data[filtered_data['Start_time'] == start_time]

            
            filtered_data = filtered_data[
                (filtered_data['Price'] >= price_range[0]) & 
                (filtered_data['Price'] <= price_range[1])
            ]

            
            if rating != "All":
                filtered_data = filtered_data[filtered_data['Ratings'] == rating]

            return filtered_data

        df_result = query_bus_details(route, selected_bus_name, selected_bus_type, selected_start_time, selected_price_range, selected_rating)
        slt.dataframe(df_result)




# Bus Booking page:

elif web == "Bus Booking":
    slt.header("🚌 Bus Booking")

   
    state = slt.selectbox("🗺️ Select State", ["Andhra Pradesh", "Telangana", "Kerala", "Rajasthan", "Himachal", 
                                                 "Chandigarh", "South Bengal", "Uttar Pradesh", 
                                                 "Punjab", "West Bengal", "Bihar", "Assam"])

   
    route = slt.selectbox("📍 Select Route", get_routes(state))

    
    filtered_data_by_route = df_redbus[df_redbus['Route_name'] == route].copy()

   
    bus_names = filtered_data_by_route['Bus_name'].unique()
    selected_bus_name = slt.selectbox("🚌 Select Bus Name", bus_names.tolist())

   
    bus_details = filtered_data_by_route[filtered_data_by_route['Bus_name'] == selected_bus_name].iloc[0]
    slt.write("**Bus Details:**")
    slt.write(f"**Bus Type:** {bus_details['Bus_type']}")
    slt.write(f"**Price:** ₹{bus_details['Price']}")

   
    start_time = pd.to_datetime(bus_details['Start_time'], format='%H:%M', errors='coerce')
    if not pd.isna(start_time):
        start_time_formatted = start_time.strftime('%I:%M %p')  
        slt.write(f"**Departure Time:** {start_time_formatted}")
    else:
        slt.write("**Departure Time:** Not available")

    slt.write(f"**Ratings:** {bus_details['Ratings']}")

    
    slt.subheader("📝 Passenger Details")
    name = slt.text_input("Full Name")
    email = slt.text_input("Email Address")
    phone = slt.text_input("Phone Number")
    num_passengers = slt.number_input("Number of Passengers", min_value=1, max_value=10, value=1)

    if slt.button("Confirm Booking"):
        if not name or not email or not phone:
            slt.error("Please fill out all fields.")
        else:
            total_price = bus_details['Price'] * num_passengers
            slt.success(f"Booking confirmed for {num_passengers} passenger(s) on {selected_bus_name}.")
            slt.write(f"**Total Price:** ₹{total_price}")
            slt.write(f"**Passenger Name:** {name}")
            slt.write(f"**Contact Email:** {email}")
            slt.write(f"**Contact Phone:** {phone}")
            slt.write("Thank you for booking with us! 🚍")




# Terms and Conditions page:

if web == "Terms and Conditions":
    slt.title("📄 Terms and Conditions")
    slt.markdown("""
    ### 1. Booking Policy
    - All bookings are subject to availability.
    - Tickets once booked cannot be cancelled or transferred.
    - The bus operator reserves the right to cancel or modify the schedule without prior notice.

    ### 2. Refund Policy
    - No refunds will be provided in case of missed buses due to delay by the user.
    - Full refunds will only be provided if the bus service is canceled by the operator.

    ### 3. Luggage Policy
    - Passengers are responsible for their personal belongings.
    - Each passenger is allowed to carry up to 20 kg of luggage.

    ### 4. Travel Policy
    - Passengers must carry a valid ID card during travel.
    - Smoking, alcohol consumption, and carrying hazardous materials are strictly prohibited on board.

    ### 5. Responsibility Disclaimer
    - The bus operator will not be responsible for any delays due to unforeseen circumstances like traffic, weather, or roadblocks.
    - Any disputes arising are subject to the jurisdiction of the respective state.

    ### 6. User Agreement
    - By booking a bus ticket through this platform, you agree to these terms and conditions.
    """)
    slt.subheader("📋 Acknowledgement")
    agree = slt.checkbox("I agree to the Terms and Conditions")

    if agree:
        slt.success("Thank you for accepting the Terms and Conditions!")
    else:
        slt.warning("You must accept the Terms and Conditions to proceed.")




# FAQ page:

if web == "FAQ":
    slt.title("❓ Frequently Asked Questions (FAQ)")

     #Question 1
    slt.subheader ("1.What is Redbus Data Scraping with Selenium & Streamlit?") 
    slt.markdown("""This is a project that automates the extraction of bus route data from Redbus and provides a user-friendly interface for filtering and exploring the data.
                 """)
    
    #Question 2
    slt.subheader ("2.What states are supported? ")
    slt.markdown(""" The application currently supports bus routes from Andhra Pradesh, Telangana, Kerala, Rajasthan, Himachal Pradesh, Chandigarh, South Bengal, Uttar Pradesh, Punjab, West Bengal, Bihar, and Assam.
                 """)
    
    # Question 3
    slt.subheader("3.How do I book a bus ticket?")
    slt.markdown("""
    You can book a bus ticket by selecting the **Bus Booking** page from the menu. 
    Simply choose your **State**, **Route**, **Bus Type**, **Travel Date**, and the number of passengers.
    After reviewing the summary, click the **Done** button to complete your booking.
    """)
    
    # Question 4
    slt.subheader("4. Can I cancel or modify my bus booking?")
    slt.markdown("""
    Unfortunately, once a ticket is booked, it cannot be canceled or modified. Please make sure all details are correct before booking.
    """)
    
    # Question 5
    slt.subheader("5. How do I rate the bus service?")
    slt.markdown("""
    After selecting a bus for booking, you can rate the service using the rating slider provided during the booking process.
    The average rating of the bus service will be shown in the booking summary.
    """)
    
    # Question 6
    slt.subheader("6. What payment options are available?")
    slt.markdown("""
    Currently, this platform does not handle payments directly. It's designed to help users find bus routes and get relevant information. For payment, please visit the official Redbus website.
    """)
    
    # Question 7
    slt.subheader("7. What should I do if I miss my bus?")
    slt.markdown("""
    If you miss your bus, no refunds will be provided. Please ensure you arrive at the departure point early to avoid any inconvenience.
    """)
    
    # Question 8
    slt.subheader("8. How do I know if my bus is delayed or canceled?")
    slt.markdown("""
    You will be notified via email or SMS if there are any delays or cancellations. You can also contact the bus operator directly for real-time updates.
    """)

    #Question 9
    slt.subheader("9. Who developed this application?")
    slt.markdown(""" The application was developed by Shalini Raju as part of a project focusing on data scraping and visualization. """)
    
