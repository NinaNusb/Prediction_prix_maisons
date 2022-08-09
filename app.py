"""
Creating the app for the house prices prediction

"""

import pandas as pd
import streamlit as st
import numpy as np
import pickle

with open("pickle_model.pkl", 'rb') as file:
    model = pickle.load(file)


# Titre de la page
st.title('House Sales in King County, USA')

#Header
st.header("Vous cherchez une maison dans la ville de Seattle? Ajustez les paramètres ci-dessous pour découvrir la prédiction de votre future maison.")

# zipcode
st.subheader('Code postal')
zipcode = st.number_input("Entrez le code postal du quartier dans lequel vous cherchez une maison", 98001, 98100)

st.subheader('Carte de tous les quartiers')
df1 = pd.read_csv('kc_house_data.csv')
df1['lon'] = df1['long']
columns=['latitude', 'longitude']
st.map(df1)

# Nb chambres
st.subheader('Nombre de chambre')
bedrooms =  st.slider("Choisissez un nombre", 0, 10)
st.text('Sélection: {}'.format(bedrooms))

# Nb sdb
st.subheader('Nombre de salle-de-bains')
bathrooms =  st.slider("Choisissez un nombre", 0, 8) 
st.text('Sélection: {}'.format(bathrooms))
# [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5]

# floors
st.subheader("Nombre d'étages")
floors =  st.selectbox("Choisissez un nombre", [0, 1, 1.5, 2, 2.5, 3, 3.5])
st.write("Vous avez choisi ", floors, " étages")

# Condition
st.subheader("Qualité intérieure")
condition = st.radio(
    "Choisissez le niveau de la condition",
    (1, 2, 3, 4, 5)
)

# Grade
st.subheader("Qualité de la structure")
grade = st.slider("Choisissez un nombre", 0, 13)


# Sqft_living
st.subheader('Surface habitable en pieds carrés')
sqft_living =  st.slider("Choisissez un nombre", 0, 13540)
st.text('Sélection: {}'.format(sqft_living))

# Sqft_lot
st.subheader('Surface du terrain en pieds carrés')
sqft_lot =  st.slider("Choisissez un nombre", 0, 1651359)
st.text('Sélection: {}'.format(sqft_lot))

# Waterfront
st.subheader("Proximité à l'eau")
waterfront = st.radio(
     "Voulez-vous être au bord de l'eau?",
     ('Oui', 'Non'))


if waterfront == 'Oui':
    waterfront = 1
    st.write("Vous avez choisi d'être au bord de l'eau")
else:
    waterfront = 0
    st.write("Vous ne souhaitez pas être au bord de l'eau")

# View
st.subheader("Qualité de la vue")
view = st.radio(
    "Choisissez le niveau de la vue",
    (1, 2, 3, 4)
)

# yr_built
st.subheader("Année de construction")
yr_built = st.slider("Choisissez un nombre", 1900, 2015)

# yr_renovated
st.subheader("Année de rénovation")
st.text("Si vous ne souhaitez pas de maison rénovée, indiquez 0")
yr_renovated = st.number_input("Choisissez un nombre", 0,2015)

variables= [bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, int(yr_built), int(yr_renovated), str(zipcode)]

colonnes = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
       'waterfront', 'view', 'condition', 'grade', 'yr_built',
       'yr_renovated', 'zipcode']

prediction = pd.DataFrame(np.array(variables).reshape(1,-1), columns=colonnes)

# Trouver la prédiction
if(st.button("Estimer")):
    prix = int(model.predict(prediction))
    st.write("Résumé des paramètres", prediction)
    st.success("La prédiction est de: {} $".format(prix))