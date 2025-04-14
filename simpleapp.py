import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")

st.markdown("""
    <style>
    .screen {
        font-size: 32px;
        padding: 15px;
        background-color: #f0f2f6;
        border-radius: 10px;
        text-align: right;
        margin-bottom: 20px;
        border: 1px solid #ccc;
    }
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 10px;
    }
    h2 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2>📱 Simple Calculator</h2>", unsafe_allow_html=True)

if "expression" not in st.session_state:
    st.session_state.expression = ""
if "display" not in st.session_state:
    st.session_state.display = ""

st.markdown(f"<div class='screen'>{st.session_state.display}</div>", unsafe_allow_html=True)

buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

symbol_map = {
    "÷": "/",
    "×": "*",
    "+": "+",
    "-": "-"
}

def press(btn):
    if btn == "C":
        st.session_state.expression = ""
        st.session_state.display = ""
    elif btn == "=":
        try:
            expr = st.session_state.expression
            result = eval(expr)
            st.session_state.expression = str(round(result, 2))
            st.session_state.display = st.session_state.expression
        except:
            st.session_state.expression = ""
            st.session_state.display = "Error"
    else:
        val = symbol_map.get(btn, btn)
        st.session_state.expression += val
        st.session_state.display += btn

for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        with cols[i]:
            if st.button(f"**{btn}**"):
                press(btn)
