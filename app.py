import streamlit as st
from PIL import Image
import os

# Page config
st.set_page_config(
    page_title="SoulFuel-DSfolio",
    page_icon="🔥",
    layout="wide"
)

# --- Helper functions for sections ---


def about_me():
    st.header("👨‍💻 About Me")
    st.write(
        """
        I'm Amit Chougule — an AI/ML Architect & Product Engineer based in Pennsylvania, with 7+ years of experience designing intelligent systems, full-stack ML platforms, and scalable AI solutions.

        I specialize in GenAI, MLOps, and real-time data pipelines across healthcare, retail, and manufacturing. My approach blends ethical building, fast learning, and remix-first deployment — turning business goals into measurable, data-driven impact.

        SoulFuel-DSfolio is my living portfolio: a remix-first showcase of AI/ML projects built for speed, clarity, and recruiter-readiness.
        """
    )
    profile_path = os.path.join("images", "profile.jpg")
    if os.path.exists(profile_path):
        img = Image.open(profile_path)
        st.image(img, caption="Amit Chougule", use_container_width=True)
    else:
        st.warning("Profile image not found in 'images/profile.jpg'.")


def skills():
    st.header("⚙️ Core Skills — Expanding & Pushing Limits")
    with st.expander("AI/ML & Data Science"):
        st.write(
            "- Python, PyTorch, TensorFlow, Scikit-learn, Hugging Face, LangChain, OpenCV, YOLO")
        st.write(
            "- NLP, LLM Fine-tuning, Computer Vision, Pandas, NumPy, Matplotlib, Plotly, XGBoost, LightGBM")
    with st.expander("Backend & Cloud"):
        st.write("- FastAPI, Django, Flask, Node.js, Express, REST, GraphQL")
        st.write("- MLflow, Docker, Kubernetes, AWS SageMaker, GCP Vertex AI, Azure ML, CI/CD, Airflow, Spark, Kafka, Terraform")
    with st.expander("Frontend & UI"):
        st.write(
            "- React.js, Next.js, Angular, Tailwind, Material UI, Redux, D3.js, HTML5, CSS3")
    with st.expander("Databases"):
        st.write(
            "- PostgreSQL, MongoDB, MySQL, Redis, Pinecone, FAISS, Elasticsearch, Neo4j, Snowflake, BigQuery")
    with st.expander("Programming & Tools"):
        st.write(
            "- JavaScript/TypeScript, C++, Git, Linux, Bash, Jupyter, VS Code, Postman")
    with st.expander("Additional Expertise"):
        st.write(
            "- MLOps, AI Productization, Real-Time Analytics, RPA/Automation, Healthcare & Manufacturing AI")


def projects():
    st.header("🚀 Remix Projects")

    st.subheader("1. AI-Powered Investment Navigator")
    st.write("Engineered a financial assistant offering stock suggestions, news analysis, and real-time portfolio tracking. Increased user decision confidence by 25%.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/AI-Powered-Investment-Navigator-main)")
    st.markdown("---")

    st.subheader("2. USA Housing Price Predictor")
    st.write("Predicted home prices using regression and tree-based models. Achieved 88% accuracy across test datasets.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/USA-PricePredict-AI-Powered)")
    st.markdown("---")

    st.subheader("3. Laychatbot")
    st.write("Built a retrieval-augmented chatbot using LangChain + OpenAI. Achieved 95% accuracy in Q&A automation.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/Laychatbot)")
    st.markdown("---")

    st.subheader("4. SoulMonitor")
    st.write("Developed a health-focused AI model that analyzes user data to deliver personalized wellness recommendations. Improved wellness scores by 20%.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/SoulMonitor)")
    st.markdown("---")

    st.subheader("5. End-to-End ML Pipeline")
    st.write("Designed a complete ML workflow from preprocessing to deployment using scikit-learn. Reduced deployment time by 30%.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/end-to-end-ml-pipeline)")


def experience_education():
    st.header("💼 Experience & Education")
    st.subheader("Experience")
    st.write(
        """
        - Python Developer / Tech Support — Alcon Vision & Independent Projects (Jan 2023 – Present)  
        - Full Stack Developer — Ace Hardware (Mar 2020 – Nov 2022)  
        - Front-End Developer — Matel Manufacturing (Jan 2018 – Oct 2019)
        """
    )
    st.subheader("Education & Learning")
    st.write(
        """
        - Generative AI, LangChain Agents, RLHF, Multi-Cloud MLOps, Zero Trust Security  
        - Ongoing: Federated Learning, XAI, Serverless Deployments, Vector Databases, Data Lakehouses
        """
    )


# --- Main app ---
st.title("🔥 SoulFuel-DSfolio")
st.markdown(
    "**Explore my remix-first portfolio of AI/ML projects — built for speed, impact, and affirmation.**")

nav_mode = st.radio(
    "Choose Navigation Mode:",
    ["Sidebar Navbar", "Single Page Scroll"]
)

if nav_mode == "Sidebar Navbar":
    st.sidebar.title("Navigation")
    section = st.sidebar.radio(
        "Go to",
        [
            "About Me",
            "Skills",
            "Projects",
            "Experience & Education"
        ]
    )

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

# Footer
st.markdown("---")
st.markdown(
    "Made with 🔥 by Amit Chougule | SoulFuel Remix Sprint | 100% Python-powered")
st.markdown("📧 amitchouguleack@gmail.com")
st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/amit-chougule-software-developer/) | [🔗 GitHub](https://github.com/amitchouguleack)")
