import streamlit as st

# ============================================================
# MIDNIGHT AURORA — FOR RUHII
# Complete single-file Streamlit website
# Python + Streamlit + HTML/CSS
# No JavaScript
# ============================================================

st.set_page_config(
    page_title="For Ruhii 🤍",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap');

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    padding: 0;
    background: #03030b;
    color: white;
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 15%, rgba(111, 45, 189, 0.15), transparent 28%),
        radial-gradient(circle at 85% 25%, rgba(0, 174, 255, 0.10), transparent 25%),
        radial-gradient(circle at 50% 80%, rgba(132, 0, 255, 0.08), transparent 30%),
        #03030b;
    overflow-x: hidden;
}

/* Hide Streamlit UI */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { background: transparent !important; }

/* STAR FIELD */
.star-field {
    position: fixed;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}

.star {
    position: absolute;
    width: 2px;
    height: 2px;
    background: white;
    border-radius: 50%;
    opacity: 0.6;
    animation: twinkle 4s infinite ease-in-out;
}

.star:nth-child(1) { left: 5%; top: 12%; animation-delay: 0s; }
.star:nth-child(2) { left: 12%; top: 67%; animation-delay: 1s; }
.star:nth-child(3) { left: 19%; top: 33%; animation-delay: 2s; }
.star:nth-child(4) { left: 27%; top: 82%; animation-delay: .5s; }
.star:nth-child(5) { left: 34%; top: 19%; animation-delay: 1.5s; }
.star:nth-child(6) { left: 41%; top: 58%; animation-delay: 2.5s; }
.star:nth-child(7) { left: 48%; top: 8%; animation-delay: 1s; }
.star:nth-child(8) { left: 55%; top: 74%; animation-delay: 3s; }
.star:nth-child(9) { left: 63%; top: 28%; animation-delay: .8s; }
.star:nth-child(10) { left: 70%; top: 91%; animation-delay: 1.7s; }
.star:nth-child(11) { left: 77%; top: 44%; animation-delay: 2.2s; }
.star:nth-child(12) { left: 84%; top: 13%; animation-delay: .4s; }
.star:nth-child(13) { left: 91%; top: 63%; animation-delay: 2.8s; }
.star:nth-child(14) { left: 96%; top: 29%; animation-delay: 1.3s; }
.star:nth-child(15) { left: 9%; top: 91%; animation-delay: 2.6s; }

@keyframes twinkle {
    0%, 100% { opacity: .2; transform: scale(.7); }
    50% { opacity: 1; transform: scale(1.5); }
}

/* AURORA GLOWS */
.aurora {
    position: fixed;
    width: 900px;
    height: 500px;
    border-radius: 50%;
    filter: blur(90px);
    opacity: .15;
    pointer-events: none;
    z-index: 0;
}

.aurora.one {
    background: #7c3aed;
    top: -200px;
    left: -200px;
    animation: auroraOne 14s ease-in-out infinite alternate;
}

.aurora.two {
    background: #06b6d4;
    right: -250px;
    top: 25%;
    animation: auroraTwo 17s ease-in-out infinite alternate;
}

@keyframes auroraOne {
    0% { transform: translate(0,0) rotate(0deg); }
    100% { transform: translate(250px,180px) rotate(25deg); }
}

@keyframes auroraTwo {
    0% { transform: translate(0,0) scale(1); }
    100% { transform: translate(-180px,100px) scale(1.3); }
}

/* SHOOTING STARS */
.shooting-star {
    position: fixed;
    width: 120px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,.9), transparent);
    transform: rotate(-35deg);
    animation: shooting 8s linear infinite;
    opacity: 0;
    z-index: 1;
}

.shooting-star.a { top: 18%; left: -10%; animation-delay: 2s; }
.shooting-star.b { top: 42%; left: -15%; animation-delay: 7s; }

@keyframes shooting {
    0% { transform: translate(0,0) rotate(-35deg); opacity: 0; }
    5% { opacity: 1; }
    20% { transform: translate(120vw,80vh) rotate(-35deg); opacity: 0; }
    100% { opacity: 0; }
}

.main-content {
    position: relative;
    z-index: 5;
    max-width: 1100px;
    margin: auto;
    padding: 20px;
}

/* HERO */
.hero {
    min-height: 94vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.eyebrow {
    letter-spacing: 7px;
    text-transform: uppercase;
    color: #a5b4fc;
    font-size: 11px;
    margin-bottom: 22px;
}

.hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(64px, 11vw, 125px);
    font-weight: 500;
    line-height: .9;
    margin: 0;
    background: linear-gradient(110deg, #ffffff, #d8b4fe, #67e8f9, #ffffff);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 7s ease infinite;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero-sub {
    max-width: 600px;
    margin: 35px auto;
    color: rgba(255,255,255,.68);
    font-size: 17px;
    line-height: 1.9;
    font-weight: 300;
}

/* GLASS CARDS */
.glass {
    background: linear-gradient(135deg, rgba(255,255,255,.075), rgba(255,255,255,.025));
    border: 1px solid rgba(255,255,255,.10);
    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);
    border-radius: 28px;
    padding: 42px;
    box-shadow: 0 25px 70px rgba(0,0,0,.35), inset 0 1px rgba(255,255,255,.08);
}

.section-label {
    color: #a78bfa;
    text-transform: uppercase;
    letter-spacing: 5px;
    font-size: 10px;
    margin-bottom: 16px;
}

.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(42px, 7vw, 75px);
    font-weight: 500;
    line-height: 1;
    margin-bottom: 35px;
}

.quote-card {
    margin: 50px 0;
    text-align: center;
}

.quote {
    font-family: 'Playfair Display', serif;
    font-size: clamp(24px, 4vw, 42px);
    line-height: 1.55;
    font-style: italic;
    color: #f5f3ff;
}

/* LETTER CARD */
.letter {
    background: linear-gradient(135deg, rgba(255,255,255,.07), rgba(167,139,250,.035));
    border: 1px solid rgba(255,255,255,.11);
    border-radius: 30px;
    padding: clamp(28px, 6vw, 70px);
}

.signature {
    margin-top: 50px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 30px;
    color: #ddd6fe;
    font-style: italic;
}

.stButton > button {
    width: 100%;
    border-radius: 999px !important;
    border: 1px solid rgba(167,139,250,.4) !important;
    background: linear-gradient(100deg, rgba(124,58,237,.25), rgba(34,211,238,.12)) !important;
    color: white !important;
    padding: 15px 28px !important;
}

</style>
""", unsafe_allow_html=True)

# BACKGROUND ELEMENTS
st.markdown("""
<div class="star-field">
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div><div class="star"></div>
</div>
<div class="aurora one"></div>
<div class="aurora two"></div>
<div class="shooting-star a"></div>
<div class="shooting-star b"></div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

# HERO SECTION
st.markdown("""
<section class="hero">
<div>
    <div class="eyebrow">A little something for someone important</div>
    <h1>Ruhii</h1>
    <div class="hero-sub">
        I know you're angry. And honestly… I understand why.<br><br>
        So this isn't here to convince you. It's simply here to say what I should have said properly.
    </div>
</div>
</section>
""", unsafe_allow_html=True)

# SECTION 1
st.markdown("""
<section style="padding: 80px 0;">
    <div class="section-label">01 / No Excuses</div>
    <div class="section-title">I won't defend myself.</div>
    <div class="glass">
        <p style="color: rgba(255,255,255,.7); line-height: 2; font-size: 16px;">
            Ruhii, you trusted me with something that was supposed to stay between us.<br><br>
            I should have protected that trust. Instead, I told someone I was specifically asked not to tell.<br><br>
            There isn't a clever explanation that can make that okay. There isn't a good enough excuse. I was wrong.
        </p>
    </div>
    <div class="quote-card glass" style="margin-top: 30px;">
        <div class="quote">“You trusted me with something private, and I failed to protect it.”</div>
    </div>
</section>
""", unsafe_allow_html=True)

# SECTION 2 - LETTER
st.markdown("""
<section style="padding: 60px 0;">
    <div class="letter">
        <div class="section-label">A letter from me</div>
        <div class="section-title">Ruhii…</div>
        <p style="color: rgba(255,255,255,.75); line-height: 2; font-size: 16px;">
            I don't really know whether these words can fix anything, and I'm not going to pretend that they can.<br><br>
            You trusted me with something. You clearly told me not to share it. And I still told the same person. That was my mistake. Completely.<br><br>
            What makes me feel worse is knowing that this isn't the first time you've had to forgive me for something similar. You gave me chances before, and instead of proving that I had learned, I repeated the same mistake.<br><br>
            So I understand why you're angry. I understand why you're hurt. And I understand why “sorry” probably doesn't mean much right now.<br><br>
            I'm not asking you to forget what happened. I'm not asking you to immediately forgive me. And I'm definitely not asking you to pretend everything is normal.<br><br>
            I just want you to know that I genuinely regret breaking your trust. Not because you blocked me. Not because you're angry. But because I should have been someone you could safely trust.<br><br>
            If one day you decide to give me another chance, I want to deserve it through my actions.<br><br>
            I'm sorry, Ruhii. Really.
        </p>
        <div class="signature">— Hassan 🤍</div>
    </div>
</section>
""", unsafe_allow_html=True)

# FINAL BUTTON INTERACTION
if st.button("🤍 I Read Everything", use_container_width=True):
    st.balloons()
    st.success("Thank you for reading, Ruhii. Take all the time you need. 🤍")

st.markdown('</div>', unsafe_allow_html=True)
