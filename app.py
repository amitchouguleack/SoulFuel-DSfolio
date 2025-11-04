import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="SoulFuel-DSfolio",
    page_icon="🔥",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        .clickable-img {
            width: 800px;
            height: 450px;
            object-fit: cover;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }
        .clickable-img:hover {
            transform: scale(1.03);
        }
        .icon-links img {
            width: 30px;
            margin: 0 10px;
            transition: transform 0.2s ease;
        }
        .icon-links img:hover {
            transform: scale(1.2);
        }
    </style>
""", unsafe_allow_html=True)

# --- About Me ---
st.title("🔥 SoulFuel-DSfolio")
st.header("👨‍💻 About Me")
st.write(
    """
Hey there! I'm **Amit Chougule** — an **AI/ML Architect & Product Engineer** based in Pennsylvania 🧠💻
With 7+ years of experience building intelligent systems, full-stack ML platforms, and scalable AI solutions, I turn data into decisions and prototypes into products.

I specialize in **GenAI, MLOps, and real-time data pipelines** across healthcare, retail, and manufacturing.
**SoulFuel-DSfolio** is my living portfolio — a launchpad of AI/ML projects built for speed, clarity, and recruiter-readiness 🚀
"""
)

# ✅ Fixed Profile Image (Hosted URL)
linkedin_url = "https://www.linkedin.com/in/amit-chougule-software-developer/"
github_url = "https://github.com/amitchouguleack"
# Replace with your preferred hosted image
profile_img_url = "https://avatars.githubusercontent.com/u/122617172?v=4"

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{profile_img_url}" style="width:200px; border-radius:50%; margin-bottom:10px;" alt="Profile Image">
        <div style="margin-top:10px;">
            <a href="{linkedin_url}" target="_blank" style="margin-right:20px;">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="30">
            </a>
            <a href="{github_url}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="30">
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Skills ---
st.header("⚙️ Core Skills")
col1, col2 = st.columns(2)
with col1:
    st.subheader("🧠 AI/ML & Data Science")
    st.write(
        "- Python, PyTorch, TensorFlow, Scikit-learn, Hugging Face, LangChain, OpenCV, YOLO\n"
        "- NLP, LLM Fine-tuning, Computer Vision, Pandas, NumPy, Matplotlib, Plotly, XGBoost, LightGBM"
    )
    st.subheader("☁️ Backend & Cloud")
    st.write(
        "- FastAPI, Django, Flask, Node.js, Express, REST, GraphQL\n"
        "- MLflow, Docker, Kubernetes, AWS SageMaker, GCP Vertex AI, Azure ML, CI/CD, Airflow, Spark, Kafka, Terraform"
    )
with col2:
    st.subheader("🎨 Frontend & UI")
    st.write(
        "- React.js, Next.js, Angular, Tailwind, Material UI, Redux, D3.js, HTML5, CSS3")
    st.subheader("🗃️ Databases & More")
    st.write(
        "- PostgreSQL, MongoDB, MySQL, Redis, Pinecone, FAISS, Elasticsearch, Neo4j, Snowflake, BigQuery\n"
        "- MLOps, AI Productization, Real-Time Analytics, RPA, Healthcare & Manufacturing AI Solutions"
    )

# --- Projects ---
st.header("🚀 Featured Projects")

projects = [
    {
        "title": "AI-Powered Investment Navigator",
        "desc": "📈 Built with Hugging Face + Streamlit, this AI assistant delivers real-time stock tips, sentiment analysis, and portfolio tracking. Used by 100+ users weekly to make smarter investment decisions.",
        "img": "https://images.pexels.com/photos/6801874/pexels-photo-6801874.jpeg?auto=compress&cs=tinysrgb&w=800",
        "url": "https://huggingface.co/spaces/amitchouguleack/AI-Powered-Investment-Navigator"
    },
    {
        "title": "USA Housing Price Predictor",
        "desc": "🏠 Predicts housing prices with 88% accuracy using XGBoost and Random Forest. Trained on 25K+ records, deployed with Streamlit, and perfect for anyone wondering, 'Can I afford this zip code?'",
        "img": "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?fit=crop&w=800&q=80",
        "url": "https://usa-pricepredict-ai-powered-house-price-prediction-n5kvqcs6dgi.streamlit.app/"
    },
    {
        "title": "Laychatbot",
        "desc": "🤖 LangChain + OpenAI chatbot with 95% retrieval accuracy. Handles complex Q&A from custom docs using embeddings + vector search. Basically, your documents' new best friend.",
        "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?fit=crop&w=800&q=80",
        "url": "https://lazychatbot-8epwk7myq9higgrvinv6us.streamlit.app/"
    },
    {
        "title": "SoulMonitor",
        "desc": "💓 Health AI dashboard analyzing sleep, heart rate, and activity. Built with Pandas + Plotly. Offers personalized wellness insights across 30+ metrics — no yoga mat required.",
        "img": "https://images.pexels.com/photos/8370753/pexels-photo-8370753.jpeg?auto=compress&cs=tinysrgb&w=400",
        "url": "https://dezac4jfrtjmnpt6vtbxko.streamlit.app/"
    },
    {
        "title": "End-to-End ML Pipeline",
        "desc": "🛠️ Full ML pipeline from preprocessing to deployment using FastAPI, Docker, and CI/CD. Reduced deployment time by 30% and supports modular plug-and-play architecture.",
        "img": "https://images.pexels.com/photos/6693654/pexels-photo-6693654.jpeg?auto=compress&cs=tinysrgb&w=400",
        "url": "https://end-to-end-ml-pipeline-lite-2gwo5pj2vhqzhzaew3pyq4.streamlit.app/"
    },
]

for proj in projects:
    st.subheader(proj["title"])
    st.write(proj["desc"])
    st.markdown(
        f"""
        <div style="text-align: center;">
            <a href="{proj['url']}" target="_blank">
                <img src="{proj['img']}" class="clickable-img" alt="{proj['title']}">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")

# --- Experience & Education ---
st.header("💼 Experience & Education")
st.subheader("Experience")
st.write(
    "- 🧪 Python Developer / Tech Support — Alcon Vision & Independent Projects (Jan 2023 – Present)\n"
    "- 🛍️ Full Stack Developer — Ace Hardware (Mar 2020 – Nov 2022)\n"
    "- 🏭 Front-End Developer — Matel Manufacturing (Jan 2018 – Oct 2019)"
)
st.subheader("Education & Learning")
st.write(
    "- 📚 Generative AI, LangChain Agents, RLHF, Multi-Cloud MLOps, Zero Trust Security\n"
    "- 🧠 Ongoing: Federated Learning, XAI, Serverless Deployments, Vector Databases, Data Lakehouses"
)

# --- Footer ---
st.markdown("---")
st.write("Made with 🔥 by **Amit Chougule** | SoulFuel DSfolio | 100% Python-powered")
st.write("📧 amitchouguleack@gmail.com")
st.write("[LinkedIn](https://www.linkedin.com/in/amit-chougule-software-developer/) | [GitHub](https://github.com/amitchouguleack)")
