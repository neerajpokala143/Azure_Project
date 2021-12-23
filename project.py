import os
import streamlit as st
import pandas as pd
import numpy as np
import tempfile
from PIL import Image
import asyncio
import io
import glob
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from io import BytesIO
from PIL import ImageDraw
import json



st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title('Test the API powered by azure')
st.sidebar.subheader('select API want to test')
app_mode = st.sidebar.radio(
    "",
    ("About App","Translator","Face Recognization","Object Detection",),
)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('Pokala Neeraj|\n Neerajpokala143@gmail.com https://github.com/neerajpokala143')
if app_mode =='About App':

    st.markdown("<h1 style='text-align: center; color: skyblue; '>Azure Application </h1>", unsafe_allow_html=True)
    st.markdown('In this application we are using **Microsoft Azure APIS** for creating a Translator,Face API . **StreamLit** is to create the Web Graphical User Interface (GUI) ')
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 400px;
        margin-left: -400px;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    st.video('https://www.youtube.com/watch?v=KXkBZCe699A')

    st.markdown('''
              # About Me \n 
                Hey this is ** Neeraj Pokala **. \n
                
                
                Also check me out on Social Media
                - [git-Hub](https://github.com/neerajpokala143)
                - [LinkedIn](https://www.linkedin.com/in/neeraj-pokala-b76b60199)
                - [Instagram](https://instagram.com/neer_aj.p?utm_medium=copy_link)\n
                If you are interested in building more about Microsoft Azure then   [click here](https://azure.microsoft.com/en-in/)\n
                For any Troubleshooting and Further UI development feel free to DM me at --- neerajpokala143@gmail.com
                ''')




if app_mode =='Translator':
    st.markdown("<h1 style='text-align: center; color: skyblue; '>Overcoming language difficulties with AI and Azure services: </h1>", unsafe_allow_html=True)
    st.image(os.path.join('./images','translator2.jpg'),use_column_width=True )
    st.markdown("<h1 style='text-align: center; color: skyblue; '>Welcome to our page Translate a language now just in no time: </h1>", unsafe_allow_html=True)

    st.markdown("Translator is a cloud-based machine translation service you can use to translate text in with a simple REST API call. The service uses modern neural machine translation technology and offers statistical machine translation technology. Custom Translator is an extension of Translator, which allows you to build neural translation systems. The customized translation system can be used to translate text with Translator or Microsoft Speech Services")
    
    st.markdown("For more documentation on language support in Azure:[click here](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/language-support)")
    Entered_text = st.text_input('Enter the text of your choice (ONLY IN MEANINGFUL ENGLISH WORD OR  SENTENCE):')

    select=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'])

    if select == 'arabic':
        lang= 'ar'
    elif select == 'bangla':
        lang= 'bn'
    elif select == 'chinese':
        lang= 'lzh'
    elif select == 'dutch':
        lang= 'nl'
    elif select == 'english':
        lang= 'en'
    elif select == 'french':
        lang= 'fr'
    elif select == 'german':
        lang= 'de'
    elif select == 'greek':
        lang= 'el'
    elif select == 'hindi':
        lang= 'hi'
    elif select == 'hungarian':
        lang= 'hu'
    elif select == 'indonesian':
        lang= 'id'
    elif select == 'irish':
        lang= 'ga'
    elif select == 'italian':
        lang= 'it'
    elif select == 'japanese':
        lang= 'ja'
    elif select == 'kannada':
        lang= 'kn'
    elif select == 'korean':
        lang= 'ko'
    elif select == 'malayalam':
        lang= 'ml'
    elif select == 'nepali':
        lang= 'ne'
    elif select == 'portuguesei':
        lang= 'pt'
    elif select == 'punjabi':
        lang= 'pa'
    elif select == 'russian':
        lang= 'ru'
    elif select == 'spanish':
        lang= 'es'
    elif select == 'tamil':
        lang= 'ta'
    elif select == 'telugu':
        lang= 'te'  
    elif select == 'turkish':
        lang= 'tr'
    elif select == 'urdu':
        lang= 'ur'

    button_translate=st.button('Click me',help='To translate language')

    if button_translate and Entered_text:
        import requests, uuid, json

        # Add your subscription key and endpoint
        subscription_key = "337c389f623c484fbb31520b6d0343a9"
        endpoint = "https://api.cognitive.microsofttranslator.com/"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "centralindia"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'from': 'en',
            'to': [lang]
        }
        constructed_url = endpoint + path

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())

            
        }

        # You can pass more than one object in body.
        body = [{
            'text': Entered_text
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()


        st.success(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    elif button_translate:
        st.error("!! Please enter input text in English")

    st.markdown('---')

    detect=st.text_input('Enter the text to detect (No language Restriction):')

    detect_select=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=1)

    if detect_select == 'arabic':
        detect_lang= 'ar'
    elif detect_select == 'bangla':
        detect_lang= 'bn'
    elif detect_select == 'chinese':
        detect_lang= 'lzh'
    elif detect_select == 'dutch':
        detect_lang= 'nl'
    elif detect_select == 'english':
        detect_lang= 'en'
    elif detect_select == 'french':
        detect_lang= 'fr'
    elif detect_select == 'german':
        detect_lang= 'de'
    elif detect_select == 'greek':
        detect_lang= 'el'
    elif detect_select == 'hindi':
        detect_lang= 'hi'
    elif detect_select == 'hungarian':
        detect_lang= 'hu'
    elif detect_select == 'indonesian':
        detect_lang= 'id'
    elif detect_select == 'irish':
        detect_lang= 'ga'
    elif detect_select == 'italian':
        detect_lang= 'it'
    elif detect_select == 'japanese':
        detect_lang= 'ja'
    elif detect_select == 'kannada':
        detect_lang= 'kn'
    elif detect_select == 'korean':
        detect_lang= 'ko'
    elif detect_select == 'malayalam':
        detect_lang= 'ml'
    elif detect_select == 'nepali':
        detect_lang= 'ne'
    elif detect_select == 'portuguesei':
        detect_lang= 'pt'
    elif detect_select == 'punjabi':
        detect_lang= 'pa'
    elif detect_select == 'russian':
        detect_lang= 'ru'
    elif detect_select == 'spanish':
        detect_lang= 'es'
    elif detect_select == 'tamil':
        detect_lang= 'ta'
    elif detect_select == 'telugu':
        detect_lang= 'te'  
    elif detect_select == 'turkish':
        detect_lang= 'tr'
    elif detect_select == 'urdu':
        detect_lang= 'ur'          


    button_detect=st.button('Click me',help='To detect language')

    if button_detect and detect:
        import requests, uuid, json

        # Add your subscription key and endpoint
        subscription_key ="337c389f623c484fbb31520b6d0343a9"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "centralindia"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            'to': [detect_lang]
        }
        constructed_url = endpoint + path

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': detect
        }]

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response123 = request.json()


        st.success(json.dumps(response123, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    elif button_detect:
        st.error("!! Please enter input in any language")

    st.markdown('---')

    latin=st.text_input('Enter the text to convert to script (No language Restriction):') 

    select_latin=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=2)

    if select_latin == 'arabic':
        latin_lang= 'ar'
    elif select_latin == 'bangla':
        latin_lang= 'bn'
    elif select_latin == 'chinese':
        latin_lang= 'lzh'
    elif select_latin == 'dutch':
        latin_lang= 'nl'
    elif select_latin == 'english':
        latin_lang= 'en'
    elif select_latin == 'french':
        latin_lang= 'fr'
    elif select_latin == 'german':
        latin_lang= 'de'
    elif select_latin == 'greek':
        latin_lang= 'el'
    elif select_latin == 'hindi':
        latin_lang= 'hi'
    elif select_latin == 'hungarian':
        latin_lang= 'hu'
    elif select_latin == 'indonesian':
        latin_lang= 'id'
    elif select_latin == 'irish':
        latin_lang= 'ga'
    elif select_latin == 'italian':
        latin_lang= 'it'
    elif select_latin == 'japanese':
        latin_lang= 'ja'
    elif select_latin == 'kannada':
        latin_lang= 'kn'
    elif select_latin == 'korean':
        latin_lang= 'ko'
    elif select_latin == 'malayalam':
        latin_lang= 'ml'
    elif select_latin == 'nepali':
        latin_lang= 'ne'
    elif select_latin == 'portuguesei':
        latin_lang= 'pt'
    elif select_latin == 'punjabi':
        latin_lang= 'pa'
    elif select_latin == 'russian':
        latin_lang= 'ru'
    elif select_latin == 'spanish':
        latin_lang= 'es'
    elif select_latin == 'tamil':
        latin_lang= 'ta'
    elif select_latin == 'telugu':
        latin_lang= 'te'  
    elif select_latin == 'turkish':
        latin_lang= 'tr'
    elif select_latin == 'urdu':
        latin_lang= 'ur'          


    latin_button=st.button('Click me',help='To script language',key=2)

    if latin_button and latin:
        import requests, uuid, json

        # Add your subscription key and endpoint
        subscription_key = "337c389f623c484fbb31520b6d0343a9"
        endpoint = "https://api.cognitive.microsofttranslator.com"

        # Add your location, also known as region. The default is global.
        # This is required if using a Cognitive Services resource.
        location = "centralindia"

        path = '/translate'
        constructed_url = endpoint + path

        params = {
            'api-version': '3.0',
            # to translate
            'to': latin_lang,
            'toScript': 'latn'
        }
        constructed_url = endpoint + path

        headers = {
            'Ocp-Apim-Subscription-Key': subscription_key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        # You can pass more than one object in body.
        body = [{
            'text': latin
        }]
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response444 = request.json()

        st.success(json.dumps(response444, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    elif latin_button:
        st.error("!! Please enter input in any language")
        
        
        
if app_mode=='Face Recognization':
  st.image(os.path.join('./images','face recognition.jpg'),use_column_width=True )
  st.title("Face Recognition(Powered by Azure)")
  st.header('Face Recognition:')
  st.markdown("Using Azure I build to detect, identify and analyse faces in images.")
  st.text("Detect the objects in images")
  
  image_file =  st.file_uploader("Upload Images (less than 1mb)", type=["png","jpg","jpeg"])
  if image_file is not None:
    img = Image.open(image_file)
    #st.image(image_file,width=250,caption='Uploaded image')
    byte_io = BytesIO()
    img.save(byte_io, 'PNG')#PNG
    image = byte_io.getvalue()


  button_translate=st.button('Click me to show recognized photo',help='To give the image')

  if button_translate and image_file :

    def draw_face(img):

        subscription_key = 'ea8c44f876804e43ab35a26a09d59da5'  
        BASE_URL = "https://recognition-ai.cognitiveservices.azure.com/" + '/face/v1.0/detect'  
        headers = {
        # Request headers
        'Content-Type': 'application/octet-stream', 
        'recognitionModel': 'recognition_01' ,
        'Ocp-Apim-Subscription-Key': subscription_key,
        'detectionModel': 'detection_01',
        }
        response = requests.post(BASE_URL, headers=headers, data=image)
        faces = response.json()
        print(faces)
        def getRectangle(faceDictionary):
            rect = faceDictionary['faceRectangle']
            left = rect['left']
            top = rect['top']
            bottom = left + rect['height']
            right = top + rect['width']
            return ((left, top), (bottom, right))


        output_image = Image.open(BytesIO(image))
        
    #   For each face returned use the face rectangle and draw a red box.
        draw = ImageDraw.Draw(output_image)
        for face in faces:
            draw.rectangle(getRectangle(face), outline='red',width=2)
        return output_image
   #image_data = open(image_file, "rb").read()

    image = draw_face(img)

    st.image(image, caption='Output image')
    
    
    
if app_mode =='Object Detection':
    
    st.image(os.path.join('./images','object detection.jpg'),use_column_width=True )
    st.markdown("<h1 style='text-align: center; color: skyblue; '> Object Recognition </h1>", unsafe_allow_html=True)

    st.title("Object Recognition(Powered by Azure)")

    st.markdown("Using Azure I build to **_Object_ detection** , it identify and analyse the image.")
    st.text("Detect the objects in images")

    url_file =  title = st.text_input('Paste image address URL')
    st.text("Example :-https://media.istockphoto.com/photos/hungry-dog-picture-id497384624?k=20&m=497384624&s=612x612&w=0&h=1yf2i-X6-8RH1KqUtGAknainRw8rAMzuBUeCZF2gl-c=")
    button_translate=st.button('Click me',help='To give the image')

    if button_translate and url_file :
   
        subscription_key = 'afac470736ce49ca8352ec7c83736fc7'
        endpoint = 'https://objectdetection21.cognitiveservices.azure.com/'
        
            # Add your Computer Vision subscription key and endpoint to your environment variables.
        analyze_url = endpoint + "vision/v3.1/analyze"
        
        # Set image_url to the URL of an image that you want to analyze.
        headers = {'Ocp-Apim-Subscription-Key': subscription_key}
        params = {'visualFeatures': 'Categories,Description,Color'}
        data = {'url': url_file}
        response = requests.post(analyze_url, headers=headers,params=params, json=data)
        response.raise_for_status()

        # The 'analysis' object contains various fields that describe the image. The most
        # relevant caption for the image is obtained from the 'description' property.
        analysis = response.json()
        print(json.dumps(response.json()))
        image_caption = analysis["description"]["captions"][0]["text"].capitalize()
        response_image = requests.get(url_file)
        
        # Display the image and overlay it with the caption.
        aux_im = Image.open(BytesIO(response_image.content))
        captio=st.subheader(image_caption)
        st.image(aux_im, caption=image_caption)
