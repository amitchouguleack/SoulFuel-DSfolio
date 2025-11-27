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
        .center-title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .center-subtitle {
            text-align: center;
            font-size: 24px;
            font-weight: normal;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Centered Title ---
st.markdown('<div class="center-title"> SoulFuel-DSfolio</div>',
            unsafe_allow_html=True)
st.markdown('<div class="center-subtitle">by Amit Chougule</div>',
            unsafe_allow_html=True)
# --- About Me (Profile + Bio Side-by-Side) ---
from PIL import Image

linkedin_url = "https://www.linkedin.com/in/amit-chougule-software-developer/"
github_url = "https://github.com/amitchouguleack"
profile_img_path = "images/pro-pic.jpg"

# --- Minimal CSS for clean look ---
st.markdown("""
    <style>
        .profile-pic {
            border-radius: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 200px;
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

# --- Layout with columns ---
st.header("🧠 About Me")
col1, col2 = st.columns([1, 2])

with col1:
    profile_img = Image.open(profile_img_path)
    st.image(profile_img, caption="Amit Chougule", use_column_width=False)

    st.markdown(f"""
    <div style="text-align: center;" class="icon-links">
        <a href="{linkedin_url}" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
        </a>
        <a href="{github_url}" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    Hi! I'm Amit Chougule — Software Engineer & AI/ML Architect, Product Builder based in Pennsylvania 🧩💻  
    I’ve spent 7+ years designing and deploying intelligent systems, turning data into decisions, prototypes into products, and coffee into code ☕⚙️  

    I specialize in Generative AI, MLOps, and real-time ML pipelines — building full-stack systems that scale, sparkle ✨, and sometimes talk back (thanks LangChain 🤖).  
    My expertise spans cloud-native AI deployments, recommendation systems, chatbots, dashboards, and computer vision, with a proven track record of delivering production-grade solutions that drive measurable business impact.  

    SoulFuel-DSfolio is my living portfolio: a launchpad of AI/ML projects built for speed, clarity, and recruiter-readiness 🚀.  
    It showcases projects like:  
    • Laychabot — RAG chatbot with 95% Q&A accuracy  
    • SoulMonitor — personalized wellness tracker, improved scores by 20%  
    • Investment Navigator — boosted user confidence by 25%  
    • Housing Price Predictor — achieved 88% accuracy  
    • End-to-End ML Pipeline — reduced deployment time by 30%  

    I’ve contributed across industries — from healthcare and retail to manufacturing and finance — with roles at Santander Bank, Ace Hardware, and QVC Corporation, where I engineered automation systems, dashboards, and scalable ML platforms that improved efficiency by up to 30–40%.  

    Let’s connect if you're hiring, building something weird and wonderful, or just want to swap AI memes 🐙📡
    """)

# --- Circle Style CSS ---
st.markdown("""
    <style>
        .profile-pic {
            border-radius: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 200px;
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




# --- Skills ---
st.header("⚙️ Core Skills")
col1, col2 = st.columns(2)
with col1:
    st.subheader("🧠 AI/ML & Data Science")
    st.write("""
- Python, PyTorch, TensorFlow, Scikit-learn, Hugging Face, LangChain, OpenCV, YOLO  
- NLP, LLM Fine-tuning, Computer Vision, Pandas, NumPy, Matplotlib, Plotly, XGBoost, LightGBM
""")
    st.subheader("☁️ Backend & Cloud")
    st.write("""
- FastAPI, Django, Flask, Node.js, Express, REST, GraphQL  
- MLflow, Docker, Kubernetes, AWS SageMaker, GCP Vertex AI, Azure ML, CI/CD, Airflow, Spark, Kafka, Terraform
""")
with col2:
    st.subheader("🎨 Frontend & UI")
    st.write("""
- React.js, Next.js, Angular, Tailwind, Material UI, Redux, D3.js, HTML5, CSS3
""")
    st.subheader("🗃️ Databases & More")
    st.write("""
- PostgreSQL, MongoDB, MySQL, Redis, Pinecone, FAISS, Elasticsearch, Neo4j, Snowflake, BigQuery  
- MLOps, AI Productization, Real-Time Analytics, RPA, Healthcare & Manufacturing AI Solutions
""")

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
    st.markdown(f"""
    <div style="text-align: center;">
        <a href="{proj['url']}" target="_blank">
            <img src="{proj['img']}" class="clickable-img" alt="{proj['title']}">
        </a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

# --- Experience & Education ---
st.header("💼 Experience & Education")

st.subheader("Experience")
st.write("""
- 🤖 Software Engineer — Santander Bank Corporation| Jan 2023 – Present
    • Engineered AI-driven automation systems improving operational efficiency by 25%  
    • Built chatbots, recommendation engines, and ML pipelines for healthcare & retail  
    • Customized open-source AI frameworks for scalability and production readiness  

- 🛍️ Software Engineer — Ace Hardware Corporation | Jan 2021 – Nov 2022 
    • Developed dashboards & inventory systems using Flask, Streamlit, REST APIs  
    • Integrated ML models for demand forecasting, improving efficiency by 30%  
    • Deployed scalable apps on AWS & Heroku with CI/CD pipelines  

- 📺 Software Engineer — QVC Corporation | Jan 2019 – Dec 2020 
    • Built responsive dashboards with React, Bootstrap, and CSS  
    • Streamlined API integrations, reducing bug reports by 40%  
    • Developed reusable UI components and documentation
""")

st.subheader("Education & Learning")
st.write("""
- 📚 Generative AI, LangChain Agents, RLHF, Multi-Cloud MLOps, Zero Trust Security  
- 🧠 Ongoing: Federated Learning, XAI, Serverless Deployments, Vector Databases, Data Lakehouses
""")


# --- Footer ---
st.markdown("---")
st.write("Made with 🔥 by **Amit Chougule** | SoulFuel DSfolio | 100% Python-powered")
st.write("📧 amitchouguleack@gmail.com")
st.write("[LinkedIn](https://www.linkedin.com/in/amit-chougule-software-developer/) | [GitHub](https://github.com/amitchouguleack)")
