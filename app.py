import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="🏏 IPL Auction H2H League",
    page_icon="🏏",
    layout="wide",
)

schedule = {
    "Week 2": {
        "dates": "Apr 2 - Apr 5",
        "matches": [
            ("IPL Leo", "Cr7"),
            ("100 Pipers", "Delhi Daredevils"),
            ("Dc", "Targaryens"),
            ("RCB", "Reaper XX"),
            ("GHOP GHOP", "Asish DX"),
            ("HORNCHURCH", "XI Habibi's"),
            ("Sourav Knights", "WICK XI")
        ]
    },
    "Week 3": {
        "dates": "Apr 5 - Apr 9",
        "matches": [
            ("IPL Leo", "Delhi Daredevils"),
            ("Cr7", "Targaryens"),
            ("100 Pipers", "Reaper XX"),
            ("Dc", "Asish DX"),
            ("RCB", "XI Habibi's"),
            ("GHOP GHOP", "WICK XI"),
            ("HORNCHURCH", "Sourav Knights")
        ]
    },
    "Week 4": {
        "dates": "Apr 10 - Apr 12",
        "matches": [
            ("IPL Leo", "Targaryens"),
            ("Delhi Daredevils", "Reaper XX"),
            ("Cr7", "Asish DX"),
            ("100 Pipers", "XI Habibi's"),
            ("Dc", "WICK XI"),
            ("RCB", "Sourav Knights"),
            ("GHOP GHOP", "HORNCHURCH")
        ]
    },
    "Week 5": {
        "dates": "Apr 13 - Apr 17",
        "matches": [
            ("IPL Leo", "Reaper XX"),
            ("Targaryens", "Asish DX"),
            ("Delhi Daredevils", "XI Habibi's"),
            ("Cr7", "WICK XI"),
            ("100 Pipers", "Sourav Knights"),
            ("Dc", "HORNCHURCH"),
            ("RCB", "GHOP GHOP")
        ]
    },
    "Week 6": {
        "dates": "Apr 18 - Apr 20",
        "matches": [
            ("IPL Leo", "Asish DX"),
            ("Reaper XX", "XI Habibi's"),
            ("Targaryens", "WICK XI"),
            ("Delhi Daredevils", "Sourav Knights"),
            ("Cr7", "HORNCHURCH"),
            ("100 Pipers", "GHOP GHOP"),
            ("Dc", "RCB")
        ]
    },
    "Week 7": {
        "dates": "Apr 21 - Apr 25",
        "matches": [
            ("IPL Leo", "XI Habibi's"),
            ("Asish DX", "WICK XI"),
            ("Reaper XX", "Sourav Knights"),
            ("Targaryens", "HORNCHURCH"),
            ("Delhi Daredevils", "GHOP GHOP"),
            ("Cr7", "RCB"),
            ("100 Pipers", "Dc")
        ]
    },
    "Week 8": {
        "dates": "Apr 25 - Apr 28",
        "matches": [
            ("IPL Leo", "WICK XI"),
            ("XI Habibi's", "Sourav Knights"),
            ("Asish DX", "HORNCHURCH"),
            ("Reaper XX", "GHOP GHOP"),
            ("Targaryens", "RCB"),
            ("Delhi Daredevils", "Dc"),
            ("Cr7", "100 Pipers")
        ]
    },
    "Week 9": {
        "dates": "Apr 29 - May 3",
        "matches": [
            ("IPL Leo", "Sourav Knights"),
            ("WICK XI", "HORNCHURCH"),
            ("XI Habibi's", "GHOP GHOP"),
            ("Asish DX", "RCB"),
            ("Reaper XX", "Dc"),
            ("Targaryens", "100 Pipers"),
            ("Delhi Daredevils", "Cr7")
        ]
    },
    "Week 10": {
        "dates": "May 3 - May 7",
        "matches": [
            ("IPL Leo", "HORNCHURCH"),
            ("Sourav Knights", "GHOP GHOP"),
            ("WICK XI", "RCB"),
            ("XI Habibi's", "Dc"),
            ("Asish DX", "100 Pipers"),
            ("Reaper XX", "Cr7"),
            ("Targaryens", "Delhi Daredevils")
        ]
    },
    "Week 11": {
        "dates": "May 8 - May 11",
        "matches": [
            ("IPL Leo", "GHOP GHOP"),
            ("HORNCHURCH", "RCB"),
            ("Sourav Knights", "Dc"),
            ("WICK XI", "100 Pipers"),
            ("XI Habibi's", "Cr7"),
            ("Asish DX", "Delhi Daredevils"),
            ("Reaper XX", "Targaryens")
        ]
    },
    "Week 12": {
        "dates": "May 12 - May 16",
        "matches": [
            ("IPL Leo", "RCB"),
            ("GHOP GHOP", "Dc"),
            ("HORNCHURCH", "100 Pipers"),
            ("Sourav Knights", "Cr7"),
            ("WICK XI", "Delhi Daredevils"),
            ("XI Habibi's", "Targaryens"),
            ("Asish DX", "Reaper XX")
        ]
    },
    "Week 13": {
        "dates": "May 17 - May 20",
        "matches": [
            ("IPL Leo", "Dc"),
            ("RCB", "100 Pipers"),
            ("GHOP GHOP", "Cr7"),
            ("HORNCHURCH", "Delhi Daredevils"),
            ("Sourav Knights", "Targaryens"),
            ("WICK XI", "Reaper XX"),
            ("XI Habibi's", "Asish DX")
        ]
    },
    "Week 14": {
        "dates": "May 21 - May 24",
        "matches": [
            ("IPL Leo", "100 Pipers"),
            ("Dc", "Cr7"),
            ("RCB", "Delhi Daredevils"),
            ("GHOP GHOP", "Targaryens"),
            ("HORNCHURCH", "Reaper XX"),
            ("Sourav Knights", "Asish DX"),
            ("WICK XI", "XI Habibi's")
        ]
    }
}


week_fixtures = {
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
    "Week 5": [
        "SRH vs RR",
        "CSK vs KKR",
        "RCB vs LSG",
        "MI vs PBKS",
        "GT vs KKR",
    ],
    "Week 6": [
        "RCB vs DC",
        "SRH vs CSK",
        "KKR vs RR",
        "PBKS vs LSG",
        "GT vs MI",
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
    "Week 11": [
        "DC vs KKR",
        "RR vs GT",
        "CSK vs LSG",
        "RCB vs MI",
        "PBKS vs DC",
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
        color: white;
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
        color: white !important;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }

    div[data-testid="stDataFrame"] table {
        color: white !important;
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

st.markdown("### 🏟️ IPL Fixtures for Selected Matchweek") 

selected_gw = st.selectbox(
    "Select Matchweek", 
    list(week_fixtures.keys()), 
    key="fixture_gw"
)
for fixture in week_fixtures[selected_gw]:
    team1, team2 = fixture.split(" vs ")

    with st.container():
        c1, c2, c3 = st.columns([1, 0.5, 1])  # tighter

        with c1:
            st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
            st.image(team_logos.get(team1, "logos/default.png"), width=100)
            st.markdown(f"<p style='margin:0; font-size:14px;'>{team1}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown(
                "<div style='text-align:center; font-size:18px; margin-top:20px;'>VS</div>",
                unsafe_allow_html=True
            )

        with c3:
            st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
            st.image(team_logos.get(team2, "logos/default.png"), width=100)
            st.markdown(f"<p style='margin:0; font-size:14px;'>{team2}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<hr style='margin:8px 0;'>", unsafe_allow_html=True)
        
st.caption("Made by IPL Leo")