import matplotlib.pyplot as plt
import pytweening


def showTween(tweenFunc):
    # Example list of (x, y) tuples
    points = []
    for i in range(0, 1000):
        i = i / 1000
        points.append((i, tweenFunc(i)))

    # Separate the x and y coordinates
    x_coords, y_coords = zip(*points)

    # Plot the points
    plt.scatter(x_coords, y_coords)

    # Set the x and y limits
    plt.xlim(-0.4, 1.4)
    plt.ylim(-0.4, 1.4)


    plt.axvline(x=0.0, color='gray', linestyle='--')
    plt.axvline(x=1.0, color='gray', linestyle='--')
    plt.axhline(y=0.0, color='gray', linestyle='--')
    plt.axhline(y=1.0, color='gray', linestyle='--')

    plt.title(tweenFunc.__qualname__)

    # Display the plot
    plt.show()


graphs = (
    pytweening.easeInQuad,
    pytweening.easeOutQuad,
    pytweening.easeInOutQuad,
    pytweening.easeInCubic,
    pytweening.easeOutCubic,
    pytweening.easeInOutCubic,
    pytweening.easeInQuart,
    pytweening.easeOutQuart,
    pytweening.easeInOutQuart,
    pytweening.easeInQuint,
    pytweening.easeOutQuint,
    pytweening.easeInOutQuint,
    pytweening.easeInSine,
    pytweening.easeOutSine,
    pytweening.easeInOutSine,
    pytweening.easeInExpo,
    pytweening.easeOutExpo,
    pytweening.easeInOutExpo,
    pytweening.easeInCirc,
    pytweening.easeOutCirc,
    pytweening.easeInOutCirc,
    pytweening.easeInElastic,
    pytweening.easeOutElastic,
    pytweening.easeInOutElastic,
    pytweening.easeInBack,
    pytweening.easeOutBack,
    pytweening.easeInOutBack,
    pytweening.easeInBounce,
    pytweening.easeOutBounce,
    pytweening.easeInOutBounce,
    pytweening.easeInPoly,
    pytweening.easeOutPoly,
    pytweening.easeInOutPoly,
)

for graph in graphs:
    showTween(graph)
