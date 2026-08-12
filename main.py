import streamlit as st
import random

st.set_page_config(page_title="For Ruhii 🌸", page_icon="🌸", layout="wide", initial_sidebar_state="collapsed")

PAGES = ["welcome", "hurt", "friendship", "letter", "wait"]

if "page" not in st.session_state or st.session_state.page not in PAGES:
    st.session_state.page = "welcome"
if "letter_open" not in st.session_state:
    st.session_state.letter_open = False
if "wish_sent" not in st.session_state:
    st.session_state.wish_sent = False

def go_to(page):
    st.session_state.page = page if page in PAGES else "welcome"

def floating_layer(items, count=18):
    spans = []
    for _ in range(count):
        e = random.choice(items)
        spans.append(
            f'<span class="floaty" style="left:{random.uniform(2,98):.1f}vw;'
            f'animation-delay:{random.uniform(0,10):.1f}s;'
            f'animation-duration:{random.uniform(10,20):.1f}s;'
            f'font-size:{random.uniform(14,28):.1f}px">{e}</span>'
        )
    st.markdown('<div class="floaty-wrap">' + ''.join(spans) + '</div>', unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Dancing+Script:wght@500;600;700&family=Poppins:wght@300;400;500;600&display=swap');
*{box-sizing:border-box}
html,body{overflow-x:hidden}
#MainMenu,header,footer{visibility:hidden}
.stApp{
 background:radial-gradient(circle at 15% 15%,rgba(255,255,255,.7),transparent 25%),
 radial-gradient(circle at 85% 20%,rgba(255,182,213,.45),transparent 28%),
 linear-gradient(160deg,#fff0f5 0%,#ffe4ec 35%,#ffd9e8 65%,#f6c9e0 100%);
 background-size:300% 300%;background-attachment:fixed;animation:bg 18s ease infinite;overflow-x:hidden
}
@keyframes bg{0%,100%{background-position:0 50%}50%{background-position:100% 50%}}
.block-container{max-width:1050px;padding:1rem .9rem 3rem!important;position:relative;z-index:2}
.floaty-wrap{position:fixed;inset:0;overflow:hidden;pointer-events:none;z-index:1}
.floaty{position:absolute;top:110vh;opacity:.7;animation:up 15s ease-in-out infinite;filter:drop-shadow(0 0 6px rgba(255,143,171,.45))}
@keyframes up{0%{transform:translate(0,0) rotate(0);opacity:0}10%{opacity:.75}50%{transform:translate(20px,-55vh) rotate(12deg)}100%{transform:translate(-15px,-125vh) rotate(-10deg);opacity:0}}
.dream-title{font-family:'Playfair Display',serif;text-align:center;color:#b51f61;line-height:1.15;margin:25px auto 10px;text-shadow:0 4px 18px rgba(181,31,97,.15);animation:show 1.1s ease both}
.script-quote{font-family:'Dancing Script',cursive;text-align:center;color:#8d3154;line-height:1.6;animation:show 1.4s ease both}
.soft-para,.final-note{color:#7a2e46;text-align:center;line-height:1.9;max-width:760px;margin:auto}
@keyframes show{from{opacity:0;transform:translateY(25px)}to{opacity:1;transform:translateY(0)}}
.glass-card{background:rgba(255,255,255,.48);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.7);border-radius:26px;padding:28px 22px;text-align:center;box-shadow:0 8px 32px rgba(214,51,108,.15);transition:.4s;animation:show 1.3s ease both;margin-bottom:20px}
.glass-card:hover{transform:translateY(-8px) scale(1.02);box-shadow:0 16px 40px rgba(214,51,108,.28)}
.glass-card h3{font-family:'Playfair Display',serif;color:#c2185b}
.glass-card p{color:#8a3a55;line-height:1.7}
div.stButton>button{background:linear-gradient(135deg,#ffb6c1,#ff8fab,#e75480);color:#fff;font-weight:600;border:2px solid rgba(255,215,0,.35);border-radius:40px;min-height:48px;padding:12px 24px;box-shadow:0 6px 20px rgba(231,84,128,.35);transition:.35s}
div.stButton>button:hover{transform:translateY(-4px) scale(1.02);box-shadow:0 0 25px rgba(255,182,213,.9),0 10px 25px rgba(231,84,128,.4);border-color:gold;color:#fff}
.envelope-wrap{display:flex;justify-content:center;margin:30px auto;animation:show 1.6s ease both}
.envelope{width:min(300px,78vw);height:200px;background:linear-gradient(135deg,#fff0f5,#ffe0eb);border-radius:14px;position:relative;box-shadow:0 15px 35px rgba(214,51,108,.25);border:2px solid #ffd1dc}
.envelope:before{content:"";position:absolute;top:0;left:0;border-left:150px solid transparent;border-right:150px solid transparent;border-top:110px solid #ffc2d6}
.seal{position:absolute;top:78px;left:50%;transform:translateX(-50%);width:50px;height:50px;background:radial-gradient(circle at 35% 35%,#ff8fab,#c2185b);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;animation:glow 2.4s infinite;z-index:2}
@keyframes glow{0%,100%{box-shadow:0 0 10px rgba(255,143,171,.6)}50%{box-shadow:0 0 25px rgba(255,143,171,1)}}
.letter-paper{background:repeating-linear-gradient(#fff6f9,#fff6f9 34px,#ffe3ec 35px);border-radius:18px;padding:45px 40px;max-width:700px;width:100%;margin:20px auto;box-shadow:0 12px 35px rgba(214,51,108,.2);border:1px solid #ffd1dc;animation:show 1.4s ease}
.letter-paper p{font-family:'Dancing Script',cursive;font-size:1.5em;color:#7a2e46;line-height:1.8}
.reveal-line{font-family:'Dancing Script',cursive;font-size:1.8em;text-align:center;color:#ad1457;opacity:0;animation:show 1.4s ease forwards;line-height:1.5}
.d1{animation-delay:.2s}.d2{animation-delay:1.1s}.d3{animation-delay:2s}.d4{animation-delay:2.9s}
@media(max-width:700px){
 .block-container{padding:.6rem .7rem 2rem!important}
 .dream-title{font-size:2.25rem!important;margin-top:18px}
 .script-quote{font-size:1.35rem!important}
 .soft-para,.final-note{font-size:.92rem;line-height:1.75;padding:0 8px}
 .glass-card{padding:22px 17px;border-radius:21px}
 .glass-card h3{font-size:1.15rem}.glass-card p{font-size:.88rem}
 .letter-paper{padding:28px 20px;border-radius:15px}
 .letter-paper p{font-size:1.25rem;line-height:1.65}
 .reveal-line{font-size:1.4rem;padding:0 8px}
 .envelope{height:170px}.envelope:before{border-left-width:39vw;border-right-width:39vw;border-top-width:95px}
 .seal{top:66px}.floaty{opacity:.55}
}
</style>
""", unsafe_allow_html=True)

def page_welcome():
    floating_layer(["✨","💗","🌸","☁️","🎀"],20)
    st.markdown("<h1 class='dream-title' style='font-size:3.2em'>Hey Ruhii... 🌸</h1>",unsafe_allow_html=True)
    st.markdown("<p class='script-quote' style='font-size:1.6em'>\"I made a tiny little world for someone very special.\"</p>",unsafe_allow_html=True)
    st.markdown("<div style='height:35px'></div>",unsafe_allow_html=True)
    _,c,_=st.columns([1,1,1])
    with c:
        if st.button("Meri Choti Si Duniya Mein Aao ✨",use_container_width=True):
            go_to("hurt");st.rerun()
    st.markdown("<div style='height:55px'></div><p class='soft-para'>🌙 a soft glowing moon watches quietly over a world of pink clouds and glitter rain, waiting for you to step inside...</p>",unsafe_allow_html=True)

def page_hurt():
    floating_layer(["🌸","❤️","🥀","💮"],16)
    st.markdown("<h1 class='dream-title' style='font-size:2.6em'>Mujhe Pata Hai Tum Naraz Ho... 🥺</h1>",unsafe_allow_html=True)
    for cls,text in [("d1","You trusted me with something important. 🌷"),("d2","You asked me to keep it a secret."),("d3","And I told the same person you asked me not to."),("d4","I was wrong — and I'm not making any excuses for it.")]:
        st.markdown(f"<p class='reveal-line {cls}'>{text}</p>",unsafe_allow_html=True)
    st.markdown("<div style='height:35px'></div>",unsafe_allow_html=True)
    _,c,_=st.columns([1,1,1])
    with c:
        if st.button("Hamari Kahani Mein Agay Chalo 🦋",use_container_width=True):
            go_to("friendship");st.rerun()

def page_friendship():
    floating_layer(["🦋","💗","✨","🌙"],16)
    st.markdown("<h1 class='dream-title' style='font-size:2.6em'>Hamari Dosti 🦋</h1>",unsafe_allow_html=True)
    memories=[("🌸","Pehli Yaad","The moment this friendship quietly began."),("💗","Sab Se Mazedaar Lamha","The one we still laugh about randomly."),("🦋","Ek Muskurahat","A tiny moment that stayed with me."),("🌙","Hamari Pasandida Baat","The talk that felt like it lasted forever.")]
    cols=st.columns(2)
    for i,(e,t,d) in enumerate(memories):
        with cols[i%2]:
            st.markdown(f"<div class='glass-card'><h3>{e} {t}</h3><p>{d}</p></div>",unsafe_allow_html=True)
    st.markdown("<p class='script-quote' style='font-size:1.9em'>\"Some people slowly become home.\"</p>",unsafe_allow_html=True)
    _,c,_=st.columns([1,1,1])
    with c:
        if st.button("Meri Chitthi Parho 💌",use_container_width=True):
            go_to("letter");st.rerun()

def page_letter():
    floating_layer(["💌","🌹","✨","🦋"],14)
    st.markdown("<h1 class='dream-title' style='font-size:2.6em'>Meri Chitthi 💌</h1>",unsafe_allow_html=True)
    if not st.session_state.letter_open:
        st.markdown("<div class='envelope-wrap'><div class='envelope'><div class='seal'>🌹</div></div></div>",unsafe_allow_html=True)
        _,c,_=st.columns([1,1,1])
        with c:
            if st.button("Chitthi Kholo 💌",use_container_width=True):
                st.session_state.letter_open=True;st.rerun()
    else:
        st.markdown("""<div class="letter-paper">
        <p>Dear Ruhii,</p>
        <p>I broke your trust, and I know that's not something small.</p>
        <p>This isn't the first time I've made a mistake — and I understand why this time feels different, why it hurts more, why it's harder to just let go.</p>
        <p>I'm not asking you to forgive me right now. I don't expect that, and I don't think I deserve it yet.</p>
        <p>I just want the chance to earn your trust back — slowly, honestly, through actions and not words.</p>
        <p>Take all the time you need. I'll still be here.</p>
        <p>With love,<br>Hassan 🤍</p>
        </div>""",unsafe_allow_html=True)
        _,c,_=st.columns([1,1,1])
        with c:
            if st.button("Apna Waqt Lo 🌷",use_container_width=True):
                go_to("wait");st.rerun()

def page_wait():
    floating_layer(["🌸","🏮","✨","🦋","🕊️"],18)
    st.markdown("<h1 class='dream-title' style='font-size:2.8em'>Apna Waqt Lo, Ruhii 🌷</h1>",unsafe_allow_html=True)
    for cls,text in [("d1","Koi pressure nahi."),("d2","Koi umeed nahi."),("d3","Bas dil se ek sorry."),("d4","— Hassan 🤍")]:
        st.markdown(f"<p class='reveal-line {cls}'>{text}</p>",unsafe_allow_html=True)
    _,c,_=st.columns([1,1,1])
    with c:
        if st.button("Apni Dua Bhejo ✨",use_container_width=True):
            st.session_state.wish_sent=True;st.rerun()
    if st.session_state.wish_sent:
        floating_layer(["❤️","✨","💖"],20)
        st.markdown("<p class='script-quote' style='font-size:1.6em'>\"I hope one day this hurt becomes just one small chapter of a friendship that grew stronger.\"</p>",unsafe_allow_html=True)
    st.markdown("<p class='final-note'>Whatever you decide, I hope you know that this apology was meant sincerely. 🤍</p>",unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;padding:30px;color:rgba(122,46,70,.55);font-size:11px;letter-spacing:2px'>DIL SE BANAYA HAI · SIRF RUHII KE LIYE</div>",unsafe_allow_html=True)

def main():
    if st.session_state.page not in PAGES:
        st.session_state.page="welcome"
    {
        "welcome":page_welcome,
        "hurt":page_hurt,
        "friendship":page_friendship,
        "letter":page_letter,
        "wait":page_wait,
    }[st.session_state.page]()

if __name__=="__main__":
    main()
