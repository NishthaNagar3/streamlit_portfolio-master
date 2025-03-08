import streamlit as st

# snow feature
st.snow()
import streamlit as st

#hiding the  github logo
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True

)
#st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Nihstha Nagar</h1>", unsafe_allow_html=True)
st.empty()
st.markdown("<h2 style='text-align: center;'>Data Analyst</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'> Aggregate, manage, analyze, and visualize data – from facilitating strategic business decisions to propelling transformative global initiatives as a data analyst</h5>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

col1, spacer, col2 ,spacer,col3= st.columns([1,0.1,1,0.1,1])
st.empty()
with col1:
    st.image("images/nt.png")
    st.markdown("<h2 style='text-align: center;'>Collect</h2>", unsafe_allow_html=True)
    
   

with col2:
    st.image("images/exploration.png")
    st.markdown("<h2 style='text-align: center;'>Process</h2>", unsafe_allow_html=True)
    
with col3:
    st.image("images/analytics.png")
    st.markdown("<h2 style='text-align: center;'>Visualise</h2>", unsafe_allow_html=True)


# Custom CSS style for info boxes
info_box_style = """
    <style>
        .info-box-container {
            position: relative;
            display: inline-block;
        }
        .info-box {
            padding: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            height: 150px;
            overflow: auto;
            background-color: #f8f8f8;
            color: #222;
            font-size: 14px;
            line-height: 1.5;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .info-box:hover {
            animation: glow 1s infinite alternate;
        }
        @keyframes glow {
            from {
                box-shadow: 0 0 10px #00ffff;
            }
            to {
                box-shadow: 0 0 20px #00ffff;
            }
        }
    </style>
"""

# Render the CSS style
st.markdown(info_box_style, unsafe_allow_html=True)


# Create a row with three columns
row = st.columns(3)

# Content for the first column
with row[0]:
    content = """
"I excel in efficient data gathering and automation using a variety of tools, including Selenium, BeautifulSoup, and Scrapy."
"""
    st.markdown(f'<div class="info-box-container"><div class="info-box">{content}</div></div>', unsafe_allow_html=True)

# Content for the second column
with row[1]:
    content = """
"As a developing analyst, I specialize in workflow optimization and process innovation, leveraging expertise in data manipulation, integration, spatial analysis, predictive analytics, and more."
"""
    st.markdown(f'<div class="info-box-container"><div class="info-box">{content}</div></div>', unsafe_allow_html=True)

# Content for the third column
with row[2]:
    content = """
"As an emerging analyst, I specialize in data visualization using tools like Tableau to present insights effectively. I excel in creating compelling visuals, analyzing trends, and communicating findings to drive informed decisions."
"""
    st.markdown(f'<div class="info-box-container"><div class="info-box">{content}</div></div>', unsafe_allow_html=True)




    


st.markdown("<h2 style='text-align: center;'>About Me</h2>", unsafe_allow_html=True)    
# Creating a text block in the About Me section
about_me_text = """
I am an aspiring Data Analyst with a passion for transforming complex datasets into actionable insights.
With a keen eye for detail and a robust analytical skill set, I specialize in using tools like Tableau and Python
to uncover patterns and trends that drive strategic business decisions. My background in computer science
and experience in various analytics projects enable me to offer unique perspectives and innovative solutions
to challenges in data visualization and manipulation.
"""

# Optional: You can use markdown to enhance the presentation of the text
st.markdown(about_me_text)

with st.expander("Read more about me"):
    st.markdown("""
    
With a Master’s degree in Computer Application with a Data Science specialization at Bennett University, India, maintaining a stellar SGPA of 9/10. As a Analyst Intern at Amarjivani Pvt Ltd, I leveraged advanced data analytics to improve manufacturing processes and enhance client competitiveness.  Additionally, during my tenure as a Partner Support Specialist at Amazon India, I managed partner relations and performance analytics, utilizing tools like Excel and Google Sheets. My technical skills include Python, Java, SQL, and data visualization tools like Tableau and Matplotlib. I have developed and deployed projects such as an NLP web application and performed comprehensive startup analyses using Streamlit and advanced Pandas
    """)


import streamlit as st

def main():
    st.title("More to Know: My Key Skills")

    # Function to create a collapsible section
    def create_section(title, items):
        with st.expander(title):
            for item in items:
                st.write("- " + item)

    # Create collapsible sections for each skill category
    create_section("Programming Languages", ["Python", "Java", "SQL"])
    create_section("Data Visualization", ["Matplotlib", "Seaborn", "Plotly", "Tableau", "MS-Excel"])
    create_section("Frameworks and Libraries", ["NumPy", "Pandas", "Matplotlib", "Scikit-learn", "Time Series Analysis", "Data Analysis", "Flask", "Streamlit", "Dash", "Web Scraping using Selenium"])

    # Add custom styling
    st.markdown(
        """
        <style>
        .css-1l02zno {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #f0f0f0;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()


import streamlit as st

# Always display the "Sample of My Work" section in the sidebar
st.sidebar.title("Sample of My Work")
st.sidebar.markdown("[Indian Startup Analysis](https://example.com/indian_startup_analysis)")
# Add more content or samples here if needed
st.markdown("<h2 style='text-align: center;'>A sample of my work </h2>", unsafe_allow_html=True)

# Main content
st.write("click the button down or open side navigation bar to see my work [ > ]...")

# Button to open the sidebar
# Button to open the sidebar
if st.button("Go to Sample of My Work", help="If this button doesn't work, open sidebar manually"):
    st.markdown('<style>#MainMenu {visibility: hidden;} .sidebar .sidebar-content {transition: margin-left .5s;margin-top: 0px;} .sidebar .sidebar-content .stSelectbox {visibility: hidden;} .sidebar .sidebar-content .stSelectbox {visibility: visible;}</style>', unsafe_allow_html=True)




# Define custom CSS with keyframe animation for glowing text
glowing_text_css = """
<style>
@keyframes glowing-text {
    0% { text-shadow: 0 0 5px #FF0000; }
    50% { text-shadow: 0 0 20px #FF0000, 0 0 30px #FF0000; }
    100% { text-shadow: 0 0 5px #FF0000; }
}

.glow {
    color: #FF0000;
    animation: glowing-text 1.5s infinite alternate;
}
</style>
"""

# Load the custom CSS
st.markdown(glowing_text_css, unsafe_allow_html=True)

# Use the custom class for the header
st.markdown("<h2 class='glow' style='text-align: center;'>Get In Touch</h2>", unsafe_allow_html = True)
st.markdown("<h4 style='text-align: center;'>Interested in working together? I’d love to hear from you.</h4>", unsafe_allow_html=True)

# Create a form for user inputs
with st.form(key='contact_form'):
    st.write("Contact Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    # Create a submit button for the form
    submit_button = st.form_submit_button(label='Send')

    if submit_button:
        st.write("Thank you for your message!")
        # Here you could add code to handle the submitted data, like sending an email

# Below this line, you can continue with other parts of your Streamlit app

st.markdown("<h4 style='text-align: center;'>deepakverma41998@gmail.com</h4>", unsafe_allow_html=True)









