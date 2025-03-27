import streamlit as st
# We need to import the streamlit library as first
from datetime import datetime

# To create the list of the pages and the menu
st.set_page_config(
    page_title="My application for DV4S",
    layout="wide",
    initial_sidebar_state="expanded" # So it is open the menu
)
# We would exploit and use different tools that are present in different pages


# Title
st.title("🎈 My new app")

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

# Text and writer
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Data
value = st.slider("Select a specific value: ", 0, 100, 40)
# The values are in order the minimum, the maximum and the actual value of the slider

# To write the value of the slider (at screen)
st.write("You selected: ", value)



# There widgets that allows to introduce some text, which are:
# Title
st.title("This is a title")
# Header
st.header("_Hi_ :green[guys!]") # To have the Latin/Italic we use "_ _" and for the colour we need to use ":" followed by the name of colour and the words to be coloured into "[]"
# Subheader
st.subheader("Welcome to the site! :goat:") # To insert an emoji we need to palce its name between two ":" (so two columns)
# To write in bold (grassetto) we need to place the words between two couple of "**"
st.write("You a **goat**!")

# We need to use the HTML syntax to perform all the things, or the things already implemented in Streamlit

# To implement a markdown string using an HTML syntax and language, we could use it, placing the string in between >< and after the definition of the style and colour characterstics
st.markdown('<p style="color:yellow; font-size:20px;">This is a yellow string</p>',
            unsafe_allow_html=True)


# Additional UI and widget, more interactive and with more interactive tasks
# List
sports_list = ['soccer', 'basket', 'football', 'tennis']
# Button (that if pushed gives displays the list of before)
button_pressed = st.button('Push me for Sports List', type="primary")
# Check of the state of the button (if pressed or not)
if button_pressed: #If the button is pressed and so if the "button_pressed" is a boolean and equal to True, we could enter in the if and display the list, simply writing it with "st.write()" command
    st.write(sports_list)


# Checkbox 
# Similar to the button, where the flagged/checked box means a True boolean, instead a not checked one a False
check_pressed = st.checkbox('I like it!')
# Check of the value and of the checkbox
if check_pressed:
    st.write(sports_list)
else:
    st.write('')


# Radio Button (to check different element into a list)
chosen_item = st.radio('What sport do you like?', sports_list)
# Check of the decision and its presentation to the user
st.write('I know that you liked ' + chosen_item)


# Select Box
chosen_item_again = st.selectbox('What sport do you like?', sports_list)
# Check of the decision and its presentation to the user
st.write('I know that you liked ' + chosen_item_again)


# Multi-Item Selection
multi_item = st.multiselect('What sports do you like?', sports_list)
# Check of the decision and its presentation to the user (with a for loop)
for sport in multi_item:
    st.write(f'Your sports are {sports_list[sport]}')


# Sliders
age = st.slider('Your age', 18, 65, 24)
st.write('Your age is', age)
# To have a slider to define a range of values, we could change it in this way
age = st.slider('Your age', 18, 65, (24,50))
st.write('Your age is', age) # In this case we have put into the current value a "tuple", which is then written all together in its components


# Forms
user_name = st.text_input('Your name', placeholder='Write your name...')
st.write('Your name is: ', user_name)
# The same for a number entering
user_age = st.number_input('Your age:', 
                           min_value= 18,
                           max_value= 65,
                           value= 24,
                           step= 1)


# Date (selection or extraction)
match_date = st.date_input('Select date range',
                           value= (datetime(2025, 3, 15), datetime(2025, 3, 31)), # datetime to convert the string into dates
                           # To select only one date, it is not a tuple in the value field, like below
                           )
match = st.date_input('Select date range',
                           value= datetime(2025, 3, 15), # datetime to convert the string into dates
                           # To select only one date, it is the way
                           )


# To create a "safe" and dedicated parts/windows of the page, in which we could place a formfor example, we could start this window with the "with" command
# Try and Catch (control of the Forms and evaluation of problems into a block of code (with a "with " command and block, able to leave not impacting the issue on all the site/application))
with st.form('User Information'):
    # Forms
    user_name = st.text_input('Your name', placeholder='Write your name...')
    st.write('Your name is: ', user_name)
    # The same for a number entering
    user_age = st.number_input('Your age:', 
                           min_value= 18,
                           max_value= 65,
                           value= 24,
                           step= 1)
    submitted = st.form_submit_button('Submit it!')

if submitted:
    st.write('You submitted it!')