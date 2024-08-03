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
        fig_caption = '© '+(re.search(r'.*-([^.]+)', url.removesuffix('jpg'))[1]).replace("_", " ")
        return f'<p style="color:Gray; font-size: 0.75em;">{image_link + fig_caption}</p>'
    except Exception as e:
        # st.error(f"Error fetching image from URL: {e}")
        return ""

# def sci_name_formatter(txt):
#     return display( HTML( df.to_html().replace("\\n","<br>") ) )

# @st.cache_data
def convert_df(input_df):
    return input_df.to_html(escape=False, formatters=dict(Inner=image_formatter, Outer=image_formatter),
                            index=False, header=False).replace("\\n", "<i><br>")


def main():
    st.title("Butterflies of")
    st.subheader("Coastal Virginia 🦋")
    st.markdown("#")
# f'<p style="color:Gray; font-size: 0.75em;">{image_link + fig_caption}</p>'
    # Todo put expander in first column with species explanation, side-by-side comparison?
    # Todo change font size of species? Make photos have zoom
    df2 = pd.DataFrame(
        {
            'Species': [f"Black Swallowtail\nPapilio polyxenes",
                        "Eastern Tiger Swallowtail\nPapilio glaucus",
                        "Eastern Black Tiger Swallowtail (Female)\nPapilio glaucus",
                        "Giant Swallowtail*\nPapilio cresphontes",
                        "Palamedes Swallowtail\nPapilio palamedes",
                        "Pipevine Swallowtail*\nBattus philenor",
                        "Spicebush Swallowtail\nPapilio troilus",
                        "Zebra Swallowtail\nEurytides marcellus"],  # 7
            'Outer': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Black_Swallowtail_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Eastern_Tiger_Outer-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Black_Tiger_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Giant_Swallowtail_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Palamedes_Swallowtail_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Pipevine_Swallowtail_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Spicebush_Outer-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zebra_Swallowtail_Outer-Michelle_Gianvecchio.jpg",
                      ],
            'Inner': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Black_Swallowtail_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Tiger_Swallowtail_Inner_Female-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Black_Tiger_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Giant_Swallowtail_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Palamedes_Swallowtail_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Pipevine_Swallowtail_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Spicebush_Swallowtail_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zebra_Swallowtail_Inner-Michelle_Gianvecchio.jpg"
                      ],
        }
    )
    st.subheader("Swallowtails (Papilionidae)")
    html_view2 = convert_df(df2)
    st.markdown(html_view2, unsafe_allow_html=True)
    st.markdown("#")


    df3 = pd.DataFrame(
        {
            'Species': ["Cabbage White\nPieris rapae",
                        "Checkered White*\nPontia protodice",
                        "Clouded Sulfur\nColias philodice",
                        "Cloudless Sulfur\nPhoebis sennae",
                        "Falcate Orangetip\nAnthocharis midea",
                        "Little Yellow*\nEurema lisa",
                        "Orange Sulfur\nColias eurytheme",
                        "Sleepy orange\nEurema nicippe"],  # 8
            'Outer': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Cabbage_White_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Checkered_White_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Clouded_Sulfur_Outer-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Cloudless_Sulphur_Outer-Wikipedia.JPG",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Falcate_Orangetip_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Little_Yellow_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Orange_Sulfur_Outer-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Sleepy_Orange_Outer-Michelle_Gianvecchio.jpg",
                      ],
            'Inner': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Cabbage_White_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Checkered_White_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Clouded_Sulfur_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Cloudless_Sulfur_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Falcate_Orangetip_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Little_Yellow_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Orange_Sulfur_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Sleepy_Orange_Inner-Wikipedia.jpg"
                      ],
        }
    )

    st.subheader("Whites and Sulfurs (Pieridae)")
    html_view3 = convert_df(df3)
    st.markdown(html_view3, unsafe_allow_html=True)
    st.markdown("#")


    df4 = pd.DataFrame(
        {
            'Species': ["Summer Azure\nCelastrina neglecta",
                        "Eastern-tailed Blue\nCupido comyntas",
                        "American Copper*\nLycaena phlaeas",
                        "Bronze Copper*\nLycaena hyllus",
                        "Brown Elfin*\nCallophrys augustinus",
                        "Henry’s Elfin\nCallophrys henrici",
                        "Eastern Pine Elfin*\nCallophrys niphon",
                        "Banded Hairstreak*\nSatyrium calanus",
                        "Coral Hairstreak*\nSatyrium titus",
                        "Gray Hairstreak\nStrymon melinus",
                        "Great Purple Hairstreak*\nAtlides halesus",
                        "Juniper Hairstreak*\nCallophrys gryneus",
                        "King's Hairstreak*\nSatyrium kingi",
                        "Oak Hairstreak*\nSatyrium favonius",
                        "Red-banded Hairstreak\nCalycopis cecrops",
                        "Striped Hairstreak*\nSatyrium liparops",
                        "White M Hairstreak*\nParrhasius m-album",
                        "Harvester*\nFeniseca tarquinius"],  # 18
            'Outer': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Summer_Azure_Outer-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Easten-tailed_Blue_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/American_Copper_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Bronze_Copper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Brown_Elfin_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Henry's_Elfin_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Eastern_Pine_Elfin_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Banded_Hairstreak_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Coral_Hairstreak_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Gray_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Great_Purple_Hairstreak_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Juniper_Hairstreak_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/King's_Hairstreak_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Oak_Hairstreak_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Red_banded_Hairstreak_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Striped_Hairstreak_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/White_M_Hairstreak_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Harvester_Outer-Michelle_Gianvecchio.jpg"
                      ],
            'Inner': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Summer_Azure_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Eastern-tailed_Blue_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/American_Copper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Bronze_Copper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Brown_Elfin_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Henry's_Elfin_Inner-IllinoisDNR.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Eastern_Pine_Elfin_Inner-IllinoisDNR.jpg",
                      "",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Gray_Hairstreak_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Great_Purple_Hairstreak_Inner-IllinoisDNR.jpg",
                      "",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/King's_Hairstreak_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Oak_Hairstreak_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Red-banded_Hairstreak_Inner-IllinoisDNR.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Striped_Hairstreak_Inner-IllinoisDNR.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/White_M_Hairstreak_Inner-IllinoisDNR.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Harvester_Inner-iNaturalist.jpg"
                      ],
        }
    )

    st.subheader("Gossamer wings (Lycaenidae)")
    html_view4 = convert_df(df4)
    st.markdown(html_view4, unsafe_allow_html=True)
    st.markdown("#")

    df5 = pd.DataFrame(
        {
            'Species': ["Red Admiral\nVanessa atalanta",
                        "Red-spotted Purple\nLimenitis arthemis",
                        "Monarch\nDanaus plexippus",
                        "Viceroy\nLimenitis archippus",
                        "Common Buckeye\nJunonia coenia",
                        "Silvery Checkerspot*\nChlosyne nycteis",
                        "Pearl Crescent\nPhyciodes tharos",
                        "Phaon Crescent*\nPhyciodes phaon",
                        "Mourning Cloak\nNymphalis antiopa",
                        "Eastern Comma*\nPolygonia comma",
                        "Question Mark\nPolygonia interrogationis",
                        "Hackberry Emperor\nAsterocampa celtis",
                        "Tawny Emperor\nAsterocampa clyton",
                        "Great Spangled Fritillary*\nSpeyeria cybele",
                        "Gulf Fritillary*\nDione vanillae",
                        "Variegated Fritillary\nEuptoieta claudia",
                        "American Lady\nVanessa virginiensis",
                        "Painted lady\nVanessa cardui",
                        "Northern Pearly-eye*\nLethe anthedon",
                        "Southern Pearly-eye*\nEnodia portlandia",
                        "Creole Pearly-eye*\nEnodia creola",
                        "Appalachian Brown\nSatyrodes appalachia",
                        "Carolina Satyr\nHermeuptychia sosybius",
                        "Gemmed Satyr\nCyllopsis gemma",
                        "Little Wood Satyr\nMegisto cymela",
                        "Common Wood-Nymph\nCercyonis pegala",
                        "American Snout\nLibytheana carinenta"
                        ],  # 27

            'Outer': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Red_Admiral_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Red-spotted_Purple_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Monarch_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Viceroy_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Common_Buckeye_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Silvery_Checkerspot_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Pearl_Crescent_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Phaon_Crescent_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Mourning_Cloak_Outer-Wikipedia.JPG",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Eastern_Comma_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Question_Mark_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Hackberry_Emperor_Outer-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Tawny_Emperor_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Great_Spangled_Fritillary_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Gulf_Fritillary_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Variegated_Fritillary_Outer-Wikipedia.JPG",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/American_Lady_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Painted_Lady_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Northern_Pearly-eye_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Southern_Pearly-eye_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Creole_Pearly-eye_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Appalachian_Brown_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Carolina_Satyr_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Gemmed_Satyr_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Little_Wood_Satyr_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Common_Wood-Nymph_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/American_snout_Outer-Michelle_Gianvecchio.jpg"
                      ],
            'Inner': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Red_Admiral_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Red-spotted_Purple_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Monarch_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Viceroy_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Common_Buckeye_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Silvery_Checkerspot_Inner-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Pearl_Crescent_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Phaon_Crescent_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Mourning_Cloak_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Eastern_Comma_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Question_Mark_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Hackberry_Emperor_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Tawny_Emperor_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Great_Spangled_Fritillary_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Gulf_Fritillary_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Variegated_Fritillary_Inner-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/American_Lady_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Painted_Lady_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Northern_Pearly-eye_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Southern_Pearly-eye_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Creole_Pearly-eye_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Appalachian_Brown_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Carolina_Satyr_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Gemmed_Satyr_Inner-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Little_Wood_Satyr_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Common_Wood-Nymph_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/American_Snout_Inner-Wikipedia.jpg"
                      ],
        }
    )

    st.subheader("Brushfoots (Nymphalidae)")
    html_view5 = convert_df(df5)
    st.markdown(html_view5, unsafe_allow_html=True)
    st.markdown("#")


    df6 = pd.DataFrame(
        {
            'Species': ["Northern Broken-Dash\nWallengrenia egeremet",
                        "Southern Broken-Dash\nWallengrenia otho",
                        "Common Checkered-Skipper\nPyrgus communis",
                        "Confused Cloudywing*\nThorybes confusis",
                        "Northern Cloudywing*\nThorybes pylades",
                        "Southern Cloudywing*\nThorybes bathyllus",
                        "Horace’s Duskywing\nErynnis horatius",
                        "Juvenal’s Duskywing\nErynnis juvenalis",
                        "Wild Indigo Duskywing\nErynnis baptisiae",
                        "Zarucco Duskywing*\nErynnis zarucco",
                        "Hoary Edge*\nAchalarus lyciades",
                        "Little Glassywing\nPompeius verna",
                        "Common Roadside-Skipper*\nAmblyscirtes vialis",
                        "Lace-winged Roadside-Skipper*\nAmblyscirtes aesculapius",
                        "Reversed Roadside-Skipper*\nAmblyscirtes reversa",
                        "Sachem\nAtalopedes campestris",
                        "Hayhurst’s Scallopwing*\nStaphylus hayhurstii",
                        "Aaron's Skipper\nPoanes aaroni",
                        "Brazilian Skipper*\nCalpodes ethlius",
                        "Broad-winged Skipper\nPoanes viator",
                        "Clouded Skipper\nLerema accius",
                        "Crossline Skipper\nPolites origenes",
                        "Delaware Skipper*\nAnatrytone logan",
                        "Dion Skipper*\nEuphyes dion",
                        "Dukes’ Skipper*\nEuphyes dukesi",
                        "Dun Skipper\nEuphyes vestris",
                        "Dusted Skipper*\nAtrytonopsis hianna",
                        "Fiery Skipper\nHylephila phyleus",
                        "Least Skipper\nAncyloxypha numitor",
                        "Long-tailed Skipper*\nUrbanus proteus",
                        "Ocola Skipper\nPanoquina ocola",
                        "Peck’s Skipper*\nPolites peckius",
                        "Pepper and Salt Skipper*\nAmblyscirtes hegon",
                        "Rare Skipper*\nProblema bulenta",
                        "Salt Marsh Skipper\nPanoquina panoquin",
                        "Silver-spotted Skipper\nEpargyreus clarus",
                        "Swarthy Skipper\nNastra lherminier",
                        "Tawny-edged Skipper*\nPolites themistocles",
                        "Yehl Skipper*\nPoanes yehl",
                        "Zabulon Skipper\nPoanes zabulon",
                        "Common Sootywing\nPholisora catullus"
                        ],  # 41
            'Outer': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Northern_Broken-Dash_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Southern_Broken-Dash_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Common_Checkered-Skipper_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Common_Roadside-Skipper_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Northern_Cloudywing_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Southern_Cloudywing_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Horace's_Duskywing_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Juvenal's_Duskywing_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Wild_Indigo_Duskywing_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zarucco_Duskywing_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Hoary_Edge_Outer-IllinoisDNR.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Little_Glassywing_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Common_Roadside-Skipper_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Lace-winged_Roadside-Skipper_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Reversed_Roadside-Skipper_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Sachem_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Hayhurst's_Scallopwing_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Aaron's_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Brazilian_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Broad_winged_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Clouded_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Crossline_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Delaware_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Dion_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Dukes'_Skipper_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Dun_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Dusted_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Fiery_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Least_Skipper_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Long-tailed_Skipper_Outer-Wikipedia.JPG",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Ocola_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Peck's_Skipper_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Pepper_and_Salt_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Rare_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Salt_Marsh_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Silver-spotted_Skipper_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Swarthy_Skipper_Outer-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Tawny-edged_Skipper_Outer-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Yehl_Skipper_Outer-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Zabulon_Skipper_Outer-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Outer/Common_Sootywing_Outer-MarylandBiodiversity.jpg",
                      ],
            'Inner': ["https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Northern_Broken-Dash_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Southern_Broken-Dash_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Common_Checkered-Skipper_Inner-Wikipedia.JPG",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Common_Roadside-Skipper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Northern_Cloudywing_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Southern_Cloudywing_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Horace's_Duskywing_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Juvenal's_Duskywing_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Wild_Indigo_Duskywing_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zarucco_Duskywing_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Hoary_Edge_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Little_Glassywing_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Common_Roadside-Skipper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Lace-winged_Roadside-Skipper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Reversed_Roadside-Skipper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Sachem_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Hayhurst's_Scallopwing_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Aarons_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Brazilian_Skipper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Broad-winged_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Clouded_Skipper_Inner-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Crossline_Skipper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Delaware_Skipper_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Dion_Skipper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Dukes'_Skipper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Dun_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Dusted_Skipper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Fiery_Skipper_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Least_Skipper_Inner-eButterfly.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Long_tailed_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Ocola_Skipper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Peck's_Skipper_Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Pepper_and_Salt_Skipper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Rare_Skipper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Salt_Marsh_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Silver-spotted_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Swarthy_Skipper_Inner-MarylandBiodiversity.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Tawny-edged_Skipper-Inner-Wikipedia.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Yehl_Skipper_Inner-iNaturalist.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Zabulon_Skipper_Inner-Michelle_Gianvecchio.jpg",
                      "https://raw.githubusercontent.com/Diveeyha/Butterfly/main/Inner/Common_Sootywing_Inner-Wikipedia.jpg"
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
                    table-layout: fixed ;
                    width: 100% ;
                    margin: auto;
                }
                .stDataframe tr {
                    height: 250px; 
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
