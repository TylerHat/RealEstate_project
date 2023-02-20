import matplotlib.pyplot as plt

# Create your plots
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1, 2, 3], [4, 5, 6])
axs[0, 0].set_title('Plot 1')
axs[0, 1].scatter([1, 2, 3], [4, 5, 6])
axs[0, 1].set_title('Plot 2')
axs[1, 0].bar([1, 2, 3], [4, 5, 6])
axs[1, 0].set_title('Plot 3')
axs[1, 1].plot([1, 2, 3], [4, 2, 5])
axs[1, 1].set_title('Plot 4')

# Save the figure as a file
plt.savefig('my_plots.png')

# Generate the HTML/CSS for the page
html = '''
<!DOCTYPE html>
<html>
<head>
  <title>My Plots</title>
  <style>
    .plot {
      float: left;
      margin: 10px;
      padding: 10px;
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <h1>My Plots</h1>
  <div class="plot">
    <img src="my_plots.png" alt="Plot 1">
    <p>Plot 1</p>
  </div>
  <div class="plot">
    <img src="my_plots.png" alt="Plot 2">
    <p>Plot 2</p>
  </div>
  <div class="plot">
    <img src="my_plots.png" alt="Plot 3">
    <p>Plot 3</p>
  </div>
  <div class="plot">
    <img src="my_plots.png" alt="Plot 4">
    <p>Plot 4</p>
  </div>
</body>
</html>
'''

# Save the HTML/CSS as a file
with open('my_page.html', 'w') as f:
    f.write(html)
