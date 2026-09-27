import streamlit as st
import time
import streamlit.components.v1 as components

# --- REFRESHED CLEAN START ---
st.set_page_config(
    page_title="Professional AI Background Remover",
    page_icon="🤖"
)

# --- MONETAG DIRECT VERIFICATION HACK ---
# Is baar hum direct ek bada verification block upar render kar rahe hain
verification_html = """
<html>
    <head>
        <meta name="monetag" content="6d3578b2c52213928343828de8dc8b72">
    </head>
    <body>
        <p style='color: gray; font-size: 11px; text-align: center; margin: 0;'>Verification Connected</p>
    </body>
</html>
"""
components.html(verification_html, height=25)

# --- ISKE NICHE AAPKA BAKI SAARA PURANA TOOL KA CODE REHNE DEIN ---
st.title("🤖 AI Smart BG Remover")


from rembg import remove, new_session
from PIL import Image,ImageEnhance
import io 
#Website Title & Header 
st.set_page_config(page_title="Smart BG Erase", page_icon="👑", layout="centered")
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
if "clean_img" not in st.session_state:
   st.session_state.clean_img = None
if "prev_uploaded_file" not in st.session_state:
   st.session_state.prev_uploaded_file = None 
uploaded_file = st.file_uploader("Apni photo upload karein", type=["png", "jpg", "jpeg"])
if uploaded_file != st.session_state.prev_uploaded_file:
   st.session_state.clean_img = None
   st.session_state.prev_uploaded_file = uploaded_file   
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
            st.session_state.clean_img = output_image
if st.session_state.clean_img is not None:        
      st.subheader("Background Remove Ho Gaya !")
      st.image(st.session_state.clean_img, use_container_width=True)
      # --- BRIGHTNESS SLIDER ---
      brightness = st.slider("Enhance Brightness(Chamak)", 0.5, 2.0, 1.0, 0.1)
      enhancer = ImageEnhance.Brightness(st.session_state.clean_img)
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
    
# HIDING STREAMLIT BRANDING PERMANENTLY FOR ALL USERS
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stViewerBadge"] {display:none !important;}
.viewerBadge_link__z13gW {display:none !important;}
.styles_viewerBadge__CvC9N {display: none !important;}
iframe[title="Managed Hosting Badge"] {display: none !important;}
div[class^="viewerBadge"] {display: none !important;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# -------------------------------------------------------------
# 🎬 🔥 TRENDING DRAMA CLIPS & DOWNLOAD HUB (REPLACING OLD FOOTER)
# -------------------------------------------------------------
st.write("---") # Tool aur drama section ke beech line banayega

# 🔴 SETTINGS: Jab bhi naya drama clip dalo, bas niche wale dono links badal dena!
monetag_link = "https://extg.com"  # Aapka safe Monetag Direct Link
actual_drama_link = "https://google.com" # 👈 Yahan aapne asli drama clip/file ka link daalna hai (Drive, Mega, ya YouTube)

st.markdown("### 🔥 Trending Drama Latest Episodes & Viral Clips HD")
st.write("Aapki pasandeda viral drama scenes, deleted clips aur full episodes HD me watch/download karne ke liye niche diye gaye dono steps ko follow karein:")

# STEP 1: Monetag Click Button
st.write("**👉 Step 1:** Niche diye gaye Green Button par click karke hamari website ko support karein aur link ko unlock karein.")
st.link_button("🚀 Click Here to Support & Unlock Link", monetag_link)

# STEP 2: Asli Drama File Link (Jo ad dekhne ke baad user click karega)
st.write("**👉 Step 2:** Button par click karne ke baad, niche diye gaye link se apna drama watch/download karein.")
st.link_button("🎬 Click Here to Watch / Download Drama", actual_drama_link)

