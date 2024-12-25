import matplotlib.pyplot as plt
import math
def dist(ponto1,ponto2):
	x1,y1 = ponto1
	x2,y2 = ponto2
	return math.sqrt(pow((x2 - x1),2) + pow((y2 - y1),2))

x_min, x_max = 0, 200
y_min, y_max = 0, 200
print(dist((10,20),(20,30)))

#Utilizadores
users = [
    (10, 20), 
    (50, 50),  
    (70, 80),  
    (30, 60),  
]

antenas = [
    (40, 50), 
   # (60, 100),  
  #  (70, 30),  
  #  (30, 10),  
]

#if (a)

# Plotting
plt.figure(figsize=(8, 8))  # Set figure size

# Remove axes for a clean map look
plt.axis('off')

# Set map background color
#plt.gca().set_facecolor("lightblue")

# Plot points as dots
for x, y in users:
    plt.scatter(x, y, color="red", s=100)  # 's' sets the size of the dots

for x, y in antenas:
    plt.scatter(x, y, color="red", s=100)

# Optionally connect the points (if you want a path)
for i in range(len(users) ):
   plt.plot(
        [users[i][0], antenas[0][0]],  # X-coordinates
        [users[i][1], antenas[0][1]],  # Y-coordinates
        color="green", linestyle="--", linewidth=2,
    )

# Add labels for points
for i, (x, y) in enumerate(users, start=1):
    plt.text(x + 2, y, f"P{i}", fontsize=12, color="black")

for i, (x, y) in enumerate(antenas, start=1):
    plt.text(x + 2, y, f"A{i}", fontsize=12, color="black")

# Set fixed aspect ratio for the map
plt.gca().set_aspect('equal', adjustable='box')

# Add a title (optional)
#plt.title("Customized 2D Map", fontsize=16, pad=20)

# Show the map
plt.show()