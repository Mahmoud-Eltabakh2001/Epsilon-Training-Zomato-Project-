
import joblib
import numpy as np
import pandas as pd
import streamlit as st

model1=joblib.load("zomato.pkl")

def predict_zomato(name, online_order ,book_table ,votes ,rest_type ,approx_cost,
                   list_type ,city ,num_phone ,number_food_styles ):
    
                   prediction =model1.predict( pd.DataFrame({"name":[name],
                                             "online_order":[online_order],
                                             "book_table":[book_table],
                                             "votes":[votes],
                                             "rest_type":[rest_type],
                                             "approx_cost(for two people)":[approx_cost] ,
                                             "listed_in(type)":[list_type],
                                             "listed_in(city)":[city],
                                             "num_phone":[num_phone],
                                             "number_food_styles":[number_food_styles]},index=[1] ) )
                   if prediction[0]==1:
                      return "Good Resturant!"
                   else:
                      return "Bad Resturant!"

def main():
    
    st.set_page_config(layout="wide")
    html_temp = """
            <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">Zomato Resturant.</h2>
            </div>
                   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.title("")
    
    name=st.text_input("Enter name of Resturant")
    rest_type=st.text_input("Enter rest type") 
    city=st.text_input("Enter the city name" )

    num_phone=st.selectbox("Choose number of phones",[1,2,3,4,5])
    listed_type=st.selectbox("Choose the type of order",['Buffet','Cafes','Delivery','Desserts','Dine-out',
                                                         'Drinks & nightlife','Pubs and bars'])

    online_order=st.radio("Is there an online order",["Yes","No"],index=0)
    book_table=st.radio("Is there a table reservation",["Yes","No"],index=0)
    
    approx_cost=st.number_input("Enter approx cost for 2 persons",min_value=10,max_value=10000,step=10) 
    
    votes=st.slider("Enter the number of votes",min_value=0,max_value=20000,step=100)
    number_food_styles=st.slider("Choose number of food styles",min_value=1,max_value=8,step=1)

    result=""
    if st.button("Predict"):
        result=predict_zomato(name,online_order,book_table,votes,rest_type,approx_cost,listed_type,city,num_phone,number_food_styles)
        st.success("Expected Evaluation : {} ".format(result)) 

main()
