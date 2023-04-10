import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, show, output_notebook
from bokeh.palettes import Category10

from bokeh.embed import components


def grafiquita():
# Load Bokeh resources for inline display
    from IPython.core.display import display, HTML

    output_notebook()

    grecia = [
        {"year": 1994, "event": "Un Gatite was born", "image": "https://raw.githubusercontent.com/AltamarMx/gasm/main/gasm/img/new_born.jpg"},
        {"year": 2015, "event": "Mi, first kitten", "image": "https://raw.githubusercontent.com/AltamarMx/gasm/main/gasm/img/first.jpg"},
        {"year": 2019, "event": "Promotora UBA", "image": "https://raw.githubusercontent.com/AltamarMx/gasm/main/gasm/img/ier.png"},
        {"year": 2021, "event": "Se une a la Twitter y a la UEC", "image": "https://raw.githubusercontent.com/AltamarMx/gasm/main/gasm/img/python.png"},
        {"year": 2023, "event": "29 años, Lechuga & Pechuga", "image": "https://raw.githubusercontent.com/AltamarMx/gasm/main/gasm/img/canion_sumidero.png"},
        # ... add other events from the timeline, along with corresponding image URLs
    ]


    kitty = [
        {"year": 1974, "event": "Hello Kitty is created by Sanrio", "image": "https://raw.githubusercontent.com/AltamarMx/gasm/main/gasm/img/1974.jpg"},
        {"year": 1975, "event": "Hello Kitty is introduced to the United States", "image": "https://raw.githubusercontent.com/AltamarMx/gasm/main/gasm/img/1975.jpg"},
        {"year": 1976, "event": "Hello Kitty gets her iconic bow", "image": "https://example.com/hello_kitty_1976.jpg"},
        {"year": 1980, "event": "Sanrio launches the first Hello Kitty themed merchandise", "image": "https://example.com/hello_kitty_1980.jpg"},
        {"year": 1983, "event": "First Hello Kitty animated television series", "image": "https://example.com/hello_kitty_1983.jpg"},
        {"year": 1987, "event": "First Hello Kitty feature film, 'Kitty and Mimi's New Umbrella'", "image": "https://example.com/hello_kitty_1987.jpg"},
        {"year": 1993, "event": "First Hello Kitty video game for Nintendo Game Boy", "image": "https://example.com/hello_kitty_1993.jpg"},
        {"year": 1999, "event": "Hello Kitty appears on MasterCard debit cards", "image": "https://example.com/hello_kitty_1999.jpg"},
        {"year": 2004, "event": "Hello Kitty celebrates her 30th anniversary", "image": "https://example.com/hello_kitty_2004.jpg"},
        {"year": 2008, "event": "Hello Kitty is named the official ambassador of Japanese tourism", "image": "https://example.com/hello_kitty_2008.jpg"},
        {"year": 2009, "event": "Hello Kitty becomes a UNICEF ambassador", "image": "https://example.com/hello_kitty_2009.jpg"},
        {"year": 2014, "event": "Hello Kitty celebrates her 40th anniversary", "image": "https://example.com/hello_kitty_2014.jpg"},
        {"year": 2015, "event": "Hello Kitty Cafe food truck debuts in the United States", "image": "https://example.com/hello_kitty_2015.jpg"},
        {"year": 2018, "event": "Hello Kitty and Friends themed attraction opens at Universal Studios Hollywood", "image": "https://example.com/hello_kitty_2018.jpg"},
    ]

    # Convert data to a pandas DataFrame
    df_grecia = pd.DataFrame(grecia)
    df_kitty = pd.DataFrame(kitty)

    # Convert DataFrame to a Bokeh ColumnDataSource
    source_kitty = ColumnDataSource(df_kitty)
    source_grecia = ColumnDataSource(df_grecia)

    # Create a Bokeh figure
    plot = figure(title="Hello Kitty & Grecia Timeline",
                  x_axis_label="Events",
                  y_axis_label="Year",
                  x_range=(-0.5, 3),
                  y_range=(1970, 2025),
                  width=480,
                  height=800,
                  tools="",
            # Set the background color and margin size
                  border_fill_color="white",
                  min_border_left=200,
                  min_border_right=100,
                  min_border_top=50,
                  min_border_bottom=50
                 )

    # Add circle glyphs for each data point (y coordinates aligned)
    circles_kitty =  plot.circle( x=0, y="year", size=10, source=source_kitty, color=Category10[10][0], alpha=0.8)
    circles_grecia = plot.circle( x=2, y="year", size=10, source=source_grecia, color="red", alpha=0.8)

    # Add hover tool
    hover_kitty = HoverTool(
        tooltips="""
        <div>
            <div>
                <img src="@image" alt="Hello Kitty Image" width="80" height="auto" border="2" style="float: left; right: 0px 15px 15px 0px;"/>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@year</span>
                <br>
                <span style="font-size: 15px;">@event</span>
            </div>
        </div>
        """,
        renderers=[circles_kitty],
        mode="mouse"
    )
     # Add hover tool
    hover_grecia = HoverTool(
        tooltips="""
        <div>
            <div>
                <img src="@image" alt="Hello Kitty Image" width="80" height="auto" border="2" style="float: right; margin: 0px 15px 15px 0px;"/>
            </div>
            <div>
                <span style="font-size: 17px; font-weight: bold;">@year</span>
                <br>
                <span style="font-size: 15px;">@event</span>
            </div>
        </div>
        """,
        renderers=[circles_grecia],
        mode="mouse"
    )
    plot.add_tools(hover_kitty)
    plot.add_tools(hover_grecia)

    # Remove gridlines and minor ticks
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None
    plot.xaxis.minor_tick_line_color = None
    plot.xaxis.minor_tick_line_color = None
    plot.yaxis.minor_tick_line_color = None
    plot.xaxis.ticker = []

#     show(plot)


    script, div = components(plot)
    html_repr = f"<div>{script}{div}</div>"
    display(HTML(html_repr))

    # Show the result
#
