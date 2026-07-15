import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# 1. Page Config
st.set_page_config(page_title="RANITHRI HEWASILIYAN | Portfolio", layout="wide")

# The 'Invisible Anchor' - this is what the link looks for
st.markdown("<div id='home'></div>", unsafe_allow_html=True)

# --- THE ABSOLUTE FLOATING NAVBAR ---
st.markdown("""
    <style>
        /* This creates a completely independent floating box at the top */
        .super-sticky-nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw; /* Spans the entire viewport width */
            height: 60px;
            background-color: #f8f9fa; /* Sleek light grey background */
            z-index: 999999; /* Forces it to sit on top of everything else */
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 50px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
            border-bottom: 1px solid #e0e0e0;
        }
        
        /* Links inside the floating box */
        .super-sticky-nav a {
            text-decoration: none;
            color: #1a1a1a !important;
            font-weight: bold;
            font-size: 14px;
            letter-spacing: 1px;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }
        
        .super-sticky-nav a:hover {
            color: #007bff !important; /* Changes to blue on hover */
        }

        /* This forces your actual Streamlit content down so it isn't hidden behind the navbar */
        .stApp {
            margin-top: 60px !important;
        }
        
        /* Hides Streamlit's default native header decoration lines that might overlap */
        [data-testid="stHeader"] {
            background-color: rgba(0,0,0,0) !important;
            z-index: 999;
        }
    </style>
    
    <div class="super-sticky-nav">
        <a href="#home">HOME</a>
        <a href="#visualizations">VISUALIZATIONS</a>
        <a href="#projects">ML PROJECTS</a>
        <a href="#articles">ARTICLES</a>
        <a href="#research">RESEARCH</a>
    </div>
""", unsafe_allow_html=True)

# 2. Minimalist CSS
st.markdown("""
    <style>
            html {
  scroll-behavior: smooth;
}
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

    /* Background: Pure Canvas */
    .stApp {
        background-color: #faf9f6; /* Off-white / Eggshell */
        color: #1a1a1a;
    }

    /* Project Card: Clean borders, no shadows */
    .project-card {
        border-top: 1.5px solid #1a1a1a;
        padding-top: 20px;
        padding-bottom: 40px;
        margin-bottom: 20px;
    }

    /* Typography */
    .title-text {
        font-family: 'Libre Baskerville', serif;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .subtitle-text {
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 0.9rem;
        color: #555;
    }
    .project-heading {
        font-family: 'Libre Baskerville', serif;
        font-size: 1.8rem;
        color: #1a1a1a;
        margin-bottom: 8px;
    }
    .tag {
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;
        border: 1px solid #1a1a1a;
        padding: 2px 8px;
        margin-right: 5px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Clean Navigation)

# --- REMOVE SIDEBAR LINK UNDERLINES ---
st.markdown("""
    <style>
        /* Target all links inside the sidebar container */
        [data-testid="stSidebar"] a {
            text-decoration: none !important;
            color: #1a1a1a; /* Changes the link color if you want it darker, or remove this line to keep the default blue */
        }
        
        /* Optional: Add a subtle hover effect so users know it's clickable */
        [data-testid="stSidebar"] a:hover {
            text-decoration: none !important;
            color: #007bff; /* Turns a subtle blue when hovered */
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<p class='subtitle-text'>Get in Touch</p>", unsafe_allow_html=True)
    st.markdown("🔗 ranithric@gmail.com")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/ranithri-hewasiliyan-10036117b)")
    st.markdown("🔗 [GitHub](https://github.com/ranithric)")


# 4. Hero Section
# The visible title
st.markdown("<h1 class='title-text'>RANITHRI HEWASILIYAN | Portfolio</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Everything about Data</p>", unsafe_allow_html=True)
# 1. Define your links
article_url = "https://www.notion.so/About-Me-331099428a098011aee8fff1340a985e?source=copy_link"
image_url = "https://github.com/ranithric-cyber/image-3/blob/aacc3a49cd0fb2a3be923754be31f12e688e741a/2410223.jpg?raw=true"
st.markdown(f"""
    <div style="text-align: left;">
        <a href="{article_url}" target="_blank">
            <img src="{image_url}" 
                 style="width: 100%; max-width: 70px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); transition: 0.3s;"
                 onmouseover="this.style.transform='scale(1.02)'; this.style.opacity='0.9';" 
                 onmouseout="this.style.transform='scale(1)'; this.style.opacity='1';">
        </a>
        <p style="font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #666; margin-top: 10px;">
            <i>Want to get to know more about me? Click me!</i>
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# --- TEXT-ONLY ABOUT WIDGET ---
st.markdown("""
    <div style="padding: 40px 0; max-width: 800px; margin: auto; text-align: center;">
        <h3 style='font-family: "Libre Baskerville", serif; font-style: italic; color: #1a1a1a; border:none; font-size: 1.5rem;'>
            "The goal is to turn data into information, and information into insights."
        </h3>
        <p style='font-family: "Inter", sans-serif; font-weight: 300; line-height: 1.8; color: #444; margin-top: 20px;'>
            I am a <b>Data Analyst & Researcher</b> specializing in 
            Business Intelligence and Data Analytics. I focus on building accurate, scalable 
            data narratives using <b>Tableau, Power BI and Python.</b> My academic 
            background drives me to treat every dataset as a primary source, uncovering 
            truths that help organizations and businesses navigate complex decision making.
        </p>
        <div style="margin-top: 20px;">
            <span style="font-size: 0.8rem; letter-spacing: 1px; text-transform: uppercase; border-right: 1px solid #ccc; padding-right: 15px; margin-right: 15px;">ACURATE</span>
            <span style="font-size: 0.8rem; letter-spacing: 1px; text-transform: uppercase; border-right: 1px solid #ccc; padding-right: 15px; margin-right: 15px;">DECISIONS</span>
            <span style="font-size: 0.8rem; letter-spacing: 1px; text-transform: uppercase;">ON TIME</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("---") # Visual separator before projects begin

# TABLEAU
st.markdown("<div id='visualizations'></div>", unsafe_allow_html=True)
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown("<span class='tag'>Tableau</span><span class='tag'>Power BI</span><span class='tag'>Visualizations</span>", unsafe_allow_html=True)
st.markdown("<h2 class='project-heading'>Correlation between Fertility rate and Life expectancy</h2>", unsafe_allow_html=True)
st.write("This Rosling graph illustrates a negative correlation between fertility rate and life expectancy, where countries with longer life expectancy typically exhibit lower fertility rates. Just click the right arrow button to see how the countries with higher life expectancy tend to have lower fertility rates.")

# Tableau Embed
tab_url = "https://public.tableau.com/views/QuestionBRoslingGraph/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
components.iframe(f"{tab_url}?:showVizHome=no&:embed=true", height=500)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2 class='project-heading'>What if pizza sales ??</h2>", unsafe_allow_html=True)
st.write("By simulating different scenarios of growth and churn rates, this analysis helps identify potential risks and opportunities, allowing the business to optimize sales strategies and improve customer retention. Just check out adjusting two sliders to see how the sales change with different growth and churn rates.")

# Tableau Embed
tab_url = "https://public.tableau.com/views/QuestionEWhatifAnalysis/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
components.iframe(f"{tab_url}?:showVizHome=no&:embed=true", height=500)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2 class='project-heading'>Market Basket Analysis for Global Superstore</h2>", unsafe_allow_html=True)
# 2. Define the exact text split points
first_three_lines = "This analysis highlights purchasing patterns across product sub categories, revealing which items are frequently bought together and enabling more effective cross selling and bundling strategies. In this graph, darker shades indicate strong co-purchase behavior."

# Print the initial 3 lines of text
st.write(first_three_lines)

# 3. Initialize a session state toggle to track if "Read More" has been clicked
if "expanded" not in st.session_state:
    st.session_state.expanded = False

# 4. If expanded, show the rest of the content natively
if st.session_state.expanded:
    st.markdown("""
**Key observations:**
- Categories like Binders, Paper, Storage, Art, Labels show consistently high interactions.
- Categories like Tables, Chairs, Furnishings generally show lower co-occurrence values.
""")
    st.markdown("""
**Practical Actions:**
- Bundle Binders + Storage + Paper
- Recommend Binders and Storage when Art supplies are purchased
- Create discounts for office kits
- Improve cross-selling for low performing combinations like Tables
""")
    # Click to close
    if st.button("Read Less"):
        st.session_state.expanded = False
        st.rerun()
else:
    # If not expanded, just display the subtle link button right under the 3 lines
    if st.button("Read More..."):
        st.session_state.expanded = True
        st.rerun()

# Tableau Embed
tab_url = "https://public.tableau.com/views/QuestionFMarketBasketAnalysis/Sheet3?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
components.iframe(f"{tab_url}?:showVizHome=no&:embed=true", height=500)
st.markdown('</div>', unsafe_allow_html=True)


st.markdown("<h2 class='project-heading'>Story telling with Data</h2>", unsafe_allow_html=True)
# 2. Define the exact text split points
first_three_lines = "This dashboard displays the electric vehicle landscape in Washington state, USA. " \
"The data set consists of 280,000 registartions and 15 columns which is complex in terms of " \
"understanding the insights just looking at the data points in excel format. " \
"But the decision making process has been made easy with the below Power BI dashboard."

# Print the initial 3 lines of text
st.write(first_three_lines)

# 3. Initialize a session state toggle UNIQUE to the EV dashboard
if "ev_expanded" not in st.session_state:
    st.session_state.ev_expanded = False

# 4. If expanded, show the rest of the content natively
if st.session_state.ev_expanded:
    st.markdown("""
**Without using filters, at a glance we can get some overall insights such as,**
- Average miles of all EVs is 107.46 - KPI Card
- Total EVs in the data set is 280,000 - KPI Card
- Tesla is the most popular brand with 114,000 EVs - Bar chart
- In the year 2023 has the highest number of EV registrations - Line chart
- Battery electric vehicles (BEVs) are more popular (80%) than plug-in hybrid electric vehicles (PHEVs) (20%) - Pie chart
- Battery technology has been improved over the years as there are vehicles with more than 300 miles of range in the year 2020 - scatter plot
- Top 10 counties of the state which are using EVs are King (highest), Snohomish, Pierce, Clark, Thurston, Kitsap, Spokane, Whatcom, Skagit and Benton - Treemap
""")
    st.markdown("""
**Using filters which are "Brand", "Model", "Model Year" and tool tips for indepth insights,**
- As per the "at a glance insights" first I have selected Tesla Modle S which has the highest number of registrations and much longer range compared to other EVs in the market.
- Tesla Modle S has the average miles of 228 which exceeds the overall average miles of all EVs in the data set which is 107.46 and it has 7734 EVs registered. 
- But Tesla Modle S has the downward trend in market growth over a decade while having highest number (930) in 2015 and lowest number (80) in 2025. but the overall trend in Tesla brand has an upward trend.
- This model has Battery electric vehicles (BEVs) only and the battery technology has been improved significantly over the years and by 2020 it has range of more than 300 miles.
- King county has the highest number of Tesla Modle S registrations with 3726 EVs and the Skagit county has the lower number of registrations with 113 EVs. further counties can be drilled down to cities to get more insights on the distribution of EVs in the state.

like wise we can select other brands and models to get more insights on the EV landscape in the state and make informed decisions on where to invest in charging infrastructure, which models are more popular and how the market is evolving over time.
""")
    # CRITICAL FIX: Assigned unique key="ev_read_less"
    if st.button("Read Less", key="ev_read_less"):
        st.session_state.ev_expanded = False
        st.rerun()
else:
    # CRITICAL FIX: Assigned unique key="ev_read_more"
    if st.button("Read More...", key="ev_read_more"):
        st.session_state.ev_expanded = True
        st.rerun()


# POWER BI Embed

video_raw_url = "https://github.com/ranithric-cyber/image-1/raw/refs/heads/main/Go%20green.mp4"
st.markdown(f"""
    <div style="text-align: center;">
        <video width="100%" max-width="700px" controls>
            <source src="{video_raw_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
""", unsafe_allow_html=True)

# projects
st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown("<span class='tag'>ML Projects</span>", unsafe_allow_html=True)
st.markdown("<h2 class='project-heading'>RFM Analysis</h2>", unsafe_allow_html=True)
st.write("Customer segmentation based on their purchasing behavior")

st.markdown("""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
    <a href="https://rfm-analysis-by-ranithri.streamlit.app/"_blank" style="text-decoration: none; background-color: #ff4b4b; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
        Open Interactive Dashboard ↗    
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='project-heading'>Tea Crop Prediction</h2>", unsafe_allow_html=True)
st.write("Tea crop prediction based on historical data and environmental factors - COMING SOON....")

st.markdown("""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">
    <a href="https://tea-crop-by-ranithri.streamlit.app/"_blank" style="text-decoration: none; background-color: #ff4b4b; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
        Open app ↗    
    </a>
</div>
""", unsafe_allow_html=True)

# Close project card HTML tag
st.markdown("</div>", unsafe_allow_html=True)

# articles
st.markdown("<div id='articles'></div>", unsafe_allow_html=True)
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown("<span class='tag'>Articles</span><span class='tag'>Analysis</span><span class='tag'>Different Scenarios</span>", unsafe_allow_html=True)
st.markdown("<h2 class='project-heading'>The Psychology of Data Visualization</h2>", unsafe_allow_html=True)
st.write("How many variables can a human brain actually process in one dashboard?")
# 1. Define your links
article_url = "https://www.notion.so/Article-Draft-Artificial-Intelligence-005e7199b7354aae85865c954b5913d7?source=copy_link"
image_url = "https://github.com/ranithric-cyber/image-1/blob/d4b3583844173ae6758b12c90466abc9b6e93adf/The%20Psychology%20of%20Data%20Visualization.jpg?raw=true"

# 2. Display the Clickable Image
st.markdown(f"""
    <div style="text-align: left;">
        <a href="{article_url}" target="_blank">
            <img src="{image_url}" 
                 style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); transition: 0.3s;"
                 onmouseover="this.style.transform='scale(1.02)'; this.style.opacity='0.9';" 
                 onmouseout="this.style.transform='scale(1)'; this.style.opacity='1';">
        </a>
        <p style="font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #666; margin-top: 10px;">
            <i>Click the image above to read the full Article</i>
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='project-heading'>Designing for Decisions</h2>", unsafe_allow_html=True)
st.write("An EV Population Analysis Backed by Data Visualization Theory")
# 1. Define your links
article_url = "https://www.notion.so/331099428a0980de920deb75ba72f226?source=copy_link"
image_url = "https://github.com/ranithric-cyber/image-3/blob/9ddd90849a358d7600abd0c8d45bfa7cd01debcc/photo-1704340142770-b52988e5b6eb.jpg?raw=true"

# 2. Display the Clickable Image
st.markdown(f"""
    <div style="text-align: left;">
        <a href="{article_url}" target="_blank">
            <img src="{image_url}" 
                 style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); transition: 0.3s;"
                 onmouseover="this.style.transform='scale(1.02)'; this.style.opacity='0.9';" 
                 onmouseout="this.style.transform='scale(1)'; this.style.opacity='1';">
        </a>
        <p style="font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #666; margin-top: 10px;">
            <i>Click the image above to read the full Article</i>
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='project-heading'>Data Visualization in Different Sectors</h2>", unsafe_allow_html=True)
st.write("A Finance data analysis using SQL and Power BI")
# 1. Define your links
article_url = "https://app.notion.com/p/COMING-SOON-399099428a09804e8c5ffe8fb38cfea1"
image_url = "https://github.com/ranithric-cyber/image-3/blob/3c56ce265f347697e0238986ca4ea370613a245b/finance%20data.jpg?raw=true" 

# 2. Display the Clickable Image
st.markdown(f"""
    <div style="text-align: left;">
        <a href="{article_url}" target="_blank">
            <img src="{image_url}" 
                 style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); transition: 0.3s;"
                 onmouseover="this.style.transform='scale(1.02)'; this.style.opacity='0.9';" 
                 onmouseout="this.style.transform='scale(1)'; this.style.opacity='1';">
        </a>
        <p style="font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #666; margin-top: 10px;">
            <i>Click the image above to read the full Article</i>
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='project-heading'>Behind the Scenes of RFM Analysis</h2>", unsafe_allow_html=True)
st.write("Why and How the Recency Freaquency Monetary Analysis was Done")
# 1. Define your links
article_url = "https://app.notion.com/p/Behind-the-Scenes-of-RFM-Analysis-39d099428a09806aa4c2d52240e7f577"
image_url = "https://github.com/ranithric-cyber/image-3/blob/ca89bcc14c85d12238b2a21b59a5950fd50e6439/Behind%20the%20scenes%20of%20RFM%20analysis.jpg?raw=true" 

# 2. Display the Clickable Image
st.markdown(f"""
    <div style="text-align: left;">
        <a href="{article_url}" target="_blank">
            <img src="{image_url}" 
                 style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); transition: 0.3s;"
                 onmouseover="this.style.transform='scale(1.02)'; this.style.opacity='0.9';" 
                 onmouseout="this.style.transform='scale(1)'; this.style.opacity='1';">
        </a>
        <p style="font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #666; margin-top: 10px;">
            <i>Click the image above to read the full Article</i>
        </p>
    </div>
""", unsafe_allow_html=True)

# RESEARCH
st.markdown("<div id='research'></div>", unsafe_allow_html=True)
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown("<span class='tag'>Research</span><span class='tag'>Python</span><span class='tag'>Predictive Analysis</span>", unsafe_allow_html=True)
st.markdown("<h2 class='project-heading'>Tea Crop Production</h2>", unsafe_allow_html=True)
st.write("This is a summary of my thesis which I did for my Master's degree and in my research I examine how tea crop production can be projected with machine learning techniques based on historical data and environmental factors.")
# 1. Define your links
article_url = "https://www.notion.so/Coming-Soon-331099428a09802e92abe06f01cf6372?source=copy_link"
image_url = "https://github.com/ranithric-cyber/image-2/blob/4f5d86c176388eb8811e762398f3a8ffccf3d797/Development%20of%20a%20Machine%20Learning%20Time%20Series%20Model%20for%20Predicting%20Tea%20Crop%20Production%20Based%20on%20Monsoon%20Rainfall%20in%20Central%20Highlands%2C%20Sri%20Lanka.jpg?raw=true"

# 2. Display the Clickable Image
st.markdown(f"""
    <div style="text-align: left;">
        <a href="{article_url}" target="_blank">
            <img src="{image_url}" 
                 style="width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); transition: 0.3s;"
                 onmouseover="this.style.transform='scale(1.02)'; this.style.opacity='0.9';" 
                 onmouseout="this.style.transform='scale(1)'; this.style.opacity='1';">
        </a>
        <p style="font-family: 'Inter', sans-serif; font-size: 0.9rem; color: #666; margin-top: 10px;">
            <i>Click the image above to read the full Article</i>
        </p>
    </div>
""", unsafe_allow_html=True)

# 6. Footer
# HTML/CSS custom centered way
st.markdown(
    """
    <div style='text-align: center; color: #888888; padding-top: 20px;'>
        © 2026 • Built with Streamlit & Python by Ranithri Hewasiliyan • All Rights Reserved
    </div>
    """,
    unsafe_allow_html=True
)
