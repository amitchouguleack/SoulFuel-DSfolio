import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="SoulFuel-DSfolio",
    page_icon="🔥",
    layout="wide"
)

# --- Helper Sections ---


def about_me():
    st.header("👨‍💻 About Me")
    st.write(
        """
        I'm **Amit Chougule** — an **AI/ML Architect & Product Engineer** based in Pennsylvania, with 7+ years of experience designing intelligent systems, full-stack ML platforms, and scalable AI solutions.

        I specialize in **GenAI, MLOps, and real-time data pipelines** across healthcare, retail, and manufacturing. My approach blends ethical building, fast learning, and system-first deployment — turning business goals into measurable, data-driven impact.

        **SoulFuel-DSfolio** is my living portfolio: a showcase of original AI/ML projects built for speed, clarity, and recruiter-readiness.
        """
    )

    # Profile Image (AI-style)
    st.markdown(
        """
        <div style="text-align:center;">
            <a href="https://www.linkedin.com/in/amit-chougule-software-developer/" target="_blank">
                <img src="https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?crop=faces&fit=crop&w=400&h=400" 
                     alt="Amit Chougule" 
                     style="width:220px;border-radius:50%;margin-top:15px;">
            </a>
            <p><em>Click the photo to visit my LinkedIn</em></p>
        </div>
        """,
        unsafe_allow_html=True
    )


def skills():
    st.header("⚙️ Core Skills — Expanding & Pushing Limits")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("AI/ML & Data Science"):
            st.write(
                "Python, PyTorch, TensorFlow, Scikit-learn, Hugging Face, LangChain, OpenCV, YOLO")
            st.write(
                "NLP, LLM Fine-tuning, Computer Vision, Pandas, NumPy, Matplotlib, Plotly, XGBoost, LightGBM")
        with st.expander("Backend & Cloud"):
            st.write("FastAPI, Django, Flask, Node.js, Express, REST, GraphQL")
            st.write(
                "MLflow, Docker, Kubernetes, AWS SageMaker, GCP Vertex AI, Azure ML, CI/CD, Airflow, Spark, Kafka, Terraform")
    with col2:
        with st.expander("Frontend & UI"):
            st.write(
                "React.js, Next.js, Angular, Tailwind, Material UI, Redux, D3.js, HTML5, CSS3")
        with st.expander("Databases"):
            st.write(
                "PostgreSQL, MongoDB, MySQL, Redis, Pinecone, FAISS, Elasticsearch, Neo4j, Snowflake, BigQuery")
        with st.expander("Additional Expertise"):
            st.write(
                "MLOps, AI Productization, Real-Time Data Analytics, RPA/Automation, Healthcare & Manufacturing AI Solutions")


def clickable_image(image_url, link_url, caption):
    st.markdown(
        f"""
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" style="width:100%;border-radius:12px;box-shadow:0 0 8px rgba(0,0,0,0.3);">
        </a>
        <p style="text-align:center;font-style:italic;">{caption}</p>
        """,
        unsafe_allow_html=True
    )


def projects():
    st.header("🚀 Featured Projects")

    projects_data = [
        {
            "title": "AI-Powered Investment Navigator",
            "desc": "A financial assistant offering stock suggestions, news analysis, and real-time portfolio tracking.",
            "img": "https://images.unsplash.com/photo-1569025690938-a00729c9e1e0?fit=crop&w=800&q=80",
            "link": "https://github.com/amitchouguleack/AI-Powered-Investment-Navigator-main"
        },
        {
            "title": "USA Housing Price Predictor",
            "desc": "Predicts housing prices using regression and tree-based models. Achieved 88% accuracy.",
            "img": "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?fit=crop&w=800&q=80",
            "link": "https://github.com/amitchouguleack/USA-PricePredict-AI-Powered"
        },
        {
            "title": "Laychatbot",
            "desc": "A LangChain + OpenAI retrieval chatbot that automates Q&A with 95% accuracy.",
            "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?fit=crop&w=800&q=80",
            "link": "https://github.com/amitchouguleack/Laychatbot"
        },
        {
            "title": "SoulMonitor",
            "desc": "Health AI model analyzing wellness data for personalized recommendations.",
            "img": "https://images.unsplash.com/photo-1576765607924-bcd3b1e57c7b?fit=crop&w=800&q=80",
            "link": "https://github.com/amitchouguleack/SoulMonitor"
        },
        {
            "title": "End-to-End ML Pipeline",
            "desc": "A complete ML workflow from preprocessing to deployment — reduced deployment time by 30%.",
            "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?fit=crop&w=800&q=80",
            "link": "https://github.com/amitchouguleack/end-to-end-ml-pipeline"
        },
    ]

    for p in projects_data:
        st.subheader(f"**{p['title']}**")
        st.write(p["desc"])
        clickable_image(p["img"], p["link"], "Click image to view GitHub Repo")
        st.markdown("---")


def experience_education():
    st.header("💼 Experience & Education")
    st.subheader("Experience")
    st.write(
        """
        - **Python Developer / Tech Support — Alcon Vision & Independent Projects** (Jan 2023 – Present)  
        - **Full Stack Developer — Ace Hardware** (Mar 2020 – Nov 2022)  
        - **Front-End Developer — Matel Manufacturing** (Jan 2018 – Oct 2019)
        """
    )
    st.subheader("Education & Learning")
    st.write(
        """
        - Generative AI, LangChain Agents, RLHF, Multi-Cloud MLOps, Zero Trust Security  
        - Ongoing: Federated Learning, XAI, Serverless Deployments, Vector Databases, Data Lakehouses
        """
    )


# --- Main App Layout ---
st.title("🔥 SoulFuel-DSfolio")
st.markdown(
    "**Explore my portfolio of AI/ML projects — built for speed, impact, and clarity.**")

nav_mode = st.radio("Choose Navigation Mode:", [
                    "Sidebar Navbar", "Single Page Scroll"])

if nav_mode == "Sidebar Navbar":
    st.sidebar.title("Navigation")
    section = st.sidebar.radio(
        "Go to", ["About Me", "Skills", "Projects", "Experience & Education"])

    if section == "About Me":
        about_me()
    elif section == "Skills":
        skills()
    elif section == "Projects":
        projects()
    elif section == "Experience & Education":
        experience_education()
else:
    about_me()
    st.markdown("---")
    skills()
    st.markdown("---")
    projects()
    st.markdown("---")
    experience_education()

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center;'>
        Made with 🔥 by <b>Amit Chougule</b> | SoulFuel DSfolio | 100% Python-powered  
        <br>
        📧 <a href="mailto:amitchouguleack@gmail.com">amitchouguleack@gmail.com</a>  
        <br>
        <a href="https://www.linkedin.com/in/amit-chougule-software-developer/" target="_blank">🔗 LinkedIn</a> |
        <a href="https://github.com/amitchouguleack" target="_blank">🔗 GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
