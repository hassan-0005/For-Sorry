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

# Track time spent on page transition
def record_page_transition(new_page):
    old_page = st.session_state.get("current_tracked_page", None)
    start_time = st.session_state.get("page_start_time", None)
    
    if old_page and start_time:
        elapsed = time.time() - start_time
        log_page_duration(old_page, elapsed)
        
    st.session_state.current_tracked_page = new_page
    st.session_state.page_start_time = time.time()
    st.session_state.page = new_page

# Set Page Config for Streamlit
st.set_page_config(
    page_title="For Ruhii 🌸 | A Magical Apology",
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
if "page" not in st.session_state:
    st.session_state.page = "🌸 Dreamy Welcome"
if "letter_opened" not in st.session_state:
    st.session_state.letter_opened = False
if "wish_sent" not in st.session_state:
    st.session_state.wish_sent = False

if "current_tracked_page" not in st.session_state:
    st.session_state.current_tracked_page = st.session_state.page
if "page_start_time" not in st.session_state:
    st.session_state.page_start_time = time.time()

# Navigation Menu
st.sidebar.title("🌸 Ruhii's World")
st.sidebar.markdown("---")

pages = [
    "🌸 Dreamy Welcome",
    "🥺 I Know I Hurt You",
    "💗 Our Friendship",
    "💌 My Letter",
    "🌷 Take Your Time"
]

selected_page = st.sidebar.radio("Navigate Pages", pages, index=pages.index(st.session_state.page))
if selected_page != st.session_state.page:
    log_click_event(f"Tab Navigation -> {selected_page}", st.session_state.page)
    record_page_transition(selected_page)
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("Designed with soft love & care by Hassan 🤍")

# -------------------------------------------------------------
# SECRET HASSAN ANALYTICS PORTAL (HIDDEN IN SIDEBAR)
# -------------------------------------------------------------
with st.sidebar.expander("🔒 Owner Secret Portal (Hassan Only)"):
    secret_pass = st.text_input("Enter Secret Password", type="password", key="admin_pwd")
    if secret_pass == "hassan786" or secret_pass == "hassan123":
        st.success("Welcome Hassan 🤍 (Secret Tracking Unlocked)")
        
        # Flush current page duration before displaying
        if "page_start_time" in st.session_state and "current_tracked_page" in st.session_state:
            current_dur = time.time() - st.session_state.page_start_time
            log_page_duration(st.session_state.current_tracked_page, current_dur)
            st.session_state.page_start_time = time.time()
            
        logs = load_logs()
        
        st.markdown("### ⏱️ Time Spent on Each Tab")
        durations = logs.get("page_durations", {})
        if durations:
            for page_name, seconds in durations.items():
                mins = round(seconds / 60, 2)
                st.write(f"• **{page_name}**: `{seconds}s` (~{mins} mins)")
        else:
            st.write("No duration logged yet.")
            
        st.markdown("### 🖱️ Button Clicks & Activity Log")
        clicks = logs.get("clicks", [])
        if clicks:
            for c in reversed(clicks):
                st.caption(f"[{c['time']}] on *{c['page']}* → **{c['button']}**")
        else:
            st.write("No clicks recorded yet.")
            
        st.markdown("### ✉️ Notes Left By Ruhii")
        notes = logs.get("notes", [])
        if notes:
            for n in reversed(notes):
                st.write(f"💌 **[{n['time']}]**: {n['text']}")
        else:
            st.write("No notes submitted yet.")
            
        if st.button("🗑️ Reset All Analytics"):
            clear_all_analytics()
            st.success("Logs reset!")
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
                <p class="handwriting">"I made a tiny little world for someone very special."</p>
                <p style="font-size: 1.1rem; color: #8A3B4E;">A place of soft thoughts, quiet honesty, and cherished memories.</p>
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
                🌸 <b>You trusted me</b> with your thoughts and privacy.<br><br>
                🤍 <b>You asked me to keep something secret</b> between us.<br><br>
                💔 <b>I told the same person</b> without thinking properly.<br><br>
                🌧️ <b>I was completely wrong</b> for doing that.<br><br>
                🕊️ <b>No excuses.</b> No shifting blame. Just pure regret.
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
            <p style="font-size: 1.2rem; color: #7A2B3E;">Every smile, secret, and story we shared holds an irreplaceable place.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="glass-card">
                <h3>🌸 First Memory</h3>
                <p><b>Where it all began:</b> The day we first started talking and realized we share the exact same crazy vibe and comfort.</p>
            </div>
            <div class="glass-card">
                <h3>🦋 A Smile I Still Remember</h3>
                <p><b>Pure warmth:</b> Your genuine smile and laughter when everything felt light and right.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="glass-card">
                <h3>💗 The Funniest Moment</h3>
                <p><b>Uncontrollable laughter:</b> That inside joke we couldn't stop laughing about for days on end!</p>
            </div>
            <div class="glass-card">
                <h3>🌙 Our Favorite Conversation</h3>
                <p><b>Late night secrets:</b> Conversations where time completely stopped and we talked about life.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <p class="handwriting">"Some people slowly become home."</p>
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
                <p style="font-size: 1.1rem; color: #8A3B4E;">Sealed with sincerity & care</p>
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
                    <p>I want to apologize from the bottom of my heart. I broke your trust when you asked me to keep something confidential, and I failed you by telling the same person.</p>
                    <p>This isn't my first mistake, and I completely understand why this time feels different to you. Your disappointment is valid, and I am not here to make excuses.</p>
                    <p>I am not asking for instant forgiveness. Real trust is built through consistency and actions, not just words.</p>
                    <p>Please take all the time and space you need. I value our bond too much to ever dismiss your feelings.</p>
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
            <p style="font-size: 2.2rem; font-family: 'Cormorant Garamond', serif;">No pressure.</p>
            <p style="font-size: 2.2rem; font-family: 'Cormorant Garamond', serif;">No expectations.</p>
            <p style="font-size: 2.5rem; font-family: 'Cormorant Garamond', serif; font-weight: bold; color: #9E2A4B;">Just a sincere sorry.</p>
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

    # Optional Message Form
    st.markdown("### 💌 Leave A Message Back (Optional)")
    with st.form(key="ruhii_note_form"):
        user_note_input = st.text_area("Write a message or thought to Hassan...", placeholder="Type your message here...")
        submit_note = st.form_submit_button("Send Note Back to Hassan 🤍")
        if submit_note and user_note_input.strip():
            log_click_event("Submitted Note Back to Hassan", "🌷 Take Your Time")
            log_user_note(user_note_input.strip())
            st.session_state.note_sent_confirm = True

    if st.session_state.get("note_sent_confirm", False):
        st.success("Thank you Ruhii! Your note has been securely received by Hassan 🤍")

    if st.session_state.wish_sent:
        st.markdown("""
            <div class="glass-card" style="text-align: center; margin-top: 20px; border: 2px solid #FFB6C1;">
                <div style="font-size: 2.5rem;">🌸 💖 ✨</div>
                <p class="handwriting">
                    "I hope one day this hurt becomes just one small chapter of a friendship that grew stronger."
                </p>
            </div>
        """, unsafe_allow_html=True)
