import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="🏏 IPL Auction H2H League",
    page_icon="🏏",
    layout="wide",
)

schedule = {
    "Week 1": {
        "dates": "Mar 28 - Apr 1",
        "matches": [
            ("Dx", "CR7"),
            ("SBKR", "ICONIC"),
            ("Joker's", "AE_XXX"),
            ("IPL Leo", "Bangaluru"),
            ("Devdutt", "XI Wizards"),
            ("HURRICANES", "Ghop Ghop")
        ]
    },
    "Week 2": {
        "dates": "Apr 2 - Apr 5",
        "matches": [
            ("Dx", "ICONIC"),
            ("CR7", "AE_XXX"),
            ("SBKR", "Bangaluru"),
            ("Joker's", "XI Wizards"),
            ("IPL Leo", "Ghop Ghop"),
            ("Devdutt", "HURRICANES")
        ]
    },
    "Week 3": {
        "dates": "Apr 5 - Apr 9",
        "matches": [
            ("Dx", "AE_XXX"),
            ("ICONIC", "Bangaluru"),
            ("CR7", "XI Wizards"),
            ("SBKR", "Ghop Ghop"),
            ("Joker's", "HURRICANES"),
            ("IPL Leo", "Devdutt")
        ]
    },
    "Week 4": {
        "dates": "Apr 10 - Apr 12",
        "matches": [
            ("Dx", "Bangaluru"),
            ("AE_XXX", "XI Wizards"),
            ("ICONIC", "Ghop Ghop"),
            ("CR7", "HURRICANES"),
            ("SBKR", "Devdutt"),
            ("Joker's", "IPL Leo")
        ]
    },
    "Week 7": {
        "dates": "Apr 21 - Apr 25",
        "matches": [
            ("Dx", "XI Wizards"),
            ("Bangaluru", "Ghop Ghop"),
            ("AE_XXX", "HURRICANES"),
            ("ICONIC", "Devdutt"),
            ("CR7", "IPL Leo"),
            ("SBKR", "Joker's")
        ]
    },
    "Week 8": {
        "dates": "Apr 25 - Apr 28",
        "matches": [
            ("Dx", "Ghop Ghop"),
            ("XI Wizards", "HURRICANES"),
            ("Bangaluru", "Devdutt"),
            ("AE_XXX", "IPL Leo"),
            ("ICONIC", "Joker's"),
            ("CR7", "SBKR")
        ]
    },
    "Week 9": {
        "dates": "Apr 29 - May 3",
        "matches": [
            ("Dx", "HURRICANES"),
            ("Ghop Ghop", "Devdutt"),
            ("XI Wizards", "IPL Leo"),
            ("Bangaluru", "Joker's"),
            ("AE_XXX", "SBKR"),
            ("ICONIC", "CR7")
        ]
    },
    "Week 10": {
        "dates": "May 3 - May 7",
        "matches": [
            ("Dx", "Devdutt"),
            ("HURRICANES", "IPL Leo"),
            ("Ghop Ghop", "Joker's"),
            ("XI Wizards", "SBKR"),
            ("Bangaluru", "CR7"),
            ("AE_XXX", "ICONIC")
        ]
    },
    "Week 12": {
        "dates": "May 12 - May 16",
        "matches": [
            ("Dx", "IPL Leo"),
            ("Devdutt", "Joker's"),
            ("HURRICANES", "SBKR"),
            ("Ghop Ghop", "CR7"),
            ("XI Wizards", "ICONIC"),
            ("Bangaluru", "AE_XXX")
        ]
    },
    "Week 13": {
        "dates": "May 17 - May 20",
        "matches": [
            ("Dx", "Joker's"),
            ("IPL Leo", "SBKR"),
            ("Devdutt", "CR7"),
            ("HURRICANES", "ICONIC"),
            ("Ghop Ghop", "AE_XXX"),
            ("XI Wizards", "Bangaluru")
        ]
    },
    "Week 14": {
        "dates": "May 21 - May 24",
        "matches": [
            ("Dx", "SBKR"),
            ("Joker's", "CR7"),
            ("IPL Leo", "ICONIC"),
            ("Devdutt", "AE_XXX"),
            ("HURRICANES", "Bangaluru"),
            ("Ghop Ghop", "XI Wizards")
        ]
    }
}


week_fixtures = {
    "Week 1": [
        "RCB vs SRH",
        "MI vs KKR",
        "RR vs CSK",
        "PBKS vs GT",
        "LSG vs DC",
    ],
    "Week 2": [
        "KKR vs SRH",
        "CSK vs PBKS",
        "DC vs MI",
        "GT vs RR",
        "SRH vs LSG",
    ],
    "Week 3": [
        "RCB vs CSK",
        "KKR vs PBKS",
        "RR vs MI",
        "DC vs GT",
        "KKR vs LSG",
    ],
    "Week 4": [
        "RR vs RCB",
        "PBKS vs SRH",
        "CSK vs DC",
        "LSG vs GT",
        "MI vs RCB",
    ],
    "Week 7": [
        "SRH vs DC",
        "LSG vs RR",
        "MI vs CSK",
        "RCB vs GT",
        "DC vs PBKS",
    ],
    "Week 8": [
        "RR vs SRH",
        "GT vs CSK",
        "LSG vs KKR",
        "DC vs RCB",
        "PBKS vs RR",
    ],
    "Week 9": [
        "MI vs SRH",
        "GT vs RCB",
        "RR vs DC",
        "CSK vs MI",
        "SRH vs KKR",
    ],
    "Week 10": [
        "GT vs PBKS",
        "MI vs LSG",
        "DC vs CSK",
        "SRH vs PBKS",
        "LSG vs RCB",
    ],
    "Week 12": [
        "GT vs SRH",
        "RCB vs KKR",
        "PBKS vs MI",
        "LSG vs CSK",
        "KKR vs GT",
    ],
    "Week 13": [
        "PBKS vs RCB",
        "DC vs RR",
        "CSK vs SRH",
        "RR vs LSG",
        "KKR vs MI",
    ],
    "Week 14": [
        "CSK vs GT",
        "SRH vs RCB",
        "LSG vs PBKS",
        "MI vs RR",
        "KKR vs DC",
    ],
}

BREAK_WEEKS = ["GW5", "GW6", "GW11"]

# ---------------- HELPERS ----------------
def get_all_teams(schedule_dict):
    teams = set()
    for gw in schedule_dict.values():
        for a, b in gw["matches"]:
            teams.add(a)
            teams.add(b)
    return sorted(teams)


def get_team_schedule(team_name):
    rows = []
    for gw, details in schedule.items():
        found = False
        for team1, team2 in details["matches"]:
            if team_name == team1:
                rows.append([gw, details["dates"], team2])
                found = True
            elif team_name == team2:
                rows.append([gw, details["dates"], team1])
                found = True
        if not found and gw in BREAK_WEEKS:
            rows.append([gw, details["dates"], "Rest Week 😴"])

    return pd.DataFrame(rows, columns=["Matchweek", "Dates", "Opponent"])

teams = get_all_teams(schedule)

# ---------------- STYLING ----------------
st.markdown(
    """
    <style>
    html, body, [class*="css"], [data-testid="stAppViewContainer"] {
        color: white !important;
    }

    .main {
        background: linear-gradient(135deg, #0f172a, #1e293b);
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        color: black;
        text-align: center;
        padding-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #e2e8f0;
        text-align: center;
        margin-bottom: 30px;
    }

    .stSelectbox label,
    .stMarkdown,
    .stCaption,
    .stMetric,
    .stText,
    p, h1, h2, h3, h4, h5, h6,
    label {
        color: black !important;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }

    div[data-testid="stDataFrame"] table {
        color: black !important;
    }

    div[data-testid="stDataFrame"] th {
        background-color: #1e293b !important;
        color: #facc15 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🏏 IPL Auction Head-to-Head League</div>', unsafe_allow_html=True)

# ---------------- UI LAYOUT ----------------
left, right = st.columns([1, 2])

with left:
    st.markdown("### 🎯 Select Team")
    selected_team = st.selectbox("Choose your team", teams)

    st.info(
        "📌 Includes all active matchweeks. Break match weeks - 5,6 and 11"
    )
    st.info(
        "🏆 At the enf of 70 matches, top 4 in the H2H table will qualify for playoffs. Playoffs rounds will be similar to actual playoffs. Qualifier 1 - 1st vs 2nd. Eliminator - 3rd vs 4th. Qualifier 2 - Eliminator winner vs Qualifier 1 loser. Final - Qualifier 1 winner vs Qualifier 2 winner."
    )

with right:
    if selected_team:
        df = get_team_schedule(selected_team)

        st.markdown(f"### 📅 {selected_team} Schedule")
        st.dataframe(df, use_container_width=True, hide_index=True)



st.divider()

team_logos = {
    "RCB": "logos/RCB.png",
    "SRH": "logos/SRH.png",
    "MI": "logos/MI.png",
    "KKR": "logos/KKR.png",
    "RR": "logos/RR.png",
    "CSK": "logos/CSK.png",
    "PBKS": "logos/PBKS.png",
    "GT": "logos/GT.png",
    "LSG": "logos/LSG.png",
    "DC": "logos/DC.png",
}

# ---------------- WEEK FIXTURES VIEW ----------------
st.markdown("### 🏟️ IPL Fixtures for Selected Matchweek")
selected_gw = st.selectbox("Select Matchweek", list(week_fixtures.keys()), key="fixture_gw")

for fixture in week_fixtures[selected_gw]:
    team1, team2 = fixture.split(" vs ")

    with st.container():
        c1, c2, c3 = st.columns([1.2, 0.4, 1.2])
        
        with c1:
            st.image(team_logos.get(team1, "logos/default.png"), width=70)
            st.markdown(f"### {team1}")

        with c2:
            st.markdown("<div style='text-align:center; font-size:36px; padding-top:20px;'>🆚</div>", unsafe_allow_html=True)

        with c3:
            st.image(team_logos.get(team2, "logos/default.png"), width=70)
            st.markdown(f"### {team2}")

        st.markdown("---")
        
st.caption("Made by IPL Leo")