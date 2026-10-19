import streamlit as st
import pandas as pd
medewerkers = pd.read_excel(
    "rooster.xlsx",
    sheet_name="Medewerkers"
)

diensten = pd.read_excel(
    "rooster.xlsx",
    sheet_name="Diensten"
)

weken = pd.read_excel(
    "rooster.xlsx",
    sheet_name="Weken"
)


if "gebruiker" in st.session_state:

    medewerker_rij = medewerkers.loc[
        medewerkers["Naam"] == st.session_state.gebruiker
    ]

    



positie = int(medewerker_rij.iloc[0]["Positie"])

week_rij = weken.loc[
    weken["Week"] == st.session_state.week
]

verschuiving = int(
    week_rij.iloc[0]["Verschuiving"]
)

nieuwe_positie = positie + verschuiving

while nieuwe_positie > 5:
    nieuwe_positie = nieuwe_positie - 5



dienst_rij = diensten.loc[
    diensten["Positie"] == nieuwe_positie
]


dienst = dienst_rij.iloc[0]["Dienst"]
starttijd, eindtijd = dienst.split("-")
st.set_page_config(
    page_title="FlexPlan",
    page_icon="FlexPlan.png"
)
st.markdown("""
<style>
.stApp {
    background-color: #1f3b66;
}

label {
    color: gold !important;
    font-size: 20px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
div.stButton > button {
    background-color: gold;
    color: black;
    font-size: 14px;
    font-weight: bold;
    border-radius: 10px;
    height: 40px;
    width: 140px;
}
</style>
""", unsafe_allow_html=True)


if "pagina" not in st.session_state:
    st.session_state.pagina = "start"





if "week" not in st.session_state:
    st.session_state.week = 43







if st.session_state.pagina == "start":   
    st.markdown(
        "<h1 style='text-align:center;color:gold;'>FlexPlan</h1>",
        unsafe_allow_html=True
    )
    st.image("FlexPlan.png", width=700)
    st.write("")
    st.write("")
    st.write("")
    
    st.write("")
    st.write("") 
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    if st.button("Verder"):
        st.session_state.pagina = "login"
        st.rerun()
    if st.button("🚪 Afmelden"):
        st.session_state.clear()
        st.rerun()
elif st.session_state.pagina == "login": 
    if st.button("🔙 Terug"):

        st.session_state.pagina = "start"

        st.rerun()
    st.markdown(
    "<h1 style='text-align:center;color:gold;'>🔐 Login</h1>",
    unsafe_allow_html=True
    )
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

            st.session_state.gebruiker = gebruikersnaam
            st.session_state.pagina = "welkom"
            st.rerun()
         
        else:
            st.error(
                "Onjuiste gebruikersnaam of wachtwoord"
            )
elif st.session_state.pagina == "welkom":
    st.markdown(
        f"<h1 style='text-align:center;color:gold;'>👋 Welkom {st.session_state.gebruiker}</h1>",
            unsafe_allow_html=True
    
    )
    st.markdown(
        "<h3 style='text-align:center;color:white;'>Kies hieronder een actie</h3>",
        unsafe_allow_html=True
    )
    st.write("")
    st.write("")
    st.write("")  
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:

        if st.button("📅 Mijn rooster"):
            st.session_state.pagina = "rooster"
            st.rerun()
        

        if st.button("💼 Vacatures"):
            st.session_state.pagina = "vacatures"
            st.rerun()
        if st.button("🚪 Afmelden"):
            st.session_state.pagina = "start"
            st.rerun()
elif st.session_state.pagina == "rooster":

    st.markdown(
        "<h1 style='text-align:center;color:gold;'>📅 Mijn rooster</h1>",
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        f"""
        <div style=" 
            background-color:#4A86E8;
            color:white;
            padding:25px;
            border-radius:15px;
            text-align:center;
            font-size:24px;
            font-weight:bold;">
            📅 Vandaag<br><br>
            Maandag 19 oktober 2026<br><br>
            
            🕒 Start: {starttijd} 
            🕒 Eind: {eindtijd}
            📍 Amstel 1
            👥 4 collega's
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📂 Open dienst"):
            st.session_state.dag = "Maandag"
            st.session_state.pagina = "dagdetail"
            st.rerun()

    with col2:
        if st.button("📅 Weekroosters"):
            st.session_state.pagina = "weekselectie"
            st.rerun()

    with col3:
        if st.button("🔙 Terug"):
            st.session_state.pagina = "welkom"
            st.rerun()
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

elif st.session_state.pagina == "weekselectie":

        st.markdown(
            "<h1 style='text-align:center;color:gold;'>📅 Selecteer week</h1>",
            unsafe_allow_html=True
        )

        if st.button("Week 43"):
            st.session_state.week = 43
            st.session_state.pagina = "weekrooster"
            st.rerun()

        if st.button("Week 44"):
            st.session_state.week = 44
            st.session_state.pagina = "weekrooster"
            st.rerun()

        if st.button("Week 45"):
            st.session_state.week = 45
            st.session_state.pagina = "weekrooster"
            st.rerun()

        if st.button("🔙 Terug"):
            st.session_state.pagina = "rooster"
            st.rerun()
    
elif st.session_state.pagina == "weekrooster":
    st.write("Gekozen week:", st.session_state.week)
    
    st.markdown(
        "<h1 style='text-align:center;color:gold;'>📅 Weekrooster</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h3 style='text-align:center;color:white;'>week {st.session_state.week}</h3>",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("""
        <div style="
            background-color:#4A86E8;
            color:white;
            padding:15px;
            border-radius:10px;
            text-align:center;
            font-weight:bold;">
            Ma<br><br>
            14:30<br>
            22:30
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background-color:#2ECC71;
            color:white;
            padding:15px;
            border-radius:10px;
            text-align:center;
            font-weight:bold;">
            Di<br><br>
            14:30<br>
            22:30
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background-color:#F39C12;
            color:white;
            padding:15px;
            border-radius:10px;
            text-align:center;
            font-weight:bold;">
            Wo<br><br>
            14:30<br>
            22:30
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="
            background-color:#E74C3C;
            color:white;
            padding:15px;
            border-radius:10px;
            text-align:center;
            font-weight:bold;">
            Do<br><br>
            14:30<br>
            22:30
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div style="
            background-color:#3498DB;
            color:white;
            padding:15px;
            border-radius:10px;
            text-align:center;
            font-weight:bold;">
            Vr<br><br>
            14:30<br>
            22:30
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("🔙 Terug naar rooster"):
        st.session_state.pagina = "rooster"
        st.rerun()


elif st.session_state.pagina == "dagdetail":    

    st.markdown(
        f"<h1 style='text-align:center;color:gold;'>📅 {st.session_state.dag}</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div style='background-color:#4A86E8;color:white;padding:20px;border-radius:10px;font-size:24px;font-weight:bold;'>🕒 Dienst<br>{starttijd} - {eindtijd}</div>",
        unsafe_allow_html=True
   
    )

    st.write("")

    st.markdown(
    "<div style='background-color:#2ECC71;color:white;padding:20px;border-radius:10px;font-size:24px;font-weight:bold;'>📍 Locatie<br>Amstel 1 - Waterlooplein 6</div>",
    unsafe_allow_html=True
    )
    st.write("")

    st.markdown(
        """
    "<div style='background-color:#F39C12;color:white;padding:20px;border-radius:10px;font-size:24px;font-weight:bold;'>👥 Collega's<br><br>
    Jay - 10:00-18:00<br>
    Piento - 12:30-20:30<br>
    Dre - 16:30-23:30<br>
    Borsoe - 16:00-23:30
    </div>
    """,
    unsafe_allow_html=True
    )
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([3,1,3])

    with col2:
        if st.button("🔙 Terug"):
            st.session_state.pagina = "rooster"
            st.rerun()
    
