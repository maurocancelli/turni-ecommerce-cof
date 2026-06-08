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
    if pd.isna(val) or val is None or str(val).strip() == "": return "Nessuno"
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
            {"Nome": "MAGTIBAY BABYJANE", "Contratto": "FT", "Squadra": 2, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "DONGHI NIKITA", "Contratto": "FT", "Squadra": 3, "Riposo 1": "Nessuno", "Riposo 2": "Nessuno", "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
        ]
        df_iniziale = pd.DataFrame(dati_base)
        salva_dati_su_file(df_iniziale)

# Vettori di riferimento per i giorni
GIORNI_BASE = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
GIORNI_8_KEYS = ["Dom_P", "Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom_S"]
OFFSETS = [-1, 0, 1, 2, 3, 4, 5, 6]
OPZIONI_TURNO = ["06:00-13:00", "12:30-19:30", "13:00-20:00", "RIPOSO", "MALATTIA", "FERIE", "PERMESSO"]
APPROV_GIORNI = {"Dom_P": "Dom", "Lun": "Lun", "Mar": "Mar", "Mer": "Mer", "Gio": "Gio", "Ven": "Ven", "Sab": "Sab", "Dom_S": "Dom"}

# --- CREAZIONE SCHEDE PRINCIPALI ---
tab_anagrafica, tab_turni = st.tabs(["📋 1. Gestione Anagrafica", "📅 2. Generazione Turni"])

# ==========================================
# SCHEDA 1: GESTIONE ANAGRAFICA
# ==========================================
with tab_anagrafica:
    col_add, col_del = st.columns(2)
    with col_add:
        st.subheader("➕ Aggiungi un nuovo dipendente")
        with st.container(border=True):
            nuovo_nome = st.text_input("Nome e Cognome")
            nuovo_contratto = st.selectbox("Tipo Contratto", ["FT", "PT"])
            nuova_squadra = st.selectbox("Squadra di appartenenza", [1, 2, 3, 4])
            nuovo_r1 = st.selectbox("Riposo Fisso 1 (Solo PT)", ["Nessuno"] + GIORNI_BASE[:-1])
            nuovo_r2 = st.selectbox("Riposo Fisso 2 (Solo PT)", ["Nessuno"] + GIORNI_BASE[:-1])
                
            if st.button("Aggiungi all'Anagrafica", use_container_width=True):
                if nuovo_nome.strip() == "":
                    st.error("Inserisci un nome valido!")
                else:
                    nuova_riga = {
                        "Nome": nuovo_nome.upper(),
                        "Contratto": nuovo_contratto,
                        "Squadra": nuova_squadra,
                        "Riposo 1": nuovo_r1 if nuovo_contratto == "PT" else "Nessuno",
                        "Riposo 2": nuovo_r2 if nuovo_contratto == "PT" else "Nessuno",
                        "Malattia Fino Al": None,
                        "Ferie W1": None, "Ferie W2": None, "Ferie W3": None
                    }
                    nuovo_df = pd.concat([st.session_state.df_anagrafica, pd.DataFrame([nuova_riga])], ignore_index=True)
                    salva_dati_su_file(nuovo_df)
                    st.success(f"✅ {nuovo_nome.upper()} aggiunto correttamente!")
                    st.rerun()

    with col_del:
        st.subheader("🗑️ Rimuovi un dipendente")
        with st.container(border=True):
            lista_nomi = st.session_state.df_anagrafica["Nome"].tolist()
            nome_da_eliminare = st.selectbox("Scegli chi eliminare:", ["Nessuno..."] + lista_nomi)
            
            if st.button("Elimina Dipendente", type="primary", use_container_width=True):
                if nome_da_eliminare != "Nessuno...":
                    nuovo_df = st.session_state.df_anagrafica[st.session_state.df_anagrafica["Nome"] != nome_da_eliminare]
                    salva_dati_su_file(nuovo_df)
                    st.success(f"❌ {nome_da_eliminare} rimosso dalla lista.")
                    st.rerun()

    st.divider()

    st.subheader("👥 Lista Attuale Personale e Assenze Programmate")
    if "Malattia Fino Al" in st.session_state.df_anagrafica.columns:
        st.session_state.df_anagrafica["Malattia Fino Al"] = pd.to_datetime(st.session_state.df_anagrafica["Malattia Fino Al"]).dt.date
    
    config_anagrafica = {
        "Contratto": st.column_config.SelectboxColumn("Contratto", options=["FT", "PT"], required=True),
        "Squadra": st.column_config.NumberColumn("Squadra", min_value=1, max_value=4, step=1, required=True),
        "Riposo 1": st.column_config.SelectboxColumn("Riposo 1 (PT)", options=["Nessuno"] + GIORNI_BASE[:-1]),
        "Riposo 2": st.column_config.SelectboxColumn("Riposo 2 (PT)", options=["Nessuno"] + GIORNI_BASE[:-1]),
        "Malattia Fino Al": st.column_config.DateColumn("Malattia Fino Al", format="DD/MM/YYYY"),
        "Ferie W1": st.column_config.NumberColumn("Ferie W1 (N. Set)"),
        "Ferie W2": st.column_config.NumberColumn("Ferie W2 (N. Set)"),
        "Ferie W3": st.column_config.NumberColumn("Ferie W3 (N. Set)")
    }
    
    df_editato = st.data_editor(
        st.session_state.df_anagrafica,
        column_config=config_anagrafica,
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True
    )

    if st.button("💾 Salva Modifiche Anagrafica", type="primary", use_container_width=True):
        salva_dati_su_file(df_editato)
        st.success("✅ Dati anagrafici e assenze aggiornati correttamente!")

# ==========================================
# SCHEDA 2: GENERAZIONE TURNI E PRODUTTIVITÀ
# ==========================================
with tab_turni:
    def determina_turno_base(squadra, numero_settimana):
        ciclo = numero_settimana % 4
        if ciclo == 0: 
            if squadra in [1, 2]: return "06:00-13:00"
            elif squadra == 3: return "13:00-20:00"
            elif squadra == 4: return "12:30-19:30"
        elif ciclo == 1: 
            if squadra == 1: return "12:30-19:30"
            elif squadra == 2: return "13:00-20:00"
            elif squadra in [3, 4]: return "06:00-13:00"
        elif ciclo == 2: 
            if squadra in [1, 2]: return "06:00-13:00"
            elif squadra == 3: return "12:30-19:30"
            elif squadra == 4: return "13:00-20:00"
        else: 
            if squadra == 1: return "13:00-20:00"
            elif squadra == 2: return "12:30-19:30"
            elif squadra in [3, 4]: return "06:00-13:00"

    def colora_celle(valore):
        if valore == "MALATTIA": return "background-color: #ffcccc; color: #cc0000; font-weight: bold;"
        elif valore == "FERIE": return "background-color: #ffe6cc; color: #cc6600; font-weight: bold;"
        elif valore == "PERMESSO": return "background-color: #e6f2ff; color: #0066cc;"
        elif valore == "RIPOSO": return "background-color: #f2f2f2; color: #7f7f7f;"
        elif "06:00" in str(valore): return "background-color: #e6ffed; color: #1a7f37;"
        elif "12:30" in str(valore) or "13:00" in str(valore): return "background-color: #fbefff; color: #8250df;"
        return ""

    st.sidebar.header("Parametri Operativi")
    data_inizio = st.sidebar.date_input("Lunedì di inizio visualizzazione", datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday()))
    week_partenza = data_inizio.isocalendar()[1]
    anno_partenza = data_inizio.isocalendar()[0]
    pieces_ora = st.sidebar.number_input("Pezzi/Ora (Default):", value=100)

    st.sidebar.subheader("Forza Lavoro Richiesta (%)")
    target_copertura = {}
    default_pct = [45, 90, 75, 75, 75, 90, 90, 45] # Dom_P, Lun, Mar, Mer, Gio, Ven, Sab, Dom_S
    for key, default in zip(GIORNI_8_KEYS, default_pct):
        target_copertura[key] = st.sidebar.slider(f"{key}", 0, 100, default) / 100

    def genera_tabellone_settimana(numero_settimana, data_lunedi, mem_domeniche):
        tabellone = []
        dati_dipendenti = st.session_state.df_anagrafica.to_dict('records')
        totale_dipendenti = len([d for d in dati_dipendenti if d.get("Nome") and str(d.get("Nome")).strip() != ""])
        
        for dip in dati_dipendenti:
            if not dip.get("Nome") or str(dip.get("Nome")).strip() == "": continue 
            
            settimane_ferie = [dip.get("Ferie W1"), dip.get("Ferie W2"), dip.get("Ferie W3")]
            in_ferie = numero_settimana in settimane_ferie
            data_fine_malattia = dip.get("Malattia Fino Al")
            turno_base = determina_turno_base(dip["Squadra"], numero_settimana)
            
            # --- LOGICA DELLE DOMENICHE E DELLE FERIE ---
            ha_lavorato_dom_scorsa = mem_domeniche.get(dip["Nome"], False)
            
            if in_ferie:
                valore_dom_p = turno_base # Regola: se in ferie, la domenica prima si lavora
                valore_dom_s = "FERIE"
            else:
                valore_dom_p = "RIPOSO" if ha_lavorato_dom_scorsa else turno_base
                valore_dom_s = turno_base if ha_lavorato_dom_scorsa else "RIPOSO"

            riga = {"Dipendente": dip["Nome"], "Contratto": dip["Contratto"], "Squadra": dip["Squadra"]}
                
            for key, offset in zip(GIORNI_8_KEYS, OFFSETS):
                data_giorno_corrente = data_lunedi + datetime.timedelta(days=offset)
                in_malattia = False
                if pd.notnull(data_fine_malattia) and data_giorno_corrente <= data_fine_malattia:
                    in_malattia = True

                if in_malattia:
                    riga[key] = "MALATTIA"
                elif in_ferie and key != "Dom_P":
                    riga[key] = "FERIE"
                elif key == "Dom_P":
                    riga[key] = valore_dom_p
                elif key == "Dom_S":
                    riga[key] = valore_dom_s
                else:
                    # Giorni feriali Lun -> Sab
                    if dip["Contratto"] == "PT":
                        riposi_fissi = [dip.get("Riposo 1"), dip.get("Riposo 2")]
                        riposi_fissi = [r for r in riposi_fissi if r != "Nessuno" and pd.notnull(r)]
                        
                        giorno_base = GIORNI_BASE[OFFSETS.index(offset) - 1] 
                        
                        if valore_dom_p == "RIPOSO" and giorno_base in riposi_fissi:
                            outro_riposo = riposi_fissi[1] if len(riposi_fissi) > 1 and giorno_base == riposi_fissi[0] else riposi_fissi[0]
                            chiave_altro = [k for k, g in zip(GIORNI_8_KEYS[1:7], GIORNI_BASE[:-1]) if g == outro_riposo]
                            chiave_corrente = key
                            if chiave_altro and target_copertura.get(chiave_corrente, 0) <= target_copertura.get(chiave_altro[0], 0):
                                riga[key] = "RIPOSO"
                            else:
                                riga[key] = turno_base
                        elif valore_dom_p != "RIPOSO" and giorno_base in riposi_fissi:
                            riga[key] = "RIPOSO"
                        else:
                            riga[key] = turno_base
                    else:
                        riga[key] = turno_base 
            
            tabellone.append(riga)
            
        df = pd.DataFrame(tabellone)
        
        # --- BILANCIAMENTO FT (Solo dal Lunedì al Sabato) ---
        if not df.empty:
            ft_indices = df[df["Contratto"] == "FT"].index.tolist()
            for index in ft_indices:
                miglior_giorno = None
                max_surplus = -9999
                
                # Cerca di piazzare il riposo tra Lunedì e Sabato
                for key in GIORNI_8_KEYS[1:7]:
                    if df.at[index, key] not in ["MALATTIA", "FERIE"]: 
                        lavoratori_attivi = (~df[key].isin(["RIPOSO", "MALATTIA", "FERIE", "PERMESSO"])).sum()
                        target_persone = totale_dipendenti * target_copertura[key]
                        surplus = lavoratori_attivi - target_persone
                        
                        if surplus > max_surplus:
                            max_surplus = surplus
                            miglior_giorno = key
                            
                if miglior_giorno:
                    df.at[index, miglior_giorno] = "RIPOSO"
                    
        return df

    tabs_week =
