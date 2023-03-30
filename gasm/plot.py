
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, show
from bokeh.palettes import Category10

def grafiquita():
# Load Bokeh resources for inline display
    output_notebook()

    data = [
        {"year": 1974, "event": "Hello Kitty is created by Sanrio", "image": "https://www.ier.unam.mx/~gbv/tux.png"},
        {"year": 1975, "event": "Hello Kitty is introduced to the United States", "image": "https://example.com/hello_kitty_1975.jpg"},
        {"year": 1983, "event": "First Hello Kitty animated television series", "image": "https://example.com/hello_kitty_1983.jpg"},
        # ... add other events from the timeline, along with corresponding image URLs
    ]

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Convert DataFrame to a Bokeh ColumnDataSource
    source = ColumnDataSource(df)

    # Create a Bokeh figure
    plot = figure(title="Hello Kitty Timeline",
                  x_axis_label="Events",
                  y_axis_label="Year",
                  x_range=(-0.5, 0.5),
                  y_range=(1970, 2025),
                  width=200,
                  height=800,
                  tools="")

    # Add circle glyphs for each data point (y coordinates aligned)
    circles = plot.circle(x=0, y="year", size=10, source=source, color=Category10[10][0], alpha=0.8)

    # Add hover tool
    hover = HoverTool(
        tooltips="""
        <div>
            <div>
                <img src="@image" alt="Hello Kitty Image" width="200" height="auto" border="2" style="float: left; margin: 0px 15px 15px 0px;"/>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@year</span>
                <br>
                <span style="font-size: 15px;">@event</span>
            </div>
        </div>
        """,
        renderers=[circles],
        mode="mouse"
    )
    plot.add_tools(hover)

    # Remove gridlines and minor ticks
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None
    plot.xaxis.minor_tick_line_color = None
    plot.yaxis.minor_tick_line_color = None

    # Show the result
    show(plot)