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

# --- INIZIALIZZAZIONE MEMORIA PERMANENTE ---
if 'df_anagrafica' not in st.session_state:
    if os.path.exists(FILE_ANAGRAFICA):
        df_caricato = pd.read_csv(FILE_ANAGRAFICA)
        df_caricato = df_caricato.where(pd.notnull(df_caricato), None)
        # Assicuriamo che le nuove colonne esistano nei vecchi salvataggi
        nuove_colonne = ["Malattia Fino Al", "Ferie W1", "Ferie W2", "Ferie W3"]
        for col in nuove_colonne:
            if col not in df_caricato.columns:
                df_caricato[col] = None
        st.session_state.df_anagrafica = df_caricato
    else:
        dati_base = [
            {"Nome": "MENDOZA MARVIN", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MENDOZA MANUEL", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "ALVES BRAGA ELAINE", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "BULOSAN CRISTOPHER", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "CAVALLARI CATERINA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "GAVAZZENI MICHELA", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "CUARESMA FRANCESCO", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "PERALTA BARBARA", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "RICCARDI SIMONA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MABANTA MARIA", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "PASCUA ARVIN", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "TOCCHETTI CAMILLA", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "SPEERING DAPHNI", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "TANADA EUGENE", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "CIPRIANO RUSSEL", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "FELIX CARBUNGCAL", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "GHITTI SARA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "BONO DANIELA", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "TAN JONIMAE", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "PETILUNA ROSARIO", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MAGTIBAY LEA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "MAGTIBAY BABYJANE", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
            {"Nome": "DONGHI NIKITA", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False, "Malattia Fino Al": None, "Ferie W1": None, "Ferie W2": None, "Ferie W3": None},
        ]
        df_iniziale = pd.DataFrame(dati_base)
        salva_dati_su_file(df_iniziale)

GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
OPZIONI_TURNO = ["06:00-13:00", "12:30-19:30", "13:00-20:00", "RIPOSO", "MALATTIA", "FERIE", "PERMESSO"]
APPROV_GIORNI = {
    "Lunedì": "Lun", "Martedì": "Mar", "Mercoledì": "Mer", 
    "Giovedì": "Gio", "Venerdì": "Ven", "Sabato": "Sab", "Domenica": "Dom"
}

# --- CREAZIONE SCHEDE PRINCIPALI ---
tab_anagrafica, tab_turni = st.tabs(["📋 1. Gestione Anagrafica", "📅 2. Generazione Turni"])

# ==========================================
# SCHEDA 1: GESTIONE ANAGRAFICA
# ==========================================
with tab_anagrafica:
    st.subheader("👥 Lista Attuale Personale e Assenze Programmate")
    st.write("Modifica le date di malattia o i numeri delle settimane di ferie. Clicca su **Salva Modifiche** per applicare.")
    
    # Conversione corretta della colonna date per Streamlit
    if "Malattia Fino Al" in st.session_state.df_anagrafica.columns:
        st.session_state.df_anagrafica["Malattia Fino Al"] = pd.to_datetime(st.session_state.df_anagrafica["Malattia Fino Al"]).dt.date
    
    config_anagrafica = {
        "Contratto": st.column_config.SelectboxColumn("Contratto", options=["FT", "PT"], required=True),
        "Squadra": st.column_config.NumberColumn("Squadra", min_value=1, max_value=4, step=1, required=True),
        "Riposo 1": st.column_config.SelectboxColumn("Riposo 1 (PT)", options=GIORNI[:-1]),
        "Riposo 2": st.column_config.SelectboxColumn("Riposo 2 (PT)", options=GIORNI[:-1]),
        "Dom Scorsa": st.column_config.CheckboxColumn("Lavorato Dom. Scorsa?"),
        "Malattia Fino Al": st.column_config.DateColumn("Malattia Fino Al", format="DD/MM/YYYY"),
        "Ferie W1": st.column_config.NumberColumn("Ferie W1 (N. Set)"),
        "Ferie W2": st.column_config.NumberColumn("Ferie W2 (N. Set)"),
        "Ferie W3": st.column_config.NumberColumn("Ferie W3 (N. Set)")
    }
    
    df_editato = st.data_editor(
        st.session_state.df_anagrafica,
        column_config=config_anagrafica,
        num_rows="dynamic", # "dynamic" permette anche di aggiungere/eliminare righe direttamente dalla tabella!
        use_container_width=True,
        hide_index=True
    )

    if st.button("💾 Salva Modifiche Anagrafica", type="primary", use_container_width=True):
        salva_dati_su_file(df_editato)
        st.success("✅ Dati anagrafici e assenze aggiornati!")

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
    default_pct = [90, 75, 75, 75, 90, 90, 45]
    for g, default in zip(GIORNI, default_pct):
        target_copertura[g] = st.sidebar.slider(g, 0, 100, default) / 100

    def genera_tabellone_settimana(numero_settimana, data_lunedi, mem_domeniche):
        tabellone = []
        dati_dipendenti = st.session_state.df_anagrafica.to_dict('records')
        totale_dipendenti = len([d for d in dati_dipendenti if d.get("Nome") and str(d.get("Nome")).strip() != ""])
        
        for dip in dati_dipendenti:
            if not dip.get("Nome") or str(dip.get("Nome")).strip() == "": continue 
            
            # --- GESTIONE FERIE ---
            settimane_ferie = [dip.get("Ferie W1"), dip.get("Ferie W2"), dip.get("Ferie W3")]
            in_ferie = numero_settimana in settimane_ferie
            
            # --- GESTIONE MALATTIA ---
            data_fine_malattia = dip.get("Malattia Fino Al")
            
            turno_base = determina_turno_base(dip["Squadra"], numero_settimana)
            riga = {"Dipendente": dip["Nome"], "Contratto": dip["Contratto"], "Squadra": dip["Squadra"]}
            
            ha_lavorato_scorsa = bool(mem_domeniche.get(dip["Nome"], False))
            dom_turno = "RIPOSO" if ha_lavorato_scorsa else "06:00-13:00"
                
            for offset, giorno in enumerate(GIORNI):
                data_giorno_corrente = data_lunedi + datetime.timedelta(days=offset)
                
                # Controllo Malattia per il giorno specifico
                in_malattia = False
                if pd.notnull(data_fine_malattia):
                    if data_giorno_corrente <= data_fine_malattia:
                        in_malattia = True

                # Assegnazione prioritaria
                if in_malattia:
                    riga[giorno] = "MALATTIA"
                elif in_ferie:
                    riga[giorno] = "FERIE"
                else:
                    if giorno == "Domenica":
                        riga[giorno] = dom_turno
                    else:
                        if dip["Contratto"] == "PT":
                            riposi_fissi = [dip.get("Riposo 1"), dip.get("Riposo 2")]
                            if dom_turno == "RIPOSO" and giorno in riposi_fissi and giorno is not None:
                                outro_riposo = riposi_fissi[1] if giorno == riposi_fissi[0] else riposi_fissi[0]
                                if target_copertura.get(giorno, 0) <= target_copertura.get(outro_riposo, 0):
                                    riga[giorno] = "RIPOSO"
                                else:
                                    riga[giorno] = turno_base
                            elif dom_turno != "RIPOSO" and giorno in riposi_fissi and giorno is not None:
                                riga[giorno] = "RIPOSO"
                            else:
                                riga[giorno] = turno_base
                        else:
                            riga[giorno] = turno_base 
            
            tabellone.append(riga)
            
        df = pd.DataFrame(tabellone)
        
        # Bilanciamento FT
        if not df.empty:
            ft_indices = df[df["Contratto"] == "FT"].index.tolist()
            for index in ft_indices:
                miglior_giorno = None
                max_surplus = -9999
                
                for giorno in GIORNI[:-1]:
                    if df.at[index, giorno] not in ["MALATTIA", "FERIE"]: # Non togliere chi è già assente
                        lavoratori_attivi = (~df[giorno].isin(["RIPOSO", "MALATTIA", "FERIE", "PERMESSO"])).sum()
                        target_persone = totale_dipendenti * target_copertura[giorno]
                        surplus = lavoratori_attivi - target_persone
                        
                        if surplus > max_surplus:
                            max_surplus = surplus
                            miglior_giorno = giorno
                            
                if miglior_giorno:
                    df.at[index, miglior_giorno] = "RIPOSO"
                    
        return df

    # Ora mostriamo 6 schede per permettere di vedere anche il passato/futuro
    tabs_week = st.tabs([f"Week {week_partenza + i}" for i in range(6)])
    
    memoria_dom = {}
    for index, row in st.session_state.df_anagrafica.iterrows():
        if row.get("Nome") and str(row.get("Nome")).strip() != "":
            memoria_dom[row["Nome"]] = row["Dom Scorsa"]

    for i, t_week in enumerate(tabs_week):
        week_corrente = week_partenza + i
        lunedi_settimana = data_inizio + datetime.timedelta(weeks=i)
        
        # Nome file per il salvataggio della settimana congelata
        FILE_BLOCCO = f"Turni_Bloccati_W{week_corrente}_{anno_partenza}.csv"

        config_colonne_turni = {}
        rinomina_esportazione = {}
        
        # Le date reali per le colonne
        for offset, g_nome in enumerate(GIORNI):
            data_giorno = lunedi_settimana + datetime.timedelta(days=offset)
            label_dinamico = f"{APPROV_GIORNI[g_nome]} {data_giorno.day}"
            config_colonne_turni[g_nome] = st.column_config.SelectboxColumn(label_dinamico, options=OPZIONI_TURNO)
            rinomina_esportazione[g_nome] = label_dinamico

        with t_week:
            if st.session_state.df_anagrafica.empty:
                st.warning("Inserisci prima i dipendenti nell'Anagrafica.")
            else:
                # Carica dati salvati se esistono, altrimenti generalo nuovo
                if os.path.exists(FILE_BLOCCO):
                    df_calcolato = pd.read_csv(FILE_BLOCCO)
                    st.info("🔒 Questa settimana è stata salvata come **Definitiva**. Qualsiasi modifica farai qui sotto andrà sovrascritta cliccando il tasto Salva.")
                else:
                    df_calcolato = genera_tabellone_settimana(week_corrente, lunedi_settimana, memoria_dom)
                
                df_modificato = st.data_editor(
                    df_calcolato, 
                    column_config=config_colonne_turni, 
                    use_container_width=True, 
                    hide_index=True, 
                    key=f"editor_w{week_corrente}"
                )
                
                col_save, col_down = st.columns(2)
                
                with col_save:
                    if st.button(f"🔒 Salva/Aggiorna Week {week_corrente} come Definitiva", type="primary", use_container_width=True, key=f"btn_save_w{week_corrente}"):
                        df_modificato.to_csv(FILE_BLOCCO, index=False)
                        st.success(f"Week {week_corrente} salvata correttamente!")
                        st.rerun()

                with col_down:
                    df_esportazione = df_modificato.copy()
                    df_esportazione.rename(columns=rinomina_esportazione, inplace=True)
                    csv = df_esportazione.to_csv(index=False, sep=";").encode('utf-8-sig')
                    
                    st.download_button(
                        label=f"📥 Scarica Excel/CSV (Week {week_corrente})",
                        data=csv,
                        file_name=f"Turni_Week_{week_corrente}.csv",
                        mime="text/csv",
                        use_container_width=True,
                        key=f"btn_down_w{week_corrente}"
                    )

                st.write("**Vista Visiva Assenze e Copertura:**")
                st.dataframe(df_modificato.style.map(colora_celle), use_container_width=True)
                
                report = []
                for g_nome in GIORNI:
                    is_mattina = df_modificato[g_nome] == "06:00-13:00"
                    is_pome = df_modificato[g_nome].isin(["12:30-19:30", "13:00-20:00"])
                    op_m = df_modificato[is_mattina][g_nome].count() if not df_modificato.empty else 0
                    op_p = df_modificato[is_pome][g_nome].count() if not df_modificato.empty else 0
                    
                    report.append({
                        "Giorno": rinomina_esportazione[g_nome], 
                        "Op. Mattina": op_m, 
                        "Op. Pomeriggio": op_p, 
                        "Pezzi Previsti": (op_m + op_p) * 7 * pieces_ora
                    })
                    
                st.write("**Stima Volumi Giornalieri (Escluse Assenze):**")
                st.dataframe(pd.DataFrame(report).set_index("Giorno").T)
                
                # Prepariamo la memoria delle domeniche lavorate per la settimana successiva
                # Ma SOLO SE la settimana è generata e non "forzata"
                for i_row, row in df_modificato.iterrows():
                    nome_dip = row.get("Dipendente")
                    if nome_dip:
                        memoria_dom[nome_dip] = (row.get("Domenica") != "RIPOSO")
