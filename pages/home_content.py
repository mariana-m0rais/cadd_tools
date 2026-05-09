import streamlit as st

def display_home_content(set_page):
    st.markdown("<h1 style='text-align: center; margin-bottom: 20px;'>What would you like to do today?</h1>", unsafe_allow_html=True)
    all_features = [
        'ai_integration', 'de_novo', 'optimization', 'properties_prediction',
        'bioactivity_prediction', 'synthesizability', 'target_fishing',
        'docking', 'retrosynthesis', 'virtual_screening'
    ]
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🔍", text_alignment="center")
        if st.button("Start from scratch or find new leads", width="stretch"):
            st.session_state.active_features = ['de_novo', 'virtual_screening']
            st.session_state.page_title = "🔍 Start from scratch or find new leads"
            st.session_state.page_caption = "Showing platforms for de-novo design and virtual screening of novel chemical entities."
            set_page('results')


    with col2:
        st.subheader("💡", text_alignment="center")
        if st.button("Refine and predict molecular behavior", width="stretch"):
            st.session_state.active_features = ['optimization', 'properties_prediction']
            st.session_state.page_title = "💡 Refine and predict molecular behavior"
            st.session_state.page_caption = "Showing tools specialized in lead optimization and ADMET properties prediction."
            set_page('results')

    with col3:
        st.subheader("🎯", text_alignment="center")
        if st.button("Understand binding and biological targets", width="stretch"):
            st.session_state.active_features = ['target_fishing', 'docking', 'bioactivity_prediction']
            st.session_state.page_title = "🎯 Understand binding and biological targets"
            st.session_state.page_caption = "Showing platforms for molecular docking simulations, target fishing and protein-ligand interaction analysis"
            set_page('results')

    st.write(" ") 
    st.write(" ") 

    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader("🧬", text_alignment="center")
        if st.button("Plan how to build a molecule", width="stretch"):
            st.session_state.active_features = ['retrosynthesis', 'synthesizability']
            st.session_state.page_title = "🧬 Plan how to build a molecule"
            st.session_state.page_caption = "Showing platforms for synthetic accessibility assessment and retrosynthetic pathway planning."
            set_page('results')

    with col5:
        st.subheader("💻", text_alignment="center")
        if st.button("Integrate my own AI model", width="stretch"):
            st.session_state.target_filter = "ai_integration"
            st.session_state.page_title = "💻 Integrate my own AI model"
            st.session_state.page_caption = "Showing flexible platforms that allow the integration and deployment of custom-made AI models."
            set_page('results')

    with col6:
        st.subheader("📂", text_alignment="center")
        if st.button("Browse all available tools and sites", width="stretch"):
            st.session_state.target_filter = all_features
            st.session_state.page_title = "📂 Browse all available tools and sites"
            st.session_state.page_caption = "Showing the complete database of web-based drug discovery interfaces and computational tools."
            set_page('results')
