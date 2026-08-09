# ==========================================================
# Import Libraries
# ==========================================================

import streamlit as st
import pandas as pd


# ==========================================================
# Classification Report
# ==========================================================

def render_classification_report(metrics):

    st.markdown("---")
    st.header("📋 Classification Report")

    report_df = (
        pd.DataFrame(metrics["report_dict"])
        .transpose()
        .round(2)
    )

    html = report_df.to_html(
        classes="report-table",
        border=0
    )

    st.markdown("""
    <style>

    .report-table{
        width:100%;
        border-collapse:collapse;
        font-size:18px;
        margin-top:10px;
    }

    .report-table th{
        background:#1f2937;
        color:white;
        font-size:20px;
        font-weight:bold;
        padding:12px;
        text-align:center;
        border:1px solid #444;
    }

    .report-table td{
        font-size:18px;
        padding:10px;
        text-align:center;
        border:1px solid #444;
    }

    .report-table tr:nth-child(even){
        background:#111827;
    }

    .report-table tr:nth-child(odd){
        background:#0f172a;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(html, unsafe_allow_html=True)