import streamlit as st
from PIL import Image

# Define the path to the data files
inferences_files = {
    'Amazon 📦': r'.\amzn_content\amzn_b.txt',
    'Nvidia 🖥️': r'.\nvda_content\nvda_b.txt',
    'GameStop 🎮': r'.\gme_content\gme_b.txt'
}

visualization_files = {
    'Amazon 📦': [
        r'.\amzn_content\a.jpg',
        r'.\amzn_content\b.jpg',
        r'.\amzn_content\c.jpg'
    ],
    'Nvidia 🖥️': [
        r'.\nvda_content\nvda1.jpg',
        r'.\nvda_content\nvda2.jpg'
    ],
    'GameStop 🎮': [
        r'.\gme_content\gme1.jpg',
        r'.\gme_content\gme2.jpg',
        r'.\gme_content\gme3.jpg'
    ]

}

# Function to read text inferences from a file
def read_inferences(file):
    with open(file, 'r') as f:
        return f.read()

def main():
    st.title('📊📈 Quantitative and Qualitative Analysis of SEC-10K filings from EDGAR Database')


    
    # Sidebar for interactions
    st.sidebar.title('User Interactions')
    
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



