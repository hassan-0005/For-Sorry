import streamlit as st

# ============================================================
# MIDNIGHT AURORA — FOR RUHII
# Complete single-file Streamlit website
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

/* Hide Streamlit Default UI elements */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { background: transparent !important; }

/* ============================================================
   STAR FIELD
   ============================================================ */

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
.star:nth-child(16) { left: 23%; top: 5%; animation-delay: .7s; }
.star:nth-child(17) { left: 38%; top: 42%; animation-delay: 1.9s; }
.star:nth-child(18) { left: 52%; top: 95%; animation-delay: 3.1s; }
.star:nth-child(19) { left: 68%; top: 6%; animation-delay: 1.1s; }
.star:nth-child(20) { left: 88%; top: 82%; animation-delay: 2.4s; }

@keyframes twinkle {
    0%, 100% {
        opacity: .2;
        transform: scale(.7);
    }
    50% {
        opacity: 1;
        transform: scale(1.5);
    }
}

/* ============================================================
   AURORA GLOWS
   ============================================================ */

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

.aurora.three {
    background: #9333ea;
    left: 30%;
    bottom: -300px;
    animation: auroraThree 20s ease-in-out infinite alternate;
}

@keyframes auroraOne {
    0% { transform: translate(0,0) rotate(0deg); }
    100% { transform: translate(250px,180px) rotate(25deg); }
}

@keyframes auroraTwo {
    0% { transform: translate(0,0) scale(1); }
    100% { transform: translate(-180px,100px) scale(1.3); }
}

@keyframes auroraThree {
    0% { transform: translate(0,0); }
    100% { transform: translate(120px,-160px) scale(1.2); }
}

/* ============================================================
   SHOOTING STARS
   ============================================================ */

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

.shooting-star.a {
    top: 18%;
    left: -10%;
    animation-delay: 2s;
}

.shooting-star.b {
    top: 42%;
    left: -15%;
    animation-delay: 7s;
}

@keyframes shooting {
    0% { transform: translate(0,0) rotate(-35deg); opacity: 0; }
    5% { opacity: 1; }
    20% { transform: translate(120vw,80vh) rotate(-35deg); opacity: 0; }
    100% { opacity: 0; }
}

/* ============================================================
   MAIN CONTENT
   ============================================================ */

.main-content {
    position: relative;
    z-index: 5;
    max-width: 1000px;
    margin: auto;
    padding: 20px;
}

/* HERO SECTION */
.hero {
    min-height: 90vh;
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
    color: rgba(255,255,255,.70);
    font-size: 17px;
    line-height: 1.9;
    font-weight: 300;
}

.scroll-hint {
    margin-top: 60px;
    color: rgba(255,255,255,.35);
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(12px); }
}

/* SECTIONS */
.section {
    padding: 90px 0;
}

.section-label {
    color: #a78bfa;
    text-transform: uppercase;
    letter-spacing: 5px;
    font-size: 11px;
    margin-bottom: 16px;
    font-weight: 600;
}

.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(38px, 6vw, 68px);
    font-weight: 500;
    line-height: 1.1;
    margin-bottom: 30px;
    color: #ffffff;
}

.section-text {
    max-width: 760px;
    color: rgba(255,255,255,.70);
    line-height: 2;
    font-size: 16px;
}

/* GLASS CARDS */
.glass {
    background: linear-gradient(135deg, rgba(255,255,255,.075), rgba(255,255,255,.025));
    border: 1px solid rgba(255,255,255,.12);
    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);
    border-radius: 24px;
    padding: 38px;
    box-shadow: 0 25px 70px rgba(0,0,0,.35);
    transition: .4s ease;
}

.glass:hover {
    border-color: rgba(167,139,250,.4);
}

/* QUOTE CARD */
.quote-card {
    margin: 40px 0;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.quote {
    font-family: 'Playfair Display', serif;
    font-size: clamp(22px, 3.5vw, 38px);
    line-height: 1.55;
    font-style: italic;
    color: #f5f3ff;
}

/* TIMELINE */
.timeline {
    position: relative;
    margin-top: 50px;
    padding-left: 50px;
}

.timeline-line {
    position: absolute;
    left: 20px;
    top: 10px;
    bottom: 10px;
    width: 2px;
    background: linear-gradient(to bottom, #8b5cf6, #22d3ee, transparent);
}

.timeline-item {
    position: relative;
    margin-bottom: 45px;
}

.timeline-dot {
    position: absolute;
    left: -38px;
    top: 5px;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #0b0715;
    border: 2px solid #a78bfa;
    box-shadow: 0 0 15px rgba(167,139,250,.8);
}

.timeline-title {
    font-size: 20px;
    margin-bottom: 8px;
    color: #ffffff;
    font-weight: 500;
}

.timeline-text {
    color: rgba(255,255,255,.60);
    line-height: 1.8;
}

/* PROMISE GRID */
.promise-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-top: 40px;
}

.promise {
    position: relative;
    overflow: hidden;
}

.promise-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 60px;
    color: rgba(167,139,250,.20);
    position: absolute;
    right: 20px;
    top: 10px;
    font-weight: 700;
}

.promise h3 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 28px;
    font-weight: 500;
    margin-bottom: 12px;
}

.promise p {
    color: rgba(255,255,255,.60);
    line-height: 1.8;
    font-size: 15px;
}

/* ENVELOPE */
.envelope-wrapper {
    display: flex;
    justify-content: center;
    padding: 40px 0;
}

.envelope {
    width: 100%;
    max-width: 540px;
    background: linear-gradient(145deg, rgba(139,92,246,.20), rgba(34,211,238,.08));
    border: 1px solid rgba(255,255,255,.15);
    border-radius: 24px;
    padding: 40px;
    text-align: center;
    box-shadow: 0 35px 100px rgba(0,0,0,.5);
}

.envelope-symbol {
    font-size: 60px;
    margin-bottom: 15px;
}

.envelope h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 42px;
    font-weight: 500;
    margin-bottom: 10px;
}

.envelope p {
    color: rgba(255,255,255,.60);
    line-height: 1.8;
}

/* LETTER */
.letter {
    background: linear-gradient(135deg, rgba(255,255,255,.08), rgba(167,139,250,.04));
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 28px;
    padding: clamp(24px, 5vw, 60px);
    margin-top: 30px;
}

.letter-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 45px;
    margin-bottom: 30px;
}

.letter p {
    color: rgba(255,255,255,.75);
    line-height: 2.1;
    font-size: 16px;
    margin-bottom: 20px;
}

.signature {
    margin-top: 40px;
    font-family: 'Cormorant Garamond', serif;
    font-size: 28px;
    color: #ddd6fe;
    font-style: italic;
}

/* FINAL SECTION */
.final {
    padding: 100px 0 60px;
    text-align: center;
}

.final h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(48px, 8vw, 90px);
    font-weight: 500;
    line-height: 1;
    margin: 20px 0;
}

.final p {
    max-width: 600px;
    margin: auto;
    color: rgba(255,255,255,.65);
    line-height: 2;
}

.final-glow {
    width: 180px;
    height: 180px;
    margin: 0 auto 30px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(167,139,250,.35), rgba(34,211,238,.08), transparent 70%);
    animation: finalGlow 4s ease-in-out infinite;
}

@keyframes finalGlow {
    0%,100% { transform: scale(.9); opacity: .65; }
    50% { transform: scale(1.15); opacity: 1; }
}

/* STYLING STREAMLIT BUTTON */
.stButton > button {
    width: 100% !important;
    max-width: 450px !important;
    display: block !important;
    margin: 20px auto !important;
    border-radius: 999px !important;
    border: 1px solid rgba(167,139,250,.5) !important;
    background: linear-gradient(100deg, rgba(124,58,237,.35), rgba(34,211,238,.20)) !important;
    color: white !important;
    padding: 16px 32px !important;
    font-size: 15px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    transition: .3s ease !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    border-color: rgba(34,211,238,.8) !important;
    box-shadow: 0 10px 30px rgba(124,58,237,.35) !important;
}

@media (max-width: 700px) {
    .promise-grid { grid-template-columns: 1fr; }
    .main-content { padding: 12px; }
    .timeline { padding-left: 35px; }
    .timeline-dot { left: -28px; }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# BACKGROUND ANIMATED HTML
# ============================================================

st.markdown("""
<div class="star-field">
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div><div class="star"></div>
    <div class="star"></div><div class="star"></div>
</div>

<div class="aurora one"></div>
<div class="aurora two"></div>
<div class="aurora three"></div>

<div class="shooting-star a"></div>
<div class="shooting-star b"></div>
""", unsafe_allow_html=True)


# ============================================================
# CONTENT WRAPPER
# ============================================================

st.markdown('<div class="main-content">', unsafe_allow_html=True)


# HERO
st.markdown("""
<section class="hero">
<div>
    <div class="eyebrow">A little something for someone important</div>
    <h1>Ruhii</h1>
    <div class="hero-sub">
        I know you're angry.<br>
        And honestly… I understand why.<br><br>
        So this isn't here to convince you.<br>
        It's simply here to say what I should have said properly.
    </div>
    <div class="scroll-hint">↓ &nbsp; Take your time &nbsp; ↓</div>
</div>
</section>
""", unsafe_allow_html=True)


# SECTION 01
st.markdown("""
<section class="section">
    <div class="section-label">01 / No Excuses</div>
    <div class="section-title">I won't defend myself.</div>
    <div class="glass">
        <p class="section-text">
            Ruhii, you trusted me with something that was supposed to stay between us.<br><br>
            I should have protected that trust.<br><br>
            Instead, I told someone I was specifically asked not to tell.<br><br>
            There isn't a clever explanation that can make that okay.<br><br>
            There isn't a good enough excuse.<br><br>
            <b>I was wrong.</b>
        </p>
    </div>

    <div class="quote-card glass">
        <div class="quote">
            “You trusted me with something private, and I failed to protect it.”
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# SECTION 02
st.markdown("""
<section class="section">
    <div class="section-label">02 / I Understand</div>
    <div class="section-title">I know why this time hurts more.</div>
    <p class="section-text">
        This wasn't the first time I made a mistake like this. You had already given me chances. You had already forgiven me. And somehow, I repeated something I should have learned from.
    </p>

    <div class="timeline">
        <div class="timeline-line"></div>
        
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">You trusted me</div>
            <div class="timeline-text">You believed something you told me would remain safe with me.</div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">I broke that trust</div>
            <div class="timeline-text">I told someone what I was supposed to keep private.</div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">You forgave me before</div>
            <div class="timeline-text">You gave me chances that I should have valued much more.</div>
        </div>

        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-title">And I repeated it</div>
            <div class="timeline-text">That's the part I can't ignore or pretend isn't serious.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# SECTION 03
st.markdown("""
<section class="section">
    <div class="section-label">03 / The Truth</div>
    <div class="section-title">Sorry isn't a reset button.</div>
    <div class="glass">
        <p class="section-text">
            I know I can write a hundred “sorry” messages.<br>
            I know I can make a beautiful website.<br>
            I know I can say that I won't do it again.<br>
            But none of those things automatically rebuild trust.<br>
            And I don't want to pretend that they do.<br><br>
            <b>If I ever get another chance, I want to earn that trust through what I actually do — not through what I promise tonight.</b>
        </p>
    </div>
</section>
""", unsafe_allow_html=True)


# SECTION 04
st.markdown("""
<section class="section">
    <div class="section-label">04 / Four Things</div>
    <div class="section-title">Things I should have understood.</div>

    <div class="promise-grid">
        <div class="promise glass">
            <div class="promise-number">01</div>
            <h3>Trust</h3>
            <p>Trust isn't something I get automatically just because we're close. It's something I have to protect.</p>
        </div>

        <div class="promise glass">
            <div class="promise-number">02</div>
            <h3>Privacy</h3>
            <p>If you tell me something privately, I should know that it belongs with me — not somewhere else.</p>
        </div>

        <div class="promise glass">
            <div class="promise-number">03</div>
            <h3>Forgiveness</h3>
            <p>Your forgiveness is a gift. It's not something I should expect simply because I apologized.</p>
        </div>

        <div class="promise glass">
            <div class="promise-number">04</div>
            <h3>Change</h3>
            <p>Real change isn't saying “I won't do it again.” It's behaving differently when the next opportunity comes.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# SECTION 05 - LETTER ENVELOPE
st.markdown("""
<section class="section">
    <div class="section-label">05 / A Letter</div>
    <div class="section-title">Something I wanted you to read.</div>

    <div class="envelope-wrapper">
        <div class="envelope">
            <div class="envelope-symbol">✉️</div>
            <h2>For Ruhii</h2>
            <p>No pressure. No conditions. Just a letter from someone who knows he messed up.</p>
        </div>
    </div>

    <div class="letter">
        <div class="section-label">A letter from me</div>
        <div class="letter-title">Ruhii…</div>

        <p>I don't really know whether these words can fix anything, and I'm not going to pretend that they can.</p>
        <p>You trusted me with something. You clearly told me not to share it. And I still told the same person. That was my mistake. Completely.</p>
        <p>What makes me feel worse is knowing that this isn't the first time you've had to forgive me for something similar. You gave me chances before, and instead of proving that I had learned, I repeated the same mistake.</p>
        <p>So I understand why you're angry. I understand why you're hurt. And I understand why “sorry” probably doesn't mean much right now.</p>
        <p>I'm not asking you to forget what happened. I'm not asking you to immediately forgive me. And I'm definitely not asking you to pretend everything is normal.</p>
        <p>I just want you to know that I genuinely regret breaking your trust. Not because you blocked me. Not because you're angry. But because I should have been someone you could safely trust.</p>
        <p>If one day you decide to give me another chance, I don't want that chance because of this website, or because I said the right words.</p>
        <p><b>I want to deserve it through my actions.</b></p>
        <p>And if you need time, I'll respect that too.</p>
        <p>I'm sorry, Ruhii. Really.</p>

        <div class="signature">— Hassan 🤍</div>
    </div>
</section>
""", unsafe_allow_html=True)


# SECTION 06 - PROMISE
st.markdown("""
<section class="section">
    <div class="section-label">06 / Not A Promise To Impress You</div>
    <div class="section-title">I won't ask you to trust my words.</div>

    <div class="glass">
        <div class="quote">“I'll let my actions speak.”</div>
        <br>
        <p class="section-text">
            If I ever get the opportunity again:<br><br>
            • I will protect what you tell me.<br><br>
            • I will understand that private means private.<br><br>
            • I will stop treating forgiveness like a reset button.<br><br>
            • And most importantly, I will understand that being your best friend is a responsibility, not just a title.
        </p>
    </div>
</section>
""", unsafe_allow_html=True)


# FINAL SECTION
st.markdown("""
<section class="final">
    <div class="final-glow"></div>
    <div class="section-label">07 / One Last Thing</div>
    <h1>Take your time,<br>Ruhii.</h1>
    <p>
        I can't undo what I did.<br>
        I can't force you to forgive me.<br>
        And I can't demand your trust back.<br><br>
        All I can do is accept that I hurt you, be genuinely sorry, and become better than the person who made that mistake.<br><br>
        Whenever you're ready.<br><br>
        <b>I'm sorry. 🤍</b>
    </p>
</section>
""", unsafe_allow_html=True)


# BUTTON INTERACTION
if st.button("🤍 I Read Everything", use_container_width=True):
    st.balloons()
    st.markdown("""
    <div style="text-align:center; padding: 40px 20px; background: rgba(139,92,246,.15); border-radius: 24px; border: 1px solid rgba(167,139,250,.4); margin-top: 30px;">
        <div style="font-family:'Cormorant Garamond',serif; font-size:42px; color:#ffffff; margin-bottom: 15px;">
            Thank you, Ruhii.
        </div>
        <p style="color:rgba(255,255,255,.70); font-size:16px; line-height:1.8; max-width:550px; margin:0 auto;">
            Whatever you decide, I hope you know that this apology was meant sincerely. 🤍
        </p>
    </div>
    """, unsafe_allow_html=True)


# FOOTER
st.markdown("""
<div style="text-align:center; padding: 60px 0 30px; color:rgba(255,255,255,.2); font-size:11px; letter-spacing:2px;">
    MADE WITH SINCERITY · FOR RUHII
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
