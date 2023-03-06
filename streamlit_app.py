import streamlit as st
import numpy as np
from scipy.stats import norm
import logging

@st.cache_data
def calc_percent(kinikura, mean, stdev):
  return norm.cdf(kinikura, loc=mean, scale=stdev)

@st.cache_data
def calc_standard_score(kinikura, mean, stdev):
  return ((kinikura - mean) / stdev * 10) + 50

st.title('ビッグラン偏差値計算')
kinikura = st.number_input('金イクラの数を入力してください', value=100, step=1)
mean = 90
stdev = 31.8
# 第1回
# mean = 88
# stdev = 29.75
if st.button('計算'):
  your_percent = calc_percent(int(kinikura), mean, stdev)
  logging.info(str(kinikura))
  st.write('あなたは上位:{}'.format(int(round((1 - your_percent) * 100, 0))) + ' %')
  standard_score = calc_standard_score(int(kinikura), mean, stdev)
  st.write('偏差値:{}'.format(round(standard_score), 2))

st.write('')  
st.write('')
st.write('現在、第2回ビッグランに対応')
st.write('※公式発表のボーダー値をもとに算出した推定値のため、実際の値とは異なる場合がございます。')
st.write('')
st.write('参考値:')
st.write('141個 -> 上位5% 偏差値66')
st.write('117個 -> 上位20% 偏差値58')
st.write('90個 -> 上位50% 偏差値50')
# st.write('参考値 137個 -> 上位5% 偏差値66, 113個 -> 上位20% 偏差値58, 88個 -> 上位50% 偏差値50')
