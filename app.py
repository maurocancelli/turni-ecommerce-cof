import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Pianificazione Turni E-commerce COF", layout="wide")
st.title("Pianificazione Mensile Reparto E-commerce")

# --- ANAGRAFICA DI ESEMPIO ---
if 'dipendenti' not in st.session_state:
    st.session_state.dipendenti = [
        {"id": 1, "nome": "Nikita D.", "contratto": "FT", "squadra": 1, "riposo_1": None, "riposo_2": None, "lavorato_dom_scorsa": True},
        {"id": 2, "nome": "Mia", "contratto": "PT", "squadra": 2, "riposo_1": "Martedì", "riposo_2": "Mercoledì", "lavorato_dom_scorsa": False},
        {"id": 3, "nome": "Operatore 3", "contratto": "FT", "squadra": 3, "riposo_1": None, "riposo_2": None, "lavorato_dom_scorsa": False},
        {"id": 4, "nome": "Operatore 4", "contratto": "PT", "squadra": 4, "riposo_1": "Lunedì", "riposo_2": "Giovedì", "lavorato_dom_scorsa": True},
    ]

# --- OPZIONI E VARIABILI GLOBALI ---
GIORNI = ["Domenica", "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
OPZIONI_TURNO = ["06:00-13:00", "12:30-19:30", "13:00-20:00", "RIPOSO", "MALATTIA", "FERIE", "PERMESSO"]

def determina_turno_base(squadra, numero_settimana):
    """Calcola il turno base per la settimana lavorativa con ciclo a 4 (Modulo 4)"""
    ciclo = numero_settimana % 4
    if ciclo == 1 or ciclo == 3:
        return "06:00-13:00"
    elif ciclo == 2:
        return "12:30-19:30"
    else:
        return "13:00-20:00"

def colora_celle(valore):
    if valore == "MALATTIA": return "background-color: #ffcccc; color: #cc0000; font-weight: bold;"
    elif valore == "FERIE": return "background-color: #ffe6cc; color: #cc6600; font-weight: bold;"
    elif valore == "RIPOSO": return "background-color: #f2f2f2; color: #7f7f7f;"
    elif "06:00" in str(valore): return "background-color: #e6ffed; color: #1a7f37;"
    elif "12:30" in str(valore) or "13:00" in str(valore): return "background-color: #fbefff; color: #8250df;"
    return ""

# --- SIDEBAR: PARAMETRI E FORZA LAVORO ---
st.sidebar.header("Parametri Operativi")
data_inizio = st.sidebar.date_input("Lunedì di inizio pianificazione", datetime.date.today())
week_partenza = data_inizio.isocalendar()[1]
pezzi_ora = st.sidebar.number_input("Pezzi/Ora per operatore (Default):", value=100)

st.sidebar.subheader("Forza Lavoro Richiesta (%)")
target_copertura = {}
default_pct = [45, 90, 75, 75, 75, 90, 90]
for g, default in zip(GIORNI, default_pct):
    target_copertura[g] = st.sidebar.slider(g, 0, 100, default) / 100

# --- MOTORE ALGORITMICO ---
def genera_tabellone_settimana(numero_settimana, mem_domeniche):
    tabellone = []
    
    for dip in st.session_state.dipendenti:
        turno_base = determina_turno_base(dip["squadra"], numero_settimana)
        riga = {"Dipendente": dip["nome"], "Contratto": dip["contratto"], "Squadra": dip["squadra"]}
        
        # 1. Gestione Domenica
        ha_lavorato_scorsa = mem_domeniche.get(dip["nome"], False)
        if ha_lavorato_scorsa:
            riga["Domenica"] = "RIPOSO"
        else:
            riga["Domenica"] = "06:00-13:00"
            
        # 2. Gestione Feriali (Lunedì-Sabato)
        for giorno in GIORNI[1:]:
            if dip["contratto"] == "PT":
                riposi_fissi = [dip["riposo_1"], dip["riposo_2"]]
                # Logica ottimizzazione PT se la domenica è di riposo
                if riga["Domenica"] == "RIPOSO" and giorno in riposi_fissi:
                    altro_riposo = riposi_fissi[1] if giorno == riposi_fissi[0] else riposi_fissi[0]
                    # Consuma il riposo nel giorno con MENO carico richiesto
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
    
    # 3. Ottimizzazione Riposi FT
    giorni_ordinati = sorted(GIORNI[1:], key=lambda x: target_copertura[x])
    for index, row in df.iterrows():
        if row["Contratto"] == "FT":
            for g_riposo in giorni_ordinati:
                df.at[index, g_riposo] = "RIPOSO"
                break
                
    return df

# --- GENERAZIONE MENSILE (A SCHEDE) ---
tabs = st.tabs([f"Week {week_partenza + i}" for i in range(4)])
memoria_dom = {d["nome"]: d["lavorato_dom_scorsa"] for d in st.session_state.dipendenti}

config_colonne = {g: st.column_config.SelectboxColumn(g, options=OPZIONI_TURNO) for g in GIORNI}

for i, tab in enumerate(tabs):
    week_corrente = week_partenza + i
    with tab:
        st.subheader(f"Pianificazione Settimana {week_corrente}")
        
        # Genera
        df_calcolato = genera_tabellone_settimana(week_corrente, memoria_dom)
        
        # Editor Interattivo
        df_modificato = st.data_editor(df_calcolato, column_config=config_colonne, use_container_width=True, hide_index=True, key=f"editor_w{week_corrente}")
        
        # Anteprima Colorata
        st.dataframe(df_modificato.style.map(colora_celle), use_container_width=True)
        
        # Calcolo Produttività
        report = []
        for g in GIORNI:
            is_mattina = df_modificato[g] == "06:00-13:00"
            is_pome = df_modificato[g].isin(["12:30-19:30", "13:00-20:00"])
            op_m = df_modificato[is_mattina][g].count()
            op_p = df_modificato[is_pome][g].count()
            
            report.append({
                "Giorno": g, "Op. Mattina": op_m, "Op. Pomeriggio": op_p, 
                "Pezzi Previsti": (op_m + op_p) * 7 * pezzi_ora
            })
            
        st.write("**Stima Volumi (Esclusi Riposi/Malattie/Ferie):**")
        st.dataframe(pd.DataFrame(report).set_index("Giorno").T)
        
        # Aggiorna memoria domeniche per la settimana successiva
        for nome in memoria_dom:
            memoria_dom[nome] = not memoria_dom[nome]

# --- ESPORTAZIONE ---
st.divider()
if st.button("Esporta su Google Fogli (Week selezionate)"):
    st.info("Per abilitare l'esportazione reale, inserire qui le credenziali gspread (service_account.json) e attivare le API di Google Sheets.")
    # Esempio di logica di esportazione trattata in precedenza
