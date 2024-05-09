import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import base64
import re


def image_to_base64(img):
    if img:
        with BytesIO() as buffer:
            img.save(buffer, 'jpeg')  # 'png' or 'jpeg'
            return base64.b64encode(buffer.getvalue()).decode()


def image_formatter(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        current_image = Image.open(BytesIO(response.content))
        image_link = f'<img src="data:image/jpeg;base64,{image_to_base64(current_image)}" style="width:100%">'
        fig_caption = 'Photo By: '+(re.search(r'.*-([^.]+)', url.removesuffix('jpg'))[1]).replace("_", " ")
        return f'<p style="color:Gray; font-size: 12px;">{image_link + fig_caption}</p>'
    except Exception as e:
        # st.error(f"Error fetching image from URL: {e}")
        return None


# @st.cache_data
def convert_df(input_df):
    return input_df.to_html(escape=False, formatters=dict(Inner=image_formatter, Outer=image_formatter),
                            index=False, header=False)


def main():
    st.title("Coastal Virginia")
    st.subheader("Butterflies 🦋")

    # Todo put expander in first column with species explanation, side-by-side comparison?
    df = pd.DataFrame(
        {
            'Species': ["Eastern Tiger Swallowtail (Female)", "Black Tiger Swallowtail (Female)", "Zebra Swallowtail", "Banded Hairstreak",
                        "Red-banded Hairstreak", "American snout", "Painted lady", "Sleepy orange", "Salt-marsh Skipper", "Long-tailed Skipper"],
            'Outer': ["",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Black_Tiger_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zebra_Swallowtail_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Banded_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Red_banded_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/American_snout_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Painted_lady_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Sleepy_orange_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Salt_Marsh_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      ""],
            'Inner': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Tiger_Swallowtail_Inner_Female-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Black_Tiger_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zebra_Swallowtail_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Long_tailed_Skipper_Inner-Michelle_Gianvecchio.jpg"],

        }
    )

    html_view = convert_df(df)
    st.markdown(html_view, unsafe_allow_html=True)
    st.divider()
    st.download_button(
         label="Download data as HTML",
         data=html_view,
         file_name='output.html',
         mime='text/html',
     )


if __name__ == '__main__':
    st.set_page_config(page_icon='🦋', layout="wide")
    st.markdown("""<style>
                body {text-align: center}
                p {text-align: center}
                button {float: center}
                [data-testid=stVerticalBlock]{
                    gap: 0rem
                }
                [data-testid=stHorizontalBlock]{
                    gap: 0rem
                }
                [data-testid=stForm] [data-testid=stHorizontalBlock] 
                [data-testid=stHorizontalBlock] [data-testid=column]
                {
                    width: calc(25% - 1rem) !important;
                    flex: 1 1 calc(25% - 1rem) !important;
                    min-width: calc(20% - 1rem) !important;
                }
                table {
                    width: fit-content;
                    margin: auto;
                }
                .stDataframe tr {
                    height: 250px; # use this to adjust the height
                }
                [data-testid="stDataFrameResizable"] {
                    height: 250px;
                    max-height: 300px;
                }
                [data-testid="data-grid-canvas"] {
                    height: 250px;
                    max-height: 300px;
                }
                dvn-stack {
                    height: 250px;
                }
                dvn-scroller glideDataEditor {
                    height: 250px;
                }
                .image-cell img {
                    max-width: 200px;
                    max-height: 200px;
                }
                glideDataEditor wzg2m5k {
                    --wzg2m5k-1 250px;
                }
                </style>""", unsafe_allow_html=True)
    hide_streamlit_style = """ <style>
              [data-testid="stData_Editor"] {border: 0px}
              MainMenu {visibility: hidden;}
              header {visibility: hidden;}
              footer {visibility: hidden;}
              </style>"""
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main()
