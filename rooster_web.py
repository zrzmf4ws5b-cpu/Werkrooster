import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="WerkRooster",
    page_icon="📅"
)
if "pagina" not in st.session_state:
    st.session_state.pagina = "start"
if st.session_state.pagina == "start":   
    st.markdown(
        "<h1 style='text-align:center;color:gold;'>WerkRooster</h1>",
        unsafe_allow_html=True
    )  
    st.image("logo.png", use_container_width=True)
    st.write("")
    st.write("") 
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    if st.button("Verder"):
        st.session_state.pagina = "login"
        st.rerun()     
elif st.session_state.pagina == "login": 
    st.subheader("🔐 Login")
    gebruikersnaam = st.text_input(
        "Gebruikersnaam"
    )
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
            (gebruikers["Naam"] == gebruikersnaam) &
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

