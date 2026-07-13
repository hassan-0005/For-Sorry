# -*- coding: utf-8 -*-
"""
Dear Ruhii ❤️ - A Heartfelt Apology Website
Author: Hassan
Technology: Streamlit (Pure Python)
Theme: Pink 💗 with per-page entrance animations + floating hearts & sprinkles
"""

import streamlit as st
import random

# --- Page Configuration ---
st.set_page_config(
    page_title="Dear Ruhii ❤️",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# GLOBAL PINK THEME + ANIMATION CSS
# =========================================================
st.markdown(
    """
    <style>
    /* ---------- Pink Theme ---------- */
    .stApp {
        background: linear-gradient(180deg, #fff0f5 0%, #ffe4ec 50%, #ffd6e8 100%);
        position: relative;
        overflow-x: hidden;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffd6e8 0%, #ffb3d1 100%);
    }

    h1, h2, h3, h4, h5, h6 {
        color: #d6336c !important;
    }

    p, li, span, label {
        color: #7a2e4d;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #ff6fa5, #ff9ec4);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 10px 18px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(255, 105, 165, 0.4);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        position: relative;
        z-index: 5;
    }
    div.stButton > button:hover {
        transform: scale(1.06) translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 105, 165, 0.6);
        color: white;
    }
    div.stButton > button:active {
        transform: scale(0.96);
    }

    /* Alerts (info/success/warning boxes) */
    div[data-testid="stAlert"] {
        border-radius: 16px;
        border-left: 6px solid #ff6fa5 !important;
        animation: pulseGlow 2.5s ease-in-out infinite;
        position: relative;
        z-index: 5;
    }

    /* Expanders */
    details {
        background: #fff0f6;
        border-radius: 12px;
        border: 1px solid #ffc2dc !important;
        margin-bottom: 8px;
        position: relative;
        z-index: 5;
    }

    /* Containers with border (Reasons page cards) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        border: 1px solid #ffc2dc !important;
        background: #fff5f9;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        position: relative;
        z-index: 5;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(255, 105, 165, 0.25);
    }

    /* Heart pulse used on interactive page */
    .heart-pulse {
        display: inline-block;
        animation: heartbeat 1.3s ease-in-out infinite;
        font-size: 3rem;
        text-align: center;
        width: 100%;
    }

    /* Big soft watermark heart pulsing behind content */
    .watermark-heart {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 32vw;
        opacity: 0.06;
        z-index: -1;
        pointer-events: none;
        animation: watermarkPulse 4s ease-in-out infinite;
        user-select: none;
    }

    /* Floating hearts & sprinkles container */
    .floating-decor {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        pointer-events: none;
        z-index: -1;
    }
    .floating-item {
        position: absolute;
        bottom: -10%;
        opacity: 0;
        animation-name: floatUp;
        animation-timing-function: ease-in;
        animation-iteration-count: infinite;
        will-change: transform, opacity;
    }

    /* ---------- Keyframes ---------- */
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-60px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(60px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes slideInUp {
        from { opacity: 0; transform: translateY(40px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes zoomIn {
        from { opacity: 0; transform: scale(0.85); }
        to   { opacity: 1; transform: scale(1); }
    }
    @keyframes bounceIn {
        0%   { opacity: 0; transform: scale(0.6); }
        60%  { opacity: 1; transform: scale(1.08); }
        80%  { transform: scale(0.96); }
        100% { transform: scale(1); }
    }
    @keyframes rotateIn {
        from { opacity: 0; transform: rotate(-8deg) scale(0.9); }
        to   { opacity: 1; transform: rotate(0deg) scale(1); }
    }
    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 6px rgba(255,105,165,0.15); }
        50%      { box-shadow: 0 0 18px rgba(255,105,165,0.45); }
    }
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        25%      { transform: scale(1.2); }
        40%      { transform: scale(1); }
        60%      { transform: scale(1.15); }
    }
    @keyframes floatUpDown {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-10px); }
    }
    @keyframes watermarkPulse {
        0%, 100% { transform: translate(-50%, -50%) scale(1);   opacity: 0.06; }
        50%      { transform: translate(-50%, -50%) scale(1.08); opacity: 0.1; }
    }
    @keyframes floatUp {
        0%   { transform: translateY(0) translateX(0) rotate(0deg);   opacity: 0; }
        10%  { opacity: 0.85; }
        50%  { transform: translateY(-55vh) translateX(15px) rotate(180deg); opacity: 0.9; }
        90%  { opacity: 0.4; }
        100% { transform: translateY(-110vh) translateX(-15px) rotate(360deg); opacity: 0; }
    }

    /* ---------- Per-page animation classes ---------- */
    .anim-welcome   { animation: fadeIn 1.1s ease-out; }
    .anim-matter    { animation: slideInLeft 0.9s ease-out; }
    .anim-memories  { animation: slideInRight 0.9s ease-out; }
    .anim-reasons   { animation: zoomIn 0.9s ease-out; }
    .anim-promises  { animation: slideInUp 0.9s ease-out; }
    .anim-heart     { animation: bounceIn 1s ease-out; }
    .anim-letter    { animation: rotateIn 1s ease-out; }
    .anim-surprise  { animation: bounceIn 1.1s ease-out; }

    .floaty { animation: floatUpDown 3s ease-in-out infinite; }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# DECORATION HELPERS: floating hearts/sprinkles + watermark
# =========================================================

# Emoji sets tailored to each page for extra variety
PAGE_DECOR = {
    "1. Welcome 🌸":            ["🌸", "💗", "💕"],
    "2. Why You Matter 🤍":     ["🤍", "💫", "✨"],
    "3. Beautiful Memories ✨": ["✨", "🌟", "💖"],
    "4. Reasons ❤️":            ["❤️", "💐", "💗"],
    "5. Promises 🤝":           ["🤝", "🌸", "💫"],
    "6. Interactive Heart 💖":  ["💖", "💓", "💗"],
    "7. Letter ✉️":             ["✉️", "💌", "🌸"],
    "8. Final Surprise 🎁":     ["🎁", "🎉", "💗"],
}

WATERMARK_HEARTS = {
    "1. Welcome 🌸": "💗", "2. Why You Matter 🤍": "🤍", "3. Beautiful Memories ✨": "💖",
    "4. Reasons ❤️": "❤️", "5. Promises 🤝": "💗", "6. Interactive Heart 💖": "💓",
    "7. Letter ✉️": "💌", "8. Final Surprise 🎁": "🎁",
}


def render_floating_decor(emojis, count=18):
    """Render a full-screen layer of rising, rotating hearts/sprinkles."""
    items = []
    for _ in range(count):
        emoji = random.choice(emojis)
        left = random.uniform(0, 96)
        delay = random.uniform(0, 6)
        duration = random.uniform(6, 12)
        size = random.uniform(14, 30)
        items.append(
            f'<span class="floating-item" style="left:{left:.1f}%; '
            f'font-size:{size:.0f}px; animation-delay:{delay:.2f}s; '
            f'animation-duration:{duration:.2f}s;">{emoji}</span>'
        )
    html = f'<div class="floating-decor">{"".join(items)}</div>'
    st.markdown(html, unsafe_allow_html=True)


def render_watermark(emoji):
    st.markdown(f'<div class="watermark-heart">{emoji}</div>', unsafe_allow_html=True)


# --- Define 40+ Heartfelt Apology Messages ---
APOLOGY_MESSAGES = [
    "Ruhii, our friendship is too precious to lose over a silly misunderstanding. I am really sorry. 🤍",
    "I promise to be a better friend who listens, understands, and cares. Please forgive me. 🥺",
    "Tumhari dosti mere liye sab kuch hai. Please gussa thuk do, yaar. 💔",
    "Every single day without talking to you feels completely empty. I miss our laughs. 😭",
    "I hate myself for being the reason behind your sadness. I am truly sorry, Ruhii. 🙏",
    "You're the best friend I could ever ask for. I'm sorry for letting you down. ❤️",
    "Mujhse galti ho gayi, Ruhii. Par tumse dosti khone ka darr sabse bada darr hai. 🤍",
    "I never intended to hurt you. If my words or actions did, I sincerely apologize. 🌸",
    "Can we please hit the reset button and start fresh? I miss my best friend. 🥺",
    "Please look at how sorry I am. Your smile is what makes our friendship special. ✨",
    "No matter how angry you are, I won't stop trying to make things right. You matter too much. ❤️",
    "Aapki dosti mere liye ek blessing hai, aur main apni galti ki dil se maafi maangta hoon. 🙏",
    "Our silly arguments shouldn't be bigger than all the beautiful memories we share. 🤍",
    "I miss our midnight chats, our inside jokes, and how you always understood me. Sorry. 😭",
    "I was stupid and selfish, but I promise to work on myself for our friendship. Please. 🥺",
    "Hassan is truly, deeply, and honestly sorry. Please forgimme, Ruhii! ❤️",
    "Life is too short to hold grudges, especially against your closest buddy. Let's fix this? ✨",
    "I respect your space, but I also want you to know I'm standing right here, waiting for you. 🤍",
    "Dosti mein galti ho sakti hai, par dosti ko khatam nahi kiya jata. Please maan jao. 🙏",
    "If I could turn back time, I would change how I reacted. I'm sorry for being immature. 💔",
    "You have every right to be mad at me, but please don't shut me out forever. 🥺",
    "I appreciate you more than words can express. Losing you would be my biggest regret. ❤️",
    "I value your presence in my life more than my own ego. I am sorry, Ruhii. 🤍",
    "You always supported me when everyone else left. I feel terrible for hurting you. 😭",
    "May our friendship heal and grow stronger than ever. I'm sorry from the bottom of my heart. ✨",
    "Aapki naraazgi mujhse bardaasht nahi hoti. Please maaf kar do. 🙏",
    "I promise to listen more and talk less next time. I want to understand you better. ❤️",
    "Our bond is special, and I promise to guard it with all my heart from now on. 🤍",
    "No matter how far apart we get, you'll always remain my best friend. I'm sorry. 🥺",
    "I will never take your kindness for granted again. I am truly sorry, Ruhii. 🌸",
    "You are the sister/bestie I always wanted to protect, not hurt. Please forgive me. 💔",
    "I'm sorry for being a difficult friend. Thank you for always being patient with me. 🤍",
    "Let's make new beautiful memories and leave this dark patch behind. Will you? 🙏",
    "My heart aches knowing I caused you pain. I promise to make it up to you, Ruhii. ❤️",
    "I miss sharing everything with you. Without you, my stories have no listener. 😭",
    "Sorry for making you sad. You deserve nothing but endless happiness and laughs. ✨",
    "Tumhari jagah koi nahi le sakta, Ruhii. Hassan dil se maafi maangta hai. 🥺",
    "Let's laugh together again soon. I am waiting for that happy day! ❤️",
    "Even when we don't speak, my prayers always include your happiness. I'm sorry. 🤍",
    "Please give me one last chance to prove my loyalty and care. I won't disappoint you. 🙏",
    "I am sorry, Ruhii. Our friendship is my happy place, please don't take it away. ❤️",
    "A thousand apologies wouldn't be enough, but I'll start with this sincere one. I am sorry. 🥺"
]

# --- Initialize Session States ---
if "current_page" not in st.session_state:
    st.session_state.current_page = "1. Welcome 🌸"

if "apology_text" not in st.session_state:
    st.session_state.apology_text = "Click the button below to see my thoughts..."

if "apology_clicks" not in st.session_state:
    st.session_state.apology_clicks = 0

if "seen_apologies" not in st.session_state:
    st.session_state.seen_apologies = []

if "forgive_choice" not in st.session_state:
    st.session_state.forgive_choice = None

# --- Page Navigation in Sidebar ---
st.sidebar.title("Navigate 🎈")
pages_list = [
    "1. Welcome 🌸",
    "2. Why You Matter 🤍",
    "3. Beautiful Memories ✨",
    "4. Reasons ❤️",
    "5. Promises 🤝",
    "6. Interactive Heart 💖",
    "7. Letter ✉️",
    "8. Final Surprise 🎁"
]
selected_page = st.sidebar.radio("Go to Section:", pages_list, index=pages_list.index(st.session_state.current_page))

# Sync sidebar navigation with main stage
if selected_page != st.session_state.current_page:
    st.session_state.current_page = selected_page
    st.rerun()

# --- Render page-specific floating decor + watermark heart (every page) ---
render_watermark(WATERMARK_HEARTS[st.session_state.current_page])
render_floating_decor(PAGE_DECOR[st.session_state.current_page], count=18)

# --- HEADER SECTION ---
st.markdown("<h4 style='text-align: center; color: #d6336c;'>Besties Forever 💗</h4>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# PAGE 1: Welcome  (fade in)
# ==========================================
if st.session_state.current_page == "1. Welcome 🌸":
    st.markdown('<div class="anim-welcome">', unsafe_allow_html=True)

    st.header("Dear Ruhii 💗")

    st.subheader("I'm Sorry Ruhii ❤️")

    st.info(
        """
        "I know I made mistakes.
        Maybe I hurt you.
        But losing our friendship hurts me even more."
        """
    )

    st.write(
        "I have created this little space to explain my heart and ask for your forgiveness. "
        "Please navigate through this website to read my honest thoughts."
    )

    if st.button("Continue ❤️", use_container_width=True):
        st.session_state.current_page = "2. Why You Matter 🤍"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 2: Why You Matter  (slide in from left)
# ==========================================
elif st.session_state.current_page == "2. Why You Matter 🤍":
    st.markdown('<div class="anim-matter">', unsafe_allow_html=True)

    st.header("Why You Matter 🤍")

    st.subheader("To My Favorite Person")

    st.write(
        "Ruhii, you are more than just a best friend. You are my anchor, the person who made my "
        "ordinary days extraordinary. Your laughter is the music of our friendship, and your support "
        "is what kept me going through thick and thin."
    )

    st.write(
        "When I look back at my happiest memories, they almost always have you in them. That's why "
        "your anger hurts me, and why fixing this is the most important thing to me."
    )

    st.success("💗 'True friends are like stars, you don't always see them but you know they're always there.'")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back ⬅️", use_container_width=True):
            st.session_state.current_page = "1. Welcome 🌸"
            st.rerun()
    with col2:
        if st.button("See Our Journey ✨", use_container_width=True):
            st.session_state.current_page = "3. Beautiful Memories ✨"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 3: Beautiful Memories  (slide in from right)
# ==========================================
elif st.session_state.current_page == "3. Beautiful Memories ✨":
    st.markdown('<div class="anim-memories">', unsafe_allow_html=True)

    st.header("Our Beautiful Memories ✨")
    st.caption("Here is a quick look at the timeline of our friendship. Click each phase to read.")

    with st.expander("✨ We became friends"):
        st.write(
            "Who knew that a casual conversation would turn into one of the most beautiful and "
            "meaningful friendships of my life? Meeting you was the best thing that ever happened to me."
        )

    with st.expander("😊 We laughed together"):
        st.write(
            "From silly jokes to laughing until our stomachs hurt, our laughters are the most "
            "genuine moments I cherish. Your happiness has always been contagious."
        )

    with st.expander("🤍 We supported each other"):
        st.write(
            "In low times, we stood together. You were the one who understood me when I was silent, "
            "and gave me strength when I had none. Your kindness is unmatched."
        )

    with st.expander("💔 Something went wrong"):
        st.write(
            "I made mistakes and let my immaturity or words cause a rift between us. Knowing that "
            "I am the source of your pain or distance hurts me deeply every day."
        )

    with st.expander("🙏 I hope we fix everything"):
        st.write(
            "I am writing this because our bond is too special to let go. I am ready to do whatever "
            "it takes to heal our friendship and bring back those golden days."
        )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back ⬅️", use_container_width=True):
            st.session_state.current_page = "2. Why You Matter 🤍"
            st.rerun()
    with col2:
        if st.button("Why I Value You ❤️", use_container_width=True):
            st.session_state.current_page = "4. Reasons ❤️"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 4: Reasons  (zoom in)
# ==========================================
elif st.session_state.current_page == "4. Reasons ❤️":
    st.markdown('<div class="anim-reasons">', unsafe_allow_html=True)

    st.header("Reasons Why You Matter ❤️")
    st.write("Five reasons why our friendship is the most valuable connection to me.")

    with st.container(border=True):
        st.subheader("💗 I Respect You")
        st.write(
            "I deeply respect your personality, your boundaries, and the amazing person you are. "
            "Your opinions and values will always matter immensely to me."
        )

    with st.container(border=True):
        st.subheader("💗 I Appreciate You")
        st.write(
            "I appreciate every little effort you put into being my friend. Your patience, your caring "
            "nature, and your presence make my world so much brighter."
        )

    with st.container(border=True):
        st.subheader("💗 I Miss You")
        st.write(
            "I miss our random chats, your dry humor, your advice, and just knowing that my best friend "
            "is one tap away. Life feels empty without you."
        )

    with st.container(border=True):
        st.subheader("💗 I Never Wanted To Hurt You")
        st.write(
            "Hurting you was never, ever my intention. I am deeply regretful for any moment where my "
            "actions or words failed to show how much I value you."
        )

    with st.container(border=True):
        st.subheader("💗 Our Friendship Matters")
        st.write(
            "This bond isn't just another contact in my list. It's a connection I want to preserve for "
            "a lifetime. True friends are rare, and you are irreplaceable."
        )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back ⬅️", use_container_width=True):
            st.session_state.current_page = "3. Beautiful Memories ✨"
            st.rerun()
    with col2:
        if st.button("My Promises 🤝", use_container_width=True):
            st.session_state.current_page = "5. Promises 🤝"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 5: Promises  (slide up)
# ==========================================
elif st.session_state.current_page == "5. Promises 🤝":
    st.markdown('<div class="anim-promises">', unsafe_allow_html=True)

    st.header("My Promises To You 🤝")
    st.write("These are my pledges to ensure we never have to face a rough patch like this again.")

    with st.expander("👂 I will listen more"):
        st.write(
            "I promise to pay close attention to your feelings, your thoughts, and your concerns, "
            "without letting my own ego or reactions get in the way."
        )

    with st.expander("🧠 I will understand better"):
        st.write(
            "I will put effort into looking at things from your perspective, understanding your mood, "
            "and giving you the warmth and space you deserve."
        )

    with st.expander("🛡️ I will never intentionally hurt you"):
        st.write(
            "I pledge to think before I speak and act, and to protect your peace. Your trust is sacred, "
            "and I will do my best to rebuild and honor it."
        )

    with st.expander("🤝 I will always respect our friendship"):
        st.write(
            "I promise to prioritize our connection, stay honest, apologize quickly when I am wrong, "
            "and support you through thick and thin, always."
        )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back ⬅️", use_container_width=True):
            st.session_state.current_page = "4. Reasons ❤️"
            st.rerun()
    with col2:
        if st.button("Click My Heart 💖", use_container_width=True):
            st.session_state.current_page = "6. Interactive Heart 💖"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 6: Interactive Heart  (bounce in + heartbeat)
# ==========================================
elif st.session_state.current_page == "6. Interactive Heart 💖":
    st.markdown('<div class="anim-heart">', unsafe_allow_html=True)

    st.header("Interactive Heart 💖")
    st.markdown('<div class="heart-pulse">💗</div>', unsafe_allow_html=True)
    st.write("Every single tap on this heart will show you a unique thought of apology and value from me.")

    st.write(f"**Apologies Read:** {len(st.session_state.seen_apologies)} / {len(APOLOGY_MESSAGES)}")

    if st.button("❤️ Click My Heart ❤️", use_container_width=True, type="primary"):
        if len(st.session_state.seen_apologies) >= len(APOLOGY_MESSAGES):
            st.session_state.seen_apologies = []

        remaining_indices = [i for i in range(len(APOLOGY_MESSAGES)) if i not in st.session_state.seen_apologies]
        chosen_idx = random.choice(remaining_indices)

        st.session_state.seen_apologies.append(chosen_idx)
        st.session_state.apology_text = APOLOGY_MESSAGES[chosen_idx]
        st.session_state.apology_clicks += 1
        st.balloons()

    st.info(f'"{st.session_state.apology_text}"')

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back ⬅️", use_container_width=True):
            st.session_state.current_page = "5. Promises 🤝"
            st.rerun()
    with col2:
        if st.button("Read Letter ✉️", use_container_width=True):
            st.session_state.current_page = "7. Letter ✉️"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 7: Letter  (rotate in)
# ==========================================
elif st.session_state.current_page == "7. Letter ✉️":
    st.markdown('<div class="anim-letter">', unsafe_allow_html=True)

    st.header("Dear Ruhii ✉️")

    st.write(
        """
        *Dear Ruhii,*

        I'm not perfect.

        But every day without our friendship reminds me how valuable you are.

        I'm truly sorry.

        I never wanted to hurt you.

        Please give our friendship another chance.

        No matter what happens, you'll always be special to me.

        — **Hassan** 💗
        """
    )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back ⬅️", use_container_width=True):
            st.session_state.current_page = "6. Interactive Heart 💖"
            st.rerun()
    with col2:
        if st.button("One Last Surprise 🎁", use_container_width=True):
            st.session_state.current_page = "8. Final Surprise 🎁"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 8: Final Surprise  (bounce in + floaty)
# ==========================================
elif st.session_state.current_page == "8. Final Surprise 🎁":
    st.markdown('<div class="anim-surprise">', unsafe_allow_html=True)

    st.header("One Last Surprise 🎁")
    st.markdown('<div class="floaty" style="text-align:center; font-size:2.5rem;">🎁💗🎁</div>', unsafe_allow_html=True)
    st.write("Please tap the button below to open your surprise!")

    if st.button("🎁 Open Your Surprise ❤️", use_container_width=True):
        st.session_state.forgive_choice = "pending"
        st.balloons()
        st.snow()

    if st.session_state.forgive_choice is not None:
        st.write("---")
        st.markdown("<h3 style='text-align: center;'>Will You Forgive Me?</h3>", unsafe_allow_html=True)

        col_yes, col_time = st.columns(2)
        with col_yes:
            if st.button("❤️ Yes", use_container_width=True):
                st.session_state.forgive_choice = "yes"
                st.balloons()
        with col_time:
            if st.button("😊 I Need More Time", use_container_width=True):
                st.session_state.forgive_choice = "need_time"

        if st.session_state.forgive_choice == "yes":
            st.success(
                "**Thank You 💗**  \n"
                "You made me the happiest friend. I promise to protect our friendship with all my heart!"
            )
            st.balloons()

        elif st.session_state.forgive_choice == "need_time":
            st.warning(
                "**I'll patiently wait.**  \n"
                "Because true friendships are worth waiting for. Take all the time you need, Ruhii. 🤍"
            )

    st.write("")
    if st.button("Back ⬅️", use_container_width=True):
        st.session_state.current_page = "7. Letter ✉️"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER SECTION ---
st.write("---")
st.markdown(
    "<p style='text-align: center; font-size: 11px; color: #d6336c;'>"
    "Made with respect, hope and friendship. — Hassan 💗"
    "</p>",
    unsafe_allow_html=True
)
