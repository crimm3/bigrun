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
mean = 88
stdev = 29.75
if st.button('計算'):
  your_percent = calc_percent(int(kinikura), mean, stdev)
  logging.info(str(kinikura))
  st.write('あなたは上位:{}'.format(round((1 - your_percent) * 100, 1)) + ' %')
  standard_score = calc_standard_score(int(kinikura), mean, stdev)
  st.write('偏差値:{}'.format(round(standard_score), 2))

st.write('')  
st.write('')
st.write('現在、第1回ビッグランに対応')
st.write('参考値 137個 -> 上位5.0% 偏差値66, 88個 -> 上位50.0% 偏差値50')
st.write('第2回分は結果発表後に対応予定')
st.write('※公式発表のボーダー値をもとに算出した推定値のため、実際の値とは異なる場合がございます。')