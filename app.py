import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pytrends.request import TrendReq
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Google Trends Analysis Tool",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Google Trends Analysis Tool")
st.markdown("Analyze search interest trends for different keywords across countries and time periods.")

# Sidebar for user inputs
st.sidebar.header("🔧 Settings")

# Keyword input
keyword = st.sidebar.text_input("Enter a keyword to analyze:", value="AI/ML")

# Timeframe selection
timeframe_options = {
    "Last 12 months": "today 12-m",
    "Last 5 years": "today 5-y", 
    "Last 7 days": "now 7-d",
    "Last 30 days": "today 1-m",
    "Last 90 days": "today 3-m"
}
selected_timeframe = st.sidebar.selectbox("Select time period:", list(timeframe_options.keys()))

# Country selection
country = st.sidebar.text_input("Enter country code (optional, leave empty for worldwide):", value="")

# Analysis type
analysis_type = st.sidebar.selectbox(
    "Choose analysis type:",
    ["Regional Interest", "Time Series", "Keyword Comparison", "All Analyses"]
)

# Initialize pytrends
@st.cache_data
def get_trends_data(keyword, timeframe, geo=''):
    """Get Google Trends data with caching"""
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=geo, gprop='')
        return pytrends
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Main analysis function
def run_analysis():
    if not keyword.strip():
        st.warning("Please enter a keyword to analyze.")
        return
    
    st.info(f"Analyzing trends for: **{keyword}**")
    
    # Get data
    pytrends = get_trends_data(keyword, timeframe_options[selected_timeframe], country)
    if pytrends is None:
        return
    
    # Regional Interest Analysis
    if analysis_type in ["Regional Interest", "All Analyses"]:
        st.header("🌍 Regional Interest Analysis")
        
        try:
            region_data = pytrends.interest_by_region()
            region_data = region_data.sort_values(by=keyword, ascending=False).head(15)
            
            # Create bar chart using plotly
            fig_bar = px.bar(
                x=region_data[keyword],
                y=region_data.index,
                orientation='h',
                title=f"Top Countries searching for '{keyword}'",
                labels={'x': 'Interest', 'y': 'Country'},
                color=region_data[keyword],
                color_continuous_scale='Blues'
            )
            fig_bar.update_layout(height=500)
            st.plotly_chart(fig_bar, use_container_width=True)
            
            # Create choropleth map
            region_data_reset = region_data.reset_index()
            fig_map = px.choropleth(
                region_data_reset,
                locations='geoName',
                locationmode='country names',
                color=keyword,
                title=f"Search Interest for '{keyword}' by Country",
                color_continuous_scale='Blues'
            )
            st.plotly_chart(fig_map, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error in regional analysis: {e}")
    
    # Time Series Analysis
    if analysis_type in ["Time Series", "All Analyses"]:
        st.header("📈 Time Series Analysis")
        
        try:
            time_df = pytrends.interest_over_time()
            
            fig_time = px.line(
                x=time_df.index,
                y=time_df[keyword],
                title=f"Search Interest Over Time for '{keyword}'",
                labels={'x': 'Date', 'y': 'Interest'},
                markers=True
            )
            fig_time.update_traces(line_color='purple')
            fig_time.update_layout(height=400)
            st.plotly_chart(fig_time, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error in time series analysis: {e}")
    
    # Keyword Comparison
    if analysis_type in ["Keyword Comparison", "All Analyses"]:
        st.header("🔍 Keyword Comparison")
        
        # Predefined keywords for comparison
        comparison_keywords = st.multiselect(
            "Select keywords to compare:",
            ["Cloud computing", "Data Science", "Web Development", "AI/ML", "Machine Learning", "Python", "JavaScript"],
            default=["AI/ML", "Data Science", "Cloud computing"]
        )
        
        if comparison_keywords:
            try:
                pytrends.build_payload(comparison_keywords, cat=0, timeframe=timeframe_options[selected_timeframe], geo=country, gprop='')
                compare_df = pytrends.interest_over_time()
                
                fig_compare = go.Figure()
                for kw in comparison_keywords:
                    fig_compare.add_trace(
                        go.Scatter(
                            x=compare_df.index,
                            y=compare_df[kw],
                            mode='lines+markers',
                            name=kw
                        )
                    )
                
                fig_compare.update_layout(
                    title="Keyword Comparison Over Time",
                    xaxis_title="Date",
                    yaxis_title="Interest",
                    height=400
                )
                st.plotly_chart(fig_compare, use_container_width=True)
                
            except Exception as e:
                st.error(f"Error in keyword comparison: {e}")

# Run button
if st.sidebar.button("🚀 Run Analysis", type="primary"):
    with st.spinner("Fetching data from Google Trends..."):
        run_analysis()

# Instructions
st.sidebar.markdown("---")
st.sidebar.markdown("### 📖 Instructions")
st.sidebar.markdown("""
1. Enter a keyword to analyze
2. Select a time period
3. Choose analysis type
4. Click 'Run Analysis'
5. View interactive charts
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Built with Streamlit • Data from Google Trends</p>
</div>
""", unsafe_allow_html=True) 