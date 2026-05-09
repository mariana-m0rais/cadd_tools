import streamlit as st
import pandas as pd

def display_results_content(set_page):
    page_title = st.session_state.get('page_title', "Results")
    page_caption = st.session_state.get('page_caption', "")
    active_features_home = st.session_state.get('active_features', [])

    col_title, col_back = st.columns([0.75, 0.25])
    with col_back:
        if st.button("Return to Home Page", use_container_width=True, type="primary"):
            set_page('home')
    with col_title:
        st.subheader(f"{page_title}")

    df = pd.read_csv('data/tools.csv', sep=';')
    
    with st.sidebar:
        access_filter = st.multiselect("Access Type", 
            options=df['access_type'].unique(),
            default=df['access_type'].unique()
        )
        
        st.write("Features:")
        feat_cols = [
            'ai_integration', 'de_novo', 'optimization', 'properties_prediction',
            'bioactivity_prediction', 'synthesizability', 'target_fishing',
            'docking', 'retrosynthesis', 'virtual_screening'
        ]
        
        selected_features = []
        for feat in feat_cols:
            is_active = feat in active_features_home
            if st.checkbox(feat.replace('_', ' ').title(), value=is_active, key=f"cb_{feat}"):
                selected_features.append(feat)

    filtered_df = df[df['access_type'].isin(access_filter)].copy()

    if selected_features:
        filtered_df['match_count'] = filtered_df[selected_features].astype(int).sum(axis=1)
    else:
        filtered_df['match_count'] = 0
    
    if selected_features:
        results_df = filtered_df[filtered_df['match_count'] > 0].copy()
    else:
        results_df = filtered_df.copy()

    num_recommended = len(results_df[results_df['match_count'] == len(selected_features)]) if selected_features else 0
    results_df = results_df.sort_values(by='match_count', ascending=False).reset_index(drop=True)
    num_total = len(results_df)

    st.write(f"{page_caption} You can further filter the results using the sidebar options.")

    if selected_features:
        if num_recommended > 0:
            st.write(f"**{num_recommended} tools exactly match your filters.**")
            if num_total > num_recommended:
                st.write(f"Showing also {num_total - num_recommended} tools that match some of your criteria.")
        else:
            st.write("**There are no tools with that specific combination of filters.**")
            st.write(f"However, showing {num_total} tools that match at least one of your chosen filters.")
    else:
        st.write(f"**Number of tools found: {num_total}**")

    grid_col1, grid_col2 = st.columns(2)
    
    for index, row in results_df.iterrows():
        target_col = grid_col1 if index % 2 == 0 else grid_col2
        
        with target_col:
            with st.container(border=True):
                header_col, rec_col, tag_col = st.columns([0.7,0.50, 0.30], gap="xxsmall")
            
                with header_col:
                    st.markdown(f"### {row['name']}")
                
                with rec_col:
                    st.write(" ")
                    is_rec = selected_features and row['match_count'] == len(selected_features)
                    if is_rec:
                        st.badge("Exact Filter Match", color="blue")
                    else:
                        st.write(" ")

                with tag_col:
                    st.write(" ")
                    if str(row['access_type']).lower() == 'open':
                        st.badge("Open Access", color="green")
                    else:
                        st.badge("Commercial", color="red")
                st.markdown(f"**Focus:** *{row['primary_focus']}*")
                
                # Tags de Features
                tags = [f"`{c.replace('_', ' ')}`" for c in feat_cols if row[c] == True]
                if tags:
                    st.markdown(f"**Features:** {' '.join(tags)}")
                
                # Funções Adicionais
                other_func = str(row['other_functions']).strip()
                if other_func and other_func not in ["-", "nan", "None", "nan"]:
                    with st.expander("Additional Functions"):
                        st.write(other_func)
                
                st.write("") # Espaçador
                st.link_button(f"Go to {row['name']}", row['url'], use_container_width=True)

    if results_df.empty:
        st.warning("No tools found with the selected filters.")