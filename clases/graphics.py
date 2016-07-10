from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.charts import Bar, output_file, show, hplot

from clases.models import Exposicion, ContadorPreguntas


def tiempo_expo_graphic(exposiciones):
    expo = []
    tiempos = []
    for exposicion in exposiciones:
        t_expo = (exposicion.start_ques - exposicion.start_expo).seconds/60.
        t_preg = (exposicion.finish_expo - exposicion.start_ques).seconds/60.

        expo.extend(['G{} - {}'.format(exposicion.grupo.numero, exposicion.grupo.empresa),
                     'G{} - {}'.format(exposicion.grupo.numero, exposicion.grupo.empresa)])
        tiempos.extend([t_expo, t_preg])


    data = {
        'tags': [t for t in ('T. exposicion', 'T. pregutnas')*len(exposiciones)],
        'expo': expo,
        'tiempos': tiempos,
    }
    bar = Bar(data, values='tiempos', label='expo', stack='tags',
        palette=['#2980B9', '#404040'], title="Tiempos de exposicion",
        plot_width=300, plot_height=500, legend="bottom_center"
        )
    return components(bar, CDN)


def q_pregs_graphic(exposicion):
    pregs = ContadorPreguntas.objects.filter(exposicion=exposicion)\
                                     .order_by('preguntador__numero')

    data = {
        'grupos': ['G{}'.format(p.preguntador.numero) for p in pregs],
        'cantidad': [p.cantidad for p in pregs]
    }

    bar = Bar(data, label="grupos", values="cantidad",
        plot_width=300, plot_height=500, legend=False,
        palette=['#2980B9',],
        title="Cantidad de preguntas"
    )

    return components(bar, CDN)


def graphic():
    x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    y0 = [i**2 for i in x]
    y1 = [10**i for i in x]
    y2 = [10**(i**2) for i in x]

    # create a new plot
    p = figure(
       tools="pan,box_zoom,reset,save",
       y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
       x_axis_label='sections', y_axis_label='particles'
    )

    # add some renderers
    p.line(x, x, legend="y=x")
    p.circle(x, x, legend="y=x", fill_color="white", size=8)
    p.line(x, y0, legend="y=x^2", line_width=3)
    p.line(x, y1, legend="y=10^x", line_color="red")
    p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
    p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

    return components(p, CDN)
