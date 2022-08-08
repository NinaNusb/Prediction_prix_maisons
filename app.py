"""
Creating the app for the house prices prediction

"""

import pandas as pd
import streamlit as st
import numpy as np


df= pd.read_csv("data_cleaning_analysis.csv")



# Titre de la page
st.title('House Sales in King County, USA')

# zipcode
st.number_input("Entrez le code postal du quartier dans lequel vous cherchez une maison")
st.number_input()

st.subheader('Map of all neighborhoods')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [47.7776, -121.315],
    columns=['lat', 'lon'])

st.map(map_data)

# Nb chambres
bedrooms =  st.slider("Choisissez un nombre", 0, 10)

# Nb sdb
bathrooms =  st.slider("Choisissez un nombre", 0, 8)

# Sqft_living
sqft_living =  st.slider("Choisissez un nombre", 0, 13540)

# Sqft_lot
sqft_lot =  st.slider("Choisissez un nombre", 0, 1651359)

# floors
floors =  st.slider("Choisissez un nombre", 0, 3.5)

# Waterfront
waterfront = st.radio(
     "Voulez-vous être au bord de l'eau?",
     ('Oui', 'Non'))

if waterfront == 'Oui':
     st.write("Vous avez choisi d'être au bord de l'eau")
else:
     st.write("Vous ne souhaitez pas être au bord de l'eau")


# View
view = st.radio(
    "Choisissez le niveau de la vue",
    (1, 2, 3, 4)
)

# Condition
condition = st.radio(
    "Choisissez le niveau de la condition",
    (1, 2, 3, 4, 5)
)

# Grade
grade = st.slider("Choisissez un nombre", 0, 13)

# sqft_above
sqft_above = st.slider("Choisissez un nombre", 0, 9410)

# yr_built
yr_built = st.slider("Choisissez un nombre", 1900, 2015)

# yr_renovated
yr_renovated = st.write("Choisissez un nombre")

st.button("Trouver")