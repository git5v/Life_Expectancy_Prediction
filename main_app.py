from curses.ascii import US
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


string = "Life Expectancy Prediction of each country"

st.set_page_config(page_title=string, page_icon='🎯', layout="wide",
                   initial_sidebar_state="auto", menu_items=None)

st.title(string, anchor=None)

im = Image.open("Life_exp.png")
st.image(im, width=700)

df = pd.read_csv("Life Expectancy Data.csv")


country = {"Afghanistan": 0, 'Albania': 1, 'Algeria': 2, 'Angola': 3,
           'Antigua and Barbuda': 4, 'Argentina': 5, 'Armenia': 6,
           'Australia': 7, 'Austria': 8, 'Azerbaijan': 9, 'Bahamas': 10,
           'Bahrain': 11, 'Bangladesh': 12, 'Barbados': 13, 'Belarus': 14,
           'Belgium': 15, 'Belize': 16, 'Benin': 17, 'Bhutan': 18,
           'Bolivia (Plurinational State of)': 19,
           'Bosnia and Herzegovina': 20,
           'Botswana': 21, 'Brazil': 22, 'Brunei Darussalam': 23,
           'Bulgaria': 24,
           'Burkina Faso': 25, 'Burundi': 26, 'Cabo Verde': 27,
           'Cambodia': 28,
           'Cameroon': 29, 'Canada': 30, 'Central African Republic': 31,
           'Chad': 32, 'Chile': 33, 'China': 34, 'Colombia': 35,
           'Comoros': 36,
           'Congo': 37, 'Cook Islands': 38, 'Costa Rica': 39, 'Croatia': 40,
           'Cuba': 41, 'Cyprus': 42, 'Czechia': 43, "Côte d'Ivoire": 44,
           "Democratic People's Republic of Korea": 45,
           'Democratic Republic of the Congo': 46, 'Denmark': 47,
           'Djibouti': 48,
           'Dominica': 49, 'Dominican Republic': 50,
           'Ecuador': 51, 'Egypt': 52, 'El Salvador': 53,
           'Equatorial Guinea': 54, 'Eritrea': 55, 'Estonia': 56,
           'Ethiopia': 57, 'Fiji': 58, 'Finland': 59, 'France': 60,
           'Gabon': 61, 'Gambia': 62, 'Georgia': 63, 'Germany': 64,
           'Ghana': 65, 'Greece': 66, 'Grenada': 67, 'Guatemala': 68,
           'Guinea': 69, 'Guinea-Bissau': 70, 'Guyana': 71,
           'Haiti': 72, 'Honduras': 73, 'Hungary': 74, 'Iceland': 75,
           'India': 76, 'Indonesia': 77, 'Iran (Islamic Republic of)': 78,
           'Iraq': 79, 'Ireland': 80, 'Israel': 81, 'Italy': 82,
           'Jamaica': 83,
           'Japan': 84, 'Jordan': 85, 'Kazakhstan': 86, 'Kenya': 87,
           'Kiribati': 88, 'Kuwait': 89, 'Kyrgyzstan': 90,
           "Lao People's Democratic Republic": 91, 'Latvia': 92,
           'Lebanon': 93,
           'Lesotho': 94, 'Liberia': 95, 'Libya': 96, 'Lithuania': 97,
           'Luxembourg': 98, 'Madagascar': 99, 'Malawi': 100,
           'Malaysia': 101,
           'Maldives': 102, 'Mali': 103, 'Malta': 104,
           'Marshall Islands': 105,
           'Mauritania': 106, 'Mauritius': 107, 'Mexico': 108,
           'Micronesia (Federated States of)': 109, 'Monaco': 110,
           'Mongolia': 111, 'Montenegro': 112, 'Morocco': 113,
           'Mozambique': 114, 'Myanmar': 115, 'Namibia': 116, 'Nauru': 117,
           'Nepal': 118, 'Netherlands': 119, 'New Zealand': 120,
           'Nicaragua': 121, 'Niger': 122, 'Nigeria': 123, 'Niue': 124,
           'Norway': 125, 'Oman': 126, 'Pakistan': 127, 'Palau': 128,
           'Panama': 129, 'Papua New Guinea': 130, 'Paraguay': 131,
           'Peru': 132, 'Philippines': 133, 'Poland': 134, 'Portugal': 135,
           'Qatar': 136,
           'Republic of Korea': 137, 'Republic of Moldova': 138,
           'Romania': 139, 'Russian Federation': 140, 'Rwanda': 141,
           'Saint Kitts and Nevis': 142, 'Saint Lucia': 143,
           'Saint Vincent and the Grenadines': 144, 'Samoa': 145,
           'San Marino': 146, 'Sao Tome and Principe': 147,
           'Saudi Arabia': 148,
           'Senegal': 149, 'Serbia': 150, 'Seychelles': 151,
           'Sierra Leone': 152,
           'Singapore': 153, 'Slovakia': 154, 'Slovenia': 155,
           'Solomon Islands': 156,
           'Somalia': 157, 'South Africa': 158, 'South Sudan': 159,
           'Spain': 160,
           'Sri Lanka': 161, 'Sudan': 162, 'Suriname': 163, 'Swaziland': 164,
           'Sweden': 165,
           'Switzerland': 166, 'Syrian Arab Republic': 167, 'Tajikistan': 168,
           'Thailand': 169, 'The former Yugoslav republic of Macedonia': 170,
           'Timor-Leste': 171, 'Togo': 172, 'Tonga': 173,
           'Trinidad and Tobago': 174,
           'Tunisia': 175, 'Turkey': 176, 'Turkmenistan': 177, 'Tuvalu': 178,
           'Uganda': 179, 'Ukraine': 180, 'United Arab Emirates': 181,
           'United Kingdom of Great Britain and Northern Ireland': 182,
           'United Republic of Tanzania': 183,
           'United States of America': 184,
           'Uruguay': 185, 'Uzbekistan': 186, 'Vanuatu': 187,
           'Venezuela (Bolivarian Republic of)': 188, 'Viet Nam': 189,
           'Yemen': 190, 'Zambia': 191, 'Zimbabwe': 192}

number1 = "United States of America"
number1 = st.text_input('Enter your country with each of first letter with'
                        'capital example United States of America')
st.write('The current number is ', number1)
st.markdown("""---""")


df.groupby('Country')['Life expectancy '].mean()


st.markdown('**The featured data is from year 2000 to 2015**')

list1 = []
list1 = df.groupby('Country')['Life expectancy '].mean()

x = 0
try:
    x = country[number1]
    print("Value associated to the key is:", list1[x])
except KeyError:
    print("Key not present in Dictionary")


input1 = list1[x]
st.write('The Avarage Life expectancy of your country is ')


st.success(input1)
st.markdown("""---""")

list2 = []
list2 = df.groupby('Country')['Adult Mortality'].mean()

x = 0
try:
    x = country[number1]
    print("Value associated to the key is:", list2[x])
except KeyError:
    print("Key not present in Dictionary")

input1 = list2[x]


st.write('The Avarage Adult Mortality of your country is ')
st.success(input1)

st.markdown("""---""")


list3 = []
list3 = df.groupby('Country')['Alcohol'].mean()

x = 0
try:
    x = country[number1]
    print("Value associated to the key is:", list3[x])
except KeyError:
    print("Key not present in Dictionary")

input1 = list3[x]
st.write('The Avarage Alcohol consumption perecent of your country is ')
st.success(input1*10)

st.markdown("""---""")

list4 = []
list4 = df.groupby('Country')['GDP'].mean()
x = 0
try:
    x = country[number1]
    print("Value associated to the key is:", list4[x])
except KeyError:
    print("Key not present in Dictionary")
input1 = list4[x]
st.write('The Avarage GDP of your country in million is ')
st.success(input1)

st.markdown("""---""")

list5 = []
list5 = df.groupby('Country')['Population'].mean()
x = 0
try:
    x = country[number1]
    print("Value associated to the key is:", list4[x])
except KeyError:
    print("Key not present in Dictionary")

input1 = list5[x]
st.write('The Avarage Population of your country is ')
st.success(input1*10)

st.markdown("""---""")

list6 = []
list6 = df.groupby('Country')['Income composition of resources'].mean()
x = 0
try:
    x = country[number1]
    print("Value associated to the key is:", list5[x])
except KeyError:
    print("Key not present in Dictionary")
input1 = list6[x]
st.write('The Avarage Income composition of resources of your country is ')
st.success(input1)

st.markdown("""---""")

list7 = []
list7 = df.groupby('Country')['Schooling'].mean()
x = 0
try:
    x = country[number1]
    print("Value associated to the key is:", list6[x])
except KeyError:
    print("Key not present in Dictionary")
input1 = list7[x]
st.write('The Avarage Schooling years of your country is ')
st.success(input1)

st.markdown("""---""")

footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with love <a style=' text-align: center;'
 target="_blank"></a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
