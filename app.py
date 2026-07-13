import streamlit as st
import random
import time

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
# SAFE & BEAUTIFUL CUSTOM CSS (ROMAN ENGLISH FRIENDLY)
# ==========================================
st.markdown(
    """
    <style>
    /* Premium Gradient Background for the entire App */
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4ec 50%, #ffd6e8 100%) !important;
        font-family: 'Outfit', sans-serif;
    }

    /* Elegant Custom Glassmorphism Card styling */
    .premium-card {
        background: rgba(255, 255, 255, 0.65);
        border: 1px solid rgba(255, 105, 180, 0.3);
        border-radius: 20px;
        padding: 24px;
        margin: 15px 0;
        box-shadow: 0 8px 32px 0 rgba(255, 105, 180, 0.15);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        transition: transform 0.3s ease;
    }
    .premium-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(255, 105, 180, 0.25);
    }

    /* Custom Titles & Headings */
    .main-title {
        font-family: 'Playfair Display', serif;
        color: #d6336c !important;
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.2);
    }
    .subtitle {
        color: #9b5de5 !important;
        text-align: center;
        font-style: italic;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* Smooth Custom Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #ff6fa5, #ff9ec4) !important;
        color: white !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 15px rgba(255, 111, 165, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 6px 22px rgba(255, 111, 165, 0.5) !important;
    }
    div.stButton > button:active {
        transform: scale(0.97) !important;
    }

    /* Heartbeat Pulse Animation */
    .heart-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px 0;
    }
    .heart-icon {
        font-size: 5rem;
        animation: heartbeat 1.4s infinite ease-in-out;
        cursor: pointer;
        user-select: none;
    }
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); filter: drop-shadow(0 0 5px rgba(214, 51, 108, 0.3)); }
        25% { transform: scale(1.15); filter: drop-shadow(0 0 15px rgba(214, 51, 108, 0.6)); }
        40% { transform: scale(1.05); filter: drop-shadow(0 0 8px rgba(214, 51, 108, 0.4)); }
        60% { transform: scale(1.15); filter: drop-shadow(0 0 15px rgba(214, 51, 108, 0.6)); }
    }

    /* Floating particles simulation banner */
    .particles-banner {
        text-align: center;
        font-size: 1.5rem;
        letter-spacing: 12px;
        margin: 15px 0;
        animation: floatParticles 4s ease-in-out infinite;
    }
    @keyframes floatParticles {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# INITIALIZE SESSION STATES
# ==========================================
if "welcome_step" not in st.session_state:
    st.session_state.welcome_step = 0
if "heart_clicks" not in st.session_state:
    st.session_state.heart_clicks = 0
if "current_apology_msg" not in st.session_state:
    st.session_state.current_apology_msg = "Niche diye gaye button par click karein aur mere dil ki baat padhein... ❤️"
if "surprise_opened" not in st.session_state:
    st.session_state.surprise_opened = False
if "forgive_status" not in st.session_state:
    st.session_state.forgive_status = None
if "current_memory_index" not in st.session_state:
    st.session_state.current_memory_index = 0

# ==========================================
# 60+ EMOTIONAL APOLOGY MESSAGES (ROMAN ENGLISH)
# ==========================================
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
# APP LAYOUT (MOBILE FIRST DESIGN)
# ==========================================

# Particles animation simulation (Floating Hearts, Stars, Flowers)
st.markdown('<div class="particles-banner">❤️ ✨ 🌸 ⭐ 💖 🌸 ✨ ❤️</div>', unsafe_allow_html=True)

# Main Title & Subtitle
st.markdown('<h1 class="main-title">💖 Dear Ruhii</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">"Ek choti si website... Sirf tumhare liye ❤️"</p>', unsafe_allow_html=True)

# --- 1. BACKGROUND PIANO MUSIC ---
st.markdown("### 🎵 Background Music")
music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" # Soft, nostalgic piano track
st.audio(music_url, format="audio/mp3", loop=True)
st.caption("Music on karne ke liye upar play button press karein! 🎧")

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 2. ANIMATED WELCOME SCREEN (Line by line) ---
st.markdown("### 👋 Message from Hassan")

welcome_sentences = [
    "Hi Ruhii 👋",
    "Aaj main tumse sirf ek baat kehna chahta hoon...",
    "Please poori website dekhna...",
    "Ye sirf website nahi...",
    "Mere dil ki baat hai ❤️"
]

# Render sentences progressively based on state
for i in range(st.session_state.welcome_step + 1):
    if i < len(welcome_sentences):
        st.info(welcome_sentences[i])

# Button to advance the welcome steps
if st.session_state.welcome_step < len(welcome_sentences) - 1:
    if st.button("Aage Padhein... 💌"):
        st.session_state.welcome_step += 1
        st.rerun()
else:
    st.success("Thank you so much poori baat sunne ke liye. Let's explore more down below! 👇")

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 3. IMPORTANT CARDS SECTION ---
st.markdown("### ❤️ Tum Mere Liye Bohat Important Ho")

important_cards = [
    {"icon": "❤️", "title": "Tum meri best friend ho", "desc": "Har ek baat share karna, bematlab hasna, tumse zyada comfortable aur trustworthy friend meri life mein koi nahi hai."},
    {"icon": "😊", "title": "Tumhari smile bohat achi lagti hai", "desc": "Jab tum khush hoti ho, to mujhe lagta hai sab sahi hai. Tumhari smile meri sabse favorite khushi hai."},
    {"icon": "🌸", "title": "Tumhare bina sab adhura lagta hai", "desc": "Din chahe kitna bhi busy ho, tumhare sath bina baat kiye poora din khali khali sa beetta hai."},
    {"icon": "💖", "title": "Mujhe hamari friendship pyari hai", "desc": "Main is dosti ko hamesha dil se laga kar rakhunga. Is rishte ka meri life mein koi badal nahi hai."}
]

# Grid of cards using premium box styles
for card in important_cards:
    st.markdown(
        f"""
        <div class="premium-card">
            <h4 style="color: #d6336c; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                <span>{card['icon']}</span> {card['title']}
            </h4>
            <p style="color: #7a2e4d; font-size: 14px; margin: 0; line-height: 1.5;">{card['desc']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 4. MEMORY CAROUSEL ---
st.markdown("### 📸 Hamari Yaadein")
current_mem = memories[st.session_state.current_memory_index]

# Beautiful Card for Memories
st.markdown(
    f"""
    <div class="premium-card" style="text-align: center; background: rgba(255, 230, 240, 0.85); border: 2px solid #ff6fa5;">
        <span style="font-size: 3.5rem; display: block; margin-bottom: 10px;">{current_mem['icon']}</span>
        <h3 style="color: #d6336c; margin-top: 0; font-family: 'Playfair Display', serif;">{current_mem['title']}</h3>
        <p style="color: #4a1525; font-size: 15px; line-height: 1.6; margin: 0 10px;">"{current_mem['desc']}"</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Navigation Buttons
col_prev, col_next = st.columns(2)
with col_prev:
    if st.button("⬅️ Previous Memory"):
        st.session_state.current_memory_index = (st.session_state.current_memory_index - 1) % len(memories)
        st.rerun()
with col_next:
    if st.button("Next Memory ➡️"):
        st.session_state.current_memory_index = (st.session_state.current_memory_index + 1) % len(memories)
        st.rerun()

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 5. INTERACTIVE HEARTBEAT APOLOGY SECTION ---
st.markdown("### 💖 Tap The Heart")
st.write("Aapki narazgi door karne ke liye maine 60+ emotional messages/apologies likhi hain. Heart par click karein!")

# Large pulsing heart display
st.markdown(
    """
    <div class="heart-container">
        <div class="heart-icon">❤️</div>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("💖 Click to Beat the Heart 💖"):
    st.session_state.heart_clicks += 1
    st.session_state.current_apology_msg = random.choice(apology_messages)
    st.balloons() # Interactive balloon effect

# Dynamic feedback message
st.markdown(
    f"""
    <div style="background: rgba(255, 255, 255, 0.8); border-left: 5px solid #ff6fa5; padding: 15px; border-radius: 12px; margin-top: 10px; text-align: center;">
        <span style="font-size: 11px; font-weight: bold; text-transform: uppercase; color: #ff6fa5; tracking-widest: 1px;">Apology #{st.session_state.heart_clicks}</span>
        <p style="font-size: 16px; font-weight: bold; color: #4a1525; font-style: italic; margin-top: 5px; line-height: 1.5;">
            "{st.session_state.current_apology_msg}"
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 6. APOLOGY LETTER (Typewriter progressive release) ---
st.markdown("### 📝 Dil se Sorry Letter")

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

show_letter = st.checkbox("📖 Click to open the letter...")
if show_letter:
    for line in letter_lines:
        # Centering special lines
        if "Dear Ruhii" in line or "— Hassan" in line or "❤️" == line.strip():
            st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 16px; color: #d6336c;'>{line}</p>", unsafe_allow_html=True)
        else:
            st.write(line)
        time.sleep(0.01) # Soft progressive typing feel

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 7. PROMISE SECTION ---
st.markdown("### 🤝 My Promises to You")

promises = [
    ("🌸 Respect", "Main hamesha tumhari respect karunga, tumhare rules aur limits ki."),
    ("🤍 Better Friend", "Main pehle se behtar, samajhdar dost banne ki koshish karunga."),
    ("😊 Listener", "Main hamesha tumhari baat sununga aur dhyan se samajhunga."),
    ("❤️ No Heartbreak", "Main kabhi jaan bujh kar tumhara dil hurt nahi karunga."),
    ("🌹 High Priority", "Hamari friendship mere liye hamesha sab se important rahegi.")
]

# Use Streamlit expanders as beautiful premium accordion cards
for title, desc in promises:
    with st.expander(f"✨ {title}"):
        st.write(desc)

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 8. SURPRISE FORGIVENESS BOX ---
st.markdown("### 🎁 Surprise Forgiveness Box")

if not st.session_state.surprise_opened:
    if st.button("🎁 Open My Heart ❤️"):
        st.session_state.surprise_opened = True
        st.snow()
        st.rerun()
else:
    st.markdown("<h3 style='text-align: center; color: #d6336c;'>💖 Will You Forgive Me? 💖</h3>", unsafe_allow_html=True)
    
    col_yes, col_no = st.columns(2)
    with col_yes:
        if st.button("❤️ Yes"):
            st.session_state.forgive_status = "yes"
            st.rerun()
    with col_no:
        if st.button("🥺 Let Me Think"):
            st.session_state.forgive_status = "think"
            st.rerun()
            
    if st.session_state.forgive_status == "yes":
        st.balloons()
        st.success("🥹 Thank You Ruhii ❤️ Tumne meri dunya phir se haseen aur beautiful bana di hai. Main hamesha dosti nibhaunga!")
    elif st.session_state.forgive_status == "think":
        st.info("Main hamesha wait karunga... Jitna bhi waqt lage. Kyun ke sachi dosti dubaara nahi milti ❤️")

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 9. ENDING GLOW QUOTE ---
st.markdown(
    """
    <div style="text-align: center; font-size: 1.3rem; font-family: 'Playfair Display', serif; font-style: italic; color: #d6336c; font-weight: bold; margin: 25px 0;">
        "Kuch log life mein special hote hain... <br> Aur tum un mein se ek ho." <br> ❤️
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr style='border: 1px solid rgba(255,105,180,0.15);'>", unsafe_allow_html=True)

# --- 10. FOOTER ---
st.markdown(
    """
    <div style="text-align: center; color: #9b5de5; margin-bottom: 20px;">
        <p style="font-size: 13px; margin-bottom: 5px;">Made with Love, Respect & Hope.</p>
        <p style="font-size: 14px; font-weight: bold; margin-bottom: 0;">Forever Your Best Friend,</p>
        <h3 style="color: #d6336c; margin-top: 5px; font-family: 'Playfair Display', serif;">Hassan ❤️</h3>
    </div>
    """,
    unsafe_allow_html=True
)
