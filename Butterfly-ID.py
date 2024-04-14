import streamlit as st
import pandas as pd
import numpy as np
import glob
import base64
from PIL import Image
from io import BytesIO
import os

projectDir = os.getcwd()


def get_thumbnail(path: str) -> Image:
    img = Image.open(path)
    img.thumbnail((200, 200))
    return img


def image_to_base64(img_path: str) -> str:
    img = get_thumbnail(img_path)
    with BytesIO() as buffer:
        img.save(buffer, 'png')  # or 'jpeg'
        return base64.b64encode(buffer.getvalue()).decode()


def image_formatter(img_path: str) -> str:
    return f'<img src="data:image/png;base64,{image_to_base64(img_path)}">'


@st.cache_data
def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(Inner=image_formatter, Outer=image_formatter),
                             index=False, header=False)


def main():
    st.title("VA Butterfly ID 🦋")

    # col1, col2, col3 = st.columns(3)
    # col1.write("Zebra_Swallowtail")
    # col1.write("'Black' Eastern Tiger Swallowtail ♀️")
    # image1 = (projectDir + '\Butterfly_Photos\Zebra_Swallowtail_Inner.jpg')
    # col2.image(image1)
    # image2 = Image.open(projectDir + '\Butterfly_Photos\Black_Tiger_Inner.jpg')
    # col2.image(image2)
    # image3 = Image.open(projectDir + '\Butterfly_Photos\Zebra_Swallowtail_Outer.jpg')
    # col3.image(image3)
    # image4 = Image.open(projectDir + '\Butterfly_Photos\Black_Tiger_Outer.jpg')
    # col3.image(image4)
    st.write(projectDir)
    inner = glob.glob(f'{projectDir}\Butterfly_Photos\Inner/*.jpg')
    outer = glob.glob(f'{projectDir}\Butterfly_Photos\Outer/*.jpg')
    df = pd.DataFrame(
            {
                'Species': ["Black Tiger Swallowtail", "Zebra Swallowtail"],
                'Inner': inner,
                'Outer': outer
            }
        )

    html = convert_df(df)

    st.markdown(
        html,
        unsafe_allow_html=True
    )

    st.download_button(
         label="Download data as HTML",
         data=html,
         file_name='output.html',
         mime='text/html',
     )

    # st.dataframe(
    #     df,
    #     column_config={
    #         "Outer_image": st.column_config.ImageColumn(
    #             width="small"
    #         )
    #     },
    #     hide_index=True,
    # )
    #

if __name__ == '__main__':
    st.set_page_config(page_icon='🦋', layout="wide")
    st.markdown("""<style>
                body {text-align: center}
                p {text-align: center} 
                button {float: center}   
                table {
                    width: fit-content;
                    margin: auto;
                }       
                </style>""", unsafe_allow_html=True)
    hide_streamlit_style = """ <style>
              [data-testid="stData_Editor"] {border: 0px}
              MainMenu {visibility: hidden;}
              header {visibility: hidden;}
              footer {visibility: hidden;}
              </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    main()
