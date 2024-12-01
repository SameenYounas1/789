# Developed by Adnan Belal

import streamlit as st


st.set_page_config(
    page_title="QC Leap By Adnan Belali",
    page_icon=":dna:" ,
    layout="wide",
)

with st.sidebar:
    st.image('./images/qc leap.png')
    
    #st.markdown('---')
    st.info('*Developed by Adnan Belali')
    
#st.write("# :blue[QC Leap]")
st.image('./images/qc leap.png')
st.write(" ")

instructions = """
Welcome to QC Constellation, an innovative web application designed to transform quality control practices in clinical laboratories. This tool is meticulously built to help laboratory professionals manage the complexities of modern quality control, enabling them to apply risk-based quality control practices with accuracy and confidence.

Quality control in clinical laboratories involves a range of techniques, from basic rules to advanced methods such as moving averages. Tools like sigma-metric measurements and method decision charts are essential for evaluating analytical procedures. QC Constellation uses these tools effectively, ensuring their use is tailored to the performance of specific analytical methods and the associated risks to patients.

The application integrates traditional Westgard rules, trend detection techniques such as EWMA and CUSUM, and the Six Sigma methodology for thorough performance assessment. Additionally, it offers moving average charts for patient-specific QC and an optimization tool. The essence of QC Constellation is to make these advanced practices accessible and actionable for laboratory professionals, all within a risk-based framework.
"""

st.markdown(instructions)

st.info("""**Please note:** *QC Leap: a cutting-edge solution for risk and 
patient-based quality control in clinical laboratories. *""")

st.write(" ")

