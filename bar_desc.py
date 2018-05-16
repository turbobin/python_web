# -*- coding: utf-8 -*-
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

my_style = LS('#333366',base_style=LCS)
charts = pygal.Bar(style=my_style,x_lable_rotation=45,show_legend=False)

charts.title = 'Python Project'
charts.x_labels = ['awesome-python','youtube-dl']

plot_dicts = [
    {'value':48769,'lable':'Description of awesome-python'},
    {'value':36130,'lable':'Description of youtube-dl'}
    ]

charts.add('',plot_dicts)
charts.render_to_file('bar_desc.svg')