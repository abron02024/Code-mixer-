#Any use and editing of the code without permission will be prosecuted 
import os
import sys
import random
import time
import pyfiglet

pl  = "\033[32m","\033[31m","\033[36m", "\033[35m", "\033[93m", "\033[34m"

#....

r= "\033[31m"
g = "\033[32m"
y= "\033[33m"
u = "\033[35m"
i = "\033[93m"
o = "\033[34m"
lrd = '\033[01;32m'
cn = '\033[00;36m'
pe = '\033[01;35m'
b= "\033[94m"
w='\033[1;37m'
pk='\033[1;101m'

mi =[f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⣶⣶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⢶⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡿⠿⣿⠀⠀⠀⠀⣿⠿⢿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀
⠀⢠⣾⣿⣿⣿⣿⣿⡿⠋⣠⣴⣿⣷⣤⣤⣾⣿⣦⣄⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⣼⣿⣿⣿⣿⣿⡏⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢹⣿⣿⣿⣿⣿⣧⠀
⢰⣿⣿⣿⣿⣿⡿⠀⣾⣿⣿⣿⣿⠟⠉⠉⠻⣿⣿⣿⣿⣷⠀⢿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣇⣰⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣆⣸⣿⣿⣿⣿⣿⡇
⠸⣿⣿⣿⡿⣿⠟⠋⠙⠻⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⣿⠛⠙⠻⣿⣿⣿⣿⣿⠇
⠀⢻⣿⣿⣧⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⡟⠀
⠀⠘⢿⣿⣿⣷⣦⣤⣴⣾⠛⠻⢿⣿⣿⣿⣿⡿⠟⠋⣿⣦⣤⠀⣰⣿⣿⡿⠃⠀
⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⣈⣁⣠⣤⣶⣾⣿⣿⣷⣾⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⠿⠿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
""","""

⠀⠀⡇⠀⠀⠀⠀⢀⣴⣿⡿⠿⢿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣇
⠀⠉⡏⠁⠀⠀⣴⣿⡿⠋⢙⡆⢀⣧⠀⠉⠛⢿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠘⠀
⠀⠀⠀⠀⠀⣼⣿⢛⣁⡴⣋⣴⣿⣿⣷⣄⣀⠀⠈⣻⣿⣿⣿⣶⣶⣶⣶⣤⡀⠀
⠀⠀⠀⠀⢰⣿⣿⠏⣹⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠉⠻⣿⡄
⠀⠀⠀⢠⣾⣿⣟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢻⣿
⠀⢀⣴⣿⣿⡿⠋⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢸⣿
⣠⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⠉⢹⣿⣦⡀⠀⠀⣀⣾⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⣿⣿⣷⣿⣿⠟⠀
⢿⣿⣆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⢀⣼⣿⣿⣿⠿⠋⠀⠀
⠈⠻⣿⣶⣍⣻⣿⣿⣿⣿⠿⠛⠛⠛⢿⣿⣿⣿⣿⣶⣶⣿⣿⡿⠛⠁⠀⠀⡀⠀
⠀⠀⠈⠙⠻⢿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣼⡿⠿⢿⡿⠛⠋⠁⠀⠀⠀⠀⠀⠈⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢹⣿⡆⠀⠀⠀⢸⣿⠀⠀⠀⠀⣀⣆⡄⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣀⠀⠀⠀⠀⠀⢸⣿⠀⠀⡠⠄⢸⣿⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⢾⣇⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣦⣤⣴⡿⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠄
""","""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠒⠒⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣶⡾⠿⠿⠿⠿⣿⣿⣶⣦⣄⠙⠷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣠⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣷⣄⠘⢿⡄⠀⠀⠀
⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠠⢄⡀⠈⢿⣿⣧⠈⢿⡄⠀⠀
⢀⠏⠀⠀⠀⢀⠄⣀⣴⣾⠿⠛⠛⠛⠷⣦⡙⢦⠀⢻⣿⡆⠘⡇⠀⠀
⠀⠀⠀⠀⡐⢁⣴⡿⠋⢀⠠⣠⠤⠒⠲⡜⣧⢸⠄⢸⣿⡇⠀⡇⠀⠀
⠀⠀⠀⡼⠀⣾⡿⠁⣠⢃⡞⢁⢔⣆⠔⣰⠏⡼⠀⣸⣿⠃⢸⠃⠀⠀
⠀⠀⢰⡇⢸⣿⡇⠀⡇⢸⡇⣇⣀⣠⠔⠫⠊⠀⣰⣿⠏⡠⠃⠀⠀⢀
⠀⠀⢸⡇⠸⣿⣷⠀⢳⡈⢿⣦⣀⣀⣀⣠⣴⣾⠟⠁⠀⠀⠀⠀⢀⡎
⠀⠀⠘⣷⠀⢻⣿⣧⠀⠙⠢⠌⢉⣛⠛⠋⠉⠀⠀⠀⠀⠀⠀⣠⠎⠀
⠀⠀⠀⠹⣧⡀⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠃⠀⠀
⠀⠀⠀⠀⠈⠻⣤⡈⠻⢿⣿⣷⣦⣤⣤⣤⣤⣤⣴⡾⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠶⢤⣈⣉⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""","""

⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀ ⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀ ⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀
⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆
⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟
⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀
⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀
  ⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀ ⠀⠀⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀ ⠀⠀⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀ ⠀⠀⠙⠛⠛⠛⠋⠁⠀⠙⠻⠿⠟⠋⠑⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""","""
    ⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⢤⡿⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡿⠀⠀⠀⢬⡱⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣷⠀⠀⠀⠀⠙⣦⠙⠦⠤⠴⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣧⠀⠀⠀⠀⠘⣿⠓⠶⣄⡈⣻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡤⣿⣷⠀⠀⠀⠀⣻⣄⡀⠀⠁⣬⡟⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢧⣈⠉⡀⠀⠀⠀⡈⠻⣿⣿⣇⠈⡇⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⢿⡆⠀⠀⣼⠀⢹⡙⢿⣆⠀⢻⣿⣻⣿⣿⢿⣿⡶⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡾⡄⣰⣿⡆⠀⠙⣦⠹⡆⠰⣿⠛⢿⣿⣞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢐⣿⠇⣟⠋⢸⣿⣼⠀⣿⣷⣼⡹⣾⡆⠈⢿⣿⣛⣒⠂⠀⠀⠀⠀
⠀⠀⠀⣚⣻⣿⣶⣿⠀⠈⡛⢿⡀⢸⣿⢛⣿⣿⢹⠀⠀⠉⠛⢻⡿⠁⠀⠀⠀
⣀⣀⣉⣩⣿⣿⣿⠋⠀⠀⡇⠈⢓⠏⠏⡀⢸⠇⢈⣷⣄⠀⢲⣸⠀⠀⠀⠀⠀
⢀⠉⠛⣛⣛⡛⠁⠀⠀⣾⠃⠀⣸⠇⣠⡇⢠⡀⠈⢿⡻⣦⠈⢻⣦⣀⡀⠀⠀
⠈⠙⠛⣿⣶⡾⠛⣡⣾⡟⢠⣾⣿⣿⣟⡤⠀⣷⡀⢨⣿⣽⡄⢀⣿⣿⣿⠇⠀
⠀⢠⣾⡟⢁⣴⡿⠹⠋⡰⣿⣿⣿⣿⡟⠀⢀⣿⣇⣼⣿⡿⡇⠞⣿⣿⣧⣤⡤
⠀⢠⡾⠚⣿⡟⢀⣴⠏⣸⣿⣿⣿⣿⣧⢰⣿⣿⡿⢻⠉⠀⡔⢶⣽⣿⠿⠥⠀
⠀⠈⠀⢸⠟⣠⡾⠏⠀⡿⢹⣿⣿⣿⣿⣿⣿⣿⣶⣿⣶⣾⣿⣮⣍⠉⠙⢲⠄
⠀⠀⠀⠘⠉⠁⠀⠀⢸⠁⠘⣿⡿⠻⣿⡿⣿⣿⣿⣿⣿⣿⡏⢻⣛⠛⠒⠛⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⠈⢻⡄⠹⣿⣿⡇⠙⢷⡈⢿⡟⠒⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⠀⣿⣿⠃⠀⠀⠀⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠈⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""","""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠻⣥⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⡿⠻⣆⠙⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠁⠀⠘⣆⡔⢶⣆⠉⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⡿⢿⡀⠉⠀⠞⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⡄⠀⡇⠘⣧⣀⣀⣀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠁⢀⣠⠞⣹⢿⠻⡟⢿⣿⣯⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠃⠶⠒⠉⠁⣴⠇⢸⡇⡟⡷⢬⡙⠎⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠇⢀⣠⣄⡀⠚⠁⠀⠈⠀⠀⣷⠀⠉⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣽⣿⣶⠋⢉⡿⠇⠀⠀⠀⠀⠀⣰⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣿⣿⠇⠀⣠⣥⣤⡀⠀⠀⠀⢀⡟⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣿⢀⣾⡟⠉⢹⡇⠀⠀⠀⢸⠁⡿⠙⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⣇⣾⡟⠀⠸⡏⣄⡀⠀⠀⢹⢀⡇⢀⢘⢿⣮⡙⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣇⠀⡀⣧⠰⣿⣶⣄⠀⠀⠀⠘⣎⠳⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⣿⣆⠹⣿⡐⣾⣷⣹⣆⠀⠀⠀⠘⢷⣄⣻⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣦⠽⣇⣹⣟⢿⠙⠁⠀⠀⠀⣤⠉⠻⣿⣿⣿⣿⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠙⡟⠂⣿⢹⡿⣼⠇⠀⠀⣀⠀⣷⡀⠀⠈⠻⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⢻⠀⠉⢸⡇⠈⣀⣠⣾⠇⠀⠻⣿⣦⣤⣴⣿⠿⣿⡿⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⡀⠀⢸⠁⣰⠛⣽⡧⠖⠻⢿⡆⠈⠉⠉⠀⠀⢻⣷⠹⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠘⡇⠀⢸⢰⡏⢰⡟⠀⣀⣀⡼⠃⠀⢀⡆⠀⠀⠘⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣿⣶⣷⣶⣾⣿⣧⣾⣤⣄⣀⣀⣤⣤⣶⡿⠀⠀⠀⢠⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣟⡛⠛⠛⠉⠉⠉⠉⢉⣭⣽⡿⠿⠿⠿⠛⠛⠛⠓⠲⠦⠄⣼⢻⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢉⣼⣿⣿⠿⠛⠛⠁⠀⠀⣠⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⣸⡇⠀
⠀⠀⠀⠀⠀⢀⣴⠿⠛⠁⢀⣀⣀⣀⣀⣀⣄⡀⠀⠀⠀⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⣰⣿⠁⠀
⠀⠀⠀⢀⣴⣟⣥⣶⣾⣿⣿⣿⣿⣿⣿⣭⣤⣤⣤⣀⣀⡀⠈⠛⠶⢶⣶⣶⣶⣾⣿⣿⣿⠟⠁⠀⠀
⠀⢀⣴⡿⠟⠋⡽⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠛⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀
⠐⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""","""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠟⠋⠉⠉⠉⠛⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⢰⣶⣶⣦⡀⠈⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣄⡈⠉⣻⣿⣷⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⡿⠃⠀⣼⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⢀⣠⣾⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣶⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⢀⣀⣀⣀⠀⠀⠀⠀
⠀⣴⣿⣿⠋⠁⠀⣀⡀⠀⠙⢿⣿⣿⣿⣿⡟⠁⢀⣴⣿⣿⣿⣿⣿⣶⡄⠀
⢸⣿⣿⠁⠀⣴⣿⣿⣿⣷⣄⠀⢹⣿⣿⡟⠀⢀⣿⣿⡟⠁⡀⠈⠙⣿⣿⡆
⢸⣿⣿⠀⠘⣿⣿⡅⠙⣿⣿⡀⠀⢿⣿⣇⠀⠘⣿⣿⣷⣿⣿⠇⠀⣿⣿⡇
⠘⣿⣿⣆⠀⠉⠋⠁⣠⣿⣿⠃⠀⠘⣿⣿⣦⡀⠈⠛⠛⠛⠁⠀⣰⣿⣿⠃
⠀⠘⢿⣿⣿⣶⣶⣾⣿⡿⠋⠀⠀⠀⠈⠻⣿⣿⣶⣤⣤⣤⣴⣾⣿⡿⠃⠀
⠀⠀⠀⠈⠙⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠿⠿⠟⠛⠉⠀⠀⠀
""","""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⠖⠀⠀⠲⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣇⣤⠶⠛⣛⣉⣙⡛⠛⢶⣄⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣿⣿⣿⡟⢁⣴⣿⣿⣿⣿⣿⣿⣦⡈⢿⣿⣿⣿⣀⡀⠀⠀⠀⠀
⠀⠀⢠⣴⣿⣿⣿⣿⡟⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢿⣿⣿⣿⣿⣦⡄⠀⠀
⠀⣴⣿⣿⡿⠿⢛⣻⡇⢸⡟⠻⣿⣿⣿⣿⣿⡿⠟⢻⡇⣸⣛⡛⠿⣿⣿⣿⣦⠀
⢸⣿⡿⠋⠀⠀⢸⣿⣿⡜⢧⣄⣀⣉⡿⣿⣉⣀⣠⣼⢁⣿⣿⡇⠀⠀⠙⢿⣿⡆
⣿⣿⠁⠀⠀⠀⠈⣿⣿⡇⣿⡿⠛⣿⣵⣮⣿⡟⢻⡿⢨⣿⣿⠀⠀⠀⠀⠈⣿⣿
⢿⡟⠀⠀⠀⠀⠀⠘⣿⣷⣤⣄⡀⣿⣿⣿⣿⢁⣤⣶⣿⣿⠃⠀⠀⠀⠀⠀⣿⡟
⠘⠇⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⢿⣿⣿⣿⢸⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠻⠃
⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⢩⣦⣘⡘⠋⣛⣸⡍⠁⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠘⢿⣷⣤⣤⣄⣤⣤⣶⣿⣿⣿⡿⢿⣿⣿⣿⣷⣤⣤⣠⣤⣴⣾⡿⠁⠀⠀
⠀⠀⠀⠀⠉⠛⠿⠿⠿⡿⠿⠿⠛⠉⠀⠀⠉⠛⠿⠿⣿⠿⠿⠿⠛⠉⠀⠀⠀⠀

""","""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣷⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⣴⣆⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣷⡀⠀⠀
⠀⢠⣾⣿⣿⣿⣿⣿⡏⠀⠀⠀⢠⣾⣿⣿⣷⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⠆⠀
⠀⠀⠉⠻⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⣿⣿⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠙⢿⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⡿⠋⠀⠀⠀⠀
⠠⣄⡀⠀⠀⣿⣿⣿⡀⠀⠀⠀⠀⠈⠻⠟⠀⠀⠀⠀⠀⢠⣿⣿⡇⠀⠀⢀⣠⠖
⠀⠹⣿⣷⣶⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⠏⠀
⠀⠀⠘⢿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠈⠋⠁⠀⠀⠈⠻⣷⡀⠀⠀⠀⠀⠀⠀⢠⣿⠏⠁⠀⠀⠈⠙⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⢀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣴⣿⣿⠀⠀⠀⠀⣿⣿⣦⣤⡴⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠀⠀⠀⠀⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠀⠀⠀⠹⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""]

print(f"{r}")
banner = (random.choice(mi))

#
#
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.005)
print("\033[32m")
print(pyfiglet.figlet_format("filtring",font='epic'))
print("\033[31m")
print(pyfiglet.figlet_format("Mr abron",font='epic'))
print("\033[33m")
print(pyfiglet.figlet_format(" mixer",font='epic'))
print("\033[34m")
print(pyfiglet.figlet_format("code ",font='epic'))

algoritm =input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your algoritm code\033[31m_-_\033[31m❯❯❯\033[32m")

virus=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your virus code \033[31m_-_\033[31m❯❯❯\033[32m")

tor =input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your  tor code\033[31m_-_\033[31m❯❯❯\033[32m")

di_escript=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your di escript code \033[31m_-_\033[31m ❯❯❯\033[32m")

cd_seror=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your seror code \033[31m_-_\033[31m ❯❯❯\033[32m")

site_mokharb=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter site mokharb code \033[31m_-_\033[31m❯❯❯\033[32m")

ip =input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your ip rubika code \033[31m_-_\033[31m❯❯❯\033[32m")

id_targt=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your id targt code \033[31m_-_\033[31m ❯❯❯\033[32m")

id_support=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your id support code \033[31m_-_\033[31m❯❯❯\033[32m")

cd_dsti=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32m Enter your dsti code \033[31m_-_\033[31m❯❯❯\033[32m")

link_xxx=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your link xxx code \033[31m_-_\033[31m❯❯❯\033[32m")

goid=input(f"\033[33m[\033[31m<\033[32#\033[33m>\033[33m]\033[31m_-_\033[32mEnter your goid code \033[31m_-_\033[31m❯❯❯\033[32m")

asd =(f"\033[31m{algoritm}\n \033[32m{virus}\n \033[33m{tor}\n \033[34m{di_escript}\n \033[35m{cd_seror}\n \033[36m{site_mokharb}\n \033[01;32m{ip}\n \033[01;36m{id_targt}\n \033[01;35m{id_support}\n '\033[1;32m{cd_dsti}\n '\033[1;33m{link_xxx}\n '\033[1;32m{goid}\n \n ")

code_1 =(f"""\033[31m{cd_seror}fil.fil.fil.rubika.3.1.1({virus})/{site_mokharb}algoritm{ip}[https://www.cyber-diplomacy-toolbox.com{link_xxx}[http://dscript-hazrat-285-92-pantrex-hacker-yftt15l.gigfa.com/sex.admins.rubika.html]{goid}[Gif.sxs.github.com/yftt15k/yftt-filter-rubika.hackers68628-arn-ytff10k/]{id_support}{cd_dsti}(http://10.10.34.36)({di_escript})filtring({tor})account.Fil.3.1.1=Rubika.fil""")

bnr= (f"""\033[31m
⠀⠀⠀⠀⠀⠀⠀⣰⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠃⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠸⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⡇⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⢸⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⡿⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⢿⡆⠀⠀⠀⠀
⠀⠀⠀⢀⣾⡇⠀⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⢸⣿⡀⠀⠀⠀
⠀⠀⠀⢸⣿⠁⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠈⣿⣇⠀⠀⠀
⠀⠀⢀⣿⡟⠀⠀⢿⣿⣶⠶⠶⠶⠶⢾⣦⡀⡴⢀⣀⣦⢀⣴⡷⠶⠶⠶⠶⣶⣿⡿⠀⠀⢹⣿⡀⠀⠀
⠀⠀⢸⣿⡇⠀⠀⣀⣉⣤⣴⣶⣶⣶⣶⣽⣿⣿⣿⣿⣿⣿⣯⣶⣶⣶⣶⣦⣤⣉⣀⠀⠀⢸⣿⡇⠀⠀
⠀⠀⠸⢿⣷⣶⠿⠟⠋⠉⠀⣠⣄⣤⣭⣿⣿⣿⣿⣿⣿⡿⣿⣭⣥⣠⣄⠀⠉⠉⠻⠿⣷⣾⡿⠇⠀⠀
⠀⠀⠀⠀⠉⠁⠀⠀⢀⣠⣾⡿⠟⢋⣹⣿⢿⣿⣿⣿⣿⡿⣿⣯⡙⠻⠿⣷⣄⡀⠀⠀⠈⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠾⠋⠁⣠⣴⡾⠋⠁⣾⣿⣿⣿⣿⣷⠈⠙⢿⣦⣄⠈⠙⠷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣶⠟⠁⠀⠀⠀⣿⣿⠁⠀⢰⣿⣿⣿⣿⣿⣿⡆⠀⠈⣿⣿⠀⠀⠀⠉⠻⣶⣄⡀⠀⠀⠀
⢰⣤⣶⣿⠟⠁⠀⠀⠀⠀⠀⣿⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⠁⠀⠀⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣶⣤⡆
⢸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⡏⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇
⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠈⢿⣿⣿⡿⠁⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀
⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀
⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⠇⠀⠀⠀⠀⠀⠀⠀⣸⡏⠀⠀
⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀
⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀
⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ """)
os.system("clear")
print ()

def slow_print(Str):
    for char in Str:
        print(char, end='', flush=True)
        time.sleep(0.03)
def clear():
    system('' if name == 'posix' else 'cls')
    
slow_print (f"{bnr}\n \n {asd}\n \n {code_1}")

