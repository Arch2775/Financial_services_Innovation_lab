import streamlit as st
from PIL import Image

# Define the path to the data files
inferences_files = {
    'Amazon 📦': './amzn_content/amzn_b.txt',
    'Nvidia 🖥️': './nvda_content/nvda_b.txt',
    'GameStop 🎮': './gme_content/gme_b.txt'
}

visualization_files = {
    'Amazon 📦': [
        './amzn_content/a.jpg',
        './amzn_content/b.jpg',
        './amzn_content/c.jpg'
    ],
    'Nvidia 🖥️': [
        './nvda_content/nvda1.jpg',
        './nvda_content/nvda2.jpg'
    ],
    'GameStop 🎮': [
        './gme_content/gme1.jpg',
        './gme_content/gme2.jpg',
        './gme_content/gme3.jpg'
    ]

}

# Function to read text inferences from a file
def read_inferences(file):
    with open(file, 'r') as f:
        return f.read()

def main():

    # URL of the image
    image_url = "./hs.jpg"
    
    # Embed image and text using HTML in markdown
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 10px;">
            <img src="{image_url}" alt="Title Image" style="height: 50px;">
        </div>
        """, unsafe_allow_html=True)



    
    # Sidebar for interactions
    st.sidebar.title('Companies')
    
    # Dropdown to select the stock in the sidebar
    selected_stock = st.sidebar.selectbox('Select Stock', options=['Amazon 📦','Nvidia 🖥️','GameStop 🎮'])
    
    # Display inferences and visualizations buttons in the sidebar
    if st.sidebar.button('Show Inferences'):
        inference_text = read_inferences(inferences_files[selected_stock])
        st.write(inference_text)
    
    if st.sidebar.button('Show Visualizations'):
        images = visualization_files[selected_stock]
        if images:
            # Each image is displayed in a full-width single column for better visibility
            for index, img_path in enumerate(images):
                st.image(Image.open(img_path), caption='', use_column_width='always')
        else:
            st.sidebar.error('No images available for the selected stock.')


if __name__ == '__main__':
    main()



