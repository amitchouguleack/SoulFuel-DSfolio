import streamlit as st
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="SoulFuel-DSfolio",
    page_icon="🔥",
    layout="wide"
)

# --- About Me ---
st.title("🔥 SoulFuel-DSfolio")
st.header("👨‍💻 About Me")
st.write(
    """
I'm **Amit Chougule** — an **AI/ML Architect & Product Engineer** based in Pennsylvania,
with 7+ years of experience designing intelligent systems, full-stack ML platforms, and scalable AI solutions.

I specialize in **GenAI, MLOps, and real-time data pipelines** across healthcare, retail, and manufacturing.
**SoulFuel-DSfolio** is my living portfolio: a showcase of AI/ML projects built for speed, clarity, and recruiter-readiness.
"""
)

# ✅ Profile Image
linkedin_url = "https://www.linkedin.com/in/amit-chougule-software-developer/"
profile_path = "images/profile.jpg"

if os.path.exists(profile_path):
    st.image(profile_path, caption="Click image to visit LinkedIn 😄", width=200)
    st.markdown(f"[Visit LinkedIn]({linkedin_url})", unsafe_allow_html=True)
else:
    st.warning("⚠️ Profile image not found. Please check 'images/profile.jpg'.")
    st.markdown(f"[Visit LinkedIn]({linkedin_url})", unsafe_allow_html=True)

# --- Skills ---
st.header("⚙️ Core Skills")
col1, col2 = st.columns(2)
with col1:
    st.subheader("AI/ML & Data Science")
    st.write(
        "- Python, PyTorch, TensorFlow, Scikit-learn, Hugging Face, LangChain, OpenCV, YOLO\n"
        "- NLP, LLM Fine-tuning, Computer Vision, Pandas, NumPy, Matplotlib, Plotly, XGBoost, LightGBM"
    )
    st.subheader("Backend & Cloud")
    st.write(
        "- FastAPI, Django, Flask, Node.js, Express, REST, GraphQL\n"
        "- MLflow, Docker, Kubernetes, AWS SageMaker, GCP Vertex AI, Azure ML, CI/CD, Airflow, Spark, Kafka, Terraform"
    )
with col2:
    st.subheader("Frontend & UI")
    st.write(
        "- React.js, Next.js, Angular, Tailwind, Material UI, Redux, D3.js, HTML5, CSS3")
    st.subheader("Databases & Additional")
    st.write(
        "- PostgreSQL, MongoDB, MySQL, Redis, Pinecone, FAISS, Elasticsearch, Neo4j, Snowflake, BigQuery\n"
        "- MLOps, AI Productization, Real-Time Data Analytics, RPA/Automation, Healthcare & Manufacturing AI Solutions"
    )

# --- Projects ---
st.header("🚀 Featured Projects")

projects = [
    {
        "title": "AI-Powered Investment Navigator",
        "desc": "A financial assistant offering stock suggestions, news analysis, and real-time portfolio tracking.",
        "img": "https://images.pexels.com/photos/6801874/pexels-photo-6801874.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://huggingface.co/spaces/amitchouguleack/AI-Powered-Investment-Navigator"
    },
    {
        "title": "USA Housing Price Predictor",
        "desc": "Predicts housing prices using regression and tree-based models. Achieved 88% accuracy.",
        "img": "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?fit=crop&w=800&q=80",
        "url": "https://usa-pricepredict-ai-powered-house-price-prediction-n5kvqcs6dgi.streamlit.app/"
    },
    {
        "title": "Laychatbot",
        "desc": "A LangChain + OpenAI retrieval chatbot that automates Q&A with 95% accuracy.",
        "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?fit=crop&w=800&q=80",
        "url": "https://lazychatbot-8epwk7myq9higgrvinv6us.streamlit.app/"
    },
    {
        "title": "SoulMonitor",
        "desc": "Health AI model analyzing wellness data for personalized recommendations.",
        "img": "https://images.pexels.com/photos/8370753/pexels-photo-8370753.jpeg?auto=compress&cs=tinysrgb&w=400",
        "url": "https://dezac4jfrtjmnpt6vtbxko.streamlit.app/"
    },
    {
        "title": "End-to-End ML Pipeline",
        "desc": "A complete ML workflow from preprocessing to deployment — reduced deployment time by 30%.",
        "img": "https://images.pexels.com/photos/6693654/pexels-photo-6693654.jpeg?auto=compress&cs=tinysrgb&w=400",
        "url": "https://end-to-end-ml-pipeline-lite-2gwo5pj2vhqzhzaew3pyq4.streamlit.app/"
    },
]

for proj in projects:
    st.subheader(proj["title"])
    st.write(proj["desc"])
    st.markdown(
        f'<a href="{proj["url"]}" target="_blank"><img src="{proj["img"]}" width="800" height="450" style="object-fit: cover; border-radius: 10px;"></a>',
        unsafe_allow_html=True
    )
    st.markdown("---")

# --- Experience & Education ---
st.header("💼 Experience & Education")
st.subheader("Experience")
st.write(
    "- Python Developer / Tech Support — Alcon Vision & Independent Projects (Jan 2023 – Present)\n"
    "- Full Stack Developer — Ace Hardware (Mar 2020 – Nov 2022)\n"
    "- Front-End Developer — Matel Manufacturing (Jan 2018 – Oct 2019)"
)
st.subheader("Education & Learning")
st.write(
    "- Generative AI, LangChain Agents, RLHF, Multi-Cloud MLOps, Zero Trust Security\n"
    "- Ongoing: Federated Learning, XAI, Serverless Deployments, Vector Databases, Data Lakehouses"
)

# --- Footer ---
st.markdown("---")
st.write("Made with 🔥 by **Amit Chougule** | SoulFuel DSfolio | 100% Python-powered")
st.write("📧 amitchouguleack@gmail.com")
st.write("[LinkedIn](https://www.linkedin.com/in/amit-chougule-software-developer/) | [GitHub](https://github.com/amitchouguleack)")
