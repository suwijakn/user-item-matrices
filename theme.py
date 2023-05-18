import streamlit as st

customized_button = st.markdown("""
    <style >
    .stDownloadButton, div.stButton {text-align:center}
    .stDownloadButton button, div.stButton > button:first-child {
        font-weight: bold;
        background-color: #e1ecf4;
        border-radius: 3px;
        border: 1px solid #7aa7c7;
        box-shadow: rgba(255, 255, 255, .7) 0 1px 0 0 inset;
        box-sizing: border-box;
        color: #39739d !important;
        cursor: pointer;
        display: inline-block;
        line-height: 1.15385;
        margin: 0;
        outline: none;
        padding: 8px .8em;
        position: relative;
        text-align: center;
        text-decoration: none !important;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        vertical-align: baseline;
        white-space: nowrap;
    }
}

.stDownloadButton:focus {
  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);
} 0 4px rgba(0, 149, 255, .15);
}
        }
    </style>""", unsafe_allow_html=True)

button_style = '''
<style>
    .button-8 {
        font-weight: bold;
        background-color: #e1ecf4;
        border-radius: 3px;
        border: 1px solid #7aa7c7;
        box-shadow: rgba(255, 255, 255, .7) 0 1px 0 0 inset;
        box-sizing: border-box;
        color: #39739d !important;
        cursor: pointer;
        display: inline-block;
        line-height: 1.15385;
        margin: 0;
        outline: none;
        padding: 8px .8em;
        position: relative;
        text-align: center;
        text-decoration: none !important;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
        vertical-align: baseline;
        white-space: nowrap;
}

.button-8:hover,
.button-8:focus {
  background-color: #b3d3ea;
  color: #2c5777;
}

.button-8:focus {
  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);
}

.button-8:active {
  background-color: #a0c7e4;
  box-shadow: none;
  color: #2c5777;
}
</style>

'''