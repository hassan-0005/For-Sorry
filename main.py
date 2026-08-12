import streamlit as st
import time
import json
import os
import datetime

# -------------------------------------------------------------
# PERSISTENT ANALYTICS LOGGING SYSTEM (FOR HASSAN ONLY)
# -------------------------------------------------------------
LOG_FILE = "ruhii_analytics_log.json"

def load_logs():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {"clicks": [], "page_durations": {}, "notes": []}
    return {"clicks": [], "page_durations": {}, "notes": []}

def save_logs(data):
    try:
        with open(LOG_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def log_click_event(button_name, page_name):
    logs = load_logs()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs["clicks"].append({
        "time": now_str,
        "button": button_name,
        "page": page_name
    })
    save_logs(logs)

def log_page_duration(page_name, duration_seconds):
    if duration_seconds <= 0.5:
        return
    logs = load_logs()
    if page_name not in logs["page_durations"]:
        logs["page_durations"][page_name] = 0.0
    logs["page_durations"][page_name] += round(duration_seconds, 1)
    save_logs(logs)

def log_user_note(note_text):
    logs = load_logs()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logs["notes"].append({
        "time": now_str,
        "text": note_text
    })
    save_logs(logs)

def clear_all_analytics():
    save_logs({"clicks": [], "page_durations": {}, "notes": []})

# Defined Pages List in Roman Urdu
pages = [
    "🌸 Pyara Khushamdeed",
    "🥺 Mujhe Pata Hai Main Ne Hurt Kiya",
    "💗 Humari Dosti Ki Yaadein",
    "💌 Mera Khat Tumhare Naam",
    "🌷 Thoda Waqt Lo Ruhii"
]

# Track time spent on page transition
def record_page_transition(new_page):
    if new_page not in pages:
        new_page = pages[0]
        
    old_page = st.session_state.get("current_tracked_page", None)
    start_time = st.session_state.get("page_start_time", None)
    
    if old_page and start_time and old_page in pages:
        elapsed = time.time() - start_time
        log_page_duration(old_page, elapsed)
        
    st.session_state.current_tracked_page = new_page
    st.session_state.page_start_time = time.time()
    st.session_state.page = new_page

# Set Page Config for Streamlit
st.set_page_config(
    page_title="Ruhii Ke Liye 🌸 | A Magical Apology",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dreamy Princess Light-Pink Aesthetics
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Dancing+Script:wght@400..700&family=Quicksand:wght@300..700&display=swap');

    /* Global Body styling */
    .stApp {
        background: linear-gradient(180deg, #FFF5F7 0%, #FFE4E8 50%, #FFF0F4 100%);
        color: #5A3A42;
        font-family: 'Quicksand', sans-serif;
    }

    /* Headings */
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif !important;
        color: #4A1525 !important;
    }

    /* Glassmorphism Panel */
    .glass-card {
        background: rgba(255, 240, 245, 0.75);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 182, 193, 0.6);
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 12px 32px 0 rgba(230, 150, 170, 0.18);
        margin-bottom: 20px;
    }

    .handwriting {
        font-family: 'Dancing Script', cursive !important;
        font-size: 2.2rem !important;
        color: #9E2A4B !important;
    }

    .letter-text {
        font-family: 'Caveat', cursive !important;
        font-size: 1.8rem !important;
        line-height: 1.5 !important;
        color: #4A1525 !important;
    }

    /* Floating Heart Animation */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    .floating-sticker {
        display: inline-block;
        animation: float 4s ease-in-out infinite;
    }

    /* Custom Streamlit Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FFB6C1 0%, #FFC0CB 50%, #FFB7C5 100%) !important;
        color: #4A1525 !important;
        font-family: 'Cormorant Garamond', serif !important;
        font-weight: 700 !important;
        font-size: 1.3rem !important;
        border-radius: 50px !important;
        border: 2px solid #E6B8B8 !important;
        box-shadow: 0 6px 20px rgba(255, 150, 175, 0.4) !important;
        padding: 12px 32px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }

    .stButton>button:hover {
        transform: scale(1.03) translateY(-2px) !important;
        box-shadow: 0 10px 28px rgba(255, 130, 160, 0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session States
if "page" not in st.session_state or st.session_state.page not in pages:
    st.session_state.page = pages[0]
if "letter_opened" not in st.session_state:
    st.session_state.letter_opened = False
if "wish_sent" not in st.session_state:
    st.session_state.wish_sent = False

if "current_tracked_page" not in st.session_state:
    st.session_state.current_tracked_page = st.session_state.page
if "page_start_time" not in st.session_state:
    st.session_state.page_start_time = time.time()

# Navigation Menu
st.sidebar.title("🌸 Ruhii Ki Duniya")
st.sidebar.markdown("---")

current_page_idx = pages.index(st.session_state.page) if st.session_state.page in pages else 0

selected_page = st.sidebar.radio("Pages Dekhein", pages, index=current_page_idx)
if selected_page != st.session_state.page:
    log_click_event(f"Tab Navigation -> {selected_page}", st.session_state.page)
    record_page_transition(selected_page)
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("🌸 For Ruhii with love")

# -------------------------------------------------------------
# SECRET HASSAN ANALYTICS PORTAL (TOTALLY DISCREET & HIDDEN FROM RUHII)
# -------------------------------------------------------------
with st.sidebar.expander("🤍 Secret Portal"):
    secret_pass = st.text_input("Passkey", type="password", key="admin_pwd", placeholder="Key...")
    if secret_pass == "hassan786" or secret_pass == "hassan123":
        st.success("Khushamdeed Hassan 🤍 (Secret Portal Unlocked)")
        
        # Update current page duration live
        if "page_start_time" in st.session_state and "current_tracked_page" in st.session_state:
            current_dur = time.time() - st.session_state.page_start_time
            log_page_duration(st.session_state.current_tracked_page, current_dur)
            st.session_state.page_start_time = time.time()
            
        logs = load_logs()
        
        st.markdown("#### ⏱️ Har Tab Par Kitna Waqt Guazara")
        durations = logs.get("page_durations", {})
        if durations:
            for page_name, seconds in durations.items():
                mins = round(seconds / 60, 2)
                st.write(f"• **{page_name}**: `{seconds}s` (~{mins} mins)")
        else:
            st.caption("Abhi tak koi duration log nahi hui.")
            
        st.markdown("#### 🖱️ Click Activity Log")
        clicks = logs.get("clicks", [])
        if clicks:
            for c in reversed(clicks):
                st.caption(f"[{c['time']}] *{c['page']}* -> **{c['button']}**")
        else:
            st.caption("Koi click record nahi hua abhi tak.")
            
        st.markdown("#### ✉️ Ruhii Ka Paigham")
        notes = logs.get("notes", [])
        if notes:
            for n in reversed(notes):
                st.write(f"💌 **[{n['time']}]**: {n['text']}")
        else:
            st.caption("Koi message nahi aaya abhi tak.")
            
        if st.button("🗑️ Analytics Reset Karen"):
            clear_all_analytics()
            st.success("Logs reset!")
            st.rerun()

# -------------------------------------------------------------
# PAGE 1 — PYARA KHUSHAMDEED
# -------------------------------------------------------------
if st.session_state.page == "🌸 Pyara Khushamdeed":
    st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <div class="floating-sticker" style="font-size: 4rem;">🌸 ✨ 🌙</div>
            <h1 style="font-size: 4.5rem; margin-bottom: 10px;">Suno Ruhii... 🌸</h1>
            <div class="glass-card" style="max-width: 700px; margin: 0 auto 30px auto;">
                <p class="handwriting">"Main ne ek choti si pyari duniya banayi hai kisi bohat khas ke liye."</p>
                <p style="font-size: 1.1rem; color: #8A3B4E;">Ek aisi jagah jahan sirf sachai, pyari yaadein aur dil ki baatein hain.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Meri Duniya Mein Aao ✨"):
            log_click_event("Button: Meri Duniya Mein Aao ✨", "🌸 Pyara Khushamdeed")
            record_page_transition("🥺 Mujhe Pata Hai Main Ne Hurt Kiya")
            st.rerun()

# -------------------------------------------------------------
# PAGE 2 — MUJHE PATA HAI MAIN NE HURT KIYA
# -------------------------------------------------------------
elif st.session_state.page == "🥺 Mujhe Pata Hai Main Ne Hurt Kiya":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">🥺 🌧️ 🕊️</div>
            <h1 style="font-size: 3.8rem;">Mujhe Pata Hai Tum Naraz Ho... 🥺</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card">
            <p style="font-size: 1.3rem; line-height: 1.8;">
                🌸 <b>Tumne mujh par bharosa kiya tha</b> apni private baat ke sath.<br><br>
                🤍 <b>Tumne mujhe kaha tha ke yeh baat secret rakhoon</b> humare beech.<br><br>
                💔 <b>Main ne bagair soche woh baat batadi</b> usi shakhs ko.<br><br>
                🌧️ <b>Meri ghalti thi</b> aur main bilkul ghalat tha.<br><br>
                🕊️ <b>Koi bahana nahi.</b> Koi safai nahi. Sirf dil se pachtawa hai.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Humari Dosti Ki Yaadein Dekho 💗"):
            log_click_event("Button: Humari Dosti Ki Yaadein Dekho 💗", "🥺 Mujhe Pata Hai Main Ne Hurt Kiya")
            record_page_transition("💗 Humari Dosti Ki Yaadein")
            st.rerun()

# -------------------------------------------------------------
# PAGE 3 — HUMARI DOSTI KI YAADEIN
# -------------------------------------------------------------
elif st.session_state.page == "💗 Humari Dosti Ki Yaadein":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">💖 🦋 🌙</div>
            <h1 style="font-size: 3.8rem;">Humari Dosti 💗</h1>
            <p style="font-size: 1.2rem; color: #7A2B3E;">Har muskurahat, har baat aur har lamha mere dil ke bohat kareeb hai.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="glass-card">
                <h3>🌸 Pehli Yaad</h3>
                <p><b>Jahan se shuruat hui:</b> Jab humari baatein shuru hui aur pata chala ke humara comfort zone bilkul same hai.</p>
            </div>
            <div class="glass-card">
                <h3>🦋 Ek Muskurahat Jo Mujhe Yaad Hai</h3>
                <p><b>Khusboo jaisi warmth:</b> Tumhari woh sachi muskurahat jab sab kuch acha lagta tha.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="glass-card">
                <h3>💗 Sab Se Mazedar Lamha</h3>
                <p><b>Be-ihsiyaas hansi:</b> Woh inside joke jis par hum hase bina nahi reh sakte the!</p>
            </div>
            <div class="glass-card">
                <h3>🌙 Humari Khas Baatein</h3>
                <p><b>Raat ki baatein:</b> Woh guftagu jahan waqt ruk jata tha aur hum zindagi par baatein karte the.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <p class="handwriting">"Kuch log ahista ahista ghar jaisa sukoon ban jaate hain."</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mera Khat Padhon 💌"):
            log_click_event("Button: Mera Khat Padhon 💌", "💗 Humari Dosti Ki Yaadein")
            record_page_transition("💌 Mera Khat Tumhare Naam")
            st.rerun()

# -------------------------------------------------------------
# PAGE 4 — MERA KHAT TUMHARE NAAM
# -------------------------------------------------------------
elif st.session_state.page == "💌 Mera Khat Tumhare Naam":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">🎀 🌹 ✉️</div>
            <h1 style="font-size: 3.8rem;">Mera Khat Tumhare Naam 💌</h1>
        </div>
    """, unsafe_allow_html=True)

    if not st.session_state.letter_opened:
        st.markdown("""
            <div class="glass-card" style="text-align: center; padding: 50px;">
                <div style="font-size: 4rem;">🎀 🪙 🌹</div>
                <h2 style="font-size: 2.5rem;">To: Meri Pyari Ruhii 🌸</h2>
                <p style="font-size: 1.1rem; color: #8A3B4E;">Khas Mohabbat Aur Sachai Ke Sath Sealed</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Khat Kholo 💌"):
                log_click_event("Button: Khat Kholo 💌", "💌 Mera Khat Tumhare Naam")
                st.session_state.letter_opened = True
                st.rerun()
    else:
        st.markdown("""
            <div class="glass-card" style="background: rgba(255, 245, 248, 0.95); border: 2px solid #E6B8B8;">
                <h2 style="font-size: 2.5rem; margin-bottom: 20px;">Pyari Ruhii,</h2>
                <div class="letter-text">
                    <p>Main apne pooray dil se tumse maafi maangna chahta hoon. Main ne tumhara bharosa toda jab tumne mujhe ek baat secret rakhne ko kaha tha, aur main ghalti kar betha.</p>
                    <p>Yeh meri pehli ghalti nahi hai, aur main achi tarah samajhta hoon ke is baar tumhein kyun itna dukh hua hai. Tumhara naraz hona bilkul sahi hai, aur main koi bahana nahi banaunga.</p>
                    <p>Main yeh nahi keh raha ke mujhe abhi maaf kar do. Sacha bharosa lafzon se nahi, balki badle hue amal se banta hai.</p>
                    <p>Jitna waqt aur space tumhein chahiye, bilkul lo. Main humare rishte ki bohat qadar karta hoon.</p>
                </div>
                <br>
                <p class="handwriting" style="text-align: right;">— Hassan 🤍</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Aakhri Page Par Chalo 🌷"):
                log_click_event("Button: Aakhri Page Par Chalo 🌷", "💌 Mera Khat Tumhare Naam")
                record_page_transition("🌷 Thoda Waqt Lo Ruhii")
                st.rerun()

# -------------------------------------------------------------
# PAGE 5 — THODA WAQT LO RUHII
# -------------------------------------------------------------
elif st.session_state.page == "🌷 Thoda Waqt Lo Ruhii":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">🏮 ✨ 🦋</div>
            <h1 style="font-size: 3.8rem;">Thoda Waqt Lo, Ruhii 🌷</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 40px;">
            <p style="font-size: 2.2rem; font-family: 'Cormorant Garamond', serif;">Koi dabaao nahi.</p>
            <p style="font-size: 2.2rem; font-family: 'Cormorant Garamond', serif;">Koi majboori nahi.</p>
            <p style="font-size: 2.5rem; font-family: 'Cormorant Garamond', serif; font-weight: bold; color: #9E2A4B;">Sirf ek sachi aur dil se Maafi.</p>
            <br>
            <p class="handwriting">— Hassan 🤍</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mera Paigham Bhejo ✨"):
            log_click_event("Button: Mera Paigham Bhejo ✨", "🌷 Thoda Waqt Lo Ruhii")
            st.session_state.wish_sent = True
            st.balloons()

    # Message Form
    st.markdown("### 💌 Hassan Ko Koi Paigham Bhejo (Aapki Marzi)")
    with st.form(key="ruhii_note_form"):
        user_note_input = st.text_area("Apna paigham ya baat yahan likhein...", placeholder="Yahan likhein...")
        submit_note = st.form_submit_button("Hassan Ko Paigham Bhejo 🤍")
        if submit_note and user_note_input.strip():
            log_click_event("Submitted Note Back to Hassan", "🌷 Thoda Waqt Lo Ruhii")
            log_user_note(user_note_input.strip())
            st.session_state.note_sent_confirm = True

    if st.session_state.get("note_sent_confirm", False):
        st.success("Shukriya Ruhii! Aapka paigham Hassan tak pohench gaya hai 🤍")

    if st.session_state.wish_sent:
        st.markdown("""
            <div class="glass-card" style="text-align: center; margin-top: 20px; border: 2px solid #FFB6C1;">
                <div style="font-size: 2.5rem;">🌸 💖 ✨</div>
                <p class="handwriting">
                    "Mujhe umeed hai ek din yeh dukh humari dosti ka ek chota sa hissa ban kar reh jayega jo pehle se zyada pakki ho gayi."
                </p>
            </div>
        """, unsafe_allow_html=True)
