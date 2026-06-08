import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Pianificazione Turni - COF", layout="wide")
st.title("Pianificazione Mensile Reparto E-commerce")

# --- 1. INIZIALIZZAZIONE MEMORIA (SESSION STATE) ---
# Se l'app viene aperta per la prima volta, carica un'anagrafica di base
if 'df_anagrafica' not in st.session_state:
    dati_base = [
        {"Nome": "Nikita D.", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": True},
        {"Nome": "Mia", "Contratto": "PT", "Squadra": 2, "Riposo 1": "Martedì", "Riposo 2": "Mercoledì", "Dom Scorsa": False},
        {"Nome": "Operatore 3", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
        {"Nome": "Operatore 4", "Contratto": "PT", "Squadra": 4, "Riposo 1": "Lunedì", "Riposo 2": "Giovedì", "Dom Scorsa": True},
    ]
    st.session_state.df_anagrafica = pd.DataFrame(dati_base)

# Variabili globali utili
GIORNI = ["Domenica", "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
OPZIONI_TURNO = ["06:00-13:00", "12:30-19:30", "13:00-20:00", "RIPOSO", "MALATTIA", "FERIE", "PERMESSO"]

# --- CREAZIONE DELLE DUE SCHEDE PRINCIPALI ---
tab_anagrafica, tab_turni = st.tabs(["1. Gestione Anagrafica", "2. Generazione Turni"])

# ==========================================
# SCHEDA 1: GESTIONE ANAGRAFICA DINAMICA
# ==========================================
with tab_anagrafica:
    st.subheader("Anagrafica Personale")
    st.write("Aggiungi, elimina o modifica i dipendenti. Ricordati di cliccare 'Salva Anagrafica' prima di generare i turni.")
    
    # Configurazione delle colonne per evitare errori di inserimento
    config_anagrafica = {
        "Contratto": st.column_config.SelectboxColumn("Contratto", options=["FT", "PT"], required=True),
        "Squadra": st.column_config.NumberColumn("Squadra", min_value=1, max_value=4, step=1, required=True),
        "Riposo 1": st.column_config.SelectboxColumn("Riposo 1 (PT)", options=GIORNI[1:]),
        "Riposo 2": st.column_config.SelectboxColumn("Riposo 2 (PT)", options=GIORNI[1:]),
        "Dom Scorsa": st.column_config.CheckboxColumn("Lavorato Domenica Scorsa?")
    }

    # Tabella editabile (puoi aggiungere righe dinamicamente)
    df_anagrafica_modificata = st.data_editor(
        st.session_state.df_anagrafica,
        column_config=config_anagrafica,
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True
    )

    if st.button("Salva Anagrafica", type="primary"):
        st.session_state.df_anagrafica = df_anagrafica_modificata
        st.success("Anagrafica aggiornata con successo! Ora puoi passare alla scheda 'Generazione Turni'.")


# ==========================================
# SCHEDA 2: GENERAZIONE TURNI E PRODUTTIVITÀ
# ==========================================
with tab_turni:
    # --- LOGICHE DI SUPPORTO ---
    def determina_turno_base(squadra, numero_settimana):
        ciclo = numero_settimana % 4
        if ciclo == 1 or ciclo == 3: return "06:00-13:00"
        elif ciclo == 2: return "12:30-19:30"
        else: return "13:00-20:00"

    def colora_celle(valore):
        if valore == "MALATTIA": return "background-color: #ffcccc; color: #cc0000; font-weight: bold;"
        elif valore == "FERIE": return "background-color: #ffe6cc; color: #cc6600; font-weight: bold;"
        elif valore == "PERMESSO": return "background-color: #e6f2ff; color: #0066cc;"
        elif valore == "RIPOSO": return "background-color: #f2f2f2; color: #7f7f7f;"
        elif "06:00" in str(valore): return "background-color: #e6ffed; color: #1a7f37;"
        elif "12:30" in str(valore) or "13:00" in str(valore): return "background-color: #fbefff; color: #8250df;"
        return ""

    # --- SIDEBAR: PARAMETRI ---
    st.sidebar.header("Parametri Operativi")
    data_inizio = st.sidebar.date_input("Lunedì di inizio pianificazione", datetime.date.today())
    week_partenza = data_inizio.isocalendar()[1]
    pezzi_ora = st.sidebar.number_input("Pezzi/Ora (Default):", value=100)

    st.sidebar.subheader("Forza Lavoro Richiesta (%)")
    target_copertura = {}
    default_pct = [45, 90, 75, 75, 75, 90, 90]
    for g, default in zip(GIORNI, default_pct):
        target_copertura[g] = st.sidebar.slider(g, 0, 100, default) / 100

    # --- MOTORE ALGORITMICO ---
    def genera_tabellone_settimana(numero_settimana, mem_domeniche):
        tabellone = []
        dati_dipendenti = st.session_state.df_anagrafica.to_dict('records')
        
        for dip in dati_dipendenti:
            # Salta righe vuote inserite per sbaglio
            if not dip["Nome"]: continue 
            
            turno_base = determina_turno_base(dip["Squadra"], numero_settimana)
            riga = {"Dipendente": dip["Nome"], "Contratto": dip["Contratto"], "Squadra": dip["Squadra"]}
            
            # Gestione Domenica
            ha_lavorato_scorsa = mem_domeniche.get(dip["Nome"], False)
            if ha_lavorato_scorsa:
                riga["Domenica"] = "RIPOSO"
            else:
                riga["Domenica"] = "06:00-13:00"
                
            # Gestione Feriali (Lunedì-Sabato)
            for giorno in GIORNI[1:]:
                if dip["Contratto"] == "PT":
                    riposi_fissi = [dip["Riposo 1"], dip["Riposo 2"]]
                    if riga["Domenica"] == "RIPOSO" and giorno in riposi_fissi:
                        altro_riposo = riposi_fissi[1] if giorno == riposi_fissi[0] else riposi_fissi[0]
                        if target_copertura.get(giorno, 0) <= target_copertura.get(altro_riposo, 0):
                            riga[giorno] = "RIPOSO"
                        else:
                            riga[giorno] = turno_base
                    elif riga["Domenica"] != "RIPOSO" and giorno in riposi_fissi:
                        riga[giorno] = "RIPOSO"
                    else:
                        riga[giorno] = turno_base
                else:
                    riga[giorno] = turno_base # FT temporaneo
                    
            tabellone.append(riga)
            
        df = pd.DataFrame(tabellone)
        
        # Ottimizzazione Riposi FT
        giorni_ordinati = sorted(GIORNI[1:], key=lambda x: target_copertura[x])
        if not df.empty:
            for index, row in df.iterrows():
                if row["Contratto"] == "FT":
                    for g_riposo in giorni_ordinati:
                        df.at[index, g_riposo] = "RIPOSO"
                        break
                    
        return df

    # --- GENERAZIONE MENSILE A SCHEDE (WEEK) ---
    tabs_week = st.tabs([f"Week {week_partenza + i}" for i in range(4)])
    
    # Prepara la memoria iniziale delle domeniche leggendo dall'anagrafica salvata
    memoria_dom = {}
    for index, row in st.session_state.df_anagrafica.iterrows():
        if row["Nome"]: memoria_dom[row["Nome"]] = row["Dom Scorsa"]

    config_colonne_turni = {g: st.column_config.SelectboxColumn(g, options=OPZIONI_TURNO) for g in GIORNI}

    for i, t_week in enumerate(tabs_week):
        week_corrente = week_partenza + i
        with t_week:
            if st.session_state.df_anagrafica.empty:
                st.warning("Inserisci prima i dipendenti nell'Anagrafica.")
            else:
                st.subheader(f"Modifica Turni - Settimana {week_corrente}")
                
                # Genera Tabellone
                df_calcolato = genera_tabellone_settimana(week_corrente, memoria_dom)
                
                # Editor Interattivo
                df_modificato = st.data_editor(
                    df_calcolato, 
                    column_config=config_colonne_turni, 
                    use_container_width=True, 
                    hide_index=True, 
                    key=f"editor_w{week_corrente}"
                )
                
                # Anteprima Colorata
                st.write("**Vista Visiva Assenze e Copertura:**")
                st.dataframe(df_modificato.style.map(colora_celle), use_container_width=True)
                
                # Calcolo Produttività
                report = []
                for g in GIORNI:
                    is_mattina = df_modificato[g] == "06:00-13:00"
                    is_pome = df_modificato[g].isin(["12:30-19:30", "13:00-20:00"])
                    op_m = df_modificato[is_mattina][g].count() if not df_modificato.empty else 0
                    op_p = df_modificato[is_pome][g].count() if not df_modificato.empty else 0
                    
                    report.append({
                        "Giorno": g, 
                        "Op. Mattina": op_m, 
                        "Op. Pomeriggio": op_p, 
                        "Pezzi Previsti": (op_m + op_p) * 7 * pezzi_ora
                    })
                    
                st.write("**Stima Volumi Giornalieri (Escluse Assenze):**")
                st.dataframe(pd.DataFrame(report).set_index("Giorno").T)
                
                # Aggiorna memoria domeniche per la settimana successiva
                for nome in memoria_dom:
                    memoria_dom[nome] = not memoria_dom[nome]
