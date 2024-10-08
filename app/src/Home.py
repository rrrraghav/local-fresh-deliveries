##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################



# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)



# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('Local Fresh Deliveries')
st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

if st.button("Act as Steve, a Customer", 
            type = 'primary', 
            use_container_width=True):
    # when user clicks the button, they are now considered authenticated
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'customer'
    st.session_state['first_name'] = 'Steve' 
    st.session_state['customer_id'] = 1 # Sample insert Steve persona id
    # Variables to support order processing
    st.session_state['has_order'] = False 

    st.session_state['current_order_id'] = -2; # starts with no order
    st.session_state['order_button_id'] = 0
    
    logger.info("Logging in as Customer")
    st.switch_page('pages/40_Customer_Home.py')

if st.button('Act as Milly, a Data Analyst', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'analyst'
    st.session_state['first_name'] = 'Milly'
    st.session_state['id'] = 1
    logger.info('Logging in as analyst')
    st.switch_page('pages/10_Analyst_Home.py')

if st.button('Act as Max, a Fisherman', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'store'
    st.session_state['first_name'] = 'Max'
    
    logger.info('Logging in as store')
    st.switch_page('pages/20_Store_Home.py')

if st.button('Act as Rooney, a Delivery Driver', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'driver'
    st.session_state['first_name'] = 'Rooney'
    st.session_state['driver_id'] = 1
    st.session_state['order_id'] = 30
    logger.info('Logging in as driver')
    st.switch_page('pages/30_Driver_Home.py')



