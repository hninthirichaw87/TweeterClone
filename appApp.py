import streamlit as st
import pyrebase
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

@st.cache_resource
def get_db():
    db = firestore.client()
    return db

cred = credentials.Certificate("key.json")

firebase_admin.initialize_app(cred)



#configuration key
firebaseConfig = {
  "apiKey": "AIzaSyBRWmAyFNh71lagrb4TkbU-lmCXULwkXOQ",
  "authDomain": "fir-stapp-8978b.firebaseapp.com",
  "projectId": "fir-stapp-8978b",
  "databaseURL": "https://fir-stapp-8978b-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "fir-stapp-8978b.appspot.com",
  "messagingSenderId": "449510012162",
  "appId": "1:449510012162:web:c41d2c63a6e65b8211fe1b",
  "measurementId": "G-T7TFCT7YR2",
  "type" : "service_account",
    
  "private_key_id": "a57ef29a9795882aca910e1129e241224d8c22e0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC4JrtfLghmO6RL\ncZRlQc2gr736mumfLL8vaj488waaMEQnryzJ0xEKT/bIyUEcAQUISNP2jw2IRxJK\naqqIWgWMJT7x+VH/PlFwAI3yi2gOzNC6NLu2ddnU9OtGljo7XjFXK5QeYwc7/452\nHC7RbIksrYj1lNiPhJYqKgGNk5zW1/0ldD+jfZ4jyLu4HTrupcP0itpmqzrBGoaL\n9fo5F0VMVHb60HzmDjGXqZ9J6uK4H6uxwuaiczUhYVkQeoAlkYdSRsAU5uRsvOjU\nAU/1pwSTc7BibdiAzlNDggX2skivsiH/M6RVvWcwqwdSkHDd3njO3ZIUXF9ShBbf\nPTFgvbCJAgMBAAECggEAKw3vL+0ozJI0Muleux/b7i44mi9+4JbLKlBKNeDSEdmo\nDakwrQ06hjE07zPSk7QPU6UHXbWLgemv9pMixNdbRa1tnpBeofEVhDy081ixnwg2\n4toyaxH5uIb8vRehjMDUg19udX5MsjPpQGcNcSxRlA8MnvJKgZ+LplcE3u98s2QN\nYyo3UKkJ/CBNH3sLMHBLyjD8Ni5mJXgl389nI4rN7VYQty5JzsUpm/BgY+QL7qpq\nKWVUs1stmKAIL2BzIBNTB3VKDo3gH+5o7G0XWezIFDlaHpbTn4hHSwarl4JD8yEH\nUvIsrfj8UxP/MUNxRMAs+OEZ4XPAh5B6H9A3Pm6KUwKBgQDs5GKyO75TsNtFW653\nf1YyreiqqIoG2A1ixtyn+n7cqdvhnSIDaGvfVpuZh76z38Bf3ysaZzlxBQvTbEKJ\nzr7mIUxz5TjKDrHrNt3FCK2xqv2xtePS0tIXEUGNO2VPZotvIV1I4AJRNRJeXdEZ\nK46uPLEbP2A16FthE4G7JJtNJwKBgQDHAUtis/xczKAJLFIdmvFM2cnI59AdszLC\nWXTcvex/dGZ9CSiQgz1rK+2uAadUCE7501pwIwB6G7jcAPwIV0y+IdxKb0DKnhcj\nsV8O8Hry1w+uVCyfu6ubnagFv3i5EojsMLTSw++GjnugUoHmfe9LLPvXVVZ7ixKW\nGNCWZPACzwKBgCRYWggsgGQIw2udyGPPJqN56TOdzieEqHEaP6qKFUK30OOJnzlU\noRBQEml42Tpxvus2qz9OzRJZCtpyRrcsAEAApeE2LwNZQ9TpwxbC4RtcN7Y3SPAE\npnUhkaQgk8ed3RC81roinFhnQx01Wap581cqOqYKkDFVKAf53TKgSC+LAoGACtTQ\nNJQVRTvB7h3ibkgToBoueGfdlPA+8AMMcENKDvnX5jBMa+kou5+NdS4T3GgDXGeb\ngYT2Lq85lYfcL9wIikSvh8GcZirKmZ+6y8Zc+sCn0tY0A5GkWnjvPzjXqkMO/sP7\n44jUjZ9NrUEwXso17wKIxoSXi2vbXB4HpFfkFFMCgYB+376Jji160EBllXcwu18o\n+0Utc16ejBsOe7ShNFL/8ZCxGHv5G/qykEQo1uq3gRJ36ni7w/tNpkQCaWSe5Gs8\ny96CwuZjXtyPOrYyKn0A2CxNeHxQemZ9zMll/IARPp9FlahFxFhye/dUVH815jWh\n8UHHXToRE8aWspmngP52+Q==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-kn881@fir-stapp-8978b.iam.gserviceaccount.com",
  "client_id": "106373509509432904916",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-kn881%40fir-stapp-8978b.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"}

#firebase authentication

firebase2 = pyrebase.initialize_app(firebaseConfig)
auth = firebase2.auth()
    
#database
db = firebase2.database()
storage = firebase2.storage()
    
st.sidebar.title("Our community app")

#authentication
choice = st.sidebar.selectbox('login/SignUp',['Login','Sign up'])
email = st.sidebar.text_input("Please enter your email address")
password = st.sidebar.text_input("Please enter your password", type= 'password')

if choice == 'Sign up':
    handle = st.sidebar.text_input('Please enter app handle name', value = 'Default')
    submit = st.sidebar.button('Create my account')
    if submit:
        user = auth.create_user_with_email_and_password(email,password)
        st.success('Your account is created successfuly')
        st.balloons()
        
        #sign in
        user = auth.sign_in_with_email_and_password(email,password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(handle)
        st.title('Welcome'+ handle) 
        st.info('login via login')

if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email,password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)
        st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
        bio = st.radio('Jump to',['Home','Workplace feed','Settings'])
        if bio == 'Settings':
            #Check for image
            nImage = db.child(user['localId']).child("Image").get().val()
            #Image found
            if nImage is not None:
                #we plan to install all image under
                Image = db.child(user['localId']).child("Image").get()
                for img in Image.each():
                    img_choice = img.val()
                    #st.write(img_choice)
                st.image(img_choice)
                exp = st.expander('Change bio and image')
                with exp:
                    newImgPath = st.text_input('enter full path of your profile image')
                    upload_new = st.button('upload')
                    if upload_new:
                        uid = user['localId']
                        fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                        a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                        db.child(user['localId']).child("Image").push(a_imgdata_url)
                        st.success('Success!')
            else:
                st.info('No profile picture yet')
                newImgPath = st.text_input("Enter full path of profile picture")
                upload_new = st.button('upload')
                if(upload_new):
                    uid = user['localId']
                    #store initiatded bucket in firebase
                    fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                    a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens'])
                    db.child(user['localId']).child("Image").push(a_imgdata_url)

        elif bio== 'Home':
            col1, col2= st.columns(2)
            with col1:
                nImage = db.child(user['localId']).child("Image").get().val()
                if nImage is not None:
                    nImage = db.child(user['localId']).child("Image").get()
                    for img in nImage.each():
                        img_choice = img.val()
                    st.image(img_choice)
                else:
                    st.info('There is no profile picture yet. Go to edit profile and choose one!')
                post = st.text_input("Lets' share my current mood as  a post", max_chars=100)
                add_post= st.button('Share Posts')
                if add_post:
                    now = datetime.now()
                    dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
                    post ={'Posts': post,
                        'Timestamp': dt_string
                    }
                    results = db.child(user['localId']).child("Posts").push(post)
                    st.balloons()
            with col2:
                col2.header('')
                all_posts = db.child(user['localId']).child("Posts").get()
                if all_posts.val() is not None:
                    for Posts in reversed(all_posts.each()):
                        st.code(Posts.val(), language='')




                                
