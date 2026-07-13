import React, { useState, useEffect, useRef } from "react";
import { 
  Heart, 
  Sparkles, 
  ChevronLeft, 
  ChevronRight, 
  Volume2, 
  VolumeX, 
  Play, 
  Pause, 
  Gift, 
  RefreshCw,
  Info,
  CheckCircle,
  HelpCircle,
  Smile,
  Users,
  Compass,
  MessageCircle,
  Coffee,
  HeartCrack,
  Star
} from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { db } from "./firebase";
import { doc, getDoc, setDoc, updateDoc } from "firebase/firestore";

// --- MEMORY SLIDES ---
const MEMORIES = [
  {
    icon: "✨",
    title: "Pehli baar baat hui",
    desc: "Wo din jab humari pehli conversation shuru hui thi. Ekdum anjaan thhe hum dono, par us din ke baad se meri life kitni haseen ho gayi, tum soch bhi nahi sakti.",
    tag: "First Interaction",
    gradient: "from-pink-500/20 to-purple-500/20 border-pink-500/30"
  },
  {
    icon: "😂",
    title: "Hansi Mazak",
    desc: "Bematlab ke jokes par ghanto tak hasna, pagal jaisi baatein karna, aur har pal ko dher saari masti se bhar dena. Tumhari hansi sabse khoobsurat sound hai mere liye.",
    tag: "Endless Laughs",
    gradient: "from-purple-500/20 to-indigo-500/20 border-purple-500/30"
  },
  {
    icon: "📸",
    title: "Beautiful Memories",
    desc: "Humari saari pyari baatein aur lamhe jo hamesha mere dil ke sabse kareeb rahenge. Har ek chat, har ek mazaak, aur har ek serious baat mere liye bohot anmol hai.",
    tag: "Golden Moments",
    gradient: "from-indigo-500/20 to-sky-500/20 border-indigo-500/30"
  },
  {
    icon: "☕",
    title: "Random Conversations",
    desc: "Chai ke bahaane ho ya raat ke 2 baje wali baatein bina kisi darr ke... jahan humne duniya jahan ki baatein share ki. Wo sukoon mujhe kahin aur nahi milta.",
    tag: "Midnight Talks",
    gradient: "from-sky-500/20 to-pink-500/20 border-sky-500/30"
  },
  {
    icon: "🤍",
    title: "Har mushkil waqt",
    desc: "Jab bhi life ne thoda pareshan kiya, ek dusre ka dhyan rakhna aur humesha support ke liye khade rehna. Tumhare hone se mujhe har mushkil aasan lagti hai.",
    tag: "Always Together",
    gradient: "from-pink-500/20 to-violet-500/20 border-violet-500/30"
  },
  {
    icon: "🌹",
    title: "Friendship Forever",
    desc: "Ye dosti ek aisi blessing hai jo main kabhi khona nahi chahta. Chahe kitni bhi pareshaniyan aayen, tum hamesha meri best friend rahungi. Forever.",
    tag: "Infinite Bond",
    gradient: "from-violet-500/20 to-pink-500/20 border-pink-500/30"
  }
];

// --- 60+ EMOTIONAL APOLOGY MESSAGES ---
const APOLOGY_MESSAGES = [
  "Mujhe tumhari bohat yaad aati hai. Please maaf kar do na... 🥺",
  "Please naraz mat raho, tumhare bina mera din ekdum adhura hai.",
  "Main waqai sorry hoon, mera maqsad tumhara dil dukhana bilkul nahi tha.",
  "Tumhari friendship meri life mein sabse keemti cheez hai. ❤️",
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
];

// --- APOLOGY LETTER LINES ---
const LETTER_LINES = [
  "Dear Ruhii ❤️",
  "Main perfect nahi hoon, mujhe pata hai...",
  "Kabhi kabhi mujhse nadani mein bohot badi galtiyan ho jati hain...",
  "Lekin main dil se kehta hoon, kabhi bhi jaan bujh kar tumhara dil dukhana nahi chaha...",
  "Tumhari dosti meri life ki sabse khoobsurat aur anmol cheezon mein se ek hai...",
  "Agar meri kisi bhi baat, mazaak ya behavior se tum hurt hui ho...",
  "To main sach mein, dil ki गहराइयों se Sorry kehta hoon... 🥺",
  "Main sirf itna chahta hoon ki hum phir se pehle ki tarah sath has sakein...",
  "Bematlab ki baaton par ladd sakein aur dher saari achi memories bana sakein...",
  "Thank you so much for reading this till the end...",
  "Tum mere liye bohot, bohot special ho aur hamesha rahungi. ❤️",
  "— Hassan"
];

// --- MUSIC SONGS ---
const SOUND_TRACKS = [
  {
    title: "Soft Piano Melancholy",
    url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
  },
  {
    title: "Sweet Instrumental",
    url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
  },
  {
    title: "Dreamy Piano Breeze",
    url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"
  }
];

export default function App() {
  // Navigation & Screen States
  const [started, setStarted] = useState(false);
  const [welcomeStep, setWelcomeStep] = useState(0);
  
  // Firebase sync state
  const [docId] = useState<string>(() => {
    let savedId = localStorage.getItem("ruhii_feedback_id");
    if (!savedId) {
      savedId = `ruhii-${Math.random().toString(36).substring(2, 11)}`;
      localStorage.setItem("ruhii_feedback_id", savedId);
    }
    return savedId;
  });
  const [isLoaded, setIsLoaded] = useState(false);
  const [messageText, setMessageText] = useState("");
  const [isSendingMessage, setIsSendingMessage] = useState(false);
  const [messageSent, setMessageSent] = useState(false);

  // Custom interactive click states
  const [heartClicks, setHeartClicks] = useState(0);
  const [currentMessage, setCurrentMessage] = useState("Tap the glowing heart to see a secret message... ❤️");
  const [memoryIndex, setMemoryIndex] = useState(0);
  
  // Letter state
  const [isLetterOpen, setIsLetterOpen] = useState(false);
  const [revealedLetterLines, setRevealedLetterLines] = useState<string[]>([]);
  
  // Surprise state
  const [surpriseOpened, setSurpriseOpened] = useState(false);
  const [forgiveStatus, setForgiveStatus] = useState<"yes" | "think" | null>(null);
  
  // Audio state
  const [isPlaying, setIsPlaying] = useState(false);
  const [trackIndex, setTrackIndex] = useState(0);
  const [volume, setVolume] = useState(0.4);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  // Floating particles generator
  const [particles, setParticles] = useState<{ id: number; char: string; left: number; delay: number; duration: number; size: number; driftX: number; rotation: number }[]>([]);
  const [clickHearts, setClickHearts] = useState<{ id: number; left: number; delay: number; size: number }[]>([]);

  // Init base floating particles
  useEffect(() => {
    const chars = ["❤️", "✨", "🌸", "⭐", "💖"];
    const baseParticles = Array.from({ length: 28 }, (_, i) => ({
      id: i,
      char: chars[Math.floor(Math.random() * chars.length)],
      left: Math.random() * 100,
      delay: Math.random() * -15, // Negative delay so particles are already dispersed
      duration: 10 + Math.random() * 12,
      size: 14 + Math.random() * 16,
      driftX: -30 + Math.random() * 60,
      rotation: 180 + Math.random() * 360
    }));
    setParticles(baseParticles);
  }, []);

  // Sync volume state with HTML5 audio
  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.volume = volume;
    }
  }, [volume]);

  // Load saved feedback from Firebase on mount
  useEffect(() => {
    const loadSavedData = async () => {
      try {
        const docRef = doc(db, "feedback", docId);
        const docSnap = await getDoc(docRef);
        if (docSnap.exists()) {
          const data = docSnap.data();
          if (data.clicks !== undefined) {
            setHeartClicks(data.clicks);
          }
          if (data.status !== undefined && data.status !== "none") {
            setForgiveStatus(data.status as "yes" | "think");
            setSurpriseOpened(true); // Auto open if she already gave feedback
          }
          if (data.message !== undefined) {
            setMessageText(data.message);
            if (data.message) {
              setMessageSent(true);
            }
          }
        }
      } catch (error) {
        console.error("Error loading saved feedback:", error);
      } finally {
        setIsLoaded(true);
      }
    };
    loadSavedData();
  }, [docId]);

  // Save feedback changes helper
  const saveFeedback = async (updates: { status?: "yes" | "think" | "none"; clicks?: number; message?: string }) => {
    try {
      const docRef = doc(db, "feedback", docId);
      const docSnap = await getDoc(docRef);
      const timestamp = new Date().toISOString();

      if (!docSnap.exists()) {
        await setDoc(docRef, {
          status: updates.status || "none",
          clicks: updates.clicks !== undefined ? updates.clicks : 0,
          message: updates.message || "",
          timestamp
        });
      } else {
        const dataToSave: any = {};
        if (updates.status !== undefined) dataToSave.status = updates.status;
        if (updates.clicks !== undefined) dataToSave.clicks = updates.clicks;
        if (updates.message !== undefined) dataToSave.message = updates.message;
        dataToSave.timestamp = timestamp;
        await updateDoc(docRef, dataToSave);
      }
    } catch (error) {
      console.error("Error saving feedback:", error);
    }
  };

  // Welcome Step progressive reveal
  const handleNextWelcome = () => {
    if (welcomeStep < 4) {
      setWelcomeStep(prev => prev + 1);
    } else {
      setStarted(true);
      // Auto-start music softly as a friendly gesture
      setIsPlaying(true);
      if (audioRef.current) {
        audioRef.current.play().catch(() => {
          // Ignore auto-play blocking errors, standard browser behavior
        });
      }
    }
  };

  // Toggle Music play/pause
  const togglePlay = () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
      setIsPlaying(false);
    } else {
      audioRef.current.play().then(() => {
        setIsPlaying(true);
      }).catch(err => {
        console.log("Audio play failed:", err);
      });
    }
  };

  // Change Music track
  const handleTrackChange = (index: number) => {
    setTrackIndex(index);
    setIsPlaying(true);
    setTimeout(() => {
      if (audioRef.current) {
        audioRef.current.load();
        audioRef.current.play().catch(err => console.log(err));
      }
    }, 50);
  };

  // Click on main heartbeat heart
  const handleHeartClick = () => {
    setHeartClicks(prev => {
      const nextClicks = prev + 1;
      saveFeedback({ clicks: nextClicks });
      return nextClicks;
    });
    const randomIndex = Math.floor(Math.random() * APOLOGY_MESSAGES.length);
    setCurrentMessage(APOLOGY_MESSAGES[randomIndex]);

    // Spawn 8 flying hearts that rise up rapidly
    const newHearts = Array.from({ length: 8 }, (_, i) => ({
      id: Date.now() + i,
      left: 15 + Math.random() * 70, // Keep centered near heart
      delay: Math.random() * 0.4,
      size: 16 + Math.random() * 20
    }));

    setClickHearts(prev => [...prev, ...newHearts]);

    // Cleanup click hearts after animation completes (3 seconds)
    setTimeout(() => {
      setClickHearts(prev => prev.filter(h => !newHearts.some(nh => nh.id === h.id)));
    }, 3000);
  };

  // Trigger typewriter letter lines progressive animation
  useEffect(() => {
    if (isLetterOpen) {
      setRevealedLetterLines([]);
      let currentIdx = 0;
      const interval = setInterval(() => {
        if (currentIdx < LETTER_LINES.length) {
          setRevealedLetterLines(prev => [...prev, LETTER_LINES[currentIdx]]);
          currentIdx++;
        } else {
          clearInterval(interval);
        }
      }, 900); // progressive typing speed
      return () => clearInterval(interval);
    }
  }, [isLetterOpen]);

  return (
    <div id="app-container" className="min-h-screen bg-slate-950 flex justify-center items-center py-0 sm:py-6 px-0 sm:px-4 relative overflow-hidden select-none">
      
      {/* Outer Glow Background Ornaments (Desktop Decor) */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-pink-500/10 rounded-full filter blur-3xl animate-glow-circle pointer-events-none hidden md:block" style={{ "--glow-duration": "10s" } as React.CSSProperties} />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full filter blur-3xl animate-glow-circle pointer-events-none hidden md:block" style={{ "--glow-duration": "14s" } as React.CSSProperties} />
      <div className="absolute top-1/2 right-1/3 w-80 h-80 bg-sky-500/10 rounded-full filter blur-3xl animate-glow-circle pointer-events-none hidden md:block" style={{ "--glow-duration": "12s" } as React.CSSProperties} />

      {/* HTML5 Native Audio element (Hidden) */}
      <audio 
        ref={audioRef}
        src={SOUND_TRACKS[trackIndex].url}
        loop
      />

      {/* SMARTPHONE WRAPPER (Mobile-First Canvas) */}
      <div 
        id="phone-frame" 
        className={`w-full max-w-md min-h-screen sm:min-h-[850px] sm:max-h-[900px] sm:rounded-[40px] bg-slate-900/60 backdrop-blur-2xl border-0 sm:border-4 border-slate-800 shadow-[0_0_50px_rgba(244,63,94,0.15)] relative overflow-y-auto overflow-x-hidden flex flex-col justify-between scrollbar-none transition-all duration-700 ${
          surpriseOpened && forgiveStatus === 'yes' ? 'ring-8 ring-pink-500/30 bg-pink-950/20' : ''
        }`}
      >
        
        {/* Particle Overlay (Contained in Phone Viewport) */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none z-0">
          {/* Constant slow drifting background elements */}
          {particles.map((p) => (
            <div
              key={p.id}
              className="absolute animate-drift text-opacity-70 select-none"
              style={{
                left: `${p.left}%`,
                fontSize: `${p.size}px`,
                animationDelay: `${p.delay}s`,
                "--drift-duration": `${p.duration}s`,
                "--drift-x": `${p.driftX}px`,
                "--drift-rotation": `${p.rotation}deg`
              } as React.CSSProperties}
            >
              {p.char}
            </div>
          ))}

          {/* Click triggered heartbursts */}
          {clickHearts.map((h) => (
            <motion.div
              key={h.id}
              initial={{ y: "75vh", x: `${h.left}vw`, opacity: 1, scale: 0.5 }}
              animate={{ y: "-10vh", x: `${h.left + (Math.random() * 40 - 20)}vw`, opacity: 0, scale: 1.5, rotate: Math.random() * 180 - 90 }}
              transition={{ duration: 2.2, ease: "easeOut", delay: h.delay }}
              className="absolute text-pink-500 drop-shadow-[0_0_10px_rgba(239,68,68,0.7)]"
              style={{ fontSize: `${h.size}px` }}
            >
              ❤️
            </motion.div>
          ))}

          {/* Extra fast floating hearts if surprise YES is active */}
          {surpriseOpened && forgiveStatus === "yes" && (
            Array.from({ length: 20 }).map((_, i) => (
              <div
                key={`yes-heart-${i}`}
                className="absolute animate-drift text-rose-500"
                style={{
                  left: `${Math.random() * 100}%`,
                  fontSize: `${18 + Math.random() * 20}px`,
                  animationDelay: `${Math.random() * -5}s`,
                  "--drift-duration": `${4 + Math.random() * 4}s`,
                  "--drift-x": `${-50 + Math.random() * 100}px`,
                  "--drift-rotation": `${360}deg`
                } as React.CSSProperties}
              >
                {["❤️", "💖", "🌸", "✨"][Math.floor(Math.random() * 4)]}
              </div>
            ))
          )}
        </div>

        {/* --- SCREEN 1: WELCOME INTRO --- */}
        <AnimatePresence mode="wait">
          {!started ? (
            <motion.div 
              key="welcome-screen"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex-1 flex flex-col justify-between p-6 relative z-10 text-center"
            >
              {/* Decorative Top Accent */}
              <div className="flex justify-center mt-6">
                <span className="px-3 py-1 rounded-full text-[11px] font-mono tracking-widest uppercase bg-pink-500/10 text-pink-300 border border-pink-500/20">
                  Welcome in
                </span>
              </div>

              {/* Progressive Lines Container */}
              <div className="my-auto space-y-8 py-10">
                <AnimatePresence mode="popLayout">
                  {welcomeStep >= 0 && (
                    <motion.div
                      initial={{ opacity: 0, y: 15 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="space-y-6"
                    >
                      <h1 className="text-4xl font-semibold font-display text-transparent bg-clip-text bg-gradient-to-r from-pink-300 via-purple-300 to-sky-200">
                        Hi Ruhii 👋
                      </h1>
                    </motion.div>
                  )}

                  {welcomeStep >= 1 && (
                    <motion.p
                      initial={{ opacity: 0, y: 15 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.1 }}
                      className="text-lg text-slate-300 leading-relaxed max-w-xs mx-auto"
                    >
                      Aaj main tumse sirf ek baat kehna chahta hoon...
                    </motion.p>
                  )}

                  {welcomeStep >= 2 && (
                    <motion.p
                      initial={{ opacity: 0, y: 15 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.1 }}
                      className="text-lg text-pink-300 font-medium"
                    >
                      Please poori website dekhna...
                    </motion.p>
                  )}

                  {welcomeStep >= 3 && (
                    <motion.p
                      initial={{ opacity: 0, y: 15 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: 0.1 }}
                      className="text-lg text-slate-300"
                    >
                      Ye sirf website nahi...
                    </motion.p>
                  )}

                  {welcomeStep >= 4 && (
                    <motion.div
                      initial={{ opacity: 0, scale: 0.9 }}
                      animate={{ opacity: 1, scale: 1 }}
                      transition={{ delay: 0.2, type: "spring" }}
                      className="p-4 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md max-w-xs mx-auto"
                    >
                      <p className="text-xl font-display italic text-transparent bg-clip-text bg-gradient-to-r from-pink-400 to-purple-300 font-semibold">
                        "Mere dil ki baat hai ❤️"
                      </p>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>

              {/* Action Button */}
              <div className="mb-6 flex flex-col items-center">
                <button
                  id="welcome-next-btn"
                  onClick={handleNextWelcome}
                  className="px-8 py-3.5 rounded-full bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-600 hover:to-purple-700 text-white font-medium text-sm tracking-wide shadow-lg shadow-pink-500/20 active:scale-95 transition-all duration-300 flex items-center gap-2 border border-pink-400/20"
                >
                  {welcomeStep < 4 ? "Aage Dekho" : "Dil Se Suno ❤️"}
                  <ChevronRight className="w-4 h-4" />
                </button>
                <div className="flex gap-1.5 mt-4">
                  {Array.from({ length: 5 }).map((_, i) => (
                    <div 
                      key={i} 
                      className={`h-1.5 rounded-full transition-all duration-300 ${i === welcomeStep ? 'w-4 bg-pink-500' : 'w-1.5 bg-slate-700'}`} 
                    />
                  ))}
                </div>
              </div>
            </motion.div>
          ) : (
            
            /* --- SCREEN 2: MAIN APP --- */
            <motion.div 
              key="main-content"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.6 }}
              className="flex-1 flex flex-col justify-between relative z-10"
            >
              {/* COMPLEMENTARY TOP STATUS BAR */}
              <header className="p-4 border-b border-pink-500/10 flex items-center justify-between bg-slate-900/40 sticky top-0 backdrop-blur-md z-30">
                <div className="flex items-center gap-2">
                  <div className="relative">
                    <Heart className="w-5 h-5 text-pink-500 fill-pink-500 animate-pulse" />
                    <span className="absolute -top-1 -right-1 w-2 h-2 bg-sky-400 rounded-full animate-ping" />
                  </div>
                  <div>
                    <h1 className="text-sm font-semibold font-display tracking-tight text-pink-200">Dear Ruhii</h1>
                    <p className="text-[9px] font-mono text-slate-400 uppercase tracking-widest">Only For You</p>
                  </div>
                </div>

                {/* MUSIC CONTROL UNIT */}
                <div className="flex items-center gap-3 bg-white/5 border border-white/10 rounded-full px-3 py-1">
                  {/* Select box for track */}
                  <select 
                    value={trackIndex}
                    onChange={(e) => handleTrackChange(Number(e.target.value))}
                    className="bg-transparent border-none text-[10px] text-pink-200 font-sans outline-none focus:ring-0 cursor-pointer max-w-[100px]"
                  >
                    {SOUND_TRACKS.map((track, i) => (
                      <option key={i} value={i} className="bg-slate-950 text-slate-200 text-xs">
                        {track.title}
                      </option>
                    ))}
                  </select>

                  {/* Play/Pause Button */}
                  <button 
                    id="play-pause-btn"
                    onClick={togglePlay}
                    className="p-1 rounded-full bg-pink-500/20 text-pink-300 hover:bg-pink-500/30 transition-all active:scale-90"
                    title={isPlaying ? "Pause Music" : "Play Music"}
                  >
                    {isPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
                  </button>

                  {/* Volume Slider Icon */}
                  <div className="flex items-center gap-1 group relative">
                    <button 
                      id="volume-toggle"
                      onClick={() => setVolume(v => v === 0 ? 0.4 : 0)}
                      className="text-slate-400 hover:text-slate-200"
                    >
                      {volume === 0 ? <VolumeX className="w-3.5 h-3.5 text-rose-400" /> : <Volume2 className="w-3.5 h-3.5 text-pink-400" />}
                    </button>
                    <input 
                      type="range"
                      min="0"
                      max="1"
                      step="0.05"
                      value={volume}
                      onChange={(e) => setVolume(Number(e.target.value))}
                      className="w-12 h-1 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-pink-500 outline-none"
                    />
                  </div>
                </div>
              </header>

              {/* MAIN SCROLLABLE CONTENT BODY */}
              <main className="p-4 space-y-10">
                
                {/* 1. APP HERO HEADER */}
                <section className="text-center space-y-2 py-4">
                  <motion.div
                    initial={{ scale: 0.9, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    transition={{ type: "spring", stiffness: 100 }}
                  >
                    <span className="inline-block px-3 py-1 rounded-full text-[10px] font-mono tracking-widest text-pink-300 bg-pink-500/10 border border-pink-500/20 mb-2">
                      HUMARI DOSTI ❤️
                    </span>
                    <h2 className="text-3xl font-bold font-display text-transparent bg-clip-text bg-gradient-to-r from-pink-300 via-purple-300 to-sky-200">
                      💖 Dear Ruhii
                    </h2>
                    <p className="text-sm font-light text-slate-400 max-w-xs mx-auto italic">
                      "Ek choti si website... Sirf tumhare liye ❤️"
                    </p>
                  </motion.div>
                </section>

                {/* 2. SECTION: TUM MERE LIYE BOHAT IMPORTANT HO */}
                <section id="important-section" className="space-y-4">
                  <div className="flex items-center gap-2 mb-2">
                    <div className="h-px bg-pink-500/20 flex-1" />
                    <span className="text-xs font-mono uppercase tracking-widest text-pink-400 flex items-center gap-1">
                      <Heart className="w-3 h-3 text-pink-500 fill-pink-500" /> True Feelings
                    </span>
                    <div className="h-px bg-pink-500/20 flex-1" />
                  </div>
                  
                  <h3 className="text-lg font-semibold font-display text-center text-pink-100">
                    Tum Mere Liye Bohat Important Ho ❤️
                  </h3>

                  {/* Grid of beautifully designed visual cards */}
                  <div className="grid grid-cols-1 gap-3">
                    {[
                      {
                        icon: "❤️",
                        title: "Tum meri best friend ho",
                        text: "Har ek baat share karna, bematlab hasna, tumse zyada comfortable aur trustworthy friend meri life mein koi nahi hai."
                      },
                      {
                        icon: "😊",
                        title: "Tumhari smile bohat achi lagti hai",
                        text: "Jab tum khush hoti ho, to mujhe lagta hai sab sahi hai. Tumhari smile meri sabse favorite khushi hai."
                      },
                      {
                        icon: "🌸",
                        title: "Tumhare bina sab adhura lagta hai",
                        text: "Din chahe kitna bhi busy ho, tumhare sath bina baat kiye poora din khali khali sa beetta hai."
                      },
                      {
                        icon: "💖",
                        title: "Mujhe hamari friendship pyari hai",
                        text: "Main is dosti ko hamesha dil se laga kar rakhunga. Is rishte ka meri life mein koi badal nahi hai."
                      }
                    ].map((card, idx) => (
                      <motion.div
                        key={idx}
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true, margin: "-50px" }}
                        transition={{ delay: idx * 0.1, duration: 0.5 }}
                        className="p-4 rounded-2xl bg-white/[0.03] hover:bg-white/[0.05] border border-white/5 hover:border-pink-500/20 backdrop-blur-md flex gap-4 items-start transition-all"
                      >
                        <div className="w-12 h-12 rounded-xl bg-pink-500/10 border border-pink-500/20 flex items-center justify-center text-2xl shrink-0">
                          {card.icon}
                        </div>
                        <div className="space-y-1">
                          <h4 className="text-sm font-semibold text-pink-200">{card.title}</h4>
                          <p className="text-xs text-slate-400 leading-relaxed">{card.text}</p>
                        </div>
                      </motion.div>
                    ))}
                  </div>
                </section>

                {/* 3. SECTION: MEMORY CAROUSEL */}
                <section id="memory-section" className="space-y-4">
                  <div className="flex items-center gap-2 mb-2">
                    <div className="h-px bg-pink-500/20 flex-1" />
                    <span className="text-xs font-mono uppercase tracking-widest text-purple-400 flex items-center gap-1">
                      <Sparkles className="w-3 h-3 text-purple-400" /> Hamari Yaadein
                    </span>
                    <div className="h-px bg-pink-500/20 flex-1" />
                  </div>

                  {/* Swipeable Carousel Container */}
                  <div className="relative h-[280px] flex items-center justify-center">
                    <AnimatePresence mode="wait">
                      <motion.div
                        key={memoryIndex}
                        initial={{ opacity: 0, scale: 0.95, x: 50 }}
                        animate={{ opacity: 1, scale: 1, x: 0 }}
                        exit={{ opacity: 0, scale: 0.95, x: -50 }}
                        transition={{ type: "spring", stiffness: 200, damping: 20 }}
                        className={`absolute w-full h-full rounded-2xl p-6 border bg-gradient-to-br ${MEMORIES[memoryIndex].gradient} backdrop-blur-md flex flex-col justify-between shadow-lg`}
                      >
                        <div className="space-y-4">
                          <div className="flex justify-between items-center">
                            <span className="text-4xl">{MEMORIES[memoryIndex].icon}</span>
                            <span className="text-[10px] font-mono uppercase tracking-widest text-slate-400 px-2 py-0.5 rounded-full bg-white/5 border border-white/10">
                              {MEMORIES[memoryIndex].tag}
                            </span>
                          </div>
                          <div className="space-y-2">
                            <h4 className="text-lg font-bold font-display text-pink-200">
                              {MEMORIES[memoryIndex].title}
                            </h4>
                            <p className="text-xs text-slate-300 leading-relaxed">
                              {MEMORIES[memoryIndex].desc}
                            </p>
                          </div>
                        </div>
                        
                        <div className="text-[10px] font-mono text-slate-500 text-right">
                          Memory {memoryIndex + 1} of {MEMORIES.length}
                        </div>
                      </motion.div>
                    </AnimatePresence>
                  </div>

                  {/* Carousel Controls */}
                  <div className="flex justify-between items-center gap-4">
                    <button
                      id="prev-mem-btn"
                      onClick={() => setMemoryIndex(prev => (prev - 1 + MEMORIES.length) % MEMORIES.length)}
                      className="px-4 py-2 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-slate-300 hover:text-slate-100 transition-all active:scale-95 text-xs flex items-center gap-1"
                    >
                      <ChevronLeft className="w-4 h-4" /> Prev
                    </button>
                    <div className="flex gap-1">
                      {MEMORIES.map((_, i) => (
                        <div 
                          key={i} 
                          onClick={() => setMemoryIndex(i)}
                          className={`h-1.5 rounded-full transition-all duration-300 cursor-pointer ${i === memoryIndex ? 'w-4 bg-purple-400' : 'w-1.5 bg-slate-700 hover:bg-slate-600'}`} 
                        />
                      ))}
                    </div>
                    <button
                      id="next-mem-btn"
                      onClick={() => setMemoryIndex(prev => (prev + 1) % MEMORIES.length)}
                      className="px-4 py-2 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-slate-300 hover:text-slate-100 transition-all active:scale-95 text-xs flex items-center gap-1"
                    >
                      Next <ChevronRight className="w-4 h-4" />
                    </button>
                  </div>
                </section>

                {/* 4. HEARTBEAT PLAYGROUND & APOLOGY MESSAGES */}
                <section id="heart-playground" className="space-y-6 bg-pink-500/5 border border-pink-500/10 rounded-3xl p-6 text-center relative overflow-hidden backdrop-blur-md">
                  <div className="absolute top-2 right-2 flex items-center gap-1 text-[10px] font-mono text-pink-400">
                    <RefreshCw className="w-3 h-3 animate-spin" style={{ animationDuration: '4s' }} /> Click to Beat
                  </div>
                  
                  <h3 className="text-md font-semibold font-display text-pink-200">
                    Glow Heart Apology 💖
                  </h3>
                  <p className="text-xs text-slate-400 max-w-xs mx-auto">
                    Aapki narazgi door karne ke liye har tap par ek emotional aur sincere message...
                  </p>

                  {/* GIANT HEART WITH HEARTBEAT PULSE */}
                  <div className="flex flex-col items-center justify-center py-6 relative">
                    <motion.button
                      id="heartbeat-action-btn"
                      onClick={handleHeartClick}
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.9 }}
                      className="relative z-10 w-28 h-28 flex items-center justify-center outline-none select-none"
                    >
                      {/* Pulse Background Effects */}
                      <div className="absolute inset-0 bg-rose-500/20 rounded-full filter blur-xl animate-pulse" />
                      <div className="absolute w-20 h-20 bg-rose-600/30 rounded-full animate-ping" />
                      
                      <Heart 
                        className={`w-20 h-20 text-rose-500 fill-rose-500 drop-shadow-[0_0_20px_rgba(244,63,94,0.7)] cursor-pointer select-none ${
                          heartClicks > 0 ? 'animate-heartbeat' : 'animate-pulse'
                        }`} 
                      />
                    </motion.button>

                    <div className="mt-4 flex items-center gap-2">
                      <span className="px-3 py-1 rounded-full text-[10px] font-mono bg-white/5 text-pink-300 border border-pink-500/20">
                        Total Maafi Clicks: <span className="font-bold text-pink-400">{heartClicks}</span>
                      </span>
                    </div>
                  </div>

                  {/* CURRENT REVEALED MESSAGE CONTAINER */}
                  <AnimatePresence mode="wait">
                    <motion.div
                      key={currentMessage}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -10 }}
                      className="p-4 rounded-xl bg-slate-950/40 border border-white/5 text-center"
                    >
                      <p className="text-sm font-medium italic text-slate-200 leading-relaxed">
                        "{currentMessage}"
                      </p>
                    </motion.div>
                  </AnimatePresence>
                </section>

                {/* 5. APOLOGY LETTER (Typewriter progresive release) */}
                <section id="apology-letter" className="space-y-4">
                  <div className="flex items-center gap-2 mb-2">
                    <div className="h-px bg-pink-500/20 flex-1" />
                    <span className="text-xs font-mono uppercase tracking-widest text-pink-400 flex items-center gap-1">
                      <Info className="w-3 h-3 text-pink-500" /> Sincere Letter
                    </span>
                    <div className="h-px bg-pink-500/20 flex-1" />
                  </div>

                  {!isLetterOpen ? (
                    <div className="text-center py-4">
                      <button
                        id="open-letter-btn"
                        onClick={() => setIsLetterOpen(true)}
                        className="px-6 py-2.5 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-pink-300 hover:text-pink-200 font-medium text-xs tracking-wider transition-all active:scale-95"
                      >
                        📖 Read Apology Letter
                      </button>
                    </div>
                  ) : (
                    <motion.div
                      initial={{ opacity: 0, y: 15 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="p-6 rounded-2xl bg-gradient-to-b from-pink-500/5 to-purple-500/5 border border-pink-500/20 shadow-inner relative"
                    >
                      {/* Close button */}
                      <button
                        id="close-letter-btn"
                        onClick={() => setIsLetterOpen(false)}
                        className="absolute top-3 right-3 text-slate-500 hover:text-slate-300 text-xs font-mono"
                      >
                        [Close]
                      </button>

                      {/* Letter Head */}
                      <div className="border-b border-pink-500/10 pb-3 mb-4 text-center">
                        <span className="font-display italic text-pink-300 font-semibold text-lg">Dil Se, Sirf Tumhare Liye</span>
                      </div>

                      {/* Progressive Lines display */}
                      <div className="space-y-3.5">
                        {revealedLetterLines.map((line, idx) => {
                          const isSpecial = line.startsWith("Dear Ruhii") || line.startsWith("— Hassan") || line === "❤️";
                          return (
                            <motion.p
                              key={idx}
                              initial={{ opacity: 0, x: -10 }}
                              animate={{ opacity: 1, x: 0 }}
                              transition={{ duration: 0.5 }}
                              className={`text-sm leading-relaxed ${
                                isSpecial 
                                  ? 'font-semibold text-pink-300 font-display text-center my-2' 
                                  : 'text-slate-300'
                              }`}
                            >
                              {line}
                            </motion.p>
                          );
                        })}
                      </div>

                      {/* Complete indicator */}
                      {revealedLetterLines.length === LETTER_LINES.length && (
                        <motion.div 
                          initial={{ opacity: 0 }}
                          animate={{ opacity: 1 }}
                          className="mt-6 pt-3 border-t border-pink-500/10 flex justify-center"
                        >
                          <span className="text-[10px] font-mono text-slate-500 flex items-center gap-1">
                            <CheckCircle className="w-3.5 h-3.5 text-pink-500" /> Maafi Nama Completed
                          </span>
                        </motion.div>
                      )}
                    </motion.div>
                  )}
                </section>

                {/* 6. PROMISE SECTION */}
                <section id="promise-section" className="space-y-4">
                  <div className="flex items-center gap-2 mb-2">
                    <div className="h-px bg-pink-500/20 flex-1" />
                    <span className="text-xs font-mono uppercase tracking-widest text-purple-400 flex items-center gap-1">
                      <HelpCircle className="w-3 h-3 text-purple-400" /> Promises
                    </span>
                    <div className="h-px bg-pink-500/20 flex-1" />
                  </div>

                  <h3 className="text-lg font-semibold font-display text-center text-pink-100">
                    Sincere Promises To My Best Friend 🤝
                  </h3>

                  <div className="space-y-3">
                    {[
                      {
                        icon: "🌸",
                        title: "Main hamesha respect karunga",
                        desc: "Tumhari har baat, feelings aur limits mere liye sabse upar hain, unhe hamesha samman dunga."
                      },
                      {
                        icon: "🤍",
                        title: "Main pehle se better friend banunga",
                        desc: "Apni ghaltiyo par kaam karunga taaki tumhari life mein positive energy laa saku."
                      },
                      {
                        icon: "😊",
                        title: "Main tumhari baat hamesha sununga",
                        desc: "Kisi bhi baat par gussa karne se pehle tumhari baat ko dhyan se aur bina judge kiye sununga."
                      },
                      {
                        icon: "❤️",
                        title: "Kabhi jaan bujh kar hurt nahi karunga",
                        desc: "Tumhara dil dukhana mera kabhi maqsad nahi tha, aur aage bhi kabhi nahi hoga."
                      },
                      {
                        icon: "🌹",
                        title: "Friendship hamesha important rahegi",
                        desc: "Humari dosti mere liye sabse pehle hai aur hamesha bachi rahegi."
                      }
                    ].map((promise, index) => (
                      <motion.div
                        key={index}
                        initial={{ opacity: 0, x: -15 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true, margin: "-50px" }}
                        transition={{ delay: index * 0.1 }}
                        className="p-4 rounded-xl bg-white/[0.02] border border-white/5 hover:border-purple-500/10 flex gap-3.5 items-start"
                      >
                        <span className="text-2xl shrink-0">{promise.icon}</span>
                        <div className="space-y-0.5">
                          <h4 className="text-xs font-semibold text-purple-300">{promise.title}</h4>
                          <p className="text-[11px] text-slate-400 leading-relaxed">{promise.desc}</p>
                        </div>
                      </motion.div>
                    ))}
                  </div>
                </section>

                {/* 7. SURPRISE SECTION: CAN YOU FORGIVE ME */}
                <section id="surprise-section" className="space-y-6 pt-4">
                  <div className="flex items-center gap-2 mb-2">
                    <div className="h-px bg-pink-500/20 flex-1" />
                    <span className="text-xs font-mono uppercase tracking-widest text-pink-400 flex items-center gap-1">
                      <Gift className="w-3 h-3 text-pink-400" /> Surprise Box
                    </span>
                    <div className="h-px bg-pink-500/20 flex-1" />
                  </div>

                  {!surpriseOpened ? (
                    <div className="flex justify-center py-2">
                      <motion.button
                        id="open-heart-gift-btn"
                        onClick={() => {
                          setSurpriseOpened(true);
                          // Increase ambient music volume
                          setVolume(0.75);
                        }}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        className="px-8 py-4 rounded-full bg-gradient-to-r from-pink-500 via-rose-500 to-purple-600 text-white font-semibold text-sm tracking-widest uppercase shadow-[0_0_30px_rgba(244,63,94,0.3)] hover:shadow-[0_0_40px_rgba(244,63,94,0.5)] border border-pink-300/20 transition-all flex items-center gap-2.5 active:scale-95 cursor-pointer"
                      >
                        <Gift className="w-4 h-4 animate-bounce" /> Open My Heart ❤️
                      </motion.button>
                    </div>
                  ) : (
                    <motion.div
                      initial={{ opacity: 0, scale: 0.95 }}
                      animate={{ opacity: 1, scale: 1 }}
                      className="p-6 rounded-3xl bg-slate-900/80 border-2 border-pink-500/30 text-center space-y-6 shadow-2xl relative overflow-hidden"
                    >
                      <div className="absolute top-0 inset-x-0 h-1.5 bg-gradient-to-r from-pink-500 via-rose-500 to-purple-600" />
                      
                      <div className="space-y-2">
                        <span className="text-5xl inline-block animate-bounce">💖</span>
                        <h4 className="text-xl font-bold font-display text-transparent bg-clip-text bg-gradient-to-r from-pink-300 to-purple-200">
                          Will You Forgive Me, Ruhii?
                        </h4>
                        <p className="text-xs text-slate-400">
                          Aapki dosti mere liye bohot keemti hai. Kya aap mujhe maaf karenge?
                        </p>
                      </div>

                      {/* Options Buttons */}
                      <div className="grid grid-cols-2 gap-3 max-w-xs mx-auto">
                        <button
                          id="forgive-yes-btn"
                          onClick={() => {
                            setForgiveStatus("yes");
                            saveFeedback({ status: "yes" });
                          }}
                          className={`py-3 rounded-full font-semibold text-xs tracking-wider transition-all duration-300 active:scale-95 flex items-center justify-center gap-1 border ${
                            forgiveStatus === "yes"
                              ? "bg-emerald-500 hover:bg-emerald-600 text-white border-emerald-400/20 shadow-lg shadow-emerald-500/20"
                              : "bg-pink-500 hover:bg-pink-600 text-white border-pink-400/20 shadow-md"
                          }`}
                        >
                          ❤️ Yes, Forgiven
                        </button>
                        
                        <button
                          id="forgive-think-btn"
                          onClick={() => {
                            setForgiveStatus("think");
                            saveFeedback({ status: "think" });
                          }}
                          className={`py-3 rounded-full font-semibold text-xs tracking-wider transition-all duration-300 active:scale-95 flex items-center justify-center gap-1 border ${
                            forgiveStatus === "think"
                              ? "bg-amber-500 hover:bg-amber-600 text-white border-amber-400/20 shadow-lg"
                              : "bg-slate-800 hover:bg-slate-700 text-slate-300 border-white/5"
                          }`}
                        >
                          🥺 Let Me Think
                        </button>
                      </div>

                      {/* Decision Result Feedbacks */}
                      <AnimatePresence mode="wait">
                        {forgiveStatus === "yes" && (
                          <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20 space-y-2"
                          >
                            <span className="text-4xl block">🥹</span>
                            <h5 className="text-sm font-semibold text-emerald-300">Thank You Ruhii ❤️</h5>
                            <p className="text-[11px] text-slate-300 leading-relaxed">
                              Tumne meri duniya phir se sabse beautiful aur khushnuma bana di hai! Main hamesha hamari friendship ki dil se respect karunga.
                            </p>
                          </motion.div>
                        )}

                        {forgiveStatus === "think" && (
                          <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            className="p-4 rounded-xl bg-amber-500/10 border border-amber-500/20 space-y-2"
                          >
                            <span className="text-4xl block">🙏</span>
                            <h5 className="text-sm font-semibold text-amber-300">Main hamesha wait karunga...</h5>
                            <p className="text-[11px] text-slate-300 leading-relaxed">
                              Jitna bhi waqt lage, main yahin hoon. Kyun ke kuch friendships aur rishte life mein itne special hote hain ki unhe kabhi khona nahi chahiye. ❤️
                            </p>
                          </motion.div>
                        )}
                      </AnimatePresence>

                      {/* Private Message Board */}
                      <div className="pt-4 border-t border-pink-500/10 space-y-3">
                        <div className="flex items-center justify-center gap-1.5 text-xs text-pink-300 font-medium">
                          <MessageCircle className="w-4 h-4" />
                          <span>Hassan Ke Liye Koi Message? 📬</span>
                        </div>
                        
                        {!messageSent ? (
                          <div className="space-y-3">
                            <textarea
                              value={messageText}
                              onChange={(e) => setMessageText(e.target.value)}
                              placeholder="Apne dil ki baat likho yahan..."
                              className="w-full h-24 p-3 rounded-xl bg-slate-950/60 border border-pink-500/20 text-slate-200 placeholder-slate-500 text-xs focus:outline-none focus:ring-1 focus:ring-pink-500/50 resize-none"
                              maxLength={500}
                              disabled={isSendingMessage}
                            />
                            <div className="flex justify-between items-center text-[10px] text-slate-500">
                              <span>{messageText.length}/500 chars</span>
                              <button
                                id="send-ruhii-msg-btn"
                                onClick={async () => {
                                  if (!messageText.trim()) return;
                                  setIsSendingMessage(true);
                                  await saveFeedback({ message: messageText });
                                  setIsSendingMessage(false);
                                  setMessageSent(true);
                                }}
                                disabled={isSendingMessage || !messageText.trim()}
                                className="px-4 py-1.5 rounded-full bg-pink-500/20 hover:bg-pink-500/30 text-pink-300 hover:text-pink-200 border border-pink-500/30 text-[11px] font-medium transition-all active:scale-95 disabled:opacity-50 disabled:pointer-events-none"
                              >
                                {isSendingMessage ? "Bhej rahe hain..." : "Bhej Do ❤️"}
                              </button>
                            </div>
                          </div>
                        ) : (
                          <motion.div
                            initial={{ opacity: 0, scale: 0.95 }}
                            animate={{ opacity: 1, scale: 1 }}
                            className="p-3 rounded-xl bg-pink-500/10 border border-pink-500/20 text-center space-y-1.5"
                          >
                            <p className="text-xs text-pink-200 font-medium">
                              Message Bhej Diya! 🌸
                            </p>
                            <p className="text-[10px] text-slate-400">
                              Hassan tak aapka message safely pahunch gaya hai. ❤️
                            </p>
                            <button
                              id="edit-ruhii-msg-btn"
                              onClick={() => setMessageSent(false)}
                              className="text-[9px] text-pink-400 hover:underline mt-1 font-mono"
                            >
                              [Edit Message]
                            </button>
                          </motion.div>
                        )}
                      </div>
                    </motion.div>
                  )}
                </section>

                {/* 8. ENDING QUOTE */}
                <section className="text-center py-6">
                  <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    className="p-6 rounded-3xl bg-gradient-to-r from-pink-500/5 to-purple-500/5 border border-white/5 space-y-2 relative"
                  >
                    <Star className="absolute top-3 left-3 w-4 h-4 text-pink-400 animate-spin" style={{ animationDuration: '6s' }} />
                    <Star className="absolute bottom-3 right-3 w-4 h-4 text-purple-400 animate-spin" style={{ animationDuration: '8s' }} />
                    
                    <p className="font-display italic text-lg text-pink-200 leading-relaxed">
                      "Kuch log life mein bohot special hote hain... Aur tum un mein se ek ho."
                    </p>
                    <span className="block text-rose-500 text-xl">❤️</span>
                  </motion.div>
                </section>

              </main>

              {/* STICKY FOOTER ELEMENT */}
              <footer className="p-6 border-t border-pink-500/10 bg-slate-950/80 text-center space-y-1 relative z-20">
                <p className="text-[10px] font-mono tracking-widest uppercase text-slate-500">
                  Made with Love, Respect & Hope.
                </p>
                <p className="text-xs text-slate-400 font-sans">
                  Forever Your Best Friend,
                </p>
                <h4 className="text-md font-display font-bold text-transparent bg-clip-text bg-gradient-to-r from-pink-400 to-purple-300 mt-1">
                  Hassan ❤️
                </h4>
              </footer>

            </motion.div>
          )}
        </AnimatePresence>

      </div>

    </div>
  );
}
