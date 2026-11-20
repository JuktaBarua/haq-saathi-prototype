"""Haq Saathi clickable prototype, hosted as a Streamlit app.

Two ways to explore the same 12 screens:
  1. Tap the phone: the full clickable prototype, embedded as-is.
  2. Guided walkthrough: one screen at a time, with the user's story and the design reasoning.
"""
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent
HOTS = json.loads((HERE / "hotspots.json").read_text())

st.set_page_config(page_title="Haq Saathi prototype", page_icon="🩺", layout="wide")

NAMES = {1: "Welcome", 2: "Home", 3: "Choose treatment", 4: "What they're asking for", 5: "Your answer",
         6: "Haq Slip", 7: "Help call", 8: "Add receipt", 9: "Receipt Locker", 10: "Review claim",
         11: "Claim status", 12: "Hospital reports"}
TARGET = {"Continue": 2, "I'm being asked to pay": 3, "Planning treatment": 12, "I've already paid": 9, "Heart stent": 4,
          "Check this charge": 5, "Show the Haq Slip": 6, "Get help on a call": 7, "Pay now, claim later": 8,
          "Back to my options": 5, "I paid anyway: keep proof": 8, "Save receipt": 9, "Add another receipt": 8,
          "File my claim": 10, "Go to CGRMS with my details": 11, "See hospital reports": 12, "Back to home": 2,
          "Home": 2, "Hospitals": 12, "Proof": 9, "Help": 7}
PARENT = {3: 2, 4: 3, 5: 4, 6: 5, 7: 5, 8: 5, 9: 2, 10: 9, 11: 10, 12: 2}
NAV = {"Home", "Hospitals", "Proof", "Help"}

STORY = {
    1: ("Ravi's father needs a heart stent. He opens Haq Saathi for the first time.",
        "Language first, then one promise and one button.",
        "Jakob's Law: it starts like apps he already uses. One clear action keeps the first step easy."),
    2: ("The billing desk has asked him for a deposit. He is anxious and short of time.",
        "Three big choices that match where he is: being asked to pay, planning, or already paid.",
        "Hick's Law: few, plain choices. The urgent one is largest and comes first (Fitts's Law)."),
    3: ("He picks the treatment his father is getting.",
        "Common treatments are listed in everyday words, not package codes.",
        "Recognition over recall: he taps what he sees instead of typing a medical term."),
    4: ("He says what the hospital is asking for: a deposit.",
        "The app asks only what it needs to judge the charge.",
        "Miller's Law: one question per screen, so nothing has to be held in memory."),
    5: ("He gets an answer: usually covered, with a clear note that this is guidance, not a ruling.",
        "Three safe next steps, from least to most confrontation.",
        "Peak-End Rule: the stressful moment ends with a clear verdict and a way forward."),
    6: ("He shows the Haq Slip to the billing desk.",
        "A calm, official-looking summary of what the scheme covers, which he can hand over.",
        "Aesthetic-Usability Effect: a clean, formal slip is taken more seriously at the counter."),
    7: ("The desk still insists. He calls the 14555 helpline from inside the app.",
        "Someone else explains to the hospital, so he does not have to argue alone.",
        "Goal-Gradient Effect: help is one tap away when he is closest to giving up."),
    8: ("He had to pay anyway, so he photographs the receipt.",
        "Proof is kept straight away, while he still has the paper.",
        "Zeigarnik Effect: a saved receipt is an unfinished task the app later reminds him to complete."),
    9: ("Back home, his receipts are all in one place.",
        "The Receipt Locker shows what he paid and what can be claimed.",
        "Law of Common Region: each receipt is a card with its amount and status together."),
    10: ("He reviews the claim the app has prepared from his receipts.",
         "Details are filled in for the official CGRMS grievance portal.",
         "Tesler's Law: the app takes on the paperwork so he does not have to."),
    11: ("He tracks the claim until it is settled.",
         "Status in plain words, with the expected next step.",
         "Doherty Threshold: clear progress feedback stops him wondering if anything is happening."),
    12: ("For next time, he checks how hospitals near him treat card holders.",
         "Reports from other families show which hospitals ask for money.",
         "Social proof: other families' experience helps him choose before he arrives."),
}

st.markdown("""
<style>
h1, h2, h3 { color:#0E6B5C; }
div[data-testid="stButton"] button { border-radius:12px; border:1.5px solid #0E6B5C; }
div[data-testid="stButton"] button[kind="primary"] { background:#0E6B5C; border-color:#0E6B5C; }
.note { background:#FBEFD9; border-left:4px solid #E59A2F; padding:10px 14px; border-radius:8px; margin:6px 0 14px; }
.story { font-size:1.08rem; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Haq Saathi")
    st.write("A helper for families who are asked to pay at a hospital even though they hold an Ayushman (PM-JAY) card.")
    st.markdown("**Who it's for:** the family member who handles the hospital: the *family case-manager*.")
    st.markdown("**Main flow to try:** Welcome → Home → *I'm being asked to pay* → Heart stent → "
                "Check this charge → Your answer → Haq Slip, Help call, or Pay now, claim later.")
    st.caption("Student concept for Digital Innovation and Product Leadership, IIM Ranchi. Prototype only: nothing is "
               "saved or sent, and amounts, hospitals and report counts are sample data. Not a government service.")

st.title("Haq Saathi: clickable prototype")
tab_phone, tab_guided = st.tabs(["📱 Tap the phone", "🧭 Guided walkthrough"])

with tab_phone:
    st.markdown("Tap the buttons on the phone screen, as you would in an app. The list beside the phone jumps to any screen.")
    components.html((HERE / "prototype.html").read_text(), height=960, scrolling=True)

with tab_guided:
    if "screen" not in st.session_state:
        st.session_state.screen = 1
        st.session_state.path = [1]

    def go(n):
        st.session_state.screen = n
        st.session_state.path.append(n)

    n = st.session_state.screen
    key = f"{n:02d}"
    left, right = st.columns([5, 6], gap="large")
    with left:
        st.image(str(HERE / "screens" / f"{key}.png"), width=360)
    with right:
        st.progress(n / 12, text=f"Screen {n} of 12: {NAMES[n]}")
        story, what, law = STORY[n]
        st.markdown(f'<p class="story">{story}</p>', unsafe_allow_html=True)
        st.markdown(f"**What the screen does:** {what}")
        st.markdown(f'<div class="note"><b>Design reasoning:</b> {law}</div>', unsafe_allow_html=True)

        actions = [lab for lab, *_ in HOTS[key] if lab not in NAV and lab != "Back" and TARGET[lab] != n]
        st.markdown("**Tap to continue**")
        for i, lab in enumerate(actions):
            st.button(f"{lab}  →  {NAMES[TARGET[lab]]}", key=f"a{n}{i}", on_click=go, args=(TARGET[lab],),
                      type="primary" if i == 0 else "secondary", use_container_width=True)

        nav = [lab for lab, *_ in HOTS[key] if lab in NAV and TARGET[lab] != n]
        if nav:
            st.markdown("**Bottom tabs**")
            cols = st.columns(len(nav))
            for c, lab in zip(cols, nav):
                c.button(lab, key=f"n{n}{lab}", on_click=go, args=(TARGET[lab],), use_container_width=True)

        st.divider()
        b1, b2 = st.columns(2)
        if n in PARENT:
            b1.button(f"← Back to {NAMES[PARENT[n]]}", on_click=go, args=(PARENT[n],), use_container_width=True)
        b2.button("↺ Start again", on_click=lambda: st.session_state.update(screen=1, path=[1]), use_container_width=True)
        st.caption("Your path so far: " + " → ".join(NAMES[p] for p in st.session_state.path[-8:]))
