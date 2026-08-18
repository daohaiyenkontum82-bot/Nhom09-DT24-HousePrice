import streamlit as st
import pandas as pd
import joblib
import time

# ==========================================
# CẤU HÌNH TRANG (Mở rộng toàn màn hình, thanh công cụ luôn mở)
# ==========================================
st.set_page_config(
    page_title="ESTATE ANALYTICS", 
    page_icon="💎", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==========================================
# 1. NHÚNG MÃ CSS CUSTOM (GIAO DIỆN GLASSMORPHISM)
# ==========================================
st.markdown("""
<style>
    /* Ẩn menu mặc định và footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Hình nền Biệt thự */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2075&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Lớp phủ đen mờ */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(14, 17, 23, 0.75); 
        z-index: 0;
    }
    
    .stApp > header, .stApp > div {
        z-index: 1;
        position: relative;
    }

    /* Thẻ thông số */
    div[data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.05); 
        backdrop-filter: blur(15px); 
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        border-color: rgba(212, 175, 55, 0.8); 
        background: rgba(255, 255, 255, 0.1);
    }
    
    div[data-testid="metric-container"] label {
        color: #E2E8F0 !important;
        font-weight: 500;
        font-size: 1.1rem;
    }
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
        color: #D4AF37 !important; 
        font-size: 2.2rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Nút bấm */
    .stButton>button {
        background: rgba(212, 175, 55, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        color: #D4AF37;
        font-weight: 800;
        font-size: 1.3rem;
        padding: 20px 0;
        border-radius: 15px;
        border: 1px solid rgba(212, 175, 55, 0.5);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        background: rgba(212, 175, 55, 0.8);
        color: #000000;
        transform: scale(1.02);
        border: 1px solid rgba(212, 175, 55, 1);
    }
    
    /* Tiêu đề */
    .main-title {
        text-align: center;
        color: #FFFFFF;
        font-size: 3.8rem;
        font-weight: 900;
        margin-bottom: 0px;
        letter-spacing: 3px;
        text-shadow: 0 4px 15px rgba(0,0,0,0.8);
    }
    .sub-title {
        text-align: center;
        color: #D4AF37;
        font-size: 1.3rem;
        margin-bottom: 50px;
        letter-spacing: 2px;
        text-shadow: 0 2px 5px rgba(0,0,0,0.8);
    }
    
    /* Khung kết quả */
    .result-box {
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(212, 175, 55, 0.4);
        padding: 40px;
        border-radius: 20px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        animation: fadeIn 1s ease-in-out;
    }
    .result-price {
        font-size: 4.8rem;
        color: #FFFFFF;
        font-weight: 900;
        margin: 15px 0;
        text-shadow: 0 0 30px rgba(212, 175, 55, 0.6);
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. XỬ LÝ MODEL & GIAO DIỆN CHÍNH
# ==========================================
try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    st.error("Chưa tìm thấy file model.pkl!")

st.markdown('<h1 class="main-title">ESTATE ANALYTICS</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Hệ thống Định giá Bất động sản Cao cấp - Nhóm 09</p>', unsafe_allow_html=True)

st.sidebar.markdown("### ⚙️ THÔNG SỐ TÀI SẢN")
st.sidebar.markdown("---")
    
def user_input_features():
    # Chọn đơn vị đo lường
    unit_choice = st.sidebar.radio("🌐 Đơn vị đo lường (Chuẩn Việt/Mỹ):", ("Mét vuông (m²)", "Feet vuông (sq ft)"))
    st.sidebar.markdown("---")
    
    # Xử lý nhập liệu theo đơn vị
    if unit_choice == "Mét vuông (m²)":
        area_display = st.sidebar.number_input('📐 Diện tích sàn (m²)', min_value=30, max_value=1000, value=100, step=5)
        area_for_model = area_display * 10.7639 # AI dùng data Mỹ nên phải quy đổi ngầm
    else:
        area_display = st.sidebar.number_input('📐 Diện tích sàn (sq ft)', min_value=300, max_value=10000, value=1076, step=50)
        area_for_model = area_display 
        
    bedrooms = st.sidebar.number_input('🛏️ Số phòng ngủ', min_value=1, max_value=10, value=3)
    bathrooms = st.sidebar.number_input('🛁 Số phòng tắm', min_value=1, max_value=10, value=2)
    year_built = st.sidebar.number_input('🏗️ Năm xây dựng', min_value=1900, max_value=2026, value=2024)
        
    data = {
        'GrLivArea': area_for_model, 
        'BedroomAbvGr': bedrooms,
        'FullBath': bathrooms,
        'YearBuilt': year_built
    }
    features = pd.DataFrame(data, index=[0])
    return features, area_display, bedrooms, bathrooms, year_built, unit_choice

input_df, area, bedrooms, bathrooms, year_built, unit_choice = user_input_features()

# ==========================================
# 3. HIỂN THỊ THÔNG SỐ 
# ==========================================
col1, col2, col3, col4 = st.columns(4)

# Thay đổi chữ m2 hoặc sq ft tùy theo người dùng chọn
if unit_choice == "Mét vuông (m²)":
    col1.metric(label="Diện tích mặt sàn", value=f"{area} m²")
else:
    col1.metric(label="Diện tích mặt sàn", value=f"{area} sq ft")
    
col2.metric(label="Số phòng ngủ", value=f"{bedrooms} Phòng")
col3.metric(label="Số phòng tắm", value=f"{bathrooms} Phòng")
col4.metric(label="Năm hoàn thiện", value=f"Năm {year_built}")

st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# 4. NÚT DỰ ĐOÁN & KẾT QUẢ
# ==========================================
if st.button("TIẾN HÀNH PHÂN TÍCH & ĐỊNH GIÁ", use_container_width=True):
    if 'model' in locals():
        with st.spinner('Hệ thống đang quét và phân tích dữ liệu thị trường...'):
            time.sleep(1.5) 
            prediction = model.predict(input_df)
            
            result_html = f"""
            <div class="result-box">
                <h3 style="color: #FFFFFF; font-weight: 300; letter-spacing: 2px;">GIÁ TRỊ ƯỚC TÍNH THỊ TRƯỜNG</h3>
                <div class="result-price">${int(prediction[0]):,}</div>
                <p style="color: #A0AAB5; font-style: italic; margin-top: 10px;">
                    ✓ Độ tin cậy cao | Thuật toán Machine Learning đã tự động quy đổi và xử lý dữ liệu nhà ở
                </p>
            </div>
            """
            st.markdown(result_html, unsafe_allow_html=True)
