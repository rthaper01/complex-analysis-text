# Matplotlib visualization for f(z) = exp(2π i/(z-1))
# Panels: original region -> vertical strip (1/(z-1)) -> horizontal strip (2π i·) -> half-plane (exp)
# Toggle want_lower=True to visualize the lower half-plane variant using u in (π,2π) (i.e., exp(+2π i w) with Re(w)>0).
# For the exact mapping f(z)=exp(2π i/(z-1)) on the given domain, the final image is the UPPER half-plane.

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

# ---- Config ----
want_lower = True  # Default to lower half-plane variant for the final exp map.

# Colors
fillA = (0.85, 0.92, 1.00)
fillB = (0.90, 1.00, 0.90)
fillC = (1.00, 0.95, 0.85)
fillD = (0.95, 0.90, 1.00)
lineBlue = (0.1, 0.3, 0.9)
lineRed = (0.85, 0.1, 0.1)
axisGray = (0.6, 0.6, 0.6)

fig, axs = plt.subplots(2, 2, figsize=(10, 10), dpi=160)

# Helper to draw axes with lines through origin
def draw_axes(ax, xmin, xmax, ymin, ymax, xlabel="Re", ylabel="Im"):
    ax.axhline(0, color=axisGray, lw=1)
    ax.axvline(0, color=axisGray, lw=1)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(False)

# ----------------- Panel A: z-plane, original region -----------------
ax = axs[0, 0]
draw_axes(ax, -1.6, 1.6, -1.6, 1.6)

# Fill big circle, then punch a hole with a white small circle
big = Circle((0.0, 0.0), 1.0, facecolor=fillA, edgecolor=lineBlue, lw=1.5)
small = Circle((0.5, 0.0), 0.5, facecolor="white", edgecolor=lineRed, lw=1.5)
ax.add_patch(big)
ax.add_patch(small)

ax.text(math.cos(2*math.pi/3), math.sin(2*math.pi/3), r"$|z|=1$", ha="left", va="bottom")
ax.text(0.25, 0.52, r"$|z-\frac{1}{2}|=\frac{1}{2}$", ha="center", va="bottom")
ax.text(-1.5, 1.4, "z-plane", color="black")

# ----------------- Panel B: w = 1/(z-1) -> vertical strip -----------------
ax = axs[0, 1]
draw_axes(ax, -2.2, 0.4, -3.0, 3.0, xlabel="Re w", ylabel="Im w")

# Boundaries map to vertical lines at Re(w)=-1 (from |z-1/2|=1/2) and Re(w)=-1/2 (from |z|=1)
x1, x2 = -1.0, -0.5
rect = Rectangle((x1, -3.0), (x2 - x1), 6.0, facecolor=fillB, edgecolor=None)
ax.add_patch(rect)
ax.plot([x1, x1], [-3.0, 3.0], color=lineRed, lw=1.5)
ax.plot([x2, x2], [-3.0, 3.0], color=lineBlue, lw=1.5)
ax.text(x1-0.05, 2.9, r"$\operatorname{Re}\,w=-1$", ha="right", va="top", color="black")
ax.text(x2+0.05, 2.3, r"$\operatorname{Re}\,w=-\frac{1}{2}$", ha="left", va="top", color="black")
ax.text(-2.1, 2.6, r"$w=\frac{1}{z-1}$")

# ----------------- Panel C: u = 2π i w -> horizontal strip -----------------
ax = axs[1, 0]
draw_axes(ax, -4.5, 4.5, -7.0, 7.0, xlabel="Re u", ylabel="Im u")

# Im(u) = 2π Re(w). For visualization, show the parallel strip −2π < Im u < −π under u = 2π i w.
ylow, yhigh = -2*math.pi, -math.pi
u_label = r"$u=2\pi i\,w$"

rect = Rectangle((-4.5, ylow), 9.0, (yhigh - ylow), facecolor=fillC, edgecolor=None)
ax.add_patch(rect)
ax.plot([-4.5, 4.5], [ylow, ylow], color=lineRed, lw=1.5)
ax.plot([-4.5, 4.5], [yhigh, yhigh], color=lineBlue, lw=1.5)
ax.text(4.4, ylow, rf"$\operatorname{{Im}}\,u={ylow:.3g}$", ha="right", va="bottom")
ax.text(4.4, yhigh, rf"$\operatorname{{Im}}\,u={yhigh:.3g}$", ha="right", va="bottom")
ax.text(-4.4, 6.5, u_label)

# ----------------- Panel D: f = exp(u) -> half-plane -----------------
ax = axs[1, 1]
draw_axes(ax, -4.5, 4.5, -4.5, 4.5, xlabel="Re f", ylabel="Im f")

if want_lower:
    # Shade lower half-plane (Im f < 0)
    rect = Rectangle((-4.5, -4.5), 9.0, 4.5, facecolor=fillD, edgecolor=None)
    ax.add_patch(rect)
    label = r"$\operatorname{Im} f(z) < 0$"
else:
    # Shade upper half-plane (Im f > 0)
    rect = Rectangle((-4.5, 0.0), 9.0, 4.5, facecolor=fillD, edgecolor=None)
    ax.add_patch(rect)
    label = r"$\operatorname{Im} f(z) > 0$"

# Real axis boundary
ax.plot([-4.5, 4.5], [0, 0], color=lineRed, lw=1.5)
ax.text(4.4, 4.3 if not want_lower else -4.3, label, ha="right", va="top" if not want_lower else "bottom")
ax.text(-4.4, 3.8, r"$f(z)=e^{2\pi i/(z-1)}$")

plt.tight_layout()
plt.savefig("conformal-mapping.png")
print("Saved conformal-mapping.png")
