import random
import streamlit as st

def generate_captcha():
    numbers = random.sample(range(10), 5)
    captcha = ''.join(map(str, numbers))
    return captcha

def check_captcha(input_captcha, generated_captcha):
    return input_captcha == generated_captcha
