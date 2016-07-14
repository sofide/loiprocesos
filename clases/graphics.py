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
        tiempos.extend([t_expo, t_preg])

    if len(set(e.grupo for e in exposiciones)) == 1 and len(exposiciones) > 1:
        for exposicion in exposiciones:
            expo.extend(["{} - TP{}".format(exposicion.clase, exposicion.tp.numero),
                         "{} - TP{}".format(exposicion.clase, exposicion.tp.numero)])
    else:
        for exposicion in exposiciones:
            expo.extend(['G{} - {}'.format(exposicion.grupo.numero, exposicion.grupo.empresa),
                         'G{} - {}'.format(exposicion.grupo.numero, exposicion.grupo.empresa)])


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
