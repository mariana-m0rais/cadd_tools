import streamlit as st
import pandas as pd
from pages.home_content import display_home_content
from pages.results_content import display_results_content

if 'page' not in st.session_state:
    st.session_state.page = 'home'

st.set_page_config(page_title="Drug Discovery Tools", layout="wide", initial_sidebar_state="expanded")

def set_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# Hide sidebar on home page
if st.session_state.page == "home":
    st.markdown("""
        <style>
            section[data-testid="stSidebar"] {
                display: none;
            }
            [data-testid="collapsedControl"] {
                display: none;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            section[data-testid="stSidebar"] {
                display: block !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
def show_home_view():
    display_home_content(set_page)

def show_results_view():
    display_results_content(set_page)


PAGES = {
    'home': show_home_view,
    'results': show_results_view,
}

PAGES[st.session_state.page]()


