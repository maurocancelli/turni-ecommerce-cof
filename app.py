import streamlit as st
import pandas as pd
import datetime
import os

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Pianificazione Turni - COF", layout="wide")
st.title("Pianificazione Mensile Reparto E-commerce")

# --- NOME DEL FILE DI SALVATAGGIO PERMANENTE ---
FILE_ANAGRAFICA = "anagrafica_salvata.csv"

def salva_dati_su_file(df):
    """Salva il dataframe in un file CSV fisico per resistere ai refresh della pagina"""
    st.session_state.df_anagrafica = df
    df.to_csv(FILE_ANAGRAFICA, index=False)

# --- 1. INIZIALIZZAZIONE MEMORIA PERMANENTE ---
if 'df_anagrafica' not in st.session_state:
    if os.path.exists(FILE_ANAGRAFICA):
        df_caricato = pd.read_csv(FILE_ANAGRAFICA)
        df_caricato = df_caricato.where(pd.notnull(df_caricato), None)
        st.session_state.df_anagrafica = df_caricato
    else:
        dati_base = [
            {"Nome": "MENDOZA MARVIN", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "MENDOZA MANUEL", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "ALVES BRAGA ELAINE", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "BULOSAN CRISTOPHER", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "CAVALLARI CATERINA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "GAVAZZENI MICHELA", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "CUARESMA FRANCESCO", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "PERALTA BARBARA", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "RICCARDI SIMONA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "MABANTA MARIA", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "PASCUA ARVIN", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "TOCCHETTI CAMILLA", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "SPEERING DAPHNI", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "TANADA EUGENE", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "CIPRIANO RUSSEL", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "FELIX CARBUNGCAL", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "GHITTI SARA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "BONO DANIELA", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "TAN JONIMAE", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "PETILUNA ROSARIO", "Contratto": "FT", "Squadra": 4, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "MAGTIBAY LEA", "Contratto": "FT", "Squadra": 1, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "MAGTIBAY BABYJANE", "Contratto": "FT", "Squadra": 2, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
            {"Nome": "DONGHI NIKITA", "Contratto": "FT", "Squadra": 3, "Riposo 1": None, "Riposo 2": None, "Dom Scorsa": False},
        ]
        df_iniziale = pd.DataFrame(dati_base)
        salva_dati_su_file(df_iniziale)

GIORNI = ["Domenica", "Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]
OPZIONI_TURNO = ["06:00-13:00", "12:30-19:30", "13:00-20:00", "RIPOSO", "MALATTIA", "FERIE", "PERMESSO"]

# --- CREAZIONE SCHEDE ---
tab_anagrafica, tab_turni = st.tabs(["📋 1. Gestione Anagrafica", "📅 2. Generazione Turni"])

# ==========================================
# SCHEDA 1: GESTIONE ANAGRAFICA
# ==========================================
with tab_anagrafica:
    
    st.subheader("➕ Aggiungi un nuovo dipendente")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            nuovo_nome = st.text_input("Nome e Cognome")
            nuovo_contratto = st.selectbox("Tipo Contratto", ["FT", "PT"])
            nuova_squadra = st.selectbox("Squadra di appartenenza", [1, 2, 3, 4])
        with col2:
            nuovo_r1 = st.selectbox("Riposo Fisso 1 (Solo per Part-Time)", [None] + GIORNI[1:])
            nuovo_r2 = st.selectbox("Riposo Fisso 2 (Solo per Part-Time)", [None] + GIORNI[1:])
            nuova_dom = st.checkbox("Ha lavorato l'ultima Domenica?", value=False)
            
        if st.button("Aggiungi all'Anagrafica", use_container_width=True):
            if nuovo_nome.strip() == "":
                st.error("Inserisci un nome valido!")
            else:
                nuova_riga = {
                    "Nome": nuovo_nome.upper(),
                    "Contratto": nuovo_contratto,
                    "Squadra": nuova_squadra,
                    "Riposo 1": nuovo_r1 if nuovo_contratto == "PT" else None,
                    "Riposo 2": nuovo_r2 if nuovo_contratto == "PT" else None,
                    "Dom Scorsa": nuova_dom
                }
                nuovo_df = pd.concat([st.session_state.df_anagrafica, pd.DataFrame([nuova_riga])], ignore_index=True)
                salva_dati_su_file(nuovo_df)
                st.success(f"✅ {nuovo_nome.upper()} aggiunto correttamente!")
                st.rerun()

    st.subheader("🗑️ Rimuovi un dipendente")
    with st.container(border=True):
        lista_nomi = st.session_state.df_anagrafica["Nome"].tolist()
        nome_da_eliminare = st.selectbox("Scegli chi eliminare:", ["Nessuno..."] + lista_nomi)
        
        if st.button("Elimina", type="primary"):
            if nome_da_eliminare != "Nessuno...":
                nuovo_df = st.session_state.df_anagrafica[st.session_state.df_anagrafica["Nome"] != nome_da_eliminare]
                salva_dati_su_file(nuovo_df)
                st.success(f"❌ {nome_da_eliminare} rimosso dalla lista.")
                st.rerun()

    st.subheader("👥 Lista Attuale Personale (Modificabile)")
    st.write("Puoi toccare le celle della tabella per fare correzioni veloci. **Ricorda di premere Salva Modifiche!**")
    
    config_anagrafica = {
        "Contratto": st.column_config.SelectboxColumn("Contratto", options=["FT", "PT"], required=True),
        "Squadra": st.column_config.NumberColumn("Squadra", min_value=1, max_value=4, step=1, required=True),
        "Riposo 1": st.column_config.SelectboxColumn("Riposo 1 (PT)", options=GIORNI[1:]),
        "Riposo 2": st.column_config.SelectboxColumn("Riposo 2 (PT)", options=GIORNI[1:]),
        "Dom Scorsa": st.column_config.CheckboxColumn("Lavorato Domenica Scorsa?")
    }
    
    df_editato = st.data_editor(
        st.session_state.df_anagrafica,
        column_config=config_anagrafica,
        num_rows="fixed",
        use_container_width=True,
        hide_index=True
    )

    if st.button("💾 Salva Modifiche Tabella", type="primary", use_container_width=True):
        salva_dati_su_file(df_editato)
        st.success("✅ Dati salvati in modo permanente! Ora resisteranno ai refresh della pagina.")


# ==========================================
# SCHEDA 2: GENERAZIONE TURNI E PRODUTTIVITÀ
# ==========================================
with tab_turni:
    def determina_turno_base(squadra, numero_settimana):
        """Calcola il turno incrociando l'alternanza a specchio delle squadre"""
        ciclo = numero_settimana % 4
        if squadra in [1, 2]:
            if ciclo == 1 or ciclo == 3: return "06:00-13:00"
            elif ciclo == 2: return "12:30-19:30"
            else: return "13:00-20:00"
        else:
            if ciclo == 1: return "12:30-19:30"
            elif ciclo == 3: return "13:00-20:00"
            else: return "06:00-13:00"

    def colora_celle(valore):
        if valore == "MALATTIA": return "background-color: #ffcccc; color: #cc0000; font-weight: bold;"
        elif valore == "FERIE": return "background-color: #ffe6cc; color: #cc6600; font-weight: bold;"
        elif valore == "PERMESSO": return "background-color: #e6f2ff; color: #0066cc;"
        elif valore == "RIPOSO": return "background-color: #f2f2f2; color: #7f7f7f;"
        elif "06:00" in str(valore): return "background-color: #e6ffed; color: #1a7f37;"
        elif "12:30" in str(valore) or "13:00" in str(valore): return "background-color: #fbefff; color: #8250df;"
        return ""

    st.sidebar.header("Parametri Operativi")
    data_inizio = st.sidebar.date_input("Lunedì di inizio pianificazione", datetime.date.today())
    week_partenza = data_inizio.isocalendar()[1]
    pieces_ora = st.sidebar.number_input("Pezzi/Ora (Default):", value=100)

    st.sidebar.subheader("Forza Lavoro Richiesta (%)")
    target_copertura = {}
    default_pct = [45, 90, 75, 75, 75, 90, 90]
    for g, default in zip(GIORNI, default_pct):
        target_copertura[g] = st.sidebar.slider(g, 0, 100, default) / 100

    def genera_tabellone_settimana(numero_settimana, mem_domeniche):
        tabellone = []
        dati_dipendenti = st.session_state.df_anagrafica.to_dict('records')
        totale_dipendenti = len([d for d in dati_dipendenti if d.get("Nome") and str(d.get("Nome")).strip() != ""])
        
        for dip in dati_dipendenti:
            if not dip.get("Nome") or str(dip.get("Nome")).strip() == "": continue 
            
            turno_base = determina_turno_base(dip["Squadra"], numero_settimana)
            riga = {"Dipendente": dip["Nome"], "Contratto": dip["Contratto"], "Squadra": dip["Squadra"]}
            
            ha_lavorato_scorsa = bool(mem_domeniche.get(dip["Nome"], False))
            if ha_lavorato_scorsa:
                riga["Domenica"] = "RIPOSO"
            else:
                riga["Domenica"] = "06:00-13:00"
                
            for giorno in GIORNI[1:]:
                if dip["Contratto"] == "PT":
                    riposi_fissi = [dip.get("Riposo 1"), dip.get("Riposo 2")]
                    if riga["Domenica"] == "RIPOSO" and giorno in riposi_fissi and giorno is not None:
                        altro_riposo = riposi_fissi[1] if giorno == riposi_fissi[0] else riposi_fissi[0]
                        if target_copertura.get(giorno, 0) <= target_copertura.get(altro_riposo, 0):
                            riga[giorno] = "RIPOSO"
                        else:
                            riga[giorno] = turno_base
                    elif riga["Domenica"] != "RIPOSO" and giorno in riposi_fissi and giorno is not None:
                        riga[giorno] = "RIPOSO"
                    else:
                        riga[giorno] = turno_base
                else:
                    riga[giorno] = turno_base 
                    
            tabellone.append(riga)
            
        df = pd.DataFrame(tabellone)
        
        # --- NUOVA LOGICA DINAMICA RIPOSI FT ---
        if not df.empty:
            ft_indices = df[df["Contratto"] == "FT"].index.tolist()
            
            for index in ft_indices:
                miglior_giorno = None
                max_surplus = -9999
                
                # Cerca il giorno con più "sovrabbondanza" di personale rispetto al target
                for giorno in GIORNI[1:]:
                    lavoratori_attivi = (df[giorno] != "RIPOSO").sum()
                    target_persone = totale_dipendenti * target_copertura[giorno]
                    
                    surplus = lavoratori_attivi - target_persone
                    
                    if surplus > max_surplus:
                        max_surplus = surplus
                        miglior_giorno = giorno
                        
                # Assegna il riposo nel giorno migliore e aggiorna la tabella per il prossimo FT
                if miglior_giorno:
                    df.at[index, miglior_giorno] = "RIPOSO"
                    
        return df

    tabs_week = st.tabs([f"Week {week_partenza + i}" for i in range(4)])
    
    memoria_dom = {}
    for index, row in st.session_state.df_anagrafica.iterrows():
        if row.get("Nome") and str(row.get("Nome")).strip() != "":
            memoria_dom[row["Nome"]] = row["Dom Scorsa"]

    config_colonne_turni = {g: st.column_config.SelectboxColumn(g, options=OPZIONI_TURNO) for g in GIORNI}

    for i, t_week in enumerate(tabs_week):
        week_corrente = week_partenza + i
        with t_week:
            if st.session_state.df_anagrafica.empty:
                st.warning("Inserisci prima i dipendenti nell'Anagrafica.")
            else:
                st.subheader(f"Modifica Turni - Settimana {week_corrente}")
                
                df_calcolato = genera_tabellone_settimana(week_corrente, memoria_dom)
                
                df_modificato = st.data_editor(
                    df_calcolato, 
                    column_config=config_colonne_turni, 
                    use_container_width=True, 
                    hide_index=True, 
                    key=f"editor_w{week_corrente}"
                )
                
                st.write("**Vista Visiva Assenze e Copertura:**")
                st.dataframe(df_modificato.style.map(colora_celle), use_container_width=True)
                
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
                        "Pezzi Previsti": (op_m + op_p) * 7 * pieces_ora
                    })
                    
                st.write("**Stima Volumi Giornalieri (Escluse Assenze):**")
                st.dataframe(pd.DataFrame(report).set_index("Giorno").T)
                
                for nome in memoria_dom:
                    memoria_dom[nome] = not memoria_dom[nome]
