from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.charts import Bar, output_file, show, hplot
from bokeh.charts.attributes import CatAttr

from clases.models import Exposicion, ContadorPreguntas


def tiempo_expo_graphic(exposiciones):
    expo = []
    tiempos = []

    if len(set(e.grupo for e in exposiciones)) == 1 and len(exposiciones) > 1:
        exposiciones = list(reversed(exposiciones))
        for exposicion in exposiciones:
            expo.extend(["{} - TP{}".format(exposicion.clase, exposicion.tp.numero),
                         "{} - TP{}".format(exposicion.clase, exposicion.tp.numero)])
    else:
        for exposicion in exposiciones:
            expo.extend([exposicion.short_string(), exposicion.short_string()])

    for exposicion in exposiciones:
        t_expo = (exposicion.start_ques - exposicion.start_expo).seconds/60.
        t_preg = (exposicion.finish_expo - exposicion.start_ques).seconds/60.
        tiempos.extend([t_expo, t_preg])

    data = {
        'tags': [t for t in ('T. exposicion', 'T. preguntas')*len(exposiciones)],
        'expo': expo,
        'tiempos': tiempos,
    }
    bar = Bar(data, values='tiempos', label=CatAttr(columns=['expo'], sort=False),
              stack='tags', palette=['#2980B9', '#404040'], title="Tiempos de exposicion",
              plot_width=300, plot_height=500, legend="bottom_center",
              )

    bar.legend.background_fill_alpha = 0.5
    bar.legend.border_line_color = "#404040"

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
              title="Cantidad de preguntas")

    return components(bar, CDN)


def q_pregs_expos_graphic(exposiciones):
    preguntas_raw = ContadorPreguntas.objects.filter(exposicion__in=exposiciones)
    tags = []
    expos = []
    preguntas = []
    for e in exposiciones:
        for p in preguntas_raw:
            if p.exposicion == e:
                tags.append(p.preguntador.producto)
                expos.append(e.short_string())
                preguntas.append(p.cantidad)
    data = {
        'tags': tags,
        'expos': expos,
        'preguntas': preguntas,
    }

    bar = Bar(data, values='preguntas', label='expos', stack='tags',
        title="Preguntas realizadas",
        plot_width=300, plot_height=500,
        )

    bar.legend.background_fill_alpha = 0.5
    bar.legend.border_line_color = "#404040"

    return components(bar, CDN)
