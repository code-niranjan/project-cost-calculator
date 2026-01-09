import streamlit as st
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Powerzest Project Cost Calculator",
    page_icon="⚡",
    layout="wide"
)

# ---------------- CSS Styling ----------------
st.markdown("""
<style>
body {
    background-color: #f7f9fc;
}
.section-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
h1, h2, h3 {
    color: #0f4c81;
    text-align: center;
}
.key-value {
    display:flex; 
    justify-content:space-between; 
    padding:8px 0; 
    border-bottom:1px solid #e0e0e0;
}
.metric-value {
    font-weight: bold;
    color: #0f4c81;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown("<h1>⚡ Powerzest Project Cost Calculator</h1>", unsafe_allow_html=True)
st.write("")

# ---------------- Inputs ----------------
with st.container():
    st.markdown("<div class='section-card'><h3>Enter Project Details</h3></div>", unsafe_allow_html=True)
    capacity = st.number_input("Plant Capacity (kW)", min_value=1.0, step=1.0)
    cost_per_kw = st.number_input("Cost per kW (₹)", min_value=1000.0, step=1000.0)
    tariff = st.number_input("Tariff (₹ per Unit)", min_value=1.0, step=0.5)

# ---------------- Cost Calculations ----------------
total_cost = capacity * cost_per_kw
gst_rate = 0.089
gst_amount = total_cost * gst_rate
final_cost = total_cost + gst_amount
subsidy = capacity * 18000
actual_amount = final_cost - subsidy

# ---------------- Mobile-Friendly Cost Summary ----------------
with st.container():
    st.markdown("<div class='section-card'><h3>💰 Project Cost Summary</h3></div>", unsafe_allow_html=True)
    
    summary_data = {
        "Plant Capacity (kW)": f"{capacity:,.0f}",
        "Total Cost (₹)": f"₹ {total_cost:,.0f}",
        "GST (8.9%)": f"₹ {gst_amount:,.0f}",
        "Final Cost (₹)": f"₹ {final_cost:,.0f}",
        "Subsidy (₹)": f"₹ {subsidy:,.0f}",
        "Total Amount After Subsidy (₹)": f"₹ {actual_amount:,.0f}"
    }
    
    for key, value in summary_data.items():
        st.markdown(f"<div class='key-value'><span>{key}</span><span class='metric-value'>{value}</span></div>", unsafe_allow_html=True)
    
    st.caption("ℹ️ Subsidy is calculated at ₹18,000 per kW as per current scheme.")

# ---------------- Energy & Savings ----------------
month_units = capacity * 3.85 * 30
year_units = month_units * 12
monthly_saving = month_units * tariff
yearly_saving = monthly_saving * 12

with st.container():
    st.markdown("<div class='section-card'><h3>⚡ Energy Production & Savings</h3></div>", unsafe_allow_html=True)
    
    # Monthly
    st.markdown(f"<div class='key-value'><span>Monthly Units</span><span class='metric-value'>{month_units:,.0f} Units</span></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='key-value'><span>Monthly Saving</span><span class='metric-value'>₹ {monthly_saving:,.0f}</span></div>", unsafe_allow_html=True)
    
    # Yearly
    st.markdown(f"<div class='key-value'><span>Yearly Units</span><span class='metric-value'>{year_units:,.0f} Units</span></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='key-value'><span>Yearly Saving</span><span class='metric-value'>₹ {yearly_saving:,.0f}</span></div>", unsafe_allow_html=True)

# ---------------- Return on Investment (Table Layout Preserved) ----------------
payback_with_subsidy = actual_amount / yearly_saving if yearly_saving > 0 else 0
payback_without_subsidy = final_cost / yearly_saving if yearly_saving > 0 else 0

with st.container():
    st.markdown("<div class='section-card'><h3>📈 Return on Investment</h3></div>", unsafe_allow_html=True)
    
    roi_table = f"""
    <table style='width:100%; border-collapse: collapse;'>
    <tr style='background-color:#e6f0fa;'>
        <th style='padding:10px; text-align:left;'> </th>
        <th style='padding:10px; text-align:center;'>With Subsidy</th>
        <th style='padding:10px; text-align:center;'>Without Subsidy</th>
    </tr>
    <tr>
        <td style='padding:10px;'><b>Project Cost (₹)</b></td>
        <td style='padding:10px; text-align:center;'>₹ {actual_amount:,.0f}</td>
        <td style='padding:10px; text-align:center;'>₹ {final_cost:,.0f}</td>
    </tr>
    <tr style='background-color:#f4f6fb;'>
        <td style='padding:10px;'><b>Yearly Saving (₹)</b></td>
        <td style='padding:10px; text-align:center;'>₹ {yearly_saving:,.0f}</td>
        <td style='padding:10px; text-align:center;'>₹ {yearly_saving:,.0f}</td>
    </tr>
    <tr>
        <td style='padding:10px;'><b>Payback Period (Years)</b></td>
        <td style='padding:10px; text-align:center;'>{payback_with_subsidy:.1f} Years</td>
        <td style='padding:10px; text-align:center;'>{payback_without_subsidy:.1f} Years</td>
    </tr>
    </table>
    """
    st.markdown(roi_table, unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("<p style='text-align:center; color: gray; margin-top:20px;'>© 2026 Powerzest | All rights reserved</p>", unsafe_allow_html=True)
