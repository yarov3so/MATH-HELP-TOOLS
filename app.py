import streamlit as st

st.set_page_config(
    page_title="Math Help Tools",
    page_icon="MHT.png", 
)

st.image('MHT.png', width=320, use_container_width=True)
st.text("")

# st.markdown(
#     """
#     <div style="display: flex; justify-content: center;">
#         <img src="https://raw.githubusercontent.com/yarov3so/MATH-HELP-TOOLS/433fb18a9ddcef6fd7dd5c78d3288325724037fa/MHT.png" alt="Centered Image" width="300">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

#st.title("Math Help Tools")

st.markdown("###### Below are tools designed to simplify tedious calculations while also serving as valuable learning resources, offering clear, step-by-step breakdowns of each process.")

st.markdown("""
- [Basic Statistical Measurements](https://basicstat.streamlit.app)  
  Calculates range, mean, mean deviation, median and mode(s), if any.  
- [Percentile Rank Calculator](https://prcalc.streamlit.app)  
  Calculates the percentile rank of all values in a data set.  
  Supports suppressed value ranges.  
  Finds values corresponding to a given percentile rank.  
- [Stem and Leaf Plot Generator](https://slplotgen.streamlit.app)  
  Generates a compact and a full stem and leaf plot for a (reasonably well-behaved) set of values.  
- [Double Stem and Leaf Plot Generator](https://doubleslplotgen.streamlit.app)    
  Generates a compact and a full double stem and leaf plot for two (reasonably well-behaved) sets of values.  
- [Mayer Line Calculator](https://mayerline.streamlit.app)  
  Produces the equation of the line of best fit in slope-intercept form using the Mayer line method.  
  This tool can be also used to find the equation of a line passing through two points.  
- [Median-Median Line Calculator](https://medmedline.streamlit.app)  
  Produces the equation of the line of best fit in slope-intercept form using the Median-Median method.
- [Contingency Table Generator](https://conttablegen.streamlit.app)  
  Produces a contingency table for a set of data points.  
  Estimates the linear correlation coefficient.
- [Dijkstra's Shortest Path Calculator](https://dijkstracalc.streamlit.app)  
  Finds the shortest path from any node to any other node in a connected graph.   
  Documents each step of Dijkstra's algorithm, producing the distance table in the process.  
  Supports directed and undirected graphs.  
  Edges in an undirected graph need to be specified only once (supports automatic undirectional handling and resolves typos/omissions/inconsistensies).  
- [LinOptCalc - Linear Optimization Calculator](https://linoptcalc.streamlit.app)  
  Carries out the simplex method for linear optimization (minimization and maximization).  
  Thoroughly documents every step in the optimization process.
- [Schedule Helper](https://scheduleh3lper.streamlit.app)  
  A tool for generating and tweaking schedules primarily meant to be used by teachers in Quebec.
  Dynamically recommends a schedule respecting user-specified constraints.
  Detects gaps, overlaps and inconsistensies.
  Generates a Gantt chart of the recommended schedule.
  
""")

st.markdown("""*Crafted by yarov3so*  
<a href="https://www.buymeacoffee.com/yarov3so" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 9em; height: auto; padding-top: 1em;" ></a>""",unsafe_allow_html=True)

