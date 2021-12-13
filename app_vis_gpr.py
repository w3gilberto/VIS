
import streamlit as st

import altair as alt
from vega_datasets import data
import pandas as pd
import geopandas as gpd
import json
import matplotlib.pyplot as plt;
import plotly.express as px;


st.set_page_config(page_title = 'App GilbertoRamos - Powered by Streamlit', 
				   page_icon = 'icone_vis.png' ,
				   layout = 'centered', 
				   initial_sidebar_state = 'auto')

##banner
st.sidebar.image('banner_vis.png', use_column_width = 'always')
st.sidebar.write('''***Powered by [Streamlit](https://streamlit.io/)***''')



df = pd.read_csv('IPS_ok_2.csv', usecols = ['regiao','IPS','NotaDNB','Nutri','Moradia','ACB'], sep=';')

df1 = pd.read_csv('Base_IPS_RJ_2020_ok2.csv', sep=';')

# registros de 2020
df2 = pd.read_csv('Base_IPS_RJ_2020_ok3.csv', sep=';')

st.image('banner_vis02.jpg', use_column_width = 'always')

paginas = ['Home','Explorando Dados','Interatividade com Altair','Mapas Choropleth','Conclusão','Código']

pagina = st.sidebar.radio('selecione a pagina que vc deseja:', paginas)

if pagina == 'Home':

#	st.markdown('# Dimensões do Índice de Progresso Social(IPS) na cidade do Rio de Janeiro')
	
    st.image('imagem_IPS.jpg', use_column_width = 'always')

   
    
if pagina == 'Explorando Dados':   
    #df1 = pd.read_csv('Base_IPS_RJ_2020_ok2.csv', sep=';')
    #st.write(df1)
    
       
    var2 = st.selectbox('selecione uma dimensão', ['violência contra mulher','tx abandono do ensino médio','roubos de rua', 'Taxa de Homicídios'])
    
    if var2 == 'violência contra mulher':
        
        var3 = st.selectbox('selecione a variavel', ['regiao','ano'])
        
        if var3 == 'ano':
        
            st.markdown('# Violência contra mulher: média por ano')
        
            ms = df1['viol_contra_m'].groupby(df1["ano"]).mean()   
            st.write(ms)
            plot = df1['viol_contra_m'].groupby(df1["ano"]).mean().plot(kind = 'bar')
            st.pyplot(plot.figure)
            
            
            #ms = df1.query('regiao == @var3' and 'ano == @var4')
            #ms = ms[['regiao', 'ano', 'viol_contra_m']]
            #df.groupby([var3, var4])
            #st.write(ms)
            #dfx = ms[['ano'],['viol_contra_m']]
            #dfx_sorted= dfx.sort_values('viol_contra_m')
        
            #ms = ms.sort_values('viol_contra_m')
            
            #st.write(dfx_sorted)
            #st.write(df1_sorted)
           
            #plot = ms['viol_contra_m'].plot(kind = 'bar')
            
            
        if var3 == 'regiao':
        
        
            st.markdown('# Violência contra mulher por regiao em 2020')
            #ms = df1['viol_contra_m'].groupby(df1["regiao"]).mean()
            #dfx = df2.sort_values('viol_contra_m')
            dfx = df2[['regiao', 'ano', 'viol_contra_m']]
            dfx = dfx.sort_values('viol_contra_m')
            st.write(dfx)
            plot = dfx[['regiao','viol_contra_m']].plot(kind = 'bar')
            st.pyplot(plot.figure)
            
            
    
    if var2 == 'tx abandono do ensino médio':
    
        st.markdown('# Tx abandono do ensino médio por região/ano')
        
        var4 = st.selectbox('selecione uma variavel', ['regiao','ano'])
        
        if var4 == 'ano':
        
            ms = df1['ab_ens_med'].groupby(df1["ano"]).mean()
            st.write(ms)
            plot = df1['ab_ens_med'].groupby(df1["ano"]).mean().plot(kind = 'bar')
            st.pyplot(plot.figure)
        
        
    #ab_ens_med
        if var4 == 'regiao':
        
            dfx = df2[['regiao','ano','ab_ens_med']]
            dfx = dfx.sort_values('ab_ens_med')
            st.write(dfx)
            plot = dfx[['regiao','ab_ens_med']].plot(kind = 'bar')
            st.pyplot(plot.figure)
            
            
    
    if var2 == 'roubos de rua':
        st.markdown('# Roubos de rua por região/ano')
        
        var4 = st.selectbox('selecione uma variavel', ['regiao','ano'])
        
        if var4 == 'ano':
        
            ms = df1['roubos_rua'].groupby(df1["ano"]).mean()
            st.write(ms)
            plot = df1['roubos_rua'].groupby(df1["ano"]).mean().plot(kind = 'bar')
            st.pyplot(plot.figure)
            
            
        
        if var4 == 'regiao':
        
            dfx = df2[['regiao','ano','roubos_rua']]
            dfx = dfx.sort_values('roubos_rua')
            st.write(dfx)
            plot = dfx[['regiao','roubos_rua']].plot(kind = 'bar')
            st.pyplot(plot.figure)
        
        
        
        
    if var2 == 'Taxa de Homicídios':
        st.markdown('# Taxa de Homicídios por região/ano')
        
        var4 = st.selectbox('selecione uma variavel', ['regiao','ano'])
        
        if var4 == 'ano':
        
            ms = df1['tx_homic'].groupby(df1["ano"]).mean()
            st.write(ms)
            plot = df1['tx_homic'].groupby(df1["ano"]).mean().plot(kind = 'bar')
            st.pyplot(plot.figure)    
        
        if var4 == 'regiao':
        
            dfx = df2[['regiao','ano','tx_homic']]
            dfx = dfx.sort_values('tx_homic')
            st.write(dfx)
            plot = dfx[['regiao','tx_homic']].plot(kind = 'bar')
            st.pyplot(plot.figure)
            
            
            

    
    
    
    
    
    #if var2 == 'teste': 
       # st.markdown('# tx homicídio X abandono escolar no ensino médio')
    # tx_homicidio  x abandono escolar no ensino médio
        
    #    fig  = px.scatter(df1, x = 'tx_homic', y = 'ab_ens_med', log_x = True, width = 800)
    #    fig.update_traces(marker = dict(size = 12, line=dict(width = 2)), selector = dict(mode = 'markers'))
    #    fig.update_layout(title = 'tx homicídio X abandono escolar no ensino médio')
    #    fig.update_xaxes(title = 'tx homicídio')
    #    fig.update_yaxes(title = 'aband. escolar no ensino médio')
    #   st.fig.show()
     
    
        #plot = df1(['tx_homic'],['ab_ens_med']).plot(kind = 'scatter')
        #st.pyplot(plot.figure)
    
    
        #plot = plt.scatter(df1.ab_ens_med, df1.tx_homic)
        #plt.update_traces(marker = dict(size = 12, line=dict(width = 2)), selector = dict(mode = 'markers'))
        #plot.update_layout(title = 'tx homicídio X abandono escolar no ensino médio')
        #plot.update_xaxes(title = 'tx homicídio')
        #plot.update_yaxes(title = 'aband. escolar no ensino médio')
        
        #plot = plt.xlabel("aband. escolar no ensino médio", size = 16)
        #plot = plt.ylabel("tx homicídio", size = 16)

        #plot = plt.title("tx homicídio X abandono escolar no ensino médio", 
        #                    position=(0.5, 0.9),
        #                    fontdict={'family': 'serif', 
        #                    'color' : 'darkblue',
        #                    'weight': 'bold',
        #                    'size': 12})
                            
        #plot = plt.title("tx homicídio X abandono escolar no ensino médio", 
        #                    fontdict={'family': 'serif', 
        #                    'color' : 'darkblue',
        #                    'weight': 'bold',
        #                    'size': 12})                   
        
    #    st.pyplot(plot.figure)
    
    #    df1.plot.scatter(x='ab_ens_med', y='tx_homic', title= "tx homicídio X abandono escolar no ensino médio'");
        
        #st.pyplot(plot.figure)
        
      
    #    st.plot.show(block=True);
    
    

if pagina == 'Interatividade com Altair':

#'IPSxNotaDNB':	
#Explorando a visualização interativa nas dimensões : 
#Índice de Progresso Social X Nota na dimensão Necessidades Básicas.**

    var1 = st.selectbox('selecione uma relação', ['IPSxNotaDNB', 'IPSxACB', 'IPSxMoradia','IPSxNutrição', 'Tx de Homicídios x Tx Abandono do Ensino Médio','Tx Abandono do Ensino Médio X Pessoas com ensino superior'])
    
    if var1 == 'IPSxNotaDNB':

        st.markdown('# Índice de Progresso Social X Nota na dimensão Necessidades Básicas')

        brush = alt.selection_interval()

        points = alt.Chart(df).mark_point().encode(
            x=alt.X('IPS:Q', title='indice progresso social'),
            y=alt.Y('NotaDNB:Q', title='nota dimensao necessid. BAsicas'),
            color=alt.condition(brush, 'regiao:N', alt.value('lightgray'))
        ).add_selection(
            brush
        )

        bars = alt.Chart(df).mark_bar().encode(
            y='regiao:N',
            color='regiao:N',
            x='count(regiao):Q'
        ).transform_filter(
            brush
        )

        points & bars


    if var1 == 'IPSxACB':

#Explorando a visualização interativa nas dimensões : 
#Índice de Progresso Social X Acesso ao Conhecimento Básico.**

        st.markdown('# Índice de Progresso Social X Acesso ao Conhecimento Básico.')

        brush = alt.selection_interval()

        points = alt.Chart(df).mark_point().encode(
            x=alt.X('IPS:Q', title='indice progresso social'),
            y=alt.Y('ACB:Q', title='Acesso ao conhecimento Básico'),
            color=alt.condition(brush, 'regiao:N', alt.value('lightgray'))
        ).add_selection(
            brush
        )

        bars = alt.Chart(df).mark_bar().encode(
            y='regiao:N',
            color='regiao:N',
            x='count(regiao):Q'
        ).transform_filter(
            brush
        )

        points & bars


    if var1 == 'IPSxMoradia':

#Explorando a visualização interativa nas dimensões : 
#Índice de Progresso Social X Moradia**

        st.markdown('# Índice de Progresso Social X Moradia')

        brush = alt.selection_interval()

        points = alt.Chart(df).mark_point().encode(
            x=alt.X('IPS:Q', title='indice progresso social'),
            y=alt.Y('Moradia:Q', title='Moradia'),
            color=alt.condition(brush, 'regiao:N', alt.value('lightgray'))
        ).add_selection(
            brush
        )

        bars = alt.Chart(df).mark_bar().encode(
            y='regiao:N',
            color='regiao:N',
            x='count(regiao):Q'
        ).transform_filter(
            brush
        )

        points & bars

    if var1 == 'IPSxNutrição':

#Explorando a visualização interativa nas dimensões : 
#Índice de Progresso Social X Moradia**

        st.markdown('# Índice de Progresso Social X Nutrição')

        brush = alt.selection_interval()

        points = alt.Chart(df).mark_point().encode(
            x=alt.X('IPS:Q', title='indice progresso social'),
            y=alt.Y('Nutri:Q', title='Moradia'),
            color=alt.condition(brush, 'regiao:N', alt.value('lightgray'))
        ).add_selection(
            brush
        )

        bars = alt.Chart(df).mark_bar().encode(
            y='regiao:N',
            color='regiao:N',
            x='count(regiao):Q'
        ).transform_filter(
            brush
        )

        points & bars
        
    if var1 == 'Tx de Homicídios x Tx Abandono do Ensino Médio':
        
        st.markdown('# Tx de Homicídios x Tx Abandono do Ensino Médio - Ano 2020')

        brush = alt.selection_interval()

        points = alt.Chart(df2).mark_point().encode(
            x=alt.X('ab_ens_med:Q', title='abandono ensino médio'),
            y=alt.Y('tx_homic:Q', title='tx homicídios'),
            color=alt.condition(brush, 'regiao:N', alt.value('lightgray'))
        ).add_selection(
            brush
        )

        bars = alt.Chart(df2).mark_bar().encode(
            y='regiao:N',
            color='regiao:N',
            x='count(regiao):Q'
        ).transform_filter(
            brush
        )

        points & bars   
        
        
        #pess_com_ens_sup
        
        
    if var1 == 'Tx Abandono do Ensino Médio X Pessoas com ensino superior':
    
        st.markdown('# Tx Abandono do Ensino Médio X Pessoas com ensino superior - Ano 2020')

        brush = alt.selection_interval()

        points = alt.Chart(df2).mark_point().encode(
            x=alt.X('ab_ens_med:Q', title='tx abandono ensino médio'),
            y=alt.Y('pess_com_ens_sup:Q', title='pessoas com ensino superior'),
            color=alt.condition(brush, 'regiao:N', alt.value('lightgray'))
        ).add_selection(
            brush
        )

        bars = alt.Chart(df2).mark_bar().encode(
            y='regiao:N',
            color='regiao:N',
            x='count(regiao):Q'
        ).transform_filter(
            brush
        )

        points & bars      
        
        

#if pagina == 'Maps':

#        filtered_data = pd.read_csv('paises_africa_.csv', sep = ";")
        
    
#        african_countries = alt.topo_feature(
#            "https://raw.githubusercontent.com/deldersveld/topojson/master/continents/africa.json",
#            "continent_Africa_subunits",
#            )
#        africa_chart = (
#            alt.Chart(african_countries)
#            .mark_geoshape(stroke="white", strokeWidth=2)
#            .encode(
#                color="value:Q",
#                tooltip=[
#                    alt.Tooltip("properties.geounit:O", title="Country name"),
#                    alt.Tooltip("value:Q", title="Indicator value"),
#                ],
#            )
#            .transform_lookup(
#                lookup="properties.geounit",
#                from_=alt.LookupData(filtered_data, "Geo Name", ["value"]),
#            )
#        )
#        st.altair_chart(africa_chart)


#if pagina == 'MapsRio':



#    filtered_data = pd.read_csv('bairros_rio_03.csv', sep = ";")
            
#    rio_bairros = alt.topo_feature(
     #   "https://raw.githubusercontent.com/lucasbarcellosoliveira/100AnosUFRJ/master/Limite_Bairro.json",
##        "Limite_de_Bairros.geojson",
#        "Limite_de_Bairros",
#        )
#    Rio_chart = (
#        alt.Chart(rio_bairros)
#        .mark_geoshape(stroke="white", strokeWidth=2)
#        .encode(
#            color="value:Q",
#            tooltip=[
#                alt.Tooltip("properties.REGIAO_ADM:O", title="bairro"),
#                alt.Tooltip("value:Q", title="Indicator value"),
#            ],
#        )
#        .transform_lookup(
#            lookup="properties.REGIAO_ADM",
#            from_=alt.LookupData(filtered_data, "REGIAO_ADM", ["VALUE"]),
#        )
#    )
#    st.altair_chart(Rio_chart)




if pagina == 'Mapas Choropleth':


    var5 = st.selectbox('selecione uma visão 2020', ['Feminicídio-Brasil', 'IDH-Brasil', 'IDH-Mundo'])
    
    if var5 == 'Feminicídio-Brasil':
    
        st.markdown('# Feminicídio no Brasil em 2020')

        filtered_data = pd.read_csv('brasil_estados_ok.csv', sep = ";")
        
              
        brasil_estados = alt.topo_feature(
            "https://gist.githubusercontent.com/ruliana/1ccaaab05ea113b0dff3b22be3b4d637/raw/196c0332d38cb935cfca227d28f7cecfa70b412e/br-states.json",
            "estados",
            )
        Brasil_chart = (
            alt.Chart(brasil_estados)
            .mark_geoshape(stroke="white", strokeWidth=2)
            .encode(
                color="value:Q",
                tooltip=[
                    alt.Tooltip("properties.nome:O", title="Município"),
                    alt.Tooltip("value:Q", title="Indicator value"),
                ],
            )
            .transform_lookup(
                lookup="properties.nome",
                from_=alt.LookupData(filtered_data, "estado", ["value"]),
            )
        )
        st.altair_chart(Brasil_chart)

        st.markdown('Fonte:Secretaria de Segurança Pública dos Estados e do DF.')
    
    
    if var5 == 'IDH-Brasil':
    
        st.markdown('# IDH Brasil em 2020')

        filtered_data = pd.read_csv('IDH_Brasil_2020_ok.csv', sep = ";")
        
        
                      
        brasil_estados = alt.topo_feature(
            "https://gist.githubusercontent.com/ruliana/1ccaaab05ea113b0dff3b22be3b4d637/raw/196c0332d38cb935cfca227d28f7cecfa70b412e/br-states.json",
            "estados",
            )
        Brasil_chart = (
            alt.Chart(brasil_estados)
            .mark_geoshape(stroke="white", strokeWidth=2)
            .encode(
                color="value:Q",
                tooltip=[
                    alt.Tooltip("properties.nome:O", title="Estado"),
                    alt.Tooltip("value:Q", title="Indicator value"),
                ],
            )
            .transform_lookup(
                lookup="properties.nome",
                from_=alt.LookupData(filtered_data, "estado", ["value"]),
            )
        )
        st.altair_chart(Brasil_chart)

        st.markdown('Fonte:https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_IDH')
        
        
    if var5 == 'IDH-Mundo':
        
                
        st.markdown('# IDH Mundo em 2020')

        filtered_data = pd.read_csv('IDH_mundo_2020_hdr.csv', sep = ";")
        
              
        mundo_countries = alt.topo_feature(
            "https://raw.githubusercontent.com/deldersveld/topojson/master/world-countries.json",
            "countries1",
            )
        mundo_chart = (
            alt.Chart(mundo_countries)
            .mark_geoshape(stroke="white", strokeWidth=1)
            .encode(
                color="value:Q",
                tooltip=[
                    alt.Tooltip("properties.name:O", title="País"),
                    alt.Tooltip("value:Q", title="Indicator value"),
                ],
            )
            .transform_lookup(
                lookup="properties.name",
                from_=alt.LookupData(filtered_data, "Countrie", ["value"]),
            )
        )
        st.altair_chart(mundo_chart)

        st.markdown('Fonte:http://hdr.undp.org/sites/default/files/hdr2020.pdf')


if pagina == 'Conclusão':
	st.markdown(""" 

	## **Conclusão**

	Nesse Web App mostramos o poder do streamlit para construir soluções interativas e que permitem uma usabilidade bastante ampla.
		
	Existe um universo de possibilidades que temos ao combinar\
		todos os recursos do streamlit com o que já temos no Python.
		
	Esse projeto me permitiu aprender e explorar recursos básicos de Altair, Streamlit, Geopandas e TopoJson\
		e fiquei impressionado com a capacidade do Streamlit de gerar todo o background web para publicação do web app\
        com uso de poucas linhas de código.

	Por fim podemos dizer que a exploração da visualização de dados com essas bibliotecas foi\
    bastante proveitoso.

	---
	
             """) 
	
	
#st.image('imagem_IPS.jpg', use_column_width = 'always')

if pagina == 'Código':
    st.markdown('''
		## **Código para gerar esse app**
		Também pode ser encontrado [aqui](https://github.com/w3gilberto/VIS)
		''')

