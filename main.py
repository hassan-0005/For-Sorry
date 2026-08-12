import streamlit as st
from pathlib import Path
import base64

# ============================================================
# RUHII — APOLOGY WEBSITE
# Streamlit + Python + HTML/CSS
# No JavaScript / React / Node
# Responsive for mobile, tablet and desktop
# ============================================================

st.set_page_config(
    page_title="For Ruhii 🤍",
    page_icon="🦋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# SESSION STATE
# ------------------------------------------------------------

for key, default in {
    "entered": False,
    "letter_open": False,
    "wish_released": False,
    "read_everything": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ------------------------------------------------------------
# OPTIONAL AUDIO
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MUSIC_FILE = BASE_DIR / "assets" / "music.mp3"

def get_audio_uri(path: Path):
    if not path.exists():
        return None
    mime = {
        ".mp3": "audio/mpeg",
        ".wav": "audio/wav",
        ".ogg": "audio/ogg",
        ".m4a": "audio/mp4",
    }.get(path.suffix.lower())
    if not mime:
        return None
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

# ------------------------------------------------------------
# CSS
#
# IMPORTANT:
# The previous version used a separate raw-HTML background block.
# This version creates the background entirely with CSS so
# Streamlit cannot display <span>/<div> tags as visible text.
# ------------------------------------------------------------

st.markdown(
r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&display=swap');

:root {
    --bg: #07050d;
    --white: #fffaff;
    --muted: rgba(255,255,255,.68);
    --soft: rgba(255,255,255,.48);
    --lavender: #c4b5fd;
    --purple: #8b5cf6;
    --cyan: #67e8f9;
    --rose: #f9a8d4;
}

html {
    scroll-behavior: smooth;
}

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

body {
    margin: 0;
    background: #07050d;
}

.stApp {
    min-height: 100vh;
    overflow-x: hidden;
    background:
        radial-gradient(circle at 8% 4%, rgba(139,92,246,.18), transparent 25%),
        radial-gradient(circle at 92% 15%, rgba(103,232,249,.10), transparent 23%),
        radial-gradient(circle at 50% 70%, rgba(236,72,153,.08), transparent 30%),
        linear-gradient(180deg, #05040a 0%, #0a0612 48%, #05040a 100%);
    position: relative;
}

/* Animated aurora */
.stApp::before {
    content: "";
    position: fixed;
    width: 58vw;
    height: 38vw;
    left: -20vw;
    top: -15vw;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    background: #8b5cf6;
    filter: blur(100px);
    opacity: .11;
    animation: auroraOne 14s ease-in-out infinite alternate;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 50vw;
    height: 35vw;
    right: -18vw;
    top: 25vh;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
    background: #22d3ee;
    filter: blur(100px);
    opacity: .08;
    animation: auroraTwo 17s ease-in-out infinite alternate;
}

@keyframes auroraOne {
    from { transform: translate3d(0,0,0) scale(1); }
    to { transform: translate3d(90px,70px,0) scale(1.18); }
}

@keyframes auroraTwo {
    from { transform: translate3d(0,0,0) scale(1); }
    to { transform: translate3d(-80px,80px,0) scale(1.22); }
}

/* CSS-only star field */
.stApp .main::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 1;
    opacity: .55;
    background-image:
        radial-gradient(circle at 5% 10%, white 0 1px, transparent 1.6px),
        radial-gradient(circle at 12% 38%, white 0 1px, transparent 1.7px),
        radial-gradient(circle at 19% 74%, white 0 1px, transparent 1.6px),
        radial-gradient(circle at 26% 21%, white 0 1px, transparent 1.7px),
        radial-gradient(circle at 33% 63%, white 0 1px, transparent 1.6px),
        radial-gradient(circle at 40% 9%, white 0 1px, transparent 1.7px),
        radial-gradient(circle at 47% 82%, white 0 1px, transparent 1.6px),
        radial-gradient(circle at 54% 28%, white 0 1px, transparent 1.7px),
        radial-gradient(circle at 61% 70%, white 0 1px, transparent 1.6px),
        radial-gradient(circle at 68% 14%, white 0 1px, transparent 1.7px),
        radial-gradient(circle at 75% 49%, white 0 1px, transparent 1.6px),
        radial-gradient(circle at 82% 83%, white 0 1px, transparent 1.7px),
        radial-gradient(circle at 89% 25%, white 0 1px, transparent 1.6px),
        radial-gradient(circle at 96% 61%, white 0 1px, transparent 1.7px);
    animation: starPulse 5s ease-in-out infinite alternate;
}

@keyframes starPulse {
    from { opacity: .25; }
    to { opacity: .75; }
}

/* CSS-only butterfly decorations */
.butterfly-decoration {
    position: fixed;
    z-index: 2;
    pointer-events: none;
    font-size: 24px;
    opacity: .18;
    filter: drop-shadow(0 0 14px rgba(249,168,212,.5));
}

.butterfly-one {
    left: -50px;
    top: 18%;
    animation: butterflyOne 18s linear infinite;
}

.butterfly-two {
    left: -50px;
    top: 61%;
    font-size: 19px;
    animation: butterflyTwo 22s linear infinite;
    animation-delay: -7s;
}

@keyframes butterflyOne {
    0% { transform: translate(0,0) rotate(-8deg); }
    25% { transform: translate(28vw,-8vh) rotate(8deg); }
    50% { transform: translate(58vw,8vh) rotate(-6deg); }
    75% { transform: translate(82vw,-5vh) rotate(10deg); }
    100% { transform: translate(115vw,4vh) rotate(-8deg); }
}

@keyframes butterflyTwo {
    0% { transform: translate(0,0) rotate(8deg); }
    50% { transform: translate(55vw,-10vh) rotate(-7deg); }
    100% { transform: translate(115vw,5vh) rotate(8deg); }
}

/* Shooting star */
.shooting-star {
    position: fixed;
    left: -150px;
    top: 18%;
    width: 120px;
    height: 1px;
    z-index: 2;
    pointer-events: none;
    opacity: 0;
    background: linear-gradient(90deg, transparent, white, transparent);
    transform: rotate(-30deg);
    animation: shootingStar 10s linear infinite;
}

@keyframes shootingStar {
    0%, 72% { transform: translate(0,0) rotate(-30deg); opacity: 0; }
    76% { opacity: .9; }
    90% { transform: translate(125vw,65vh) rotate(-30deg); opacity: 0; }
    100% { opacity: 0; }
}

/* Streamlit chrome */
#MainMenu,
footer,
[data-testid="stHeader"] {
    visibility: hidden;
    height: 0;
}

/* Content */
.block-container {
    max-width: 1120px;
    padding: 0 22px 70px;
    position: relative;
    z-index: 4;
}

.hero {
    min-height: 94vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 45px 0 30px;
}

.hero-inner {
    width: min(850px, 100%);
    animation: entrance 1.4s ease both;
}

@keyframes entrance {
    from {
        opacity: 0;
        transform: translateY(28px) scale(.98);
        filter: blur(7px);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
}

.eyebrow,
.section-label {
    color: var(--lavender);
    text-transform: uppercase;
    letter-spacing: 5px;
    font-size: 10px;
    font-weight: 500;
}

.hero h1 {
    margin: 18px 0 0;
    font-family: "Cormorant Garamond", serif;
    font-size: clamp(72px, 13vw, 145px);
    line-height: .82;
    font-weight: 500;
    background: linear-gradient(110deg, #fff, #f9a8d4, #c4b5fd, #67e8f9, #fff);
    background-size: 320% 320%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 8s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero-sub {
    max-width: 640px;
    margin: 34px auto 0;
    color: var(--muted);
    line-height: 1.95;
    font-size: 16px;
    font-weight: 300;
}

.scroll-hint {
    margin-top: 55px;
    color: rgba(255,255,255,.34);
    letter-spacing: 4px;
    font-size: 10px;
    text-transform: uppercase;
    animation: gentleFloat 3s ease-in-out infinite;
}

@keyframes gentleFloat {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(9px); }
}

.section {
    padding: 105px 0;
    position: relative;
}

.section-title {
    margin: 14px 0 30px;
    font-family: "Cormorant Garamond", serif;
    font-size: clamp(46px, 7vw, 78px);
    line-height: .96;
    font-weight: 500;
    color: var(--white);
}

.section-text {
    color: var(--muted);
    line-height: 2;
    font-size: 16px;
    max-width: 780px;
}

.glass {
    position: relative;
    overflow: hidden;
    padding: 40px;
    border-radius: 30px;
    border: 1px solid rgba(255,255,255,.10);
    background: linear-gradient(135deg, rgba(255,255,255,.075), rgba(255,255,255,.025));
    box-shadow: 0 25px 80px rgba(0,0,0,.35), inset 0 1px rgba(255,255,255,.07);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
}

.glass::after {
    content: "";
    position: absolute;
    top: -100%;
    left: -30%;
    width: 25%;
    height: 300%;
    transform: rotate(20deg);
    background: linear-gradient(90deg, transparent, rgba(255,255,255,.07), transparent);
    animation: glassShine 8s ease-in-out infinite;
}

@keyframes glassShine {
    0%,72%,100% { left: -30%; }
    85% { left: 120%; }
}

.quote-card {
    margin-top: 32px;
    text-align: center;
}

.quote {
    position: relative;
    z-index: 2;
    font-family: "Playfair Display", serif;
    font-size: clamp(25px, 4vw, 43px);
    line-height: 1.55;
    font-style: italic;
    color: #fbf7ff;
}

/* Timeline */
.timeline {
    margin-top: 60px;
    position: relative;
}

.timeline::before {
    content: "";
    position: absolute;
    left: 19px;
    top: 0;
    bottom: 0;
    width: 1px;
    background: linear-gradient(to bottom, transparent, rgba(196,181,253,.75), rgba(103,232,249,.6), transparent);
}

.timeline-item {
    position: relative;
    padding-left: 64px;
    margin-bottom: 55px;
}

.timeline-dot {
    position: absolute;
    left: 10px;
    top: 2px;
    width: 19px;
    height: 19px;
    border-radius: 50%;
    background: #090612;
    border: 1px solid var(--lavender);
    box-shadow: 0 0 20px rgba(196,181,253,.45);
}

.timeline-title {
    font-family: "Cormorant Garamond", serif;
    font-size: 29px;
    margin-bottom: 7px;
}

.timeline-text {
    color: var(--soft);
    line-height: 1.85;
}

/* Cards */
.magic-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-top: 45px;
}

.magic-card {
    min-height: 205px;
    animation: cardFloat 6s ease-in-out infinite;
}

.magic-card:nth-child(2) { animation-delay: -1.5s; }
.magic-card:nth-child(3) { animation-delay: -3s; }
.magic-card:nth-child(4) { animation-delay: -4.5s; }

@keyframes cardFloat {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-7px); }
}

.magic-icon {
    font-size: 28px;
    margin-bottom: 14px;
    filter: drop-shadow(0 0 12px rgba(249,168,212,.25));
}

.magic-card h3 {
    margin: 0 0 10px;
    font-family: "Cormorant Garamond", serif;
    font-size: 34px;
    font-weight: 500;
}

.magic-card p {
    margin: 0;
    color: var(--soft);
    line-height: 1.8;
}

.memory-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-top: 45px;
}

.memory-card {
    min-height: 230px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 28px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,.10);
    background:
        radial-gradient(circle at 30% 20%, rgba(249,168,212,.13), transparent 32%),
        linear-gradient(145deg, rgba(255,255,255,.07), rgba(255,255,255,.025));
    box-shadow: 0 20px 60px rgba(0,0,0,.28);
    transition: .45s ease;
}

.memory-card:hover {
    transform: translateY(-8px) rotate(-.5deg);
    border-color: rgba(249,168,212,.35);
}

.memory-number {
    font-family: "Cormorant Garamond", serif;
    font-size: 62px;
    color: rgba(196,181,253,.13);
    margin-bottom: auto;
}

.memory-title {
    font-family: "Cormorant Garamond", serif;
    font-size: 28px;
}

.memory-text {
    color: var(--soft);
    line-height: 1.7;
    margin-top: 8px;
}

/* Letter */
.envelope-area {
    display: flex;
    justify-content: center;
    margin-top: 50px;
}

.envelope {
    width: min(610px, 100%);
    text-align: center;
    padding: 50px 35px;
    border-radius: 34px;
    border: 1px solid rgba(249,168,212,.18);
    background:
        radial-gradient(circle at 50% 15%, rgba(249,168,212,.12), transparent 35%),
        linear-gradient(145deg, rgba(139,92,246,.15), rgba(255,255,255,.035));
    box-shadow: 0 35px 100px rgba(0,0,0,.45), 0 0 80px rgba(249,168,212,.07);
    animation: envelopeFloat 5s ease-in-out infinite;
}

@keyframes envelopeFloat {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.envelope-icon {
    font-size: 70px;
    filter: drop-shadow(0 0 24px rgba(249,168,212,.5));
}

.envelope h2 {
    font-family: "Cormorant Garamond", serif;
    font-size: 48px;
    font-weight: 500;
    margin: 15px 0 8px;
}

.envelope p {
    color: var(--soft);
    line-height: 1.8;
    margin-bottom: 25px;
}

.letter {
    margin-top: 35px;
    padding: clamp(28px, 6vw, 70px);
    border-radius: 32px;
    border: 1px solid rgba(255,255,255,.11);
    background: linear-gradient(145deg, rgba(255,255,255,.075), rgba(196,181,253,.035));
    box-shadow: 0 35px 100px rgba(0,0,0,.4);
    animation: letterReveal .9s ease both;
}

@keyframes letterReveal {
    from { opacity: 0; transform: translateY(25px) scale(.98); filter: blur(5px); }
    to { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
}

.letter-title {
    font-family: "Cormorant Garamond", serif;
    font-size: clamp(45px, 7vw, 64px);
    margin: 14px 0 35px;
}

.letter p {
    color: rgba(255,255,255,.70);
    line-height: 2.05;
    font-size: 16px;
    margin: 0 0 20px;
}

.signature {
    margin-top: 42px;
    color: var(--lavender);
    font-family: "Cormorant Garamond", serif;
    font-size: 34px;
    font-style: italic;
}

/* Wish */
.wish-wrap {
    text-align: center;
    padding: 30px 0 10px;
}

.orb {
    width: 170px;
    height: 170px;
    margin: 0 auto 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
    background:
        radial-gradient(circle at 35% 30%, rgba(255,255,255,.65), transparent 7%),
        radial-gradient(circle, rgba(196,181,253,.48), rgba(103,232,249,.12) 45%, transparent 72%);
    box-shadow: 0 0 40px rgba(196,181,253,.28), 0 0 100px rgba(103,232,249,.10);
    animation: orbPulse 4s ease-in-out infinite;
}

@keyframes orbPulse {
    0%,100% { transform: scale(.96); }
    50% { transform: scale(1.05); }
}

.wish-result {
    margin: 30px auto 0;
    max-width: 650px;
    padding: 30px;
    border-radius: 28px;
    border: 1px solid rgba(196,181,253,.18);
    background: rgba(255,255,255,.035);
    color: rgba(255,255,255,.72);
    line-height: 1.9;
    animation: letterReveal .8s ease both;
}

/* Final */
.final {
    min-height: 88vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 90px 0;
}

.final-glow {
    width: 190px;
    height: 190px;
    margin: 0 auto 20px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(196,181,253,.38), rgba(249,168,212,.09), transparent 70%);
    animation: finalGlow 4s ease-in-out infinite;
}

@keyframes finalGlow {
    0%,100% { transform: scale(.88); opacity: .65; }
    50% { transform: scale(1.13); opacity: 1; }
}

.final h1 {
    font-family: "Cormorant Garamond", serif;
    font-size: clamp(58px, 9vw, 105px);
    font-weight: 500;
    line-height: .95;
    margin: 15px 0 30px;
}

.final p {
    max-width: 690px;
    margin: auto;
    color: var(--muted);
    line-height: 2.05;
    font-size: 16px;
}

/* Buttons */
div.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 999px !important;
    border: 1px solid rgba(196,181,253,.34) !important;
    background: linear-gradient(100deg, rgba(139,92,246,.25), rgba(249,168,212,.12)) !important;
    color: #fff !important;
    font-family: "Inter", sans-serif !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    letter-spacing: .5px !important;
    box-shadow: 0 0 30px rgba(139,92,246,.08) !important;
    transition: transform .35s ease, box-shadow .35s ease, border-color .35s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-3px) !important;
    border-color: rgba(249,168,212,.55) !important;
    box-shadow: 0 12px 38px rgba(139,92,246,.22), 0 0 35px rgba(249,168,212,.10) !important;
}

/* Audio */
audio {
    width: 100%;
    margin-top: 12px;
}

/* Mobile */
@media (max-width: 760px) {
    .block-container {
        padding: 0 14px 50px;
    }

    .hero {
        min-height: 88vh;
        padding-top: 25px;
    }

    .hero h1 {
        font-size: clamp(72px, 23vw, 105px);
    }

    .hero-sub {
        font-size: 14px;
        padding: 0 8px;
        line-height: 1.85;
    }

    .section {
        padding: 75px 0;
    }

    .section-title {
        font-size: clamp(45px, 14vw, 66px);
    }

    .section-text {
        font-size: 14px;
        line-height: 1.9;
    }

    .glass {
        padding: 27px 21px;
        border-radius: 23px;
    }

    .magic-grid,
    .memory-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }

    .magic-card {
        min-height: 190px;
    }

    .memory-card {
        min-height: 210px;
    }

    .timeline::before {
        left: 16px;
    }

    .timeline-item {
        padding-left: 48px;
        margin-bottom: 45px;
    }

    .timeline-dot {
        left: 7px;
    }

    .timeline-title {
        font-size: 27px;
    }

    .envelope {
        padding: 38px 22px;
    }

    .envelope h2 {
        font-size: 42px;
    }

    .letter {
        padding: 29px 21px;
        border-radius: 24px;
    }

    .letter p {
        font-size: 14px;
        line-height: 1.9;
    }

    .orb {
        width: 145px;
        height: 145px;
    }

    .final {
        min-height: 75vh;
        padding: 70px 0;
    }

    .final p {
        font-size: 14px;
        padding: 0 8px;
    }

    .butterfly-decoration {
        font-size: 19px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        scroll-behavior: auto !important;
    }
}
</style>
""",
unsafe_allow_html=True,
)

# CSS-only decorative elements. These are intentionally tiny HTML
# elements; unlike the previous version, they are not a large
# multiline raw-HTML background block.
st.markdown(
    """
<div class="butterfly-decoration butterfly-one">🦋</div>
<div class="butterfly-decoration butterfly-two">🦋</div>
<div class="shooting-star"></div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================

st.markdown(
"""
<section class="hero">
    <div class="hero-inner">
        <div class="eyebrow">A little world made for someone important</div>
        <h1>Ruhii</h1>
        <div class="hero-sub">
            Hey, Ruhii… 🦋<br><br>
            I made a little something for you.<br>
            Not to force anything. Not to make excuses.<br>
            Just to say what I should have said properly.
        </div>
        <div class="scroll-hint">↓ &nbsp; Take your time &nbsp; ↓</div>
    </div>
</section>
""",
unsafe_allow_html=True,
)

if not st.session_state.entered:
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        if st.button("Enter My Little World ✨", use_container_width=True):
            st.session_state.entered = True
            st.rerun()

if st.session_state.entered:

    # ========================================================
    # 01
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">01 / Welcome</div>
    <div class="section-title">Welcome, Ruhii 🌸</div>
    <div class="glass">
        <p class="section-text">
            This isn't a website made to convince you.
            It is simply a little corner of the internet where I can
            finally say what I should have said properly.
            <br><br>
            You don't have to do anything here.
            Just read it if you want to.
        </p>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 02
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">02 / I Know</div>
    <div class="section-title">I Know You're Angry… 🥺</div>
    <div class="glass">
        <p class="section-text">
            You trusted me with something private and specifically asked
            me not to tell someone.
            <br><br>
            I told that person anyway.
            <br><br>
            That was wrong.
            <br><br>
            I won't call it an accident.
            I won't blame anyone else.
            I won't hide behind an excuse.
            <br><br>
            I made the choice, and I have to own it.
        </p>
    </div>
    <div class="glass quote-card">
        <div class="quote">
            “You trusted me with something private,
            and I failed to protect it.”
        </div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 03
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">03 / No Excuses</div>
    <div class="section-title">I Won't Make Excuses.</div>
    <div class="glass">
        <p class="section-text">
            I could write a hundred reasons.
            <br><br>
            But none of them would change what I did.
            <br><br>
            You trusted me.
            <br>
            I broke that trust.
            <br><br>
            And I'm sorry.
        </p>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 04
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">04 / The Hard Part</div>
    <div class="section-title">I Understand Why This Time Is Different.</div>

    <p class="section-text">
        This wasn't the first time I made a mistake like this.
        You had already given me chances.
        You had already forgiven me.
        And I repeated something I should have learned from.
    </p>

    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">You trusted me</div>
            <div class="timeline-text">
                You believed something you told me would remain safe with me.
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">I made a mistake</div>
            <div class="timeline-text">
                I told someone what I was specifically asked to keep private.
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">You forgave me</div>
            <div class="timeline-text">
                You gave me another chance when you didn't have to.
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">I repeated the mistake</div>
            <div class="timeline-text">
                That's the part I can't hide from or pretend isn't serious.
            </div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">I understand why this hurts more</div>
            <div class="timeline-text">
                An apology cannot erase a pattern. Only consistent change can.
            </div>
        </div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 05
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">05 / What I Finally Understand</div>
    <div class="section-title">Four Things I Should Have Known.</div>

    <div class="magic-grid">
        <div class="magic-card glass">
            <div class="magic-icon">🤍</div>
            <h3>Trust</h3>
            <p>
                Trust isn't automatic just because we're close.
                It's something I have to protect.
            </p>
        </div>

        <div class="magic-card glass">
            <div class="magic-icon">🌙</div>
            <h3>Privacy</h3>
            <p>
                If you tell me something privately,
                I should know that it belongs with me.
            </p>
        </div>

        <div class="magic-card glass">
            <div class="magic-icon">🌸</div>
            <h3>Forgiveness</h3>
            <p>
                Your forgiveness is a gift.
                I should never treat it like something guaranteed.
            </p>
        </div>

        <div class="magic-card glass">
            <div class="magic-icon">🦋</div>
            <h3>Change</h3>
            <p>
                Real change isn't saying “I won't do it again.”
                It's behaving differently when the next opportunity comes.
            </p>
        </div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 06
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">06 / Our Friendship</div>
    <div class="section-title">Some People Become Special Slowly…</div>

    <p class="section-text">
        Then one day you realize they've become one of those people
        whose presence genuinely matters to you.
        <br><br>
        I won't invent memories for us.
        These spaces are for the real ones only.
    </p>

    <div class="memory-grid">
        <div class="memory-card">
            <div class="memory-number">01</div>
            <div class="memory-title">A memory worth keeping</div>
            <div class="memory-text">[ADD YOUR MEMORY HERE]</div>
        </div>

        <div class="memory-card">
            <div class="memory-number">02</div>
            <div class="memory-title">Something that made you smile</div>
            <div class="memory-text">[ADD YOUR MEMORY HERE]</div>
        </div>

        <div class="memory-card">
            <div class="memory-number">03</div>
            <div class="memory-title">A moment I still remember</div>
            <div class="memory-text">[ADD YOUR MEMORY HERE]</div>
        </div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 07
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">07 / The Letter</div>
    <div class="section-title">A Letter For Ruhii 💌</div>

    <div class="envelope-area">
        <div class="envelope">
            <div class="envelope-icon">💌</div>
            <h2>For Ruhii</h2>
            <p>
                No pressure. No conditions.
                Just a letter from someone who knows he messed up.
            </p>
        </div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        if not st.session_state.letter_open:
            if st.button("Open the Letter 💌", use_container_width=True):
                st.session_state.letter_open = True
                st.rerun()

    if st.session_state.letter_open:
        st.markdown(
"""
<div class="letter">
    <div class="section-label">A letter from Hassan</div>
    <div class="letter-title">Ruhii…</div>

    <p>
        I don't know if these words can fix what I did,
        and I'm not going to pretend that they can.
    </p>

    <p>
        You trusted me with something.
        You clearly told me not to share it.
        And I still told the same person.
        That was my mistake. Completely.
    </p>

    <p>
        What makes me even more sorry is knowing that this isn't
        the first time you've had to forgive me for something similar.
        You gave me chances, and instead of proving that I had learned,
        I repeated the same mistake.
    </p>

    <p>
        So I understand why you're hurt.
        I understand why you're angry.
        And I understand why “sorry” probably doesn't mean much right now.
    </p>

    <p>
        I'm not asking you to forget.
        I'm not asking you to forgive me immediately.
        And I'm not asking you to pretend everything is normal.
    </p>

    <p>
        I'm simply saying that I'm genuinely sorry.
        Not because you're angry.
        Not because you blocked me.
        But because I should have been someone you could safely trust.
    </p>

    <p>
        If someday you give me another chance,
        I don't want to earn it through words.
        I want to earn it through my actions.
    </p>

    <p>Take all the time you need.</p>

    <p>I'm sorry, Ruhii. Really.</p>

    <div class="signature">— Hassan 🤍</div>
</div>
""",
unsafe_allow_html=True,
        )

    # ========================================================
    # 08
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">08 / Promises That Actually Matter</div>
    <div class="section-title">I Won't Ask You To Trust My Words.</div>

    <div class="magic-grid">
        <div class="magic-card glass">
            <div class="magic-icon">🔐</div>
            <h3>I will protect what you tell me.</h3>
            <p>
                Private means private. I should have understood that without
                needing to be reminded.
            </p>
        </div>

        <div class="magic-card glass">
            <div class="magic-icon">🌙</div>
            <h3>I will respect your boundaries.</h3>
            <p>
                Your comfort matters more than my urge to explain myself.
            </p>
        </div>

        <div class="magic-card glass">
            <div class="magic-icon">🌸</div>
            <h3>I won't treat forgiveness like a reset button.</h3>
            <p>
                Being forgiven once doesn't make repeating the mistake okay.
            </p>
        </div>

        <div class="magic-card glass">
            <div class="magic-icon">🦋</div>
            <h3>I'll let my actions speak.</h3>
            <p>
                If I ever get another chance, I want my behavior to prove
                that I learned something.
            </p>
        </div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 09
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">09 / A Quiet Moment</div>
    <div class="section-title">Maybe Let This Moment Breathe.</div>

    <div class="glass" style="text-align:center;">
        <div style="font-size:42px;margin-bottom:12px;">🎧</div>
        <div class="section-text" style="margin:0 auto;">
            If you want music here, add your own royalty-free
            <strong>music.mp3</strong> inside the <strong>assets</strong> folder.
        </div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    music_uri = get_audio_uri(MUSIC_FILE)
    if music_uri:
        st.markdown(
            f'<audio controls src="{music_uri}"></audio>',
            unsafe_allow_html=True,
        )

    # ========================================================
    # 10
    # ========================================================

    st.markdown(
"""
<section class="section">
    <div class="section-label">10 / A Magical Moment</div>
    <div class="section-title">Make A Wish, Ruhii ✨</div>

    <div class="wish-wrap">
        <div class="orb">🪄</div>
        <p class="section-text" style="margin:0 auto 25px;text-align:center;">
            No wish about forgiveness.
            Just something peaceful.
        </p>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        if not st.session_state.wish_released:
            if st.button("Release the Wish ✨", use_container_width=True):
                st.session_state.wish_released = True
                st.rerun()

    if st.session_state.wish_released:
        st.markdown(
"""
<div class="wish-result">
    ✨ 🦋 ✨ 🌸 ✨ 🦋 ✨<br><br>
    I hope one day this hurt becomes just a small chapter
    in a friendship that learned something from it.<br><br>
    No pressure. No demand. Just hope.
</div>
""",
unsafe_allow_html=True,
        )

    # ========================================================
    # 11
    # ========================================================

    st.markdown(
"""
<section class="final">
    <div>
        <div class="final-glow"></div>
        <div class="section-label">11 / One Last Thing</div>

        <h1>
            I Can't Undo It.<br>
            But I Can Learn.
        </h1>

        <p>
            I can't undo what I did.<br><br>
            I can't force you to forgive me.<br><br>
            I can't demand your trust back.<br><br>
            But I can accept my mistake.
            I can learn from it.
            And if you ever give me another chance,
            I'll make sure my actions deserve it.
            <br><br>
            I'm sorry, Ruhii. 🤍
        </p>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    # ========================================================
    # 12
    # ========================================================

    st.markdown(
"""
<section class="section" style="text-align:center;padding-top:40px;">
    <div class="section-label">12 / Take Your Time</div>
    <div class="section-title">Take Your Time, Ruhii. 🌙</div>

    <div class="glass" style="max-width:650px;margin:35px auto 0;">
        <div class="quote">
            No pressure.<br>
            No expectations.<br>
            Just a sincere sorry. 🤍
        </div>
        <div class="signature">— Hassan</div>
    </div>
</section>
""",
unsafe_allow_html=True,
    )

    st.markdown(
        '<div style="max-width:360px;margin:10px auto 60px;">',
        unsafe_allow_html=True,
    )

    if st.button("🤍 I Read Everything", use_container_width=True):
        st.session_state.read_everything = True
        st.balloons()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.read_everything:
        st.markdown(
"""
<div class="glass" style="text-align:center;max-width:650px;margin:0 auto 70px;">
    <div style="font-family:'Cormorant Garamond',serif;font-size:48px;">
        Thank you, Ruhii. 🤍
    </div>
    <p class="section-text" style="margin:15px auto 0;">
        Whatever you decide, I hope you know that this apology was meant
        sincerely. Take care of yourself.
    </p>
</div>
""",
unsafe_allow_html=True,
        )

st.markdown(
"""
<div style="
    position:relative;
    z-index:4;
    text-align:center;
    color:rgba(255,255,255,.18);
    font-size:10px;
    letter-spacing:3px;
    padding:20px 0 45px;
">
    MADE WITH SINCERITY · FOR RUHII
</div>
""",
unsafe_allow_html=True,
)
