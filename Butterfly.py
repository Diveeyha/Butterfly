import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def main():
    st.title("Virginia Butterfly Tracker 🦋")

    df = pd.DataFrame(
            [
                {"Count": "", "Species": "Monarch", "Comments": ""},
                {"Count": "", "Species": "Tiger Swallowtail", "Comments": ""},
                {"Count": "", "Species": "Black Swallowtail", "Comments": ""},
            ]
        )

    edited_df = st.data_editor(
        df,
        column_config={"Count": st.column_config.NumberColumn(
            min_value=0,
            step=1,
            width="small",
            format="%d",
        )},
        disabled=["species"],
        hide_index=True
    )

    if st.button("Export PDF"):
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=edited_df.values, colLabels=edited_df.columns, cellLoc='center',
                             loc='top', colWidths=[0.05, 0.2, 0.5])

        pp = PdfPages("foo.pdf")
        pp.savefig(fig, bbox_inches='tight')
        pp.close()


# col1.number_input("Count", value=None, step=1, label_visibility="collapsed")
# col2.write("Monarch")
if __name__ == '__main__':
    st.set_page_config(page_icon='🦋')
    hide_streamlit_style = """ <style>
              [data-testid="stData_Editor"] {border: 0px}
              MainMenu {visibility: hidden;}
              header {visibility: hidden;}
              footer {visibility: hidden;}
              </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main()
