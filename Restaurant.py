import streamlit as st
import uuid
from datetime import datetime

# --------------------- CLASSES ---------------------
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, item):
        self.items.append(item)

    def clear_cart(self):
        self.items = []

    def total(self):
        return sum(item.price for item in self.items)

class Order:
    def __init__(self, user, items):
        self.order_id = str(uuid.uuid4())[:8]
        self.user = user
        self.items = items
        self.total = sum(item.price for item in items)
        self.time = datetime.now()

# --------------------- INIT DATA ---------------------
if "cart" not in st.session_state:
    st.session_state.cart = Cart()
    st.session_state.orders = []

# Restaurants
r1 = Restaurant("Pizza Hub")
r1.add_item(MenuItem("Pizza", 250))
r1.add_item(MenuItem("Cheese Pizza", 300))

r2 = Restaurant("Burger Point")
r2.add_item(MenuItem("Burger", 120))
r2.add_item(MenuItem("Paneer Burger", 180))

restaurants = [r1, r2]

# --------------------- UI ---------------------
st.title("🍽️ Food Delivery App")

name = st.text_input("Enter your name")
address = st.text_input("Enter your address")

# Select restaurant
res_names = [r.name for r in restaurants]
selected_res = st.selectbox("Select Restaurant", res_names)

# Get selected restaurant object
res_obj = next(r for r in restaurants if r.name == selected_res)

st.subheader("📋 Menu")

# Show menu with buttons
for item in res_obj.menu:
    col1, col2 = st.columns([3,1])
    col1.write(f"{item.name} - ₹{item.price}")
    if col2.button(f"Add {item.name}"):
        st.session_state.cart.add_to_cart(item)
        st.success(f"{item.name} added to cart")

# --------------------- CART ---------------------
st.subheader("🛒 Cart")

if st.session_state.cart.items:
    for item in st.session_state.cart.items:
        st.write(f"{item.name} - ₹{item.price}")

    st.write(f"### Total: ₹{st.session_state.cart.total()}")

    # Place order
    if st.button("Place Order ✅"):
        if name and address:
            order = Order(name, st.session_state.cart.items)
            st.session_state.orders.append(order)
            st.session_state.cart.clear_cart()

            st.success("🎉 Order Placed Successfully!")

            st.write("### 🧾 Order Details")
            st.write(f"Order ID: {order.order_id}")
            st.write(f"Name: {order.user}")
            st.write(f"Total: ₹{order.total}")
            st.write(f"Time: {order.time}")

            st.write("Items:")
            for i in order.items:
                st.write(f"- {i.name}")
        else:
            st.warning("Please enter name and address")

else:
    st.info("Cart is empty")

# --------------------- ORDER HISTORY ---------------------
st.subheader("📦 Order History")

if st.session_state.orders:
    for o in st.session_state.orders:
        st.write(f"🧾 {o.order_id} | ₹{o.total} | {o.time}")
else:
    st.write("No orders yet")