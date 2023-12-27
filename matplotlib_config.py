import matplotlib.pyplot as plt

# 设置 PRL 风格参数
params = {
    'font.family': 'sans-serif',    # sans-serif/serif/cursive/fantasy/monospace
    'font.serif': ['Times New Roman', 'Times', 'Palatino', 'serif'], 
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans', 'sans-serif'], 
    'mathtext.fontset': 'stix',         # stix/'cm' (Computer Modern)
    'font.size': 10,                    # medium/large/small
    'font.style': 'normal',             # normal/italic/oblique
    'font.weight': 'normal',            # normal/bold
    'axes.unicode_minus': False,        

    'axes.labelsize': 15,
    'axes.titlesize': 15,
    'xtick.labelsize': 15,
    'ytick.labelsize': 15,
    'legend.fontsize': 15,

    'figure.facecolor': 'white',        
    'figure.figsize': [4, 3],
    'axes.linewidth': 1,              

    'xtick.direction': 'out',            
    'ytick.direction': 'out',
    'xtick.major.size': 3,              
    'ytick.major.size': 3,
    'xtick.minor.size': 2,
    'ytick.minor.size': 2,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.minor.width': 0.5,           
    'ytick.minor.width': 0.5,
    'xtick.major.pad': 2,               
    'ytick.major.pad': 2,
    'xtick.minor.pad': 2,
    'ytick.minor.pad': 2,

    'lines.linewidth': 1,               
    'lines.markersize': 3,

    'errorbar.capsize': 3,              
    'pdf.fonttype': 42                  
}

plt.rcParams.update(params)