
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="WerkRooster",
    page_icon="📅"
    )
st.title("📅 WerkRooster")
st.write("Welkom in de webversie van WerkRooster")
gebruikersnaam = st.text_input("Gebruikersnaam")
wachtwoord = st.text_input(
    "Wachtwoord",
    type="password"
)
if st.button("Inloggen"):
    gebruikers = pd.read_excel(
        "rooster.xlsx",
        sheet_name="Gebruikers"
    )
    gebruiker = gebruikers.loc[
        (gebruikers["Naam"] == gebruikersnaam)&
        (gebruikers["Wachtwoord"] == wachtwoord)
    ]
    if not gebruiker.empty:
        st.success(
            f"Welkom {gebruikersnaam}"
        )
        rooster = pd.read_excel(
            "rooster.xlsx",
            sheet_name="Rooster"
        )
        medewerker = rooster.loc[
            rooster["Naam"] == gebruikersnaam
        ]
        st.subheader("📅 Mijn rooster") 
        st.write(f"Maandag: {medewerker.iloc[0]['Maandag']}")
        st.write(f"Dinsdag: {medewerker.iloc[0]['Dinsdag']}")
        st.write(f"Woensdag: {medewerker.iloc[0]['Woensdag']}")
        st.write(f"Donderdag: {medewerker.iloc[0]['Donderdag']}")
        st.write(f"Vrijdag: {medewerker.iloc[0]['Vrijdag']}")
    else:
        st.error(
            "Onjuiste gebruikersnaam of wachtwoord"
        )
