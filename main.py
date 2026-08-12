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

# Defined Pages List
pages = [
    "🌸 Dreamy Welcome",
    "🥺 I Know I Hurt You",
    "💗 Our Friendship",
    "💌 My Letter",
    "🌷 Take Your Time"
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

# Set Page Config for Streamlit (Sidebar collapsed & hidden)
st.set_page_config(
    page_title="For Ruhii 🌸 | A Magical Apology",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
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

    /* Hide Streamlit Sidebar Completely & Header */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    header[data-testid="stHeader"] {
        background: transparent !important;
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

# -------------------------------------------------------------
# TOP HEADER WITH DISCREET SECRET PORTAL (TINY HEART CORNER)
# -------------------------------------------------------------
top_col1, top_col2 = st.columns([12, 1])
with top_col2:
    with st.expander("🤍"):
        secret_pass = st.text_input("Key", type="password", key="admin_pwd")
        if secret_pass == "hassan786" or secret_pass == "hassan123":
            st.success("Welcome Hassan 🤍")
            
            # Update duration live
            if "page_start_time" in st.session_state and "current_tracked_page" in st.session_state:
                current_dur = time.time() - st.session_state.page_start_time
                log_page_duration(st.session_state.current_tracked_page, current_dur)
                st.session_state.page_start_time = time.time()
                
            logs = load_logs()
            
            st.markdown("#### ⏱️ Time Spent on Pages")
            durations = logs.get("page_durations", {})
            if durations:
                for page_name, seconds in durations.items():
                    mins = round(seconds / 60, 2)
                    st.write(f"• **{page_name}**: `{seconds}s` (~{mins}m)")
            else:
                st.caption("No data yet.")
                
            st.markdown("#### 🖱️ Clicks Log")
            clicks = logs.get("clicks", [])
            if clicks:
                for c in reversed(clicks):
                    st.caption(f"[{c['time']}] *{c['page']}* -> **{c['button']}**")
            else:
                st.caption("No clicks yet.")
                
            st.markdown("#### ✉️ Notes From Ruhii")
            notes = logs.get("notes", [])
            if notes:
                for n in reversed(notes):
                    st.write(f"💌 **[{n['time']}]**: {n['text']}")
            else:
                st.caption("No notes yet.")
                
            if st.button("🗑️ Reset All"):
                clear_all_analytics()
                st.success("Reset!")
                st.rerun()

# -------------------------------------------------------------
# PAGE 1 — DREAMY WELCOME
# -------------------------------------------------------------
if st.session_state.page == "🌸 Dreamy Welcome":
    st.markdown("""
        <div style="text-align: center; padding: 40px 0;">
            <div class="floating-sticker" style="font-size: 4rem;">🌸 ✨ 🌙</div>
            <h1 style="font-size: 4.5rem; margin-bottom: 10px;">Hey Ruhii... 🌸</h1>
            <div class="glass-card" style="max-width: 700px; margin: 0 auto 30px auto;">
                <p class="handwriting">"Main ne ek choti si pyari duniya banayi hai kisi bohat khas ke liye."</p>
                <p style="font-size: 1.1rem; color: #8A3B4E;">Ek aisi jagah jahan sirf sachai, pyari yaadein aur dil ki baatein hain.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Enter My World ✨"):
            log_click_event("Button: Enter My World ✨", "🌸 Dreamy Welcome")
            record_page_transition("🥺 I Know I Hurt You")
            st.rerun()

# -------------------------------------------------------------
# PAGE 2 — I KNOW I HURT YOU
# -------------------------------------------------------------
elif st.session_state.page == "🥺 I Know I Hurt You":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">🥺 🌧️ 🕊️</div>
            <h1 style="font-size: 3.8rem;">I Know You're Angry... 🥺</h1>
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
        if st.button("See Our Friendship Memories 💗"):
            log_click_event("Button: See Our Friendship Memories 💗", "🥺 I Know I Hurt You")
            record_page_transition("💗 Our Friendship")
            st.rerun()

# -------------------------------------------------------------
# PAGE 3 — OUR FRIENDSHIP
# -------------------------------------------------------------
elif st.session_state.page == "💗 Our Friendship":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">💖 🦋 🌙</div>
            <h1 style="font-size: 3.8rem;">Our Friendship 💗</h1>
            <p style="font-size: 1.2rem; color: #7A2B3E;">Har muskurahat, har baat aur har lamha mere dil ke bohat kareeb hai.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="glass-card">
                <h3>🌸 First Memory</h3>
                <p><b>Jahan se shuruat hui:</b> Jab humari baatein shuru hui aur pata chala ke humara comfort zone bilkul same hai.</p>
            </div>
            <div class="glass-card">
                <h3>🦋 A Smile I Still Remember</h3>
                <p><b>Khusboo jaisi warmth:</b> Tumhari woh sachi muskurahat jab sab kuch acha lagta tha.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="glass-card">
                <h3>💗 The Funniest Moment</h3>
                <p><b>Be-ihsiyaas hansi:</b> Woh inside joke jis par hum hase bina nahi reh sakte the!</p>
            </div>
            <div class="glass-card">
                <h3>🌙 Our Favorite Conversation</h3>
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
        if st.button("Read My Letter 💌"):
            log_click_event("Button: Read My Letter 💌", "💗 Our Friendship")
            record_page_transition("💌 My Letter")
            st.rerun()

# -------------------------------------------------------------
# PAGE 4 — MY LETTER
# -------------------------------------------------------------
elif st.session_state.page == "💌 My Letter":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">🎀 🌹 ✉️</div>
            <h1 style="font-size: 3.8rem;">My Letter To You 💌</h1>
        </div>
    """, unsafe_allow_html=True)

    if not st.session_state.letter_opened:
        st.markdown("""
            <div class="glass-card" style="text-align: center; padding: 50px;">
                <div style="font-size: 4rem;">🎀 🪙 🌹</div>
                <h2 style="font-size: 2.5rem;">To: Dearest Ruhii 🌸</h2>
                <p style="font-size: 1.1rem; color: #8A3B4E;">Khas Mohabbat Aur Sachai Ke Sath Sealed</p>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Open the Letter 💌"):
                log_click_event("Button: Open the Letter 💌", "💌 My Letter")
                st.session_state.letter_opened = True
                st.rerun()
    else:
        st.markdown("""
            <div class="glass-card" style="background: rgba(255, 245, 248, 0.95); border: 2px solid #E6B8B8;">
                <h2 style="font-size: 2.5rem; margin-bottom: 20px;">Dear Ruhii,</h2>
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
            if st.button("Go to Final Page 🌷"):
                log_click_event("Button: Go to Final Page 🌷", "💌 My Letter")
                record_page_transition("🌷 Take Your Time")
                st.rerun()

# -------------------------------------------------------------
# PAGE 5 — TAKE YOUR TIME
# -------------------------------------------------------------
elif st.session_state.page == "🌷 Take Your Time":
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 3rem;">🏮 ✨ 🦋</div>
            <h1 style="font-size: 3.8rem;">Take Your Time, Ruhii 🌷</h1>
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
        if st.button("Send My Wish ✨"):
            log_click_event("Button: Send My Wish ✨", "🌷 Take Your Time")
            st.session_state.wish_sent = True
            st.balloons()

    # Message Form
    st.markdown("### 💌 Hassan Ko Koi Paigham Bhejo (Optional)")
    with st.form(key="ruhii_note_form"):
        user_note_input = st.text_area("Apna paigham ya baat yahan likhein...", placeholder="Yahan likhein...")
        submit_note = st.form_submit_button("Hassan Ko Paigham Bhejo 🤍")
        if submit_note and user_note_input.strip():
            log_click_event("Submitted Note Back to Hassan", "🌷 Take Your Time")
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
