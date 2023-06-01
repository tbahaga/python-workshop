
#The second NMA training
#prepared by Gemechu Fanta (PhD)

# Let's add some interactive widgets

from ipywidgets import interact

def plot_pseudotemperature(f, A, An, offset):
    x = np.linspace(0, 2*np.pi, 100)
    y = A * np.sin(f * x) + np.random.random(100) * An + offset
    
    fig = plt.figure()
    plt.plot(x, y)
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('My Temperature Data')
    plt.show()
    
interact(plot_pseudotemperature,
         f = (0, 10),
         A = (1, 5),
         An = (1, 10),
         offset = (10, 40))
