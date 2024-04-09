import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def main():
    st.title("VA Butterfly Tracker 🦋")

    df = pd.DataFrame(
            [
                {"Count": "", "Species": "Monarch", "Comments": ""},
                {"Count": "", "Species": "Tiger Swallowtail", "Comments": ""},
                {"Count": "", "Species": "Black Swallowtail", "Comments": ""},
            ]
        )

    edited_df = st.data_editor(
        df,
        num_rows="fixed",

        column_config={
            "Count": st.column_config.NumberColumn(
                min_value=0,
                step=1,
                width="small",
                format="%d",
            ),
            "Species": st.column_config.TextColumn(
                width="medium",
                disabled=True
            ),
            "Comments": st.column_config.TextColumn(
                width="large",
                max_chars=100
            )
        },
        hide_index=True,
        use_container_width=True,
    )

    # if st.button("Export PDF"):
    #     fig, ax = plt.subplots(figsize=(8.5, 11))
    #     ax.axis('tight')
    #     ax.axis('off')
    #     the_table = ax.table(cellText=edited_df.values, colLabels=edited_df.columns, cellLoc='center',
    #                          loc='top', colWidths=[0.05, 0.2, 0.5])
    #
    #     pp = PdfPages("foo.pdf")
    #     pp.savefig(fig, bbox_inches='tight')
    #     pp.close()


    fig, ax = plt.subplots(figsize=(8.5, 11))
    fig.suptitle('Virginia Butterfly Tracker')
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=edited_df.values, colLabels=edited_df.columns, cellLoc='center',
                         loc='top', colWidths=[0.05, 0.2, 0.5])

    pp = PdfPages("foo.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

    with open("foo.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button("Export PDF", data=PDFbyte,
                       file_name="test.pdf", mime='application/octet-stream')


# col1.number_input("Count", value=None, step=1, label_visibility="collapsed")
# col2.write("Monarch")
if __name__ == '__main__':
    st.set_page_config(page_icon='🦋', layout="wide")
    st.markdown("""<style>
                body {text-align: center}
                p {text-align: center} 
                button {float: center}                 
                </style>""", unsafe_allow_html=True)
    hide_streamlit_style = """ <style>
              [data-testid="stData_Editor"] {border: 0px}
              MainMenu {visibility: hidden;}
              header {visibility: hidden;}
              footer {visibility: hidden;}
              </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main()
