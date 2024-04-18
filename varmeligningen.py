import numpy as np
import matplotlib.pyplot as plt

# Parametere
Lx = 1.0  # lengde i x-retning
Ly = 1.0  # lengde i y-retning
Nx = 50   # antall gitterpunkter i x-retning
Ny = 50   # antall gitterpunkter i y-retning
T = 1.0   # total tid
Nt = 100  # antall tidssteg
alpha = 0.01  # termisk diffusivitet

# Størrelse av gitterpunkter
dx = Lx / Nx
dy = Ly / Ny
dt = T / Nt

# Initialbetingelse (starttemperatur)
u0 = np.zeros((Nx+1, Ny+1))
u0[Nx//4:Nx//2, Ny//4:Ny//2] = 1.0  # en firkant av høyere temperatur

# Implementering av endelige differanser
u = u0.copy()
for n in range(Nt):
    un = u.copy()
    for i in range(1, Nx):
        for j in range(1, Ny):
            u[i, j] = un[i, j] + alpha * dt * (
                (un[i+1, j] - 2*un[i, j] + un[i-1, j]) / dx**2 +
                (un[i, j+1] - 2*un[i, j] + un[i, j-1]) / dy**2
            )

# resultatet
x = np.linspace(0, Lx, Nx+1)
y = np.linspace(0, Ly, Ny+1)
X, Y = np.meshgrid(x, y)
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, u.T, cmap='hot')
plt.colorbar(label='Temperatur')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Temperaturfordeling over tid')
plt.show()


