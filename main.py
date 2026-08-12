import streamlit as st
import random

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="For Ruhii 🌸",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "letter_open" not in st.session_state:
    st.session_state.letter_open = False
if "wish_sent" not in st.session_state:
    st.session_state.wish_sent = False


def go_to(page_name: str):
    st.session_state.page = page_name


# ----------------------------------------------------------------------------
# HELPERS — FLOATING DECORATIVE OVERLAYS (pure CSS, no JS)
# ----------------------------------------------------------------------------
def floating_layer(emojis, count=18, css_class="floaty"):
    """Generates a fixed full-screen overlay of randomly placed floating emoji."""
    spans = []
    for i in range(count):
        emoji = random.choice(emojis)
        left = random.uniform(0, 100)
        delay = random.uniform(0, 12)
        duration = random.uniform(10, 20)
        size = random.uniform(14, 30)
        spans.append(
            f'<span class="{css_class}" style="left:{left}vw; '
            f'animation-delay:{delay}s; animation-duration:{duration}s; '
            f'font-size:{size}px;">{emoji}</span>'
        )
    html = f'<div class="floaty-wrapper">{"".join(spans)}</div>'
    st.markdown(html, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# GLOBAL CSS
# ----------------------------------------------------------------------------
def inject_global_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Dancing+Script:wght@500;600;700&family=Poppins:wght@300;400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .stApp {
            background: linear-gradient(160deg, #fff0f5 0%, #ffe4ec 30%, #ffd9e8 60%, #f6c9e0 100%);
            background-attachment: fixed;
            background-size: 400% 400%;
            animation: gradientShift 18s ease infinite;
            overflow-x: hidden;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* ---------- Floating overlay elements ---------- */
        .floaty-wrapper {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            overflow: hidden;
            z-index: 0;
        }
        .floaty {
            position: absolute;
            top: 110vh;
            opacity: 0.85;
            animation-name: floatUp;
            animation-timing-function: ease-in-out;
            animation-iteration-count: infinite;
            filter: drop-shadow(0 0 6px rgba(255, 182, 213, 0.6));
        }
        @keyframes floatUp {
            0% { transform: translateY(0) translateX(0) rotate(0deg); opacity: 0; }
            10% { opacity: 0.9; }
            50% { transform: translateY(-55vh) translateX(15px) rotate(10deg); }
            90% { opacity: 0.7; }
            100% { transform: translateY(-115vh) translateX(-15px) rotate(-8deg); opacity: 0; }
        }

        /* ---------- Headings ---------- */
        .dream-title {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            text-align: center;
            background: linear-gradient(90deg, #d6336c, #ff8fab, #c2185b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmerText 5s ease-in-out infinite, fadeSlideUp 1.4s ease;
            text-shadow: 0 0 25px rgba(255, 182, 213, 0.35);
            margin-bottom: 0.3em;
        }
        @keyframes shimmerText {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.25); }
        }
        @keyframes fadeSlideUp {
            from { opacity: 0; transform: translateY(35px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .script-quote {
            font-family: 'Dancing Script', cursive;
            font-weight: 600;
            text-align: center;
            color: #ad1457;
            animation: fadeSlideUp 1.8s ease;
        }

        .soft-para {
            font-family: 'Poppins', sans-serif;
            font-weight: 400;
            color: #7a2e46;
            text-align: center;
            line-height: 1.9;
            animation: fadeSlideUp 2s ease;
        }

        /* ---------- Glass Card ---------- */
        .glass-card {
            background: rgba(255, 255, 255, 0.45);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-radius: 26px;
            border: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 0 8px 32px rgba(214, 51, 108, 0.15);
            padding: 28px 22px;
            text-align: center;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            animation: fadeSlideUp 1.6s ease;
            position: relative;
            z-index: 1;
            margin-bottom: 20px;
        }
        .glass-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 16px 40px rgba(214, 51, 108, 0.28);
        }
        .glass-card h3 {
            font-family: 'Playfair Display', serif;
            color: #c2185b;
            margin-bottom: 8px;
        }
        .glass-card p {
            color: #8a3a55;
            font-size: 0.95em;
        }

        /* ---------- Buttons (Streamlit native override) ---------- */
        div.stButton > button {
            background: linear-gradient(135deg, #ffb6c1, #ff8fab, #e75480);
            color: white;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            border: 2px solid rgba(255, 215, 0, 0.35);
            border-radius: 40px;
            padding: 12px 34px;
            box-shadow: 0 6px 20px rgba(231, 84, 128, 0.35);
            transition: all 0.35s ease;
            letter-spacing: 0.5px;
        }
        div.stButton > button:hover {
            transform: translateY(-4px) scale(1.04);
            box-shadow: 0 0 25px rgba(255, 182, 213, 0.9), 0 10px 25px rgba(231, 84, 128, 0.4);
            border-color: gold;
            color: white;
        }
        div.stButton > button:active {
            transform: scale(0.97);
        }

        /* ---------- Nav bar ---------- */
        .navbar {
            display: flex;
            justify-content: center;
            gap: 10px;
            padding: 14px 10px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }

        /* ---------- Envelope ---------- */
        .envelope-wrap {
            display: flex;
            justify-content: center;
            margin: 30px auto;
            animation: fadeSlideUp 1.8s ease;
        }
        .envelope {
            width: 300px;
            height: 200px;
            background: linear-gradient(135deg, #fff0f5, #ffe0eb);
            border-radius: 14px;
            position: relative;
            box-shadow: 0 15px 35px rgba(214, 51, 108, 0.25);
            border: 2px solid #ffd1dc;
        }
        .envelope::before {
            content: "";
            position: absolute;
            top: 0; left: 0;
            width: 0; height: 0;
            border-left: 150px solid transparent;
            border-right: 150px solid transparent;
            border-top: 110px solid #ffc2d6;
        }
        .seal {
            position: absolute;
            top: 78px; left: 50%;
            transform: translateX(-50%);
            width: 50px; height: 50px;
            background: radial-gradient(circle at 35% 35%, #ff8fab, #c2185b);
            border-radius: 50%;
            box-shadow: 0 4px 10px rgba(194, 24, 91, 0.5);
            display: flex; align-items: center; justify-content: center;
            font-size: 22px;
            animation: glowPulse 2.4s ease-in-out infinite;
        }
        @keyframes glowPulse {
            0%, 100% { box-shadow: 0 0 10px rgba(255, 143, 171, 0.6); }
            50% { box-shadow: 0 0 25px rgba(255, 143, 171, 1); }
        }

        /* ---------- Letter paper ---------- */
        .letter-paper {
            background: repeating-linear-gradient(#fff6f9, #fff6f9 34px, #ffe3ec 35px);
            border-radius: 18px;
            padding: 45px 40px;
            max-width: 700px;
            margin: 20px auto;
            box-shadow: 0 12px 35px rgba(214, 51, 108, 0.2);
            border: 1px solid #ffd1dc;
            animation: fadeSlideUp 1.6s ease;
        }
        .letter-paper p {
            font-family: 'Dancing Script', cursive;
            font-size: 1.5em;
            color: #7a2e46;
            line-height: 1.8;
        }

        /* ---------- Fade line reveal ---------- */
        .reveal-line {
            font-family: 'Dancing Script', cursive;
            font-size: 1.8em;
            text-align: center;
            color: #ad1457;
            opacity: 0;
            animation: fadeSlideUp 1.4s ease forwards;
        }
        .reveal-line.d1 { animation-delay: 0.2s; }
        .reveal-line.d2 { animation-delay: 1.1s; }
        .reveal-line.d3 { animation-delay: 2.0s; }
        .reveal-line.d4 { animation-delay: 2.9s; }

        hr.dreamy {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #e75480, transparent);
            margin: 30px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------------------------
# NAVIGATION BAR
# ----------------------------------------------------------------------------
def render_navbar():
    labels = {
        "welcome": "🌸 Welcome",
        "hurt": "🥺 I Know",
        "friendship": "🦋 Us",
        "letter": "💌 Letter",
        "wait": "🌷 Time",
    }
    cols = st.columns(len(labels))
    for col, (key, label) in zip(cols, labels.items()):
        with col:
            if st.button(label, key=f"nav_{key}", use_container_width=True):
                go_to(key)
    st.markdown("<hr class='dreamy'>", unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# PAGE 1 — WELCOME
# ----------------------------------------------------------------------------
def page_welcome():
    floating_layer(["✨", "💗", "🌸", "☁️", "🎀"], count=20)
    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
    st.markdown("<h1 class='dream-title' style='font-size:3.2em;'>Hey Ruhii... 🌸</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='script-quote' style='font-size:1.6em;'>"
        "\"I made a tiny little world for someone very special.\"</p>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Enter My World ✨", use_container_width=True):
            go_to("hurt")
    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)
    st.markdown(
        "<p class='soft-para'>🌙 a soft glowing moon watches quietly over a world made of pink clouds "
        "and glitter rain, waiting for you to step inside...</p>",
        unsafe_allow_html=True,
    )


# ----------------------------------------------------------------------------
# PAGE 2 — I KNOW I HURT YOU
# ----------------------------------------------------------------------------
def page_hurt():
    floating_layer(["🌸", "❤️", "🥀", "💮"], count=16)
    st.markdown("<h1 class='dream-title' style='font-size:2.6em;'>I Know You're Angry... 🥺</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    st.markdown("<p class='reveal-line d1'>You trusted me with something important. 🌷</p>", unsafe_allow_html=True)
    st.markdown("<p class='reveal-line d2'>You asked me to keep it a secret.</p>", unsafe_allow_html=True)
    st.markdown("<p class='reveal-line d3'>And I told the same person you asked me not to.</p>", unsafe_allow_html=True)
    st.markdown("<p class='reveal-line d4'>I was wrong — and I'm not making any excuses for it.</p>", unsafe_allow_html=True)

    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Continue to Our Story 🦋", use_container_width=True):
            go_to("friendship")


# ----------------------------------------------------------------------------
# PAGE 3 — OUR FRIENDSHIP
# ----------------------------------------------------------------------------
def page_friendship():
    floating_layer(["🦋", "💗", "✨", "🌙"], count=16)
    st.markdown("<h1 class='dream-title' style='font-size:2.6em;'>Our Friendship 🦋</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    memories = [
        ("🌸", "First Memory", "The moment this friendship quietly began."),
        ("💗", "The Funniest Moment", "The one we still laugh about randomly."),
        ("🦋", "A Smile I Still Remember", "A tiny moment that stayed with me."),
        ("🌙", "Our Favorite Conversation", "The talk that felt like it lasted forever."),
    ]

    cols = st.columns(2)
    for i, (emoji, title, desc) in enumerate(memories):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="glass-card">
                    <h3>{emoji} {title}</h3>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        "<p class='script-quote' style='font-size:1.9em; margin-top:20px;'>"
        "\"Some people slowly become home.\"</p>",
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Read My Letter 💌", use_container_width=True):
            go_to("letter")


# ----------------------------------------------------------------------------
# PAGE 4 — MY LETTER
# ----------------------------------------------------------------------------
def page_letter():
    floating_layer(["💌", "🌹", "✨", "🦋"], count=14)
    st.markdown("<h1 class='dream-title' style='font-size:2.6em;'>My Letter 💌</h1>", unsafe_allow_html=True)

    if not st.session_state.letter_open:
        st.markdown(
            """
            <div class="envelope-wrap">
                <div class="envelope">
                    <div class="seal">🌹</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("Open the Letter 💌", use_container_width=True):
                st.session_state.letter_open = True
                st.rerun()
    else:
        st.markdown(
            """
            <div class="letter-paper">
                <p>Dear Ruhii,</p>
                <p>I broke your trust, and I know that's not something small.</p>
                <p>This isn't the first time I've made a mistake — and I understand
                why this time feels different, why it hurts more, why it's harder
                to just let go.</p>
                <p>I'm not asking you to forgive me right now. I don't expect that,
                and I don't think I deserve it yet.</p>
                <p>I just want the chance to earn your trust back — slowly,
                honestly, through actions and not words.</p>
                <p>Take all the time you need. I'll still be here.</p>
                <p>With love,<br>Hassan 🤍</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("Take Your Time 🌷", use_container_width=True):
                go_to("wait")


# ----------------------------------------------------------------------------
# PAGE 5 — TAKE YOUR TIME
# ----------------------------------------------------------------------------
def page_wait():
    floating_layer(["🌸", "🏮", "✨", "🦋", "🕊️"], count=18)
    st.markdown("<h1 class='dream-title' style='font-size:2.8em;'>Take Your Time, Ruhii 🌷</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

    st.markdown("<p class='reveal-line d1'>No pressure.</p>", unsafe_allow_html=True)
    st.markdown("<p class='reveal-line d2'>No expectations.</p>", unsafe_allow_html=True)
    st.markdown("<p class='reveal-line d3'>Just a sincere sorry.</p>", unsafe_allow_html=True)
    st.markdown("<p class='reveal-line d4' style='font-size:2.2em;'>— Hassan 🤍</p>", unsafe_allow_html=True)

    st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Send My Wish ✨", use_container_width=True):
            st.session_state.wish_sent = True

    if st.session_state.wish_sent:
        floating_layer(["❤️", "✨", "💖"], count=26, css_class="floaty")
        st.markdown(
            "<p class='script-quote' style='font-size:1.6em; margin-top:30px;'>"
            "\"I hope one day this hurt becomes just one small chapter of a "
            "friendship that grew stronger.\"</p>",
            unsafe_allow_html=True,
        )


# ----------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------
def main():
    inject_global_css()
    render_navbar()

    page = st.session_state.page
    if page == "welcome":
        page_welcome()
    elif page == "hurt":
        page_hurt()
    elif page == "friendship":
        page_friendship()
    elif page == "letter":
        page_letter()
    elif page == "wait":
        page_wait()


if __name__ == "__main__":
    main()
