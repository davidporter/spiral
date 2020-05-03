import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as mpe
import pandas as pd
# styling
LINEWIDTH=4
EDGEWIDTH=.5
CAPSTYLE="projecting"
COLORMAP="viridis_r"
ALPHA=1
FIRSTDAY=6 # 0=Mon, 6=Sun

# load dataset and parse timestamps

# df = pd.read_csv('Trips.csv')
# df[['trip_start', 'trip_stop']] = df[['trip_start', 'trip_stop']].apply(pd.to_datetime)
N = 200
df = pd.DataFrame()
df["start"] = np.random.uniform(0, 10, size=N)
df["stop"] = df["start"] + np.random.choice([np.random.uniform(0, 0.1),
                                             np.random.uniform(1., 2.)], p=[0.98, 0.02], size=N)
df["dist"] = np.random.random(size=N)

# set origin at the first FIRSTDAY before the first trip, midnight

# first_trip = df['trip_start'].min()
# origin = (first_trip - pd.to_timedelta(first_trip.weekday() - FIRSTDAY, unit='d')).replace(hour=0, minute=0, second=0)
# weekdays = pd.date_range(origin, origin + np.timedelta64(1, 'W')).strftime("%a").tolist()

# # convert trip timestamps to week fractions
# df['start'] = (df['trip_start'] - origin) / np.timedelta64(1, 'W')
# df['stop']  = (df['trip_stop']  - origin) / np.timedelta64(1, 'W')

# sort dataset so shortest trips are plotted last
# should prevent longer events to cover shorter ones, still suboptimal
df = df.sort_values('dist', ascending=False).reset_index()
fig = plt.figure(figsize=(8, 6))
ax = fig.gca(projection="polar")

for idx, event in df.iterrows():

    # sample normalized distance from colormap
    ndist = event['dist'] / df['dist'].max()
    color = plt.cm.get_cmap(COLORMAP)(ndist)
    tstart, tstop = event.loc[['start', 'stop']]
    # timestamps are in week fractions, 2pi is one week

    nsamples = int(1000. * (tstop - tstart))
    t = np.linspace(tstart, tstop, nsamples)
    theta = 2 * np.pi * t
    arc, = ax.plot(theta, t, lw=LINEWIDTH, color=color, solid_capstyle=CAPSTYLE, alpha=ALPHA)
    if EDGEWIDTH > 0:
        arc.set_path_effects([mpe.Stroke(linewidth=LINEWIDTH+EDGEWIDTH, foreground='black'), mpe.Normal()])

# grid and labels
ax.set_rticks([])
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_xticks(np.linspace(0, 2*np.pi, 7, endpoint=False))
# ax.set_xticklabels(weekdays)
ax.tick_params('x', pad=2)
ax.grid(True)

# setup a custom colorbar, everything's always a bit tricky with mpl colorbars
vmin = df['dist'].min()
vmax = df['dist'].max()
norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
sm = plt.cm.ScalarMappable(cmap=COLORMAP, norm=norm)
sm.set_array([])
plt.colorbar(sm, ticks=np.linspace(vmin, vmax, 10), fraction=0.04, aspect=60, pad=0.1, label="distance", ax=ax)
plt.savefig("spiral.png", pad_inches=0, bbox_inches="tight")
plt.show()
#https://stackoverflow.com/questions/46575723/creating-a-temporal-range-time-series-spiral-plot


