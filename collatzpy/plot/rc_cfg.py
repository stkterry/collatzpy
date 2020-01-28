from matplotlib import cycler

colors_temp = cycler('color',
                ['#EE6666', '#3388BB', '#9988DD',
                 '#EECC55', '#88BB44', '#FFBBBB'])

rc_cfg = {
  'axes': {'facecolor': '#E6E6E6', 'edgecolor': 'none',
            'axisbelow': True, 'grid': True, 'prop_cycle': colors_temp},
  'grid': {'color': 'w', 'linestyle': 'solid'},
  # 'axes.grid': {'which': 'minor'},
  'xtick': {'direction': 'out', 'labelsize': 10},
  'ytick': {'direction': 'out', 'labelsize': 10},
  'xtick.minor': {'visible': True},
  'ytick.minor': {'visible': True},
  'patch': {'edgecolor': '#E6E6E6',},
  'lines': {'linewidth': 2},
  'font': {'family': 'serif', 'weight': 'normal', 'size': 12},
  'figure': {'figsize': [12, 6]},
  'legend': {'fontsize': 10}
}

def set_config(plt):
  for key, cfg in rc_cfg.items():
    plt.rc(key, **cfg)
