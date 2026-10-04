import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Clinical NGS Research Dashboard",
    page_icon="🧬",
    layout="wide",
)


st.title("🧬 Clinical NGS Research Dashboard")

st.warning(
    "Educational/research demonstration only. "
    "This application is not a clinical diagnostic system."
)

st.markdown(
    """
    ## About this project

    This dashboard is designed to visualize outputs from an
    end-to-end next-generation sequencing research workflow.

    Planned workflow:

    **FASTQ → QC → trimming → alignment → variant calling → reporting**
    """
)


st.header("Pipeline Status")

status_data = pd.DataFrame(
    {
        "Stage": [
            "Input FASTQ",
            "Quality Control",
            "Read Trimming",
            "Alignment",
            "Variant Calling",
            "MultiQC Reporting",
        ],
        "Status": [
            "Planned",
            "Planned",
            "Planned",
            "Planned",
            "Planned",
            "Planned",
        ],
    }
)

st.dataframe(
    status_data,
    use_container_width=True,
    hide_index=True,
)


st.header("Sample")

sample = st.selectbox(
    "Select sample",
    ["SRR8082143"],
)

st.write(f"Selected research sample: **{sample}**")


st.info(
    "Real sequencing metrics will be populated from pipeline outputs "
    "after the Nextflow/AWS Batch workflow is implemented."
)
