import streamlit as st 
import time 
from rembg import remove, new_session
from PIL import Image,ImageEnhance
import io 
#Website Title & Header 
st.set_page_config(page_title="AI Background Remover", layout="centered")
st.title("Professional AI Background Remover")
st.write("Bhaiyo, Apni photo upload karein aur ek click mein background saaf karein !")
#Custom CSS for Yellow Button 
st.markdown("""
   <style>
   [data-testid="stFileUploader"] section button {
       background-color: #FFD700 !important;
       color: black !important;
       font-weight: bold !important;
       border-radius:8px !important;
   }
   </style>
""",unsafe_allow_html=True)
#File Uploader 
uploaded_file = st.file_uploader("Apni photo upload karein", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Original Image Display 
    st.subheader("Aapki upload hui photo") 
    input_image = Image.open(uploaded_file)
    st.image(input_image,use_container_width=True)
    # 1. REMOVE BACKGROUND BUTTON 
    if st.button("Remove Background", type="primary"):
        with st.spinner("AI background saaf kar raha hai...Kripya thoda intezar karein"):
            time.sleep(5) # Yeh line 5 seconds tak loading chalaye rakhegi
            session = new_session("u2netp")
            output_image = remove(input_image, session=session)
            #Output Display 
            st.subheader("Background Remove Ho Gaya !")
            st.image(output_image, use_container_width=True)
            # --- BRIGHTNESS SLIDER ---
            brightness = st.slider("Enhance Brightness(Chamak)", 0.5, 2.0, 1.0, 0.1)
            enhancer = ImageEnhance.Brightness(output_image)
            final_image = enhancer.enhance(brightness)
            st.image(final_image,use_container_width=True)
            #Image ko download karne ke liye convert karna 
            buf = io.BytesIO()
            final_image.save(buf, format="PNG")
            
            byte_im = buf.getvalue()
            # 2. DOWNLOAD BUTTON 
            st.download_button(
                label=" Download Clean Image",
                data=byte_im,
                file_name="bg_removed.png",
                mime="image/png"
            ) 
# --- FOOTER SECTION ---
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("**Privacy Policy**\n\nYour images are secure.We process files locally and never store your private photos on our servers.")
with col2:
    st.caption("** Terms of Service**n\nFree to use for personal and commercial projects.Powered by hight_quality open_source AI models.")
with col3:
    st.caption("**Contact & Support**\n\nHave question or feedback? Reach out to us anytime for support and tool updates.")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Copyright 2026 Smart BG Erace | All Rights Reserved</p>", unsafe_allow_html=True)            
    