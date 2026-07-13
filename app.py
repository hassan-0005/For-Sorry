import streamlit as st
import random
import time
import urllib.parse

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Dear Ruhii ❤️",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# USER CONFIGURATION (Hassan, apna number yahan dalein!)
# ==========================================
# Pakistan format example: "923001234567" (bina "+" ya "-" ke)
# Agar aap isse khali chhorhenge (""), to Ruhii ko WhatsApp contact khud select karna hoga.
HASSAN_WHATSAPP_NUMBER = "" 

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if "current_step" not in st.session_state:
    st.session_state.current_step = 0 # 0: Welcome, 1: Why Special, 2: Memories, 3: Heart & Promises, 4: Letter, 5: Surprise
if "heart_clicks" not in st.session_state:
    st.session_state.heart_clicks = 0
if "current_apology_msg" not in st.session_state:
    st.session_state.current_apology_msg = "Dil par click karein ek sacha maafi message dekhne ke liye... ❤️"
if "surprise_opened" not in st.session_state:
    st.session_state.surprise_opened = False
if "forgive_status" not in st.session_state:
    st.session_state.forgive_status = None
if "current_memory_index" not in st.session_state:
    st.session_state.current_memory_index = 0

# ==========================================
# MAGICAL CUSTOM ROMANTIC CSS & THEME
# ==========================================
# - Strictly NO white-colored text on the page!
# - Beautiful gradients, animations, floating hearts, and soft borders.
st.markdown(
    """
    <style>
    /* Gradient Background for the entire page */
    .stApp {
        background: linear-gradient(135deg, #ffe5ec 0%, #ffc2d1 50%, #ffb3c1 100%) !important;
        font-family: 'Outfit', sans-serif;
    }

    /* Elegant Custom Card styling (Strictly no white text!) */
    .romantic-card {
        background: rgba(255, 255, 255, 0.75);
        border: 2px solid rgba(214, 51, 108, 0.4);
        border-radius: 24px;
        padding: 26px;
        margin: 18px 0;
        box-shadow: 0 10px 30px rgba(214, 51, 108, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .romantic-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 35px rgba(214, 51, 108, 0.25);
    }

    /* Custom Deep Contrast Typography - No White Text! */
    .romantic-title {
        color: #9E0031 !important; /* Deep crimson */
        font-family: 'Playfair Display', serif;
        text-align: center;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 2px;
        text-shadow: 1px 1px 3px rgba(214, 51, 108, 0.2);
    }
    .romantic-subtitle {
        color: #581845 !important; /* Rich deep purple */
        text-align: center;
        font-style: italic;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }
    .romantic-paragraph {
        color: #4a001a !important; /* Dark maroon for premium readability */
        font-size: 1.05rem;
        line-height: 1.6;
        font-weight: 500;
    }
    .accent-highlight {
        color: #d6336c !important;
        font-weight: bold;
    }

    /* Premium Custom Clear Navigation Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #d6336c, #9e0031) !important;
        color: #ffe5ec !important; /* Very soft pink readable text on dark crimson button */
        border: 2px solid #ff85a2 !important;
        border-radius: 40px !important;
        padding: 14px 28px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        box-shadow: 0 6px 20px rgba(214, 51, 108, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        transform: scale(1.04) translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(214, 51, 108, 0.6) !important;
        background: linear-gradient(135deg, #ff4d80, #c70039) !important;
    }
    div.stButton > button:active {
        transform: scale(0.97) !important;
    }

    /* WhatsApp custom link style buttons */
    .whatsapp-btn {
        display: inline-block;
        background: linear-gradient(135deg, #25D366, #128C7E) !important;
        color: white !important;
        text-decoration: none;
        padding: 14px 28px;
        font-weight: 700;
        font-size: 15px;
        border-radius: 40px;
        text-align: center;
        width: 100%;
        box-shadow: 0 6px 20px rgba(18, 140, 126, 0.3);
        transition: all 0.3s ease;
        margin-top: 15px;
    }
    .whatsapp-btn:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 25px rgba(18, 140, 126, 0.5);
    }

    /* Heartbeat Pulse Animation */
    .heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 15px 0;
    }
    .heart-icon {
        font-size: 5.5rem;
        animation: heartbeat 1.3s infinite ease-in-out;
        cursor: pointer;
        user-select: none;
        display: inline-block;
    }
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); filter: drop-shadow(0 0 10px rgba(214, 51, 108, 0.4)); }
        25% { transform: scale(1.18); filter: drop-shadow(0 0 25px rgba(214, 51, 108, 0.8)); }
        40% { transform: scale(1.08); filter: drop-shadow(0 0 15px rgba(214, 51, 108, 0.5)); }
        60% { transform: scale(1.18); filter: drop-shadow(0 0 25px rgba(214, 51, 108, 0.8)); }
    }

    /* Floating particles banner animation (Hearts, Sprinkles) */
    .sprinkles-banner {
        text-align: center;
        font-size: 1.6rem;
        letter-spacing: 15px;
        margin: 10px 0;
        animation: floatSprinkles 3s ease-in-out infinite;
        user-select: none;
    }
    @keyframes floatSprinkles {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-6px) rotate(2deg); }
    }

    /* Custom Streamlit Alert Box Styles to prevent white/light backgrounds from hiding text */
    div[data-testid="stAlert"] {
        border-radius: 16px;
        background-color: rgba(255, 230, 238, 0.9) !important;
        border-left: 6px solid #d6336c !important;
        box-shadow: 0 4px 15px rgba(214, 51, 108, 0.1);
    }
    div[data-testid="stAlert"] p {
        color: #4a001a !important;
        font-weight: 600 !important;
    }

    /* Expander override so text is fully readable and romantic */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(214, 51, 108, 0.2) !important;
        border-radius: 14px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# DATA FOR THE WEB APP (Roman English)
# ==========================================

# 60+ Beautiful Apology Messages in Roman English
apology_messages = [
    "Mujhe tumhari bohat yaad aati hai. Please maaf kar do na... 🥺",
    "Please naraz mat raho, tumhare bina mera din ekdum adhura hai.",
    "Main waqai sorry hoon, mera maqsad tumhara dil dukhana bilkul nahi tha.",
    "Tumhari friendship meri life mein sabse keemti aur pyaari cheez hai. ❤️",
    "I really miss my best friend. Please dubaara pehle jaise ban jao.",
    "Tumse baat kiye bina din adhoora aur udaas lagta hai.",
    "Galti meri hi thi, please mujhe maaf kar do, Ruhii.",
    "Main kabhi tumhara dil dukhane ka soch bhi nahi sakta.",
    "Hassan hamesha tumhara best friend rahega, chahe kuch bhi ho jaye.",
    "Tumhari smile se meri duniya khushnuma ho jati hai. 🌸",
    "Please hamari dosti ko ek aur pyara sa mauka do.",
    "Main tumse dosti khona nahi chahta, tum bohot special ho.",
    "Tum mere liye sabse zyada important ho, Ruhii.",
    "Meri nadaniyo aur ghaltiyo ko bacha samajh kar maaf kar do.",
    "Aapka gussa bilkul sahi hai, par hamari dosti usse bhi badi hai.",
    "Tumhare bina meri hansi aur khushi dono hi adhuri hain.",
    "Main waada karta hoon, aage se aisi galti kabhi nahi hogi. 🤝",
    "Dosti mein choti-moti nok-jhonk to hoti hai, par dooriyan nahi honi chahiye.",
    "Tum meri sabse pyari aur samajhdar dost ho.",
    "Har ek lamha mujhe hamari dosti ki yaad dilata hai.",
    "Main apne bure behavior ke liye dil se sharminda hoon. 😔",
    "Tumse baat karke mera mood kitna bhi kharab ho, automatic theek ho jata hai.",
    "Please meri ek choti si galti ke liye mujhse door mat jao.",
    "I promise, I will always listen to you and value your thoughts.",
    "Tumhari dosti mere liye upar wale ka ek sabse haseen gift hai.",
    "Main tumhara hamesha har khushi aur gham mein sath dunga.",
    "Maafi maangne se koi chota nahi hota, aur tumhare aage main hamesha jhuk sakta hoon.",
    "Ruhii, please ek baar sweet si smile de do na! 😊",
    "Main hamari dosti ko dubaara pehle jaisi mazboot banana chahta hoon.",
    "Tumhare gusse se mera dil andar se bilkul toot jata hai.",
    "Tumhe hurt karna meri life ki sabse badi galti thi.",
    "I really cherish our bond, more than words can ever describe.",
    "Tumhare bina poori duniya ekdum sunsaan lagti hai.",
    "Mere dil mein tumhare liye hamesha be-hisaab respect rahegi.",
    "Chalo gile-shikwe door karte hain aur dubaara dosti ka hath milate hain.",
    "Mujhe maaf kar do, main tumhare chehre par gussa nahi sirf smile dekhna chahta hoon.",
    "Tumhare sath kiye gaye mazaak aur sharartein bohot yaad aati hain.",
    "Dosti ka matlab hi maaf karna hai, aur tumhara dil to bohot bada hai. 💖",
    "Mujhe pata hai main perfect nahi hoon, par tumhare liye behtar dost zaroor banunga.",
    "Our friendship is too precious to lose over a small misunderstanding.",
    "Please smile, aapki khushi se hi meri khushi judi hai.",
    "Main dil se sharminda hoon aur sach mein maafi maangta hoon.",
    "Aap mere liye hamesha sabse upar rahungi, Ruhii.",
    "I will do whatever it takes to fix our friendship.",
    "Maaf kar ke meri dunya ko phir se rangeen bana do.",
    "I miss our endless night chats, sharing random thoughts and theories.",
    "You are my absolute favorite human to talk to, Ruhii.",
    "Galtiyan sabse hoti hain, par dosti ka rishta naseeb walo ko milta hai.",
    "Main tumhari har baat sunne aur samajhne ko ready hoon, please baat karo.",
    "Your friendship means the absolute world to me.",
    "Main apni har galti ko sudhaarne ke liye 100% ready hoon.",
    "Tumhari dosti meri life ki sabse beautiful memory hai jo main kabhi nahi khona chahta.",
    "Without you, my days are just long, silent, and empty.",
    "Please don't shut me out, let's talk and resolve everything.",
    "Let's be best friends again, with double the love and respect! ❤️",
    "You are the glitter and sparkle in my otherwise ordinary life.",
    "I value you more than any words can ever try to express.",
    "Maaf kar do na please, ab bohot gussa ho gaya, ab maan bhi jao. 🥺",
    "Mujhe tumhari haseen aur pyari si hansi dubaara sunni hai.",
    "Hassan is truly, deeply, and unconditionally sorry, Ruhii. ❤️",
    "You are the best best-friend anyone could ever wish for in their life.",
    "I will always protect your feelings and respect your personal choices.",
    "Humari dosti sabse khoobsurat hai, please isse aise tutne mat do."
]

# Memories Data List
memories = [
    {"icon": "✨", "title": "Pehli baar baat hui", "desc": "Wo din jab humari pehli conversation shuru hui thi. Ekdum anjaan thhe hum dono, par us din ke baad se meri life kitni haseen ho gayi!"},
    {"icon": "😂", "title": "Hansi Mazak", "desc": "Bematlab ke jokes par ghanto tak hasna, pagal jaisi baatein karna, aur har pal ko dher saari masti se bhar dena."},
    {"icon": "📸", "title": "Beautiful Memories", "desc": "Humari saari pyari baatein aur lamhe jo hamesha mere dil ke sabse kareeb rahenge. Har ek chat bohot anmol hai."},
    {"icon": "☕", "title": "Random Conversations", "desc": "Raat ke 2 baje wali baatein bina kisi darr ke... jahan humne duniya jahan ki baatein share ki. Wo sukoon behad pyaara hai."},
    {"icon": "🤍", "title": "Har mushkil waqt", "desc": "Jab bhi life ne thoda pareshan kiya, ek dusre ka dhyan rakhna aur humesha support ke liye khade rehna."},
    {"icon": "🌹", "title": "Friendship Forever", "desc": "Ye dosti ek aisi blessing hai jo main kabhi khona nahi chahta. Chahe jo bhi ho, tum hamesha meri sabse pyari dost rahungi."}
]

# ==========================================
# STEP-BY-STEP PAGE ROUTING
# ==========================================

# 1. STEP 0: WELCOME SCREEN
if st.session_state.current_step == 0:
    st.markdown('<div class="sprinkles-banner">❤️ ✨ 🌸 ⭐ 💖</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="romantic-title">💖 Dear Ruhii</h1>', unsafe_allow_html=True)
    st.markdown('<p class="romantic-subtitle">"Ek choti si website... Sirf tumhare liye ❤️"</p>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="romantic-card">
            <h3 style="color: #9E0031; text-align: center;">Welcome Ruhii 👋</h3>
            <p class="romantic-paragraph" style="text-align: center; font-style: italic;">
                "Hi Ruhii... Aaj main tumse sirf ek baat kehna chahta hoon... <br>
                Please poori website ek-ek step kar ke dekhna... <br>
                Ye sirf website nahi... Mere dil ki baat hai ❤️"
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Simple, clear and bold navigation button
    if st.button("Aage Chaliye (Start) ➡️"):
        st.session_state.current_step = 1
        st.rerun()

# 2. STEP 1: WHY YOU MATTER
elif st.session_state.current_step == 1:
    st.markdown('<div class="sprinkles-banner">🌸 🤍 🌸 🤍 🌸</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="romantic-title">Tum Mere Liye Bohat Important Ho ❤️</h1>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="romantic-card">
            <h3 style="color: #9E0031; margin-top:0;">❤️ Tum meri best friend ho</h3>
            <p class="romantic-paragraph">
                Har ek baat share karna, bematlab hasna, tumse zyada comfortable aur trustworthy friend meri life mein koi nahi hai.
            </p>
        </div>
        <div class="romantic-card">
            <h3 style="color: #9E0031; margin-top:0;">😊 Tumhari smile bohat achi lagti hai</h3>
            <p class="romantic-paragraph">
                Jab tum khush hoti ho, to mujhe lagta hai sab sahi hai. Tumhari smile meri sabse favorite khushi hai.
            </p>
        </div>
        <div class="romantic-card">
            <h3 style="color: #9E0031; margin-top:0;">🌸 Tumhare bina sab adhura lagta hai</h3>
            <p class="romantic-paragraph">
                Din chahe kitna bhi busy ho, tumhare sath bina baat kiye poora din khali khali sa beetta hai.
            </p>
        </div>
        <div class="romantic-card">
            <h3 style="color: #9E0031; margin-top:0;">💖 Mujhe hamari friendship pyari hai</h3>
            <p class="romantic-paragraph">
                Main is dosti ko hamesha dil se laga kar rakhunga. Is rishte ka meri life mein koi badal nahi hai.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Piche Jayein"):
            st.session_state.current_step = 0
            st.rerun()
    with col2:
        if st.button("Hamari Yaadein Dekhein ➡️"):
            st.session_state.current_step = 2
            st.rerun()

# 3. STEP 2: MEMORY CAROUSEL
elif st.session_state.current_step == 2:
    st.markdown('<div class="sprinkles-banner">✨ 📸 ✨ 📸 ✨</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="romantic-title">Hamari Yaadein 📸</h1>', unsafe_allow_html=True)
    
    current_mem = memories[st.session_state.current_memory_index]
    
    st.markdown(
        f"""
        <div class="romantic-card" style="text-align: center; background: rgba(255, 230, 240, 0.9); border: 2px solid #ff6fa5;">
            <span style="font-size: 3.5rem; display: block; margin-bottom: 10px;">{current_mem['icon']}</span>
            <h3 style="color: #9E0031; margin-top: 0; font-family: 'Playfair Display', serif;">{current_mem['title']}</h3>
            <p class="romantic-paragraph" style="font-style: italic; font-size: 1.1rem; line-height: 1.6;">
                "{current_mem['desc']}"
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Memory controls
    col_prev_m, col_next_m = st.columns(2)
    with col_prev_m:
        if st.button("⬅️ Previous Memory"):
            st.session_state.current_memory_index = (st.session_state.current_memory_index - 1) % len(memories)
            st.rerun()
    with col_next_m:
        if st.button("Next Memory ➡️"):
            st.session_state.current_memory_index = (st.session_state.current_memory_index + 1) % len(memories)
            st.rerun()
            
    st.write("---")
    
    col_back, col_fwd = st.columns(2)
    with col_back:
        if st.button("⬅️ Back to Benefits"):
            st.session_state.current_step = 1
            st.rerun()
    with col_fwd:
        if st.button("Maafi Heart Box Pe Chalein ➡️"):
            st.session_state.current_step = 3
            st.rerun()

# 4. STEP 3: INTERACTIVE HEART & PROMISES
elif st.session_state.current_step == 3:
    st.markdown('<div class="sprinkles-banner">💖 ❤️ 💖 ❤️ 💖</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="romantic-title">Interactive Apology Heart 💖</h1>', unsafe_allow_html=True)
    
    # Large glowing heartbeat animation
    st.markdown(
        """
        <div class="heart-container">
            <div class="heart-icon">❤️</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="romantic-card" style="text-align: center;">
            <p class="romantic-paragraph">
                Aapki narazgi door karne ke liye maine 60+ emotional messages likhe hain. <br>
                Niche diye gaye button par click karein aur har click par ek sacha message padhein.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("💖 Click to Beat the Heart 💖"):
        st.session_state.heart_clicks += 1
        st.session_state.current_apology_msg = random.choice(apology_messages)
        st.balloons()
    
    # Apology message display (No white text)
    st.markdown(
        f"""
        <div style="background: rgba(255, 230, 238, 0.9); border-left: 6px solid #d6336c; padding: 18px; border-radius: 14px; margin-top: 10px; text-align: center; box-shadow: 0 4px 15px rgba(214, 51, 108, 0.15);">
            <span style="font-size: 12px; font-weight: bold; text-transform: uppercase; color: #d6336c; tracking-widest: 1px;">Maafi Message #{st.session_state.heart_clicks}</span>
            <p style="font-size: 16px; font-weight: bold; color: #4a001a; font-style: italic; margin-top: 5px; line-height: 1.5;">
                "{st.session_state.current_apology_msg}"
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("---")
    st.markdown("### 🤝 My Promises to You")
    promises = [
        ("🌸 Respect", "Main hamesha tumhari respect karunga, tumhare rules aur limits ki."),
        ("🤍 Better Friend", "Main pehle se behtar, samajhdar dost banne ki koshish karunga."),
        ("😊 Listener", "Main hamesha tumhari baat sununga aur dhyan se samajhunga."),
        ("❤️ No Heartbreak", "Main kabhi jaan bujh kar tumhara dil hurt nahi karunga."),
        ("🌹 High Priority", "Hamari friendship mere liye hamesha sab se important rahegi.")
    ]
    for title, desc in promises:
        with st.expander(f"✨ {title}"):
            st.markdown(f"<p style='color: #4a001a; font-weight: 500;'>{desc}</p>", unsafe_allow_html=True)
            
    col_b, col_f = st.columns(2)
    with col_b:
        if st.button("⬅️ Back to Memories"):
            st.session_state.current_step = 2
            st.rerun()
    with col_f:
        if st.button("Dil se Sorry Letter Padhein ➡️"):
            st.session_state.current_step = 4
            st.rerun()

# 5. STEP 4: LETTER FROM HASSAN
elif st.session_state.current_step == 4:
    st.markdown('<div class="sprinkles-banner">✉️ 💌 ✉️ 💌 ✉️</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="romantic-title">Dil se Sorry Letter 📝</h1>', unsafe_allow_html=True)
    
    letter_lines = [
        "Dear Ruhii ❤️",
        "Main perfect nahi hoon, mujhe pata hai...",
        "Kabhi kabhi mujhse nadani mein bohot badi galtiyan ho jati hain...",
        "Lekin main dil se kehta hoon, kabhi bhi jaan bujh kar tumhara dil dukhana nahi chaha...",
        "Tumhari dosti meri life ki sabse khoobsurat aur anmol cheezon mein se ek hai...",
        "Agar meri kisi bhi baat, mazaak ya behavior se tum hurt hui ho...",
        "To main sach mein, dil ki gehraiyon se Sorry kehta hoon... 🥺",
        "Main sirf itna chahta hoon ki hum phir se pehle ki tarah sath has sakein...",
        "Bematlab ki baaton par ladd sakein aur dher saari achi memories bana sakein...",
        "Thank you so much for reading this till the end...",
        "❤️",
        "— Hassan"
    ]
    
    # Premium letter board style (Strictly readable maroon/crimson text)
    st.markdown('<div class="romantic-card" style="border: 2px dashed #d6336c; background: #fff5f8;">', unsafe_allow_html=True)
    for line in letter_lines:
        if "Dear Ruhii" in line or "— Hassan" in line or "❤️" == line.strip():
            st.markdown(f"<p style='text-align: center; font-weight: 800; font-size: 18px; color: #d6336c; margin: 10px 0;'>{line}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: #4a001a; font-size: 15px; font-weight: 500; line-height: 1.6; text-align: center;'>{line}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        if st.button("⬅️ Piche Jayein"):
            st.session_state.current_step = 3
            st.rerun()
    with col_l2:
        if st.button("Surprise Box Kholein 🎁➡️"):
            st.session_state.current_step = 5
            st.rerun()

# 6. STEP 5: SURPRISE BOX & FORGIVENESS WITH NOTIFICATION OPTIONS
elif st.session_state.current_step == 5:
    st.markdown('<div class="sprinkles-banner">🎁 🎉 🎁 🎉 🎁</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="romantic-title">Surprise Forgiveness Box 🎁</h1>', unsafe_allow_html=True)
    
    if not st.session_state.surprise_opened:
        st.markdown(
            """
            <div class="romantic-card" style="text-align: center;">
                <p class="romantic-paragraph" style="font-size: 1.15rem;">
                    Aap is website ke aakhri step par aa gayi hain. <br>
                    Niche diye gaye button par click karein aur Hassan ka dil open karein! ❤️
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("🎁 Open My Heart ❤️"):
            st.session_state.surprise_opened = True
            st.snow()
            st.rerun()
    else:
        st.markdown(
            """
            <div class="romantic-card" style="text-align: center;">
                <h2 style="color: #d6336c; font-family: 'Playfair Display', serif;">💖 Will You Forgive Me? 💖</h2>
                <p class="romantic-paragraph">Sachi dosti rishto se upar hoti hai. Kya aap apne best friend ko maaf karenge?</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col_yes, col_no = st.columns(2)
        with col_yes:
            if st.button("❤️ Yes, I Forgive You"):
                st.session_state.forgive_status = "yes"
                st.rerun()
        with col_no:
            if st.button("🥺 Let Me Think"):
                st.session_state.forgive_status = "think"
                st.rerun()
                
        # --- FORGIVENESS FEEDBACKS WITH ACTIVE NOTIFICATION OPTIONS ---
        if st.session_state.forgive_status == "yes":
            st.balloons()
            st.markdown(
                """
                <div style="background: rgba(230, 248, 235, 0.95); border: 2px solid #2e7d32; border-radius: 16px; padding: 20px; text-align: center; margin-top: 15px;">
                    <span style="font-size: 3rem;">🥹</span>
                    <h3 style="color: #2e7d32; margin-top: 5px;">Thank You Ruhii ❤️</h3>
                    <p style="color: #1b5e20; font-weight: 600; font-size: 15px;">
                        Tumne meri duniya phir se sabse beautiful aur haseen bana di hai! Main is dosti ko hamesha dil se nibhaunga.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Dynamic WhatsApp message generator with actual interactive stats!
            message_text = (
                f"Hi Hassan! ❤️ Maine tumhari website poori dekhi.\n\n"
                f"✨ Maine Interactive Heart ko {st.session_state.heart_clicks} baar click kiya aur aapke sweet messages padhe!\n"
                f"📸 Hamari saari yaadein bhi dubaara dekhin.\n\n"
                f"My Decision: YES, I Forgive You! 🥹 besties forever! ❤️"
            )
            encoded_message = urllib.parse.quote(message_text)
            if HASSAN_WHATSAPP_NUMBER:
                whatsapp_link = f"https://wa.me/{HASSAN_WHATSAPP_NUMBER}?text={encoded_message}"
            else:
                whatsapp_link = f"https://wa.me/?text={encoded_message}"
            
            st.markdown(
                f"""
                <div class="romantic-card" style="text-align: center; border: 2px solid #25D366; background: #e8f5e9; margin-top: 20px;">
                    <h4 style="color: #128C7E; margin-top:0;">Hassan ko bataiye! 📲</h4>
                    <p class="romantic-paragraph" style="font-size: 13.5px;">
                        Niche diye gaye button par click karein taaki Hassan ko pata chale ke aapne use maaf kar diya hai aur kitne heart clicks kiye:
                    </p>
                    <a href="{whatsapp_link}" target="_blank" class="whatsapp-btn">
                        📲 Hassan Ko WhatsApp Par Bhejein ❤️
                    </a>
                    <p style="color: #388e3c; font-size: 12px; font-weight: bold; margin-top: 12px;">
                        Ya phir ye secret code copy karke use WhatsApp karein: <br>
                        <span style="font-family: monospace; background: #c8e6c9; padding: 4px 8px; border-radius: 6px; font-size: 14px;">RUHII-FORGIVES-HASSAN-CLICKED-{st.session_state.heart_clicks}-TIMES-❤️</span>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        elif st.session_state.forgive_status == "think":
            st.markdown(
                """
                <div style="background: rgba(255, 243, 205, 0.95); border: 2px solid #856404; border-radius: 16px; padding: 20px; text-align: center; margin-top: 15px;">
                    <span style="font-size: 3rem;">🥺</span>
                    <h3 style="color: #856404; margin-top: 5px;">Main Wait Karunga</h3>
                    <p style="color: #533f03; font-weight: 600; font-size: 15px;">
                        Main hamesha patience ke sath wait karunga. Take all your time, kyuki sachi dosti kabhi lose nahi karni chahiye. ❤️
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Dynamic WhatsApp message generator with actual interactive stats!
            message_text = (
                f"Hi Hassan. Maine tumhari website dekhi...\n\n"
                f"✨ Maine Interactive Heart ko {st.session_state.heart_clicks} baar click kiya.\n\n"
                f"My Decision: Mujhe thoda waqt chahiye sochne ke liye. 🥺"
            )
            encoded_message = urllib.parse.quote(message_text)
            if HASSAN_WHATSAPP_NUMBER:
                whatsapp_link = f"https://wa.me/{HASSAN_WHATSAPP_NUMBER}?text={encoded_message}"
            else:
                whatsapp_link = f"https://wa.me/?text={encoded_message}"
            
            st.markdown(
                f"""
                <div class="romantic-card" style="text-align: center; border: 2px solid #ffb300; background: #fffde7; margin-top: 20px;">
                    <h4 style="color: #b78103; margin-top:0;">Hassan ko update karein! 📲</h4>
                    <p class="romantic-paragraph" style="font-size: 13.5px;">
                        Hassan ko batane ke liye niche diye gaye button par click karein:
                    </p>
                    <a href="{whatsapp_link}" target="_blank" class="whatsapp-btn" style="background: linear-gradient(135deg, #ffb300, #ff8f00) !important; box-shadow: 0 6px 20px rgba(255,143,0,0.3);">
                        📲 Hassan Ko WhatsApp Par Bhejein 🥺
                    </a>
                    <p style="color: #b78103; font-size: 12px; font-weight: bold; margin-top: 12px;">
                        Ya phir ye secret code copy karke use WhatsApp karein: <br>
                        <span style="font-family: monospace; background: #fff9c4; padding: 4px 8px; border-radius: 6px; font-size: 14px;">RUHII-THINKING-HASSAN-CLICKED-{st.session_state.heart_clicks}-TIMES-🥺</span>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    st.write("---")
    if st.button("⬅️ Letter Par Wapis Jayein"):
        st.session_state.current_step = 4
        st.rerun()

# ==========================================
# ENDING GLOW QUOTE & FOOTER
# ==========================================
st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; font-size: 1.25rem; font-family: 'Playfair Display', serif; font-style: italic; color: #9E0031; font-weight: bold; margin: 15px 0;">
        "Kuch log life mein special hote hain... <br> Aur tum un mein se ek ho." <br> ❤️
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center; color: #581845; padding-bottom: 25px;">
        <p style="font-size: 13px; margin-bottom: 2px; font-weight: 600;">Made with Love, Respect & Hope.</p>
        <p style="font-size: 14px; font-weight: bold; margin-bottom: 0;">Forever Your Best Friend,</p>
        <h3 style="color: #d6336c; margin-top: 2px; font-family: 'Playfair Display', serif;">Hassan ❤️</h3>
    </div>
    """,
    unsafe_allow_html=True
)
