import streamlit as st


def main():
    st.set_page_config(page_title="Portfolio", page_icon=":briefcase:", layout="wide")

    st.markdown(
        """
        <style>
            .header {
                background-color: #282c34;
                padding: 20px 10%;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logo {
                color: #61dafb;
                font-size: 24px;
                font-weight: bold;
                text-decoration: none;
            }
            .navbar a {
                color: #fff;
                font-size: 18px;
                font-weight: bold;
                text-decoration: none;
                margin-left: 20px;
                padding-bottom: 5px;
                border-bottom: 2px solid transparent;
                transition: border-bottom-color 0.3s;
            }
            .navbar a:hover {
                border-bottom-color: #61dafb;
            }
            .section {
                padding: 50px 10%;
                background-color: #121212;
            }
            .section h2 {
                color: #61dafb;
                font-size: 36px;
                margin-bottom: 30px;
            }
            .section p, .section ul {
                color: #fff;
                font-size: 20px;
                line-height: 1.5;
            }
            .contact {
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin-top: 50px;
            }
            .contact a img {
                width: 60px;
                height: 60px;
                margin-right: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <header class="header">
            <a href="#home" class="logo">Portfolio</a>
            <nav class="navbar">
                <a href="#home">Home</a>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#certifications">Certifications</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </nav>
        </header>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <section id="home" class="section">
            <div class="home-content">
                <h3>Hello, It's Me</h3>
                <h1>Kishan Kumar S</h1>
                 </div>
        </section>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <section id="about" class="section">
            <h2>About</h2>
            <p>Aspiring Data Learning Scientist. Passionate about leveraging the power of data to drive meaningful insights
            and innovations. Proficient in Python, C, C++, Java, with a strong foundation in data science principles.
            Currently honing skills in machine learning algorithms, I am on a journey to contribute to cutting-edge
            advancements in artificial intelligence. Excited about the intersection of technology and problem-solving, I
            thrive on challenges that require creative solutions.</p>
        </section>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <section id="skills" class="section">
            <h2>Skills</h2>
            <ul>
                <li>Data Analysis</li>
                <li>Prompt Engineering</li>
                <li>Data Visualization</li>
                <li>Machine Learning</li>
                <li>Programming</li>
                <li>Problem Solving</li>
            </ul>
        </section>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <section id="certifications" class="section">
            <h2>Certifications</h2>
            <ul>
                <li>Data Analysis using Python - <a href="https://credly.com/badges/ef16ffb5-db3c-4ded-b41b-fcaa35b2d2da/linked_in_profile" target="_blank">link</a></li>
                <li>Python for Data Science - <a href="https://www.credly.com/badges/f7efca15-02ec-46be-a0ac-84c62fea02b3/linked_in_profile" target="_blank">link</a></li>
                <li>Data Visualization Using Python - <a href="https://www.credly.com/badges/a33539eb-e491-449c-8a12-6f1f925248ba/linked_in_profile" target="_blank">link</a></li>
                <li>Applied Data Science - <a href="https://www.credly.com/badges/7b399bf8-3691-4ede-b4a9-77cfa15fb325/linked_in_profile" target="_blank">link</a></li>
                <li>Machine Learning - <a href="https://courses.cognitiveclass.ai/certificates/a3fde26a28a04c60adab05199e3294d4" target="_blank">link</a></li>
                <li>Prompt Engineering - <a href="https://courses.cognitiveclass.ai/certificates/e605bffd4da945149049fe4a2955efd4" target="_blank">link</a></li>
                <li>Data Science Methodologies - <a href="https://www.credly.com/badges/70ae2196-2b81-4544-b703-16d7b09cdccb/linked_in_profile" target="_blank">link</a></li>
            </ul>
        </section>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <section id="projects" class="section">
            <h2>Projects</h2>
            <ul>
                <li>Emotion Detection - <a href="https://github.com/Kishankumar1328/Emotion-detection" target="_blank">link</a></li>
                <li>Sentiment Analysis - <a href="https://github.com/Kishankumar1328/sentiment_analysis-with-gradio" target="_blank">link</a></li>
                <li>Lung Cancer Analysis - <a href="https://github.com/Kishankumar1328/lung_cancer_analysis" target="_blank">link</a></li>
                <li>Semiconductor stock Dashboard - <a href="https://github.com/Kishankumar1328/SEMICONDUCTOR-STOCK-DASHBOARD" target="_blank">link</a></li>
                <li>Stock Prediction - <a href="https://github.com/Kishankumar1328/Stock-prediction" target="_blank">link</a></li>
            </ul>
        </section>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <section id="contact" class="section">
            <h2>Contact</h2>
            <div class="contact">
                <a href="https://github.com/Kishankumar1328" target="_blank">GitHub</a>
                <a href="https://www.linkedin.com/in/kishan-kumar-037175259/" target="_blank">LinkedIn</a>
                <a href="mailto:krss132005@gmail.com" target="_blank">Email</a>
                <a href="https://discord.com/invite/tenacious_quail_34080" target="_blank">Discord</a>
            </div>
        </section>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
