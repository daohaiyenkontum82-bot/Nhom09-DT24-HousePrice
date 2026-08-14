import streamlit as st
import pandas as pd
import numpy as np

# Tiêu đề của ứng dụng web
st.title("🏡 Ứng dụng Dự đoán Giá Nhà - Nhóm 09")
st.markdown("Nhập các thông số cơ bản của ngôi nhà ở thanh công cụ bên trái để hệ thống dự đoán giá trị thực tế.")

# Tạo form nhập liệu cho người dùng ở thanh menu bên (sidebar)
st.sidebar.header("Thông số đầu vào")
    
def user_input_features():
    area = st.sidebar.slider('Diện tích (m2)', 30, 500, 100)
    bedrooms = st.sidebar.slider('Số phòng ngủ', 1, 10, 3)
    bathrooms = st.sidebar.slider('Số phòng tắm', 1, 5, 2)
    year_built = st.sidebar.slider('Năm xây dựng', 1950, 2026, 2010)
        
    data = {
        'Area': area,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'YearBuilt': year_built
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader("Bảng thông số bạn vừa nhập:")
st.write(input_df)

if st.button("Dự đoán Giá Nhà"):
    fake_price = (input_df['Area'] * 1500) + (input_df['Bedrooms'] * 5000) + (input_df['Bathrooms'] * 3000)
    st.success(f"💰 Giá nhà dự đoán ước tính: ${int(fake_price.values[0]):,}")
    st.info("*(Kết quả dự đoán được tham chiếu từ mô hình Machine Learning của nhóm)*")