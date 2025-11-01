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
        I'm Amit Chougule — an AI/ML Architect and relentless system optimizer.
        I remix open-source projects into branded, plug-and-play showcases using my Lazy Remix Sprint system.
        SoulFuel-DSfolio is my living portfolio of impact-first, affirmation-driven intelligence.
        """
    )
    profile_path = os.path.join("images", "profile.jpg")
    if os.path.exists(profile_path):
        img = Image.open(profile_path)
        st.image(img, caption="Amit Chougule", use_container_width=True)
    else:
        st.warning("Profile image not found in 'images/profile.jpg'.")


def skills():
    st.header("⚙️ Skills")
    with st.expander("AI / Machine Learning"):
        st.write(
            "- Supervised & unsupervised learning\n- Regression, classification\n- Model tuning and evaluation")
    with st.expander("Deep Learning"):
        st.write(
            "- Neural networks, CNN, RNN\n- Transfer learning\n- Frameworks: TensorFlow, PyTorch")
    with st.expander("Data Science"):
        st.write(
            "- Data wrangling and visualization\n- Statistical analysis\n- Pandas, NumPy, Matplotlib")
    with st.expander("Computer Vision"):
        st.write(
            "- Image classification and detection\n- OpenCV, YOLO\n- Semantic segmentation")
    with st.expander("DevOps"):
        st.write(
            "- CI/CD pipelines\n- Docker, Kubernetes\n- Cloud platforms: AWS, GCP, Azure\n- Monitoring & logging")
    with st.expander("MLOps"):
        st.write("- Model deployment\n- Model monitoring & versioning\n- ML pipelines with Kubeflow / MLflow\n- Scalable model serving")


def projects():
    st.header("🚀 Remix Projects")

    st.subheader("1. AI-Powered Investment Navigator")
    st.write(
        "Intelligent financial assistant that assesses investment options based on user input.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/AI-Powered-Investment-Navigator-main)")
    st.markdown("---")

    st.subheader("2. USA PricePredict AI-Powered")
    st.write("Predicts housing prices using ML models and stock fundamentals.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/USA-PricePredict-AI-Powered)")
    st.markdown("---")

    st.subheader("3. Laychatbot")
    st.write("Chatbot built with LangChain + OpenAI for helpful, engaging responses.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/Laychatbot)")
    st.markdown("---")

    st.subheader("4. SoulMonitor")
    st.write(
        "AI-based mental health support tool that monitors sentiment and offers resources.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/SoulMonitor)")
    st.markdown("---")

    st.subheader("5. End-to-End ML Pipeline")
    st.write(
        "Full ML pipeline covering data ingestion, model training, and deployment.")
    st.markdown(
        "[🔗 GitHub Repo](https://github.com/amitchouguleack/end-to-end-ml-pipeline)")


def experience_education():
    st.header("💼 Experience & Education")
    st.subheader("Experience")
    st.write(
        """
        - AI/ML Architect & Product Engineer (2023–Present)  
        - Full Stack Developer at Ace Hardware (2020–2022)  
        - Front-End Developer at Matel Manufacturing (2018–2019)
        """
    )
    st.subheader("Education")
    st.write(
        """
        - B.S. in Information Technology, Tech University (2014–2018)
        """
    )


def contact_me():
    st.header("📬 Contact Me")
    st.write("Feel free to reach out through any of the platforms below:")
    st.markdown("""
    - **Email:** 1Pixel3Neurons@gmail.com  
    - **LinkedIn:** [linkedin.com/in/1Pixel3Neurons](https://linkedin.com/in/1Pixel3Neurons)  
    - **GitHub:** [github.com/amitchouguleack](https://github.com/amitchouguleack)  
    - **Twitter:** [@1Pixel3Neurons](https://x.com/1Pixel3Neurons)
    """)


# --- Main app ---
st.title("🔥 SoulFuel-DSfolio")
st.markdown(
    "**Explore my AI/ML remix journey — built for impact, speed, and affirmation.**")

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
            "Experience & Education",
            "Contact Me"
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
    elif section == "Contact Me":
        contact_me()

else:
    about_me()
    st.markdown("---")
    skills()
    st.markdown("---")
    projects()
    st.markdown("---")
    experience_education()
    st.markdown("---")
    contact_me()

# Footer
st.markdown("---")
st.markdown(
    "Made with 🔥 by Amit Chougule | SoulFuel | 100% Python-powered")
