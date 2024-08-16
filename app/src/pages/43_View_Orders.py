import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()
orders_data = {}
'''
order_data = {}

def show_products(order_id):
    try:
        order_data = requests.get('http://api:4000/cl/customer/orders/{1}/products'.format(order_id)).json()
    except:
        st.write("No details available.")
        order_data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}
    for product in order_data:
        st.write(order_data['prod_name'] + ', Unit Price: $' + 
                 order_data['price'] + 'Amount Ordered: ' + order_data['quantity']) 
        #can add stuff to calculate total price
'''
def show_details(cust_id, order_id):
    try:
        orders_data = requests.get('http://api:4000/cl/customer/{0}/orders/{1}'.format(cust_id, order_id)).json()
    except:
        st.write("No details available.")
        orders_data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}
    st.write("Store Name: " + orders_data[0]['store_name']) #NOTE: need to use this weird syntax for accessing json elements
    st.write("Driver's Name: " + orders_data[0]['d_name'])  #     in response json

clicked = False
st.title("Your Orders:")

data = {}
try:
  data = requests.get('http://api:4000/cl/customer/{0}/orders'.format(st.session_state['customer_id'])).json()
  for order in data:
    c = st.container()
    
    c.write('Time placed: ' + order["time_created"])
    if order['time_fulfilled'] is None:
       c.write('Status: Not yet fulfilled')
    else:
       c.write('Status: fulfilled: ' + order['time_fulfilled'])
    c.write("Order ID: {0}".format(order['order_id']))
    if c.button('View Order Details'):
       show_details(st.session_state['customer_id'], order['order_id'])
    st.divider()
except:
  st.write("You have not placed any orders.")
  data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}



    
 
    




