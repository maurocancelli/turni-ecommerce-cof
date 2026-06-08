import streamlit as st
import pandas as pd
import datetime
import os

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Pianificazione Turni - COF", layout="wide")
st.title("Pianificazione Mensile Reparto E-commerce")

# --- FILE DI SALVATAGGIO ---
FILE_ANAGRAFICA = "anagrafica_salvata.csv"

def salva_dati_su_file(df):
    st.session_state.df_anagrafica = df
    df.to_csv(FILE_ANAGRAFICA, index=False)

def pulisci_riposi(val):
    if pd.isna(val) or val is None or str(val).strip() == "": 
        return "Nessuno"
    return val

# --- INIZIALIZZAZIONE MEMORIA PERMANENTE ---
if 'df_anagrafica' not in st.session_state:
    if os.path.exists(FILE_ANAGRAFICA):
        df_caricato = pd.read_csv(FILE_ANAGRAFICA)
        df_caricato = df_caricato.where(pd.notnull(df_caricato), None)
        
        if "Dom Scorsa" in df_caricato.columns:
            df_caricato = df_caricato.drop(columns=["Dom Scorsa"])
            
        nuove_colonne = ["Malattia Fino Al", "Ferie W1", "Ferie W2", "Ferie W3"]
        for col in nuove_colonne:
            if col not in df_caricato.columns:
                df_caricato[col] = None
                
        if "Riposo 1" in df_caricato.columns:
            df_caricato["Riposo 1"] = df_caricato["Riposo 1"].apply(pulisci_riposi)
        if "Riposo 2" in df_caricato.columns:
            df_caricato["Riposo 2"] = df_caricato["Riposo 2"].apply(pulisci_riposi)
            
        st.session_state.df_anagrafica = df_caricato
    else:
        dati_base = [
            {"Nome": "MENDOZA MARVIN", "Contratto": "FT", "Squadra": 1, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MENDOZA MANUEL", "Contratto": "FT", "Squadra": 2, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "ALVES BRAGA ELAINE", "Contratto": "FT", "Squadra": 3, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "BULOSAN CRISTOPHER", "Contratto": "FT", "Squadra": 4, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "CAVALLARI CATERINA", "Contratto": "FT", "Squadra": 1, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "GAVAZZENI MICHELA", "Contratto": "FT", "Squadra": 2, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "CUARESMA FRANCESCO", "Contratto": "FT", "Squadra": 3, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "PERALTA BARBARA", "Contratto": "FT", "Squadra": 4, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "RICCARDI SIMONA", "Contratto": "FT", "Squadra": 1, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MABANTA MARIA", "Contratto": "FT", "Squadra": 2, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "PASCUA ARVIN", "Contratto": "FT", "Squadra": 3, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "TOCCHETTI CAMILLA", "Contratto": "FT", "Squadra": 4, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "SPEERING DAPHNI", "Contratto": "FT", "Squadra": 1, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "TANADA EUGENE", "Contratto": "FT", "Squadra": 2, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "CIPRIANO RUSSEL", "Contratto": "FT", "Squadra": 3, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "FELIX CARBUNGCAL", "Contratto": "FT", "Squadra": 4, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "GHITTI SARA", "Contratto": "FT", "Squadra": 1, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "BONO DANIELA", "Contratto": "FT", "Squadra": 2, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "TAN JONIMAE", "Contratto": "FT", "Squadra": 3, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "PETILUNA ROSARIO", "Contratto": "FT", "Squadra": 4, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MAGTIBAY LEA", "Contratto": "FT", "Squadra": 1, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MAGTIBAY BABYJANE", "Contratto": "FT", "Squadra": 2, "Riposo 1": "
