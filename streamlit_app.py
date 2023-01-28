import streamlit as st
import numpy as np
from scipy.stats import norm

st.title('ビッグラン上位パーセント')
kinikura = st.text_input('金イクラの数を入力してください')
mean = 88
stdev = 29.75
if st.button('計算'):
  your_percent = norm.cdf(int(kinikura), loc=mean, scale=stdev)
  if 1 - your_percent >= 0.05:
    
    st.write(
            '<span style="color:red;background:pink">あなたは上位:{} %</span>'.format(round((1 - your_percent) * 100, 2)),
              unsafe_allow_html=True)
    deviation_value = ((int(kinikura) - mean) / stdev * 10) + 50
    st.write('偏差値:{}'.format(round(deviation_value), 2))
   else:
    st.write('あなたは上位:{}'.format(round((1 - your_percent) * 100, 2)) + ' %')
    deviation_value = ((int(kinikura) - mean) / stdev * 10) + 50
    st.write('偏差値:{}'.format(round(deviation_value), 2))
