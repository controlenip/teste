"""Ponto de entrada oficial: streamlit run app.py."""
import streamlit as st

st.set_page_config(page_title="NIP | Dashboard Demanda", page_icon="🏗️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<style>
:root {--nip-navy:#123653;--nip-teal:#087785;--nip-bg:#edf2f6}
[data-testid="stAppViewContainer"]{background:var(--nip-bg)}
[data-testid="stSidebar"], [data-testid="collapsedControl"]{display:none!important}
[data-testid="stMainBlockContainer"]{max-width:100%!important;padding:0.5rem 1rem 2rem!important}
/* Menu horizontal nativo do Streamlit */
[data-testid="stNavigation"]{background:#f6f9fc!important;border-bottom:1px solid #c9dce8!important}
[data-testid="stNavigation"] a{border:1px solid #a5c4d6!important;border-radius:6px!important;margin:4px!important;font-weight:700!important}
[data-testid="stNavigation"] a[aria-current="page"]{background:#116d7c!important;color:white!important}
.nip-top-brand{background:#123653;color:#fff;padding:13px 20px;display:flex;justify-content:space-between;align-items:center;margin:-.5rem -1rem 0;min-height:70px;font-family:Arial,sans-serif}
.nip-top-brand strong{font-size:19px}.nip-top-brand small{display:block;color:#c6dbe8;font-size:11px;margin-top:4px}
.nip-top-brand .nip-pill{background:#087785;padding:10px 15px;border-radius:5px;font-size:12px;font-weight:bold}
</style>""",unsafe_allow_html=True)

st.markdown("<div class='nip-top-brand'><div><strong>nip | NIP | Dashboard Demanda</strong><small>Gerador SGO e ferramentas operacionais</small></div><span class='nip-pill'>Base compartilhada - NIP</span></div>",unsafe_allow_html=True)

pages=[
 st.Page("Inicio.py",title="Visão geral",icon="🏠",default=True),
 st.Page("pages/1_CRIAR_SGO.py",title="Criar SGO",icon="🏗️"),
 st.Page("pages/2_RELATORIO_DE_EXPURGO.py",title="Relatório de expurgo",icon="📋"),
 st.Page("pages/3_MAPA.py",title="Mapa",icon="🗺️"),
]
pg=st.navigation(pages,position="top",expanded=True)
pg.run()
