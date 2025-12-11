import streamlit as st
import pandas as pd
from data_extractor import extract

# PAGE SETTINGS

st.set_page_config(page_title="Financial Data Extractor", layout="centered")

# TITLE

st.title("Financial Data Extractor")
st.write("Paste any financial paragraph below and extract structured insights.")

# USER INPUT

paragraph = st.text_area("Enter financial paragraph:")

# EXTRACT BUTTON

if st.button("Extract"):
    if paragraph.strip():
        try:
            extracted_data = extract(paragraph)

            # Build results table
            data = {
                'Measure': ['Revenue', 'EPS'],
                'Estimated': [
                    extracted_data.get('revenue_expected'),
                    extracted_data.get('eps_expected')
                ],
                'Actual': [
                    extracted_data.get('revenue_actual'),
                    extracted_data.get('eps_actual')
                ]
            }

            df = pd.DataFrame(data)
            st.subheader("Extracted Data")
            st.table(df)

        except Exception as e:
            st.error(f"Extraction failed: {e}")

    else:
        st.warning("Please enter a paragraph to extract data from.")
