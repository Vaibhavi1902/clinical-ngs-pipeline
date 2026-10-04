import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Clinical NGS Analytics Platform",
    page_icon="🧬",
    layout="wide",
)

st.title("🧬 Clinical NGS Analytics Platform")

st.warning(
    "Research and educational demonstration only. "
    "This application is not intended for clinical diagnosis or patient care."
)

st.markdown(
    """
    This dashboard provides a cloud-native interface for monitoring
    an educational next-generation sequencing workflow.
    """
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.header("Pipeline Controls")

sample = st.sidebar.selectbox(
    "Sample",
    ["SRR8082143"],
)

st.sidebar.selectbox(
    "Environment",
    ["Development", "AWS"],
)

st.sidebar.markdown("---")

st.sidebar.info(
    "NGS compute will run through Nextflow and AWS Batch. "
    "The dashboard is hosted separately on Amazon EKS."
)

# ---------------------------------------------------------
# Pipeline status
# ---------------------------------------------------------

st.header("Pipeline Status")

status_data = pd.DataFrame(
    {
        "Stage": [
            "FASTQ Input",
            "FastQC",
            "fastp",
            "BWA-MEM2 Alignment",
            "SAMtools",
            "BCFtools",
            "MultiQC",
        ],
        "Status": [
            "Planned",
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

# ---------------------------------------------------------
# Workflow visualization
# ---------------------------------------------------------

st.header("NGS Workflow")

workflow = pd.DataFrame(
    {
        "Stage": [
            "FASTQ",
            "FastQC",
            "fastp",
            "BWA-MEM2",
            "SAMtools",
            "BCFtools",
            "MultiQC",
        ],
        "Order": [1, 2, 3, 4, 5, 6, 7],
    }
)

fig = px.line(
    workflow,
    x="Order",
    y="Stage",
    markers=True,
    title="Planned Analysis Workflow",
)

fig.update_layout(
    xaxis_title="Pipeline Order",
    yaxis_title="",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

# ---------------------------------------------------------
# Sample information
# ---------------------------------------------------------

st.header("Sample Information")

sample_info = pd.DataFrame(
    {
        "Field": [
            "Sample ID",
            "Organism",
            "Data Type",
            "Source",
            "Purpose",
        ],
        "Value": [
            sample,
            "Escherichia coli",
            "Illumina paired-end WGS",
            "NCBI SRA",
            "Educational / research demonstration",
        ],
    }
)

st.dataframe(
    sample_info,
    use_container_width=True,
    hide_index=True,
)

# ---------------------------------------------------------
# Metrics
# ---------------------------------------------------------

st.header("Analysis Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Pipeline Status", "Planned")
col2.metric("Sample", sample)
col3.metric("QC Status", "Pending")
col4.metric("Variant Analysis", "Pending")

# ---------------------------------------------------------
# Architecture
# ---------------------------------------------------------

st.header("Cloud Architecture")

st.markdown(
    """
    **Application layer**

    Streamlit → Amazon EKS

    **Data layer**

    Amazon S3 → raw data → reference → results → reports

    **Compute layer**

    Nextflow → AWS Batch

    **DevOps layer**

    GitHub → GitHub Actions → Docker Hub → Argo CD → EKS
    """
)

st.caption(
    "Clinical NGS Analytics Platform — educational/research demonstration"
)
