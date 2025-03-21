import streamlit as st

st.title("Math Help Tools")

st.markdown("###### Below are tools designed to simplify tedious calculations while also serving as valuable learning resources, offering clear, step-by-step breakdowns of each process.")

st.markdown("""
- [Basic Statistical Measurements](https://basicstat.streamlit.app)  
  Calculates range, mean, mean deviation, median and mode(s), if any  
- [Percentile Rank Calculator](https://prcalc.streamlit.app)  
  Calculates the percentile rank of all values in a data set  
  Supports suppressed value ranges.  
  Finds values corresponding to a given percentile rank  
- [Stem and Lead Plot Generator](https://slplotgen.streamlit.app)  
  Generates a compact and a full stem and leaf plot for a (reasonably well-behaved) set of values  
- [Double Stem and Lead Plot Generator](https://doubleslplotgen.streamlit.app)    
  Generates a compact and a full double stem and leaf plot for two (reasonably well-behaved) sets of values  
""")


st.markdown("""*by yarov3so*  
<a href="https://www.buymeacoffee.com/yarov3so" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 9em; height: auto; padding-top: 1em;" ></a>""",unsafe_allow_html=True)

