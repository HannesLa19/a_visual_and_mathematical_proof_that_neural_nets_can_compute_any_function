
import inspect
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import seaborn as sns
import streamlit as st

from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

import plot_fcts as pf

def main():
    st.write('''
        # The visual (and mathematical) proof that a neuronal network can solve any function
        ''')

    welcome_text = '''
        ## Welcome.
        '''

    st.sidebar.title('What to do')
    app_mode = st.sidebar.selectbox('Choose the app mode',
        ['Welcome page', 'Run the app'])
    if app_mode == 'Welcome page':
        st.write(welcome_text)
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == 'Run the app':
        run_the_app()

def plot(plot_fct, *kwargs):
    fig, ax = plt.subplots(figsize=(8, 6))
    plot_fct(ax, *kwargs)
    return( fig )

def run_the_app():

    ## sidebar

    ## main page


    st.write(r'''
        ## Sigmoid function in one dimension
        $$\sigma(z)
        =
        \frac{1}{1+e^{-z}}
        $$
        ''')

    w_plot_sigmoid = st.slider("Weight: ", -100, 100, 1)
    b_plot_sigmoid = st.slider("Bias: ", -100, 100, 0)

    st.pyplot(plot(pf.plot_sigmoid,
        b_plot_sigmoid,
        w_plot_sigmoid))


    st.write(r'''
        ## Two sigmoid functions in one dimension
        Free parameters: $$w$$ and $$b$$
        ''')

    w_plot_sigmoid_fct_1d_wb = []
    b_plot_sigmoid_fct_1d_wb = []
    w_plot_sigmoid_fct_1d_wb.append( st.slider("Weight0: ", -100, 100, 100) )
    b_plot_sigmoid_fct_1d_wb.append( st.slider("Bias0: ", -100, 100, -40) )
    w_plot_sigmoid_fct_1d_wb.append( st.slider("Weight1: ", -100, 100, -100) )
    b_plot_sigmoid_fct_1d_wb.append( st.slider("Bias1: ", -100, 100, 50) )

    st.pyplot(plot(pf.plot_sigmoid_fct_1d_wb,
        w_plot_sigmoid_fct_1d_wb,
        b_plot_sigmoid_fct_1d_wb))


    st.write(r'''
        ## Two sigmoid functions in one dimension
        Free parameters: $$s$$ and $$w_{\mathrm{out}}$$
        ''')

    s_plot_sigmoid_fct_s_wout_1d = []
    b_plot_sigmoid_fct_s_wout_1d = []
    s_plot_sigmoid_fct_s_wout_1d.append( st.slider(r"s0: ", 0., 1., 0.4) )
    b_plot_sigmoid_fct_s_wout_1d.append( st.slider(r"w0: ", -1., 1., 1.) )
    s_plot_sigmoid_fct_s_wout_1d.append( st.slider(r"s1: ", 0., 1., 0.6) )
    b_plot_sigmoid_fct_s_wout_1d.append( st.slider(r"w1: ", -1., 1., 0.5) )

    st.pyplot(plot(pf.plot_sigmoid_fct_s_wout_1d,
        s_plot_sigmoid_fct_s_wout_1d,
        b_plot_sigmoid_fct_s_wout_1d))


    st.write(r'''
        ## Two towers in one dimension
        Free parameters: $$s$$ and $$h$$
        ''')

    s_plot_sigmoid_fct_s_h_1d = []
    h_plot_sigmoid_fct_s_h_1d = []
    s_plot_sigmoid_fct_s_h_1d.append( st.slider(r"s0: ", 0., 1., 0.45) )
    s_plot_sigmoid_fct_s_h_1d.append( st.slider(r"s1: ", 0., 1., 0.55) )
    h_plot_sigmoid_fct_s_h_1d.append( st.slider(r"Height01: ", -1., 1., 1.) )
    s_plot_sigmoid_fct_s_h_1d.append( st.slider(r"s2: ", 0., 1., 0.75) )
    s_plot_sigmoid_fct_s_h_1d.append( st.slider(r"s3: ", 0., 1., 0.85) )
    h_plot_sigmoid_fct_s_h_1d.append( st.slider(r"Height23: ", -1., 1., 1.) )

    st.pyplot(plot(pf.plot_sigmoid_fct_s_h_1d,
        s_plot_sigmoid_fct_s_h_1d,
        h_plot_sigmoid_fct_s_h_1d))


    st.write(r'''
        ## Two sigmoid functions in two dimensions
        Free parameters: $$s$$ and $$w_{\mathrm{out}}$$
        ''')

    s_plot_sigmoid_fct_s_wout_2d = []
    w_plot_sigmoid_fct_s_wout_2d = []
    s_plot_sigmoid_fct_s_wout_2d.append( [st.slider(r"sx: ", 0., 1., 0.45)] )
    w_plot_sigmoid_fct_s_wout_2d.append( [st.slider(r"wx: ", -1., 1., 0.5)] )
    s_plot_sigmoid_fct_s_wout_2d.append( [st.slider(r"sy: ", 0., 1., 0.45)] )
    w_plot_sigmoid_fct_s_wout_2d.append( [st.slider(r"wy: ", -1., 1., 1.)] )

    st.pyplot(pf.plot_sigmoid_fct_s_wout_2d(s_plot_sigmoid_fct_s_wout_2d,
        w_plot_sigmoid_fct_s_wout_2d))


    st.write(r'''
        ## Four sigmoid functions in two dimensions
        Free parameters: $$s$$ and $$w_{\mathrm{out}}$$
        ''')

    s_plot_sigmoid_fct_s_wout_2d = [[0.6, 0.7], [0.4, 0.5]]
    w_plot_sigmoid_fct_s_wout_2d = []
    w_plot_sigmoid_fct_s_wout_2d.append( [st.slider(r"w0x: ", -1., 1., 0.8),
        st.slider(r"w1x: ", -1., 1., -0.8)] )
    w_plot_sigmoid_fct_s_wout_2d.append( [st.slider(r"w0y: ", -1., 1., 0.1),
        st.slider(r"w1y: ", -1., 1., -0.1)] )

    st.pyplot(pf.plot_sigmoid_fct_s_wout_2d(s_plot_sigmoid_fct_s_wout_2d,
        w_plot_sigmoid_fct_s_wout_2d))


    st.write(r'''
        ## Four sigmoid functions in two dimensions
        Free parameters: $$s$$ and $$h$$
        ''')

    s_plot_sigmoid_fct_h_2d = [[[0.45, 0.55]], [[0.45, 0.55]]]
    h_plot_sigmoid_fct_h_2d = []
    h_plot_sigmoid_fct_h_2d.append( [st.slider(r"hx: ", -1., 1., 1.)] )
    h_plot_sigmoid_fct_h_2d.append( [st.slider(r"hy: ", -1., 1., 1.)] )

    st.pyplot(pf.plot_sigmoid_fct_h_2d(s_plot_sigmoid_fct_h_2d,
        h_plot_sigmoid_fct_h_2d))


    st.write(r'''
        ## One tower in two dimensions
        Free parameters: $$h$$ and $$b_{\mathrm{out}}$$
        ''')

    s_plot_sigmoid_fct_h_wout_b_2d = [[[0.45, 0.55]], [[0.45, 0.55]]]
    h_plot_sigmoid_fct_h_wout_b_2d = []
    h_plot_sigmoid_fct_h_wout_b_2d.append( [st.slider(r"hx: ", -50., 50., 10.)] )
    h_plot_sigmoid_fct_h_wout_b_2d.append( [st.slider(r"hy: ", -50., 50., 10.)] )
    b_plot_sigmoid_fct_h_wout_b_2d = st.slider(r"b: ", -50., 50., -15.)

    st.pyplot(pf.plot_sigmoid_fct_h_wout_b_2d(s_plot_sigmoid_fct_h_wout_b_2d,
        h_plot_sigmoid_fct_h_wout_b_2d,
        b_plot_sigmoid_fct_h_wout_b_2d))


    st.write(r'''
        ## Two towers in two dimensions
        Free parameters: $$w_{\mathrm{out}}$$
        ''')

    s_plot_sigmoid_fct_towers_bout_2d = [[[[0.8, 0.9]], [[0.3, 0.4]]], [[[0.1, 0.2]], [[0.7, 0.8]]]]
    w_plot_sigmoid_fct_towers_bout_2d = []
    w_plot_sigmoid_fct_towers_bout_2d.append( st.slider(r"w0: ", 0., 1., 0.9) )
    w_plot_sigmoid_fct_towers_bout_2d.append( st.slider(r"w1: ", 0., 1., 0.5) )

    st.pyplot(pf.plot_sigmoid_fct_towers_bout_2d(s_plot_sigmoid_fct_towers_bout_2d,
        w_plot_sigmoid_fct_towers_bout_2d))


    st.write(r'''
        ## Optional activation function
        $$\tilde{\sigma}(z)
        =
        \frac{1}{1+e^{-z}} + 0.2 \exp\left(-\frac{z^2}{4}\right) \sin\left(5z\right)
        $$
        ''')

    w_plot_optional_activation = st.slider("Weight optional activation function: ", -100, 100, 1)
    b_plot_optional_activation = st.slider("Bias optional activation function: ", -100, 100, 0)

    st.pyplot(plot(pf.plot_optional_activation,
        b_plot_optional_activation,
        w_plot_optional_activation))



if __name__ == '__main__':
    main()
