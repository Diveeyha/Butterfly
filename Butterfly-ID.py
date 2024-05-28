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
        return f'<p style="color:Gray; font-size: 0.75em;">{image_link + fig_caption}</p>'
    except Exception as e:
        # st.error(f"Error fetching image from URL: {e}")
        return None


# @st.cache_data
def convert_df(input_df):
    return input_df.to_html(escape=False, formatters=dict(Inner=image_formatter, Outer=image_formatter),
                            index=False, header=False)


def main():
    st.title("Butterflies of")
    st.subheader("Coastal Virginia 🦋")
    st.divider()

    # Todo put expander in first column with species explanation, side-by-side comparison?
    # Todo change font size of species? Make photos have zoom
    df2 = pd.DataFrame(
        {
            'Species': ["Black Swallowtail", "Eastern Tiger Swallowtail (Female)",
                        "Eastern Black Tiger Swallowtail (Female)", "Giant Swallowtail*", "Palamedes Swallowtail",
                        "Pipevine Swallowtail*", "Spicebush Swallowtail", "Zebra Swallowtail"],  # 7
            'Outer': ["",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Black_Tiger_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zebra_Swallowtail_Outer-Michelle_Gianvecchio.jpg",
                      ],
            'Inner': ["",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Tiger_Swallowtail_Inner_Female-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Black_Tiger_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Palamedes_Swallowtail_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Pipevine_Swallowtail_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Spicebush_Swallowtail_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zebra_Swallowtail_Inner-Michelle_Gianvecchio.jpg"
                      ],

        }
    )
    st.subheader("Swallowtails (Papilionidae)")
    html_view2 = convert_df(df2)
    st.markdown(html_view2, unsafe_allow_html=True)
    st.divider()


    df3 = pd.DataFrame(
        {
            'Species': ["Cabbage White", "Checkered White*", "Clouded Sulfur", "Cloudless Sulfur", "Falcate Orangetip",
                        "Little Yellow*", "Orange Sulfur", "Sleepy orange"],  # 8
            'Outer': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Cabbage_White_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Cloudless_Sulfur_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Sleepy_orange_Outer-Michelle_Gianvecchio.jpg"
                      ],
            'Inner': ["",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      ""
                      ],
        }
    )

    st.subheader("Whites and Sulfurs (Pieridae)")
    html_view3 = convert_df(df3)
    st.markdown(html_view3, unsafe_allow_html=True)
    st.divider()


    df4 = pd.DataFrame(
        {
            'Species': ["Summer Azure", "Eastern-tailed Blue", "American Copper*", "Bronze Copper*", "Brown Elfin*",
                        "Henry’s Elfin", "Eastern Pine Elfin*", "Banded Hairstreak*", "Coral Hairstreak*",
                        "Gray Hairstreak", "Great Purple Hairstreak*", "Juniper Hairstreak*", "King's Hairstreak*",
                        "Oak Hairstreak*", "Red-banded Hairstreak", "Striped Hairstreak*", "White M Hairstreak*",
                        "Harvester*"],  # 18
            'Outer': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Summer_Azure_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Eastern_tailed_Blue_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Gray_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Red_banded_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      ""
                      ],
            'Inner': ["",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      ""
                      ],
        }
    )

    st.subheader("Gossamer wings (Lycaenidae)")
    html_view4 = convert_df(df4)
    st.markdown(html_view4, unsafe_allow_html=True)
    st.divider()


    df5 = pd.DataFrame(
        {
            'Species': ["Red Admiral", "Red-spotted Purple", "Monarch", "Viceroy", "Common Buckeye",
                        "Silvery Checkerspot*", "Pearl Crescent", "Phaon Crescent*", "Mourning Cloak",
                        "Eastern Comma*", "Question Mark", "Hackberry Emperor", "Tawny Emperor",
                        "Great Spangled Fritillary*", "Gulf Fritillary*", "Variegated Fritillary",
                        "American Lady", "Painted lady",
                        "Northern Pearly-eye*", "Southern Pearly-eye*", "Creole Pearly-eye*",
                        "Appalachian Brown", "Carolina Satyr", "Gemmed Satyr", "Little Wood Satyr",
                        "Common Wood-Nymph", "American Snout"
                        ],  # 27

            'Outer': ["",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Monarch_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Common_Buckeye_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Pearl_Crescent_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Question_Mark_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/American_Lady_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Painted_Lady_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Gemmed_Satyr_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Little_Wood_Satyr_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/American_snout_Outer-Michelle_Gianvecchio.jpg"
                      ],
            'Inner': ["",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Monarch_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Common_Buckeye_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Pearl_Crescent_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Question_Mark_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Variegated_Fritillary_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Painted_Lady_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      ""
                      ],
        }
    )

    st.subheader("Brushfoots (Nymphalidae)")
    html_view5 = convert_df(df5)
    st.markdown(html_view5, unsafe_allow_html=True)
    st.divider()


    df6 = pd.DataFrame(
        {
            'Species': ["Northern Broken-Dash", "Southern Broken-Dash", "Common Checkered-Skipper",
                        "Confused Cloudywing*", "Northern Cloudywing*", "Southern Cloudywing*",
                        "Horace’s Duskywing", "Juvenal’s Duskywing", "Wild Indigo Duskywing", "Zarucco Duskywing*",
                        "Hoary Edge*", "Little Glassywing",
                        "Common Roadside-Skipper*", " Lace-winged Roadside-Skipper*", "Reversed Roadside-Skipper*",
                        "Sachem", "Hayhurst’s Scallopwing*",
                        "Aaron's Skipper", "Brazilian Skipper*", "Broad-winged Skipper",
                        "Clouded Skipper", "Crossline Skipper", "Delaware Skipper*",
                        "Dion Skipper*", "Dukes’ Skipper*", "Dun Skipper", "Dusted Skipper*", "Fiery Skipper",
                        "Least Skipper", "Long-tailed Skipper*", "Ocola Skipper",
                        "Peck’s Skipper*", "Pepper and Salt Skipper*", "Rare Skipper*",
                        "Salt Marsh Skipper", "Silver-spotted Skipper", "Swarthy Skipper", "Tawny-edged Skipper*",
                        "Yehl Skipper*", "Zabulon Skipper", "Common Sootywing"
                        ],  # 41
            'Outer': ["",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Little_Glassywing_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Broad_winged_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Fiery_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Ocola_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Salt_Marsh_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Silver_spotted_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zabulon_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      ""
                      ],
            'Inner': ["",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Horaces_Duskywing_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Little_Glassywing_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Aarons_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Broad_winged_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Clouded_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Dun_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Long_tailed_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Silver_spotted_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zabulon_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      ""
                      ],
        }
    )
    st.subheader("Skippers (Hesperiidae)")
    html_view6 = convert_df(df6)
    st.markdown(html_view6, unsafe_allow_html=True)
    st.divider()



    # df = pd.DataFrame(
    #     {
    #         'Species': [
    #             "American Lady", "American Snout", "Cabbage White", "Carolina Satyr", "Clouded Sulfur",
    #             "Cloudless Sulfur", "Common Buckeye", "Eastern Comma", "Gemmed Satyr", "Great Southern White",
    #             "Little Wood Satyr", "Monarch", "Painted lady", "Pearl Crescent", "Question Mark", "Red Admiral",
    #             "Red-spotted Purple", "Sleepy orange", "Spring/Summer Azure", "Variegated Fritillary"
    #             "Eastern-tailed Blue", "Gray Hairstreak", "Red-banded Hairstreak"
    #             "Aaron's Skipper", "Broad-winged Skipper", "Clouded Skipper", "Dun Skipper", "Fiery Skipper",
    #             "Horace's Duskywing", "Little Glassywing", "Long-tailed Skipper", "Ocola Skipper",
    #             "Salt Marsh Skipper", "Silver-spotted Skipper", "Zabulon Skipper"
    #             "Black Swallowtail", "Eastern Tiger Swallowtail (Female)", "Eastern Black Tiger Swallowtail (Female)",
    #             "Palamedes Swallowtail",
    #             "Pipevine Swallowtail", "Spicebush Swallowtail", "Zebra Swallowtail"],

            # 'Species': ["Aaron's Skipper", "American Lady", "American Snout", "Black Swallowtail",
            #             "Broad-winged Skipper", "Cabbage White", "Carolina Satyr", "Clouded Skipper",
            #             "Clouded Sulfur", "Cloudless Sulfur", "Common Buckeye", "Dun Skipper", "Eastern Comma",
            #             "Eastern Tiger Swallowtail (Female)", "Eastern Black Tiger Swallowtail (Female)",
            #             "Eastern-tailed Blue", "Fiery Skipper", "Gemmed Satyr", "Gray Hairstreak",
            #             "Great Southern White", "Horace's Duskywing", "Little Glassywing", "Little Wood Satyr",
            #             "Long-tailed Skipper", "Monarch", "Ocola Skipper", "Painted lady", "Palamedes Swallowtail",
            #             "Pearl Crescent", "Pipevine Swallowtail", "Question Mark", "Red Admiral",
            #             "Red-banded Hairstreak", "Red-spotted Purple", "Salt Marsh Skipper", "Sleepy orange",
            #             "Silver-spotted Skipper", "Spicebush Swallowtail", "Spring/Summer Azure",
            #             "Variegated Fritillary", "Zabulon Skipper", "Zebra Swallowtail"],
    #         'Outer': ["",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Black_Tiger_Outer-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zebra_Swallowtail_Outer-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Banded_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Red_banded_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/American_snout_Outer-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Painted_lady_Outer-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Sleepy_orange_Outer-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Salt_Marsh_Skipper_Outer-Michelle_Gianvecchio.jpg",
    #                   ""],
    #         'Inner': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Tiger_Swallowtail_Inner_Female-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Black_Tiger_Inner-Michelle_Gianvecchio.jpg",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zebra_Swallowtail_Inner-Michelle_Gianvecchio.jpg",
    #                   "",
    #                   "",
    #                   "",
    #                   "",
    #                   "",
    #                   "",
    #                   "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Long_tailed_Skipper_Inner-Michelle_Gianvecchio.jpg"],
    #
    #     }
    # )
    #
    # html_view = convert_df(df)
    # st.download_button(
    #      label="Download data as HTML",
    #      data=html_view,
    #      file_name='output.html',
    #      mime='text/html',
    #  )


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










# for i in range(1, 3): # number of rows in your table! = 2
#     col1, col2 = st.columns(2) # number of columns in each row! = 2
#     # first column of the ith row
#     with col1:
#         st.image('image_%i_col_1.jpg' %i, use_column_width=True)
#         expander = st.expander("See explanation")
#         expander.write('''
#             The chart above shows some numbers I picked for you.
#             I rolled actual dice for these, so they're *guaranteed* to
#             be random.
#         ''')
#     with col2:
#         st.image('image_%i_col_2.jpg' %i, use_column_width=True)
#
#         expander = st.expander("See explanation")
#         expander.write('''
#                     The chart above shows some numbers I picked for you.
#                     I rolled actual dice for these, so they're *guaranteed* to
#                     be random.
#                 ''')


    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     expander1 = st.expander("Zebra_Swallowtail")
    #     expander1.write('''
    #         The chart above shows some numbers I picked for you.
    #         I rolled actual dice for these, so they're *guaranteed* to
    #         be random.
    #     ''')
    #     expander2 = st.expander("'Black' Eastern Tiger Swallowtail ♀️")
    #     expander2.write('''
    #         The chart above shows some numbers I picked for you.
    #         I rolled actual dice for these, so they're *guaranteed* to
    #         be random.
    #     ''')
    # col1.write("Zebra_Swallowtail")
    # col1.write("'Black' Eastern Tiger Swallowtail ♀️")
    # image1 = "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Black_Tiger_Inner.jpg"
    # col2.image(image1)
    # image2 = "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zebra_Swallowtail_Inner.jpg"
    # col2.image(image2)
    # image3 = "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Black_Tiger_Outer.jpg"
    # col3.image(image3)
    # image4 = "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zebra_Swallowtail_Outer.jpg"
    # col3.image(image4)


# st.dataframe(
#     df,
#     column_config={
#         "Inner": st.column_config.ImageColumn(
#         ),
#         "Outer": st.column_config.ImageColumn(
#         )
#     },
#     hide_index=True,
# )


# st.data_editor(
#     data_df,
#     column_config={
#         "apps": st.column_config.ImageColumn(
#             "Preview Image", help="Streamlit app preview screenshots"
#         )
#     },
#     hide_index=True,
# )






# import numpy as np
# import glob
#
# import os
#
# projectDir = os.getcwd()


# def get_image_from_url(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         img = Image.open(BytesIO(response.content))
#         return img
#     except Exception as e:
#         st.error(f"Error fetching image from URL: {e}")
#         return None
#
#
# def get_thumbnail(url):
#     img = get_image_from_url(url)
#     if img:
#     # img = Image.open(url)
#         img.thumbnail(500, 800)
#     return img
#
#
# def image_to_base64(img):
#     if img:
#         with BytesIO() as buffer:
#             img.save(buffer, 'jpeg')  # or 'jpeg'
#             return base64.b64encode(buffer.getvalue()).decode()
#
#
# def image_formatter(url):
#     img = get_thumbnail(url)
#     if img:
#         return f'<img src="data:image/jpeg;base64,{image_to_base64(img)}">'
# ratio = image.width / image.height
# size = int(min(e.width, e.height * ratio)), int(min(e.height, e.width / ratio))
