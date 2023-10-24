import streamlit as st
import pyrebase
from datetime import datetime

#configuration key
firebaseConfig = {
  "apiKey": "AIzaSyBRWmAyFNh71lagrb4TkbU-lmCXULwkXOQ",
  "authDomain": "fir-stapp-8978b.firebaseapp.com",
  "databaseURL": "https://fir-stapp-8978b-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "fir-stapp-8978b.appspot.com",
  "messagingSenderId": "449510012162",
  "appId": "1:449510012162:web:c41d2c63a6e65b8211fe1b",
  "measurementId": "G-T7TFCT7YR2"}

#firebase authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
    
#database
db = firebase.database()
storage = firebase.storage()
    
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




                                