# -*- coding: utf-8 -*-
import io

import numpy
import pandas
import bokeh

from jinja2 import Template

from bokeh.io import curdoc
from bokeh.layouts import column, widgetbox
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import ColumnDataSource, HoverTool, CustomJS, Range1d, LabelSet, Label
from bokeh.models.widgets import Select

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.util.browser import view


# select the tools we want
#TOOLS="pan,wheel_zoom,box_zoom,reset,save"
TOOLS=""

#html = file_html(plot, CDN, "my plot")

#------------------------------------------------------------------------------
# Entrada de Dados
#------------------------------------------------------------------------------
flag1 = False

colExtra = 'Creditos'

#D = pandas.read_csv('DisciplinasEE - ' + opt + '.csv', delimiter=';', encoding='latin-1')
#PP = pandas.read_csv('PrePosEE - ' + opt + '.csv', delimiter=';', encoding='latin-1')

Dtemp = pandas.read_csv('DisciplinasEE.csv', delimiter=';', encoding='latin-1')
PPtemp = pandas.read_csv('PrePosEE.csv', delimiter=';', encoding='latin-1')

if(flag1):
    if(len(Dtemp.index) > 10):
        print(Dtemp[:10])
    else:
        print(Dtemp)

#    Codigo Nome Nome Curto     Tipo  Periodo Ideal  Creditos    Obrigatoria ou Optativa Departamento  
#0  1101157   A1         A1  Basicos              1         4                Obrigatoria           DF  
#1  1103118   A2         A2  Basicos              1         4                Obrigatoria           DM 
#2  1103177   B1         B1  Basicos              2         4                Obrigatoria           DM  
#3  1403153   B2         B2  Basicos              2         4                Obrigatoria         DLCV  

if(flag1):
    if(len(PPtemp.index) > 10):
        print(PPtemp[:10])
    else:
        print(PPtemp)
    
#  Disciplina Pre Disciplina Pos
#0             A1             B1
#1             B1             C1
#2             C1             D1
#3             B2             D2

#------------------------------------------------------------------------------
# Filtrando dados
#------------------------------------------------------------------------------

#opt = 'Sistemas de Energia'
opt = 'Eletronica'
#opt = 'Controle e Automacao'
#opt = 'Generalista'
#opt = 'Parte Comum'

if(opt == 'Sistemas de Energia'):
    D = Dtemp[Dtemp['SE']==1]
elif(opt == 'Eletronica'):
    D = Dtemp[Dtemp['EL']==1]
elif(opt == 'Controle e Automacao'):
    D = Dtemp[Dtemp['CA']==1]
elif(opt == 'Generalista'):
    D = Dtemp[Dtemp['GN']==1]
elif(opt == 'Parte Comum'):
    D = Dtemp[Dtemp['Periodo Ideal']<8]
    
D = D.reset_index(drop=True)
PP=PPtemp
    
#------------------------------------------------------------------------------
# Obter x, y, cor, pre e pos
#------------------------------------------------------------------------------
flag2 = False

if(colExtra != 'Nenhum'):
    listKeys = list(D[colExtra].unique())
    listKeys.sort()
    listCores = bokeh.palettes.plasma(len(listKeys))
    dictCores = dict(zip(listKeys, listCores))
    #print(dictCores)

sz = len(D.index)
conty = numpy.ones(sz)
xD = numpy.zeros(sz)
yD = numpy.zeros(sz)
corD = sz * [' ']
apelidoD = sz * [' ']
extraD = sz * [' ']
preD = {}
posD = {}
nameToind = {}

for idx in D.index:
    nome = D['Nome Curto'][idx]
    periodo = int(D['Periodo Ideal'][idx])
        
    xD[idx] = periodo*10
    yD[idx] = conty[periodo-1]*25 + 30
    corD[idx] = dictCores[D[colExtra][idx]]
    apelidoD[idx] = nome
    
    if(colExtra != 'Nenhum'):
        extraD[idx] = D[colExtra][idx]
    
    nameToind[nome] = idx
    
    #print('---> 1')
    
    temp = PP[PP['Disciplina Pos'] == nome]
    preD[idx] = temp['Disciplina Pre'].tolist()
    
    #print('---> 2')
    
    temp = PP[PP['Disciplina Pre'] == nome]
    posD[idx] = temp['Disciplina Pos'].tolist()
    
    #print('---> 3')
    
    conty[periodo-1] = conty[periodo-1] + 1
    
if(flag2):
    for idx in range(sz):
        str1 = '[' + ' '.join(preD[idx]) + ']'
        str2 = '[' + ' '.join(posD[idx]) + ']'
        print('%f,%f,%s,%s,%s' % (yD[idx], xD[idx], corD[idx], str1, str2))

#------------------------------------------------------------------------------
# Desenha o grafico: Prepara source e newsource como arestas
#------------------------------------------------------------------------------
flag3 = False

#output_file("FluxEE - " + opt + ".html")

select = Select(title="Selecione informacao extra:"
                , value="Creditos"
                , options=["Nenhum", "Tipo", "Periodo Ideal", "Creditos", "Obrigatoria ou Optativa", "Departamento"
                           , "171.MAT", "162.AP", "162.RP", "162.RF", "162.TR", "162.MA", "162.ES", "162.CA"])

def my_select_change_handler(attr, old, new):
    colExtra = select.value
    extraD = sz * [' ']
    corD = sz * [' ']       
    if(colExtra != 'Nenhum'):
        listKeys = list(D[colExtra].unique())
        listCores = bokeh.palettes.plasma(len(listKeys))
        dictCores = dict(zip(listKeys, listCores))
        for idx in D.index:
            extraD[idx] = D[colExtra][idx]
            corD[idx] = dictCores[D[colExtra][idx]]
    sourceD.data = dict(apelido=apelidoD,cor=corD,x=xD,y=yD,extra=extraD)
    
select.on_change("value", my_select_change_handler)
    
p = figure(title='Fluxograma de Engenharia Eletrica - ' + opt
           , plot_width=1100
           , plot_height=550
           , x_range=Range1d(0, 120)
           , y_range=Range1d(0, 280))

p.xaxis.visible = False
p.yaxis.visible = False
p.xgrid.visible = False
p.ygrid.visible = False

source = ColumnDataSource({'x0': [], 'y0': [], 'x1': [], 'y1': []})
sr = p.segment(x0='x0', y0='y0', x1='x1', y1='y1', color='red', alpha=0.6, line_width=5, source=source)

newsource = ColumnDataSource({'x0': [], 'y0': [], 'x1': [], 'y1': []})
newsr = p.segment(x0='x0', y0='y0', x1='x1', y1='y1', color='green', alpha=0.6, line_width=5, source=newsource)

#------------------------------------------------------------------------------
# Desenha o grafico: Adiciona circulos e nomes das disciplinas
#------------------------------------------------------------------------------

dictD=dict(apelido=apelidoD,cor=corD,x=xD,y=yD,extra=extraD)
sourceD = ColumnDataSource(data=dictD)

cr = p.rect(x = 'x'
              , y = 'y'
              , color = 'cor'
              , width = 9
              , height = 20
              , alpha=0.2
              , hover_color='blue'
              , hover_alpha=0.5
              , line_color = 'black'
              , source = sourceD)
'''
cr = p.circle(x = 'x'
              , y = 'y'
              , color = 'cor'
              , size = 15
              , alpha=0.8
              , hover_color='blue'
              , hover_alpha=0.7
              , line_color = 'black'
              , source = sourceD)
'''
labels = LabelSet(x = 'x'
                  , y = 'y'
                  , text = 'apelido'
                  , text_font_size = '8pt'
                  , level = 'glyph'
                  , x_offset = -35
                  , y_offset = 0
                  , render_mode='canvas'
                  , source = sourceD)
p.add_layout(labels)

if(colExtra != 'Nenhum'):
    labelsX = LabelSet(x = 'x'
                      , y = 'y'
                      , text = 'extra'
                      , text_font_size = '8pt'
                      , level = 'glyph'
                      , x_offset = -35
                      , y_offset = -12
                      , render_mode='canvas'
                      , source = sourceD)
    p.add_layout(labelsX)
    
#------------------------------------------------------------------------------
# Desenha o grafico: Adiciona codigo JS para efetivamente desenhar arestas
#------------------------------------------------------------------------------

code = """
var nameToind = %s;
var links = %s;
var newlinks = %s;
var data = {'x0': [], 'y0': [], 'x1': [], 'y1': []};
var newdata = {'x0': [], 'y0': [], 'x1': [], 'y1': []};

var cdata = circle.data;
var indices = cb_data.index['1d'].indices;
//window.alert('===> ' + indices[0].toString());

for (i=0; i < indices.length; i++) {
    ind0 = indices[i]
    //window.alert('ind0 = ' + ind0.toString());
    for (j=0; j < links[ind0].length; j++) {
        ind1 = nameToind[links[ind0][j]];
        //window.alert('ind1 = ' + ind1.toString());
        data['x0'].push(cdata.x[ind0]);
        data['y0'].push(cdata.y[ind0]);
        data['x1'].push(cdata.x[ind1]);
        data['y1'].push(cdata.y[ind1]);
    }
}
segment.data = data;

for (i=0; i < indices.length; i++) {
    ind0 = indices[i]
    //window.alert('ind0 = ' + ind0.toString());
    for (j=0; j < newlinks[ind0].length; j++) {
        ind1 = nameToind[newlinks[ind0][j]];
        //window.alert('ind1 = ' + ind1.toString());
        newdata['x0'].push(cdata.x[ind0]);
        newdata['y0'].push(cdata.y[ind0]);
        newdata['x1'].push(cdata.x[ind1]);
        newdata['y1'].push(cdata.y[ind1]);
    }
}    
newsegment.data = newdata;

""" % (nameToind, preD, posD)

callback = CustomJS(args={'circle': cr.data_source, 'segment': sr.data_source, 'newsegment': newsr.data_source}, code=code)
p.add_tools(HoverTool(tooltips=None, callback=callback, renderers=[cr]))

#------------------------------------------------------------------------------
# Desenha o grafico: Adiciona uma citacao no canto inferior direito
#------------------------------------------------------------------------------

citation = Label(x=90
                 , y=5
                 , text='Helon D. M. Braz 2017-07-13'
                 , text_font_size = '8pt'
                 , render_mode='css'
                 , border_line_color='black'
                 , border_line_alpha=1.0
                 , background_fill_color='blue'
                 , background_fill_alpha=0.1)
p.add_layout(citation)

#------------------------------------------------------------------------------
# Desenha o grafico: Adiciona Label para cada semestre
#------------------------------------------------------------------------------

xP = range(10,110,10)
yP = numpy.ones(10)*25
nomesP = [('%d Periodo' % item) for item in range(1,11)]

dictP=dict(apelido=nomesP,x=xP,y=yP)
sourceP = ColumnDataSource(data=dictP)

labelsP = LabelSet(x = 'x'
                  , y = 'y'
                  , text = 'apelido'
                  , text_font_size = '8pt'
                  , text_font_style = 'bold'
                  , level = 'glyph'
                  , x_offset = -35
                  , y_offset = 0
                  , render_mode='canvas'
                  , source = sourceP)
p.add_layout(labelsP)

layout = column(widgetbox(select), p)

curdoc().add_root(layout)
curdoc().title = "Grade"

#output_file('grade.html')
#show(layout)

script, div = components(p)

template = Template('''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Bokeh Scatter Plots</title>
        {{ resources }}
        {{ script }}
        <style>
            .embed-wrapper {
                width: 50%;
                height: 800px;
                margin: auto;
            }
        </style>
    </head>
    <body>
        <div class="embed-wrapper">
            {{ div }}
        </div>
    </body>
</html>
''')


resources = INLINE.render()

filename = 'embed.html'

html = template.render(resources=resources,
                       script=script,
                       div=div)

with io.open(filename, mode='w', encoding='utf-8') as f:
    f.write(html)

#view(filename)
