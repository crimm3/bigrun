import streamlit as st
import numpy as np
from scipy.stats import norm

st.title('ビッグラン上位パーセント')
kinikura = st.text_input('金イクラの数')

if st.button('計算'):
  your_percent = norm.cdf(int(kinikura), loc=88, scale=29.75)
  st.write('あなたは上位:{}'.format(your_percent))
  st.write('偏差値:{}'.format((int(kinikura) - 88)/29.75*10)+50)
