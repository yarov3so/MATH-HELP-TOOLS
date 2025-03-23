import streamlit as st


st.image('MHT.png', width=320, use_container_width=True)

st.title("Math Help Tools")

st.markdown("###### Below are tools designed to simplify tedious calculations while also serving as valuable learning resources, offering clear, step-by-step breakdowns of each process.")

st.markdown("""
- [Basic Statistical Measurements](https://basicstat.streamlit.app)  
  Calculates range, mean, mean deviation, median and mode(s), if any  
- [Percentile Rank Calculator](https://prcalc.streamlit.app)  
  Calculates the percentile rank of all values in a data set  
  Supports suppressed value ranges  
  Finds values corresponding to a given percentile rank  
- [Stem and Leaf Plot Generator](https://slplotgen.streamlit.app)  
  Generates a compact and a full stem and leaf plot for a (reasonably well-behaved) set of values  
- [Double Stem and Leaf Plot Generator](https://doubleslplotgen.streamlit.app)    
  Generates a compact and a full double stem and leaf plot for two (reasonably well-behaved) sets of values  
- [Mayer Line Calculator](https://mayerline.streamlit.app)  
  Produces the equation of the line of best fit in slope-intercept form using the Mayer line method
- [Median-Median Line Calculator](https://medmedline.streamlit.app)  
  Produces the equation of the line of best fit in slope-intercept form using the Median-Median method
- [Dijkstra's Shortest Path Calculator](https://dijkstracalc.streamlit.app)  
  Documents each step of Dijkstra's algorithm, producing the distance table in the process  
  Finds the shortest path from any node to any other node in a connected graph  
  Supports directed and undirected graphs
  Edges in an undirected graph need to be specified only once (supports automatic undirectional handling and resolves typos/omissions/inconsistensies)
- [LinOptCalc - Linear Optimization Calculator](https://linoptcalc.streamlit.app)  
  Carries out the simplex method for linear optimization (minimization and maximization)  
  Thoroughly documents every step in the optimization process
""")

st.markdown("""*Crafted by yarov3so*  
<a href="https://www.buymeacoffee.com/yarov3so" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 9em; height: auto; padding-top: 1em;" ></a>""",unsafe_allow_html=True)

