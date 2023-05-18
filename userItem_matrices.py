import streamlit as st
import pandas as pd
from PIL import Image
from theme import customized_button, button_style

customized_button = customized_button
button_style=button_style

def load_text(file_path):
    """A convenience function for reading in the files used for the site's text"""
    with open(file_path) as in_file:
        return in_file.read()

st.markdown('''<div style="text-align: center;">
  <h1 style="display: inline-block; text-align: center;">Revealing Customer Preferences</h1>
  <h3 style="display: inline-block;">&nbsp 🎉 🎁</h3>
</div>''', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;padding-top:0px'>Building User Profile for Personalized Marketing with Python</h3>", unsafe_allow_html=True)


# Display the combined HTML code in Streamlit
component_profile = load_text('profile.html')
st.components.v1.html(component_profile,  height=50)

st.markdown("<p style='text-align: center'>Imagine being able to predict what products a customer is most likely to purchase 💵 based on their past behaviors.</p>", unsafe_allow_html=True)
st.markdown('''
<h4 style='text-align: center;font-weight: bold;'>"User-item matrix can uncover valuable insights into individual customer preferences"</h4>
''', unsafe_allow_html=True)

st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>
<p style='text-align: center'>The matrix allow us <span class='highlight'>to deliver personalized experiences </span> and create targeted marketing campaigns.</p>
''', unsafe_allow_html=True)

st.header('Introduction')

st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>
<p>Understand customer preferences is crucial for delivering personalized experiences in any industry. In this post,
we will explore how to create <span class='highlight'> user-item matrix (from users’ behavior) </span> used for understanding <span class='highlight'>individual customer preferences.</span>
</p>
<p>By leveraging this matrix, businesses can enhance their recommendations and tailor marketing strategies to meet the unique needs of each customer.</p>
''',
unsafe_allow_html=True)

st.header('User-item matrix')

st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>
<p>
The user-item matrix can be visualized as a table below, where each row corresponds to a distinct user, and each column represents an item.
Within this matrix, the numerical value in each cell shows the user's sentiment or <span class='highlight'> preference score </ span> towards the respective item, indicating how much they like or dislike it.
</p>
''',
unsafe_allow_html=True)

image = Image.open('table_1.png')

st.image(image)

st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>
<p>
Note that <span class='highlight'> an empty cell </span> in the user-item matrix means no prior interaction between the user and the item.
In the world of <span style='font-weight: bold;'>recommender systems</span>, there is an interest in predicting how much a user will like or dislike items they have never interacted with before.
However, this topic goes beyond the scope of this post, as we will focus on understanding the current preferences of the user.
</p>
''',
unsafe_allow_html=True)

st.header('Explicit vs implicit scores')

st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>
<p>
The scores in the matrix generally come from two sources:
</p>
<ul>
    <li>
        <span class='highlight'>Explicit scores</span> added by users
        <ul>
            <li>Upvotes or downvotes 👍🏻 👎🏻 on platforms like Netflix</li>
            <li>Rating score ranging from 1 to 5, for instance ⭐️⭐️⭐️</li>
        </ul>
    </li>
    <li>
        Scores derived <span class='highlight'>from user behaviors</span>, which are implicit in nature
        <ul>
            <li>Views, adding to cart 🛒, purchases, and more</li>
        </ul>
    </li>
</ul>
<p>
Keep in mind that explicit scores may not always accurately reflect users' true opinions.
Various external factors, such as social pressure or influence from friends, can impact how users rate items.
Moreover, low scores might be influenced by factors unrelated to the product itself, such as delivery delays or damaged packaging.
</p>
''',
unsafe_allow_html=True)

st.header('Calculating implicit scores')

st.markdown('''
<style>
        .highlight {
            background: linear-gradient(to bottom, transparent 50%, #ADD8E6 50%);
            font-weight: bold;
        }
</style>

<p>
While explicit scores are obtained by directly asking users to rate items, we will shift our focus to implicit scores, which are more complex in nature. Implicit scores are derived from user behaviors and interactions, making them a valuable indicator of user preferences.
</p>
<p>
To compute implicit scores, it can be seen as an attempt to infer the scores that users would assign to the content they have interacted with, such as viewing, streaming, or making purchases.
</p>
''',
unsafe_allow_html=True)

image = Image.open('shopping.png')
st.image(image)