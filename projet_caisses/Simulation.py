from Event import *
from Fct_alea import *
import Fct_alea as fct
from alea import *
from File import *
import streamlit as st 
import pandas 
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from random import randint
import json
st.set_option('deprecation.showPyplotGlobalUse', False)
sidebar_options=st.sidebar.selectbox(
    "Options",
    ("Presentation","Simulation","Comparaison")
    )

liste_information3=[]
liste_information2=[]


if sidebar_options == "Presentation":
    #st.title("Presentation")
        
        st.title("Presentation Generale du projet")
        st.write("Dans le cadre du cours de simulation, notre équipe sous la tutelle de notre professeur Mme. Khadija EL OUAZZANI TOUHAMI a mené un mini projet de simulation. ")        
        st.write("Dans ce mini projet, on s’est intéressé au problème du super marché tel que décrit dans le cours. Le but de cette simulation est de mesurer l’impact de l’ajout d’une 3ème caisse sur le nombre de clients perdus.")
        st.write("En se basant sur nos connaissances et ce qu’on a appris durant ce cours, et en utilisant le langage Python et le Framework Streamlit, on a réussi à développé une solution de simulation correspondante à notre problématique, avec une interface simple et soignée qui va permettre l’affichage des indicateurs et les graphes correspondants aux différentes manipulations possibles. ")

if(sidebar_options == "Simulation"): 
    st.title("Entrer les valeurs correspondantes ")
    st.write("")
    #IX1=st.text_input('IX','100')
    #IY1=st.text_input('IY','200')
    #IZ1=st.text_input('IZ','300')
    st.sidebar.write("")
    st.sidebar.write("Choisir les germes")
    IX1= st.sidebar.slider('IX', min_value=100, max_value=1000,
                             value=200,  step=10)
    IY1= st.sidebar.slider('IY', min_value=100, max_value=1000,
                             value=750,  step=10)
    
    IZ1= st.sidebar.slider('IZ', min_value=100, max_value=1000,
                             value=500,  step=10)
    
    st.sidebar.write("")
    genre = st.sidebar.radio(
     "Quel est le nombre de caisse ?",
     ('2', '3'))
    st.title("Tableau des valeurs")
    cols = st.columns(10)
    cols[0].write("Numero")
    cols[1].write("NCP")
    cols[2].write("NCE")
    cols[3].write("DFS")   
    cols[4].write("Tsmoy") 
    cols[5].write("TATmoy")
    cols[6].write("PN")
    cols[7].write("PP")
    #cols[9].write("CAM")
    cols[8].write("NCPC")
    button=st.sidebar.button("Envoyer")
    if(button):
        if genre == '3':
            st.write('You selected 3.')
            
        
            IX=int(IX1)
            IY=int(IY1)
            IZ=int(IZ1)
            aleat=Alea(IX,IY,IZ)
            #st.write("#######################")
            
                    
            compteur=0
            file=file()
            while(compteur<40):
                H=0
                i=1
                LQ=0
                fct.pn=0
                fct.pp=0
                CAM=0
                NCPC=0
                NCP=0
                NCE=0
                C1=0
                C2=0
                C3=0
                alea=aleat
                #alea=Alea(1600,980,1299)
                file.file=[]
                calendrier=[]
                historique=[]
                def create(ref,type,date):
                    event=Evenement(ref,type,date)
                    return (event)
                
                def ajouter_event(calendrier,event):
                    calendrier.append(event)
                    trier_calendrier(calendrier)
                
                def planifier_evt(ref,type,date):
                    global calendrier
                    e=create(ref,type,date)
                    ajouter_event(calendrier,e)
                    print(e.afficher_event())
                
                
                def selectionner_evt(calendrier):
                    global H
                    trier_calendrier(calendrier)
                    if (len(calendrier)>0):
                        a=calendrier.pop(0)
                        historique.append(a)
                        return (a)
                    else:
                        return ("calendrier vide")
                
                
                def trier_calendrier(calendrier):
                    n= len(calendrier)
                    # Traverser tous les éléments du tableau
                    for i in range(n):
                        for j in range(0, n - i - 1):
                            # échanger si l'élément trouvé est plus grand que le suivant
                            if calendrier[j].date > calendrier[j + 1].date:
                                calendrier[j], calendrier[j + 1] = calendrier[j + 1], calendrier[j]
                
                
                
                
                def arrivee(ref):
                    global NCE,NCP,i,alea,H
                    if(LQ<=1):
                        NCE=NCE+1
                        planifier_evt(ref,"FM",H+F2(alea.alea()))
                    else:
                        NCP=NCP+1
                    i=i+1
                    DA=H+F1(alea.alea())
                    if (DA<=720):
                        planifier_evt(i,"A",DA)
                
                def fin_magasinage(ref):
                    global C1,C2,C3,LQ,file,NCPC
                    aleatoire=randint(1,100)
                    if(aleatoire<85):
                        
                        if(C1==0 or C2==0 or C3==0):
                            if(C1==0):
                                C1=ref
                            elif(C2==0):
                                C2=ref
                            elif(C3==0):
                                C3=ref
                            planifier_evt(ref,"FP",H+F3(alea.alea()))
                        else:
                            LQ=LQ+1
                            file.enfiler(ref)
                    else:
                        NCPC=NCPC+1
                        planifier_evt(ref,"FP",H+0)
                
                def fin_paiment(ref):
                    global LQ,C1,C2,C3,file,alea,H
                    if(LQ==0):
                        if(C1==ref):
                            C1=0
                        elif(C2==ref):
                            C2=0
                        elif(C3==ref):
                            C3=0
                    else:
                        j=file.file[0]
                        file.defiler()
                        LQ=LQ-1
                        if(C1==ref):
                            C1=j
                        elif(C2==ref):
                            C2=j
                        elif(C3==ref):
                            C3=j
                        planifier_evt(j,"FP",H+F3(alea.alea()))
                
                
                def calculerTsmoy(NCE):
                    l=[]
                    for i in range(len(historique)):
                        if historique[i].type=="A":
                            for j in range(i,len(historique)):
                                if(historique[j].type=="FP" and historique[j].reference==historique[i].reference):
                                    a=abs(historique[i].date-historique[j].date)
                                    l=l+[a]
                    s = 0
                    for i in range(len(l)):
                        s = s + l[i]
                    return (s / NCE)
                
                def calculerTATmoy(NCE):
                    l=[]
                    for i in range(len(historique)):
                        if historique[i].type=="FM":
                            for j in range(i,len(historique)):
                                if(historique[j].type=="FP" and historique[j].reference==historique[i].reference):
                                    a=abs(historique[i].date-historique[j].date)
                                    l=l+[a]
                    s = 0
                    for i in range(len(l)):
                        s = s + l[i]
                    return (s / NCE)
                
                def calculerGermes(IX,IY,IZ):
                    IX=IX+5
                    IY=IY+5
                    IZ=IZ+5
                    return (IX,IY,IZ)
                
                def cam():
                    global CAM
                    for i in range(len(historique)):
                        for j in range(i,len(historique)):
                            if(historique[i].date==historique[j].date):
                                CAM=1+CAM
                
                #---------Programme Principale-----------------
                planifier_evt(1,"A",F1(alea.alea()))
                while(len(calendrier)!=0):
                    
                    fct.date = calendrier[-1].date
                    a=selectionner_evt(calendrier)
                    H=a.date
                    if(a.type=="A"):
                        arrivee(a.reference)
                    if(a.type=="FM"):
                        fin_magasinage(a.reference)
                    if(a.type=="FP"):
                        fin_paiment(a.reference)
                DFS=H
                #print(NCP,NCE,DFS)
                Tsmoy=round(calculerTsmoy(NCE),3)
                TATmoy=round(calculerTATmoy(NCE),3)
                IX=IX+5
                IY=IY+5
                IZ=IZ+5
                
            
                liste_information3 +=[[NCP,NCE,DFS,Tsmoy,TATmoy]]
                
                
                
                cols[0].write(compteur+1)
                
                cols[1].write(liste_information3[int(compteur)][0])
                
                
                cols[2].write(liste_information3[int(compteur)][1])
                
                
                cols[3].write(liste_information3[int(compteur)][2])
                
                
                cols[4].write(liste_information3[int(compteur)][3])
                
                
                cols[5].write(liste_information3[int(compteur)][4])
                
                cols[6].write(fct.pn)
                cols[7].write(fct.pp)
                #cols[9].write(CAM)
                cols[8].write(NCPC)
                
                compteur=compteur+1
            
            
            
            with open("trois.txt", "w") as f:
                json.dump(liste_information3, f)
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][0] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCP"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)
            
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCP"
            )
            
            st.plotly_chart(fig)
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][1] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCE"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)  
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCE"
            )
            
            st.plotly_chart(fig)
            
            
            
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][2] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "DFS"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)
            
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "DFS"
            )
            
            st.plotly_chart(fig)
            
            
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][3] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "Tsmoy"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "Tsmoy"
            )
            
            st.plotly_chart(fig)
            
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][4] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "TATmoy"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "TATmoy"
            )
            
            st.plotly_chart(fig)
            
            
            
            
        else:
            st.write("You selected 2.")
        
            IX=int(IX1)
            IY=int(IY1)
            IZ=int(IZ1)
            aleat=Alea(IX,IY,IZ)
            #st.write("#######################")
            
                    
            compteur=0
            file=file()
            while(compteur<40):
                H=0
                i=1
                LQ=0
                NCP=0
                CAM=0
                fct.pn=0
                fct.pp=0
                NCPC=0
                NCE=0
                C1=0
                C2=0
                alea=aleat
                #alea=Alea(1600,980,1299)
                file.file=[]
                calendrier=[]
                historique=[]
                def create(ref,type,date):
                    event=Evenement(ref,type,date)
                    return (event)
                
                def ajouter_event(calendrier,event):
                    calendrier.append(event)
                    trier_calendrier(calendrier)
                
                def planifier_evt(ref,type,date):
                    global calendrier
                    e=create(ref,type,date)
                    ajouter_event(calendrier,e)
                    print(e.afficher_event())
                
                
                def selectionner_evt(calendrier):
                    global H
                    trier_calendrier(calendrier)
                    if (len(calendrier)>0):
                        a=calendrier.pop(0)
                        historique.append(a)
                        return (a)
                    else:
                        return ("calendrier vide")
                
                
                def trier_calendrier(calendrier):
                    n= len(calendrier)
                    # Traverser tous les éléments du tableau
                    for i in range(n):
                        for j in range(0, n - i - 1):
                            # échanger si l'élément trouvé est plus grand que le suivant
                            if calendrier[j].date > calendrier[j + 1].date:
                                calendrier[j], calendrier[j + 1] = calendrier[j + 1], calendrier[j]
                
                
                
                
                def arrivee(ref):
                    global NCE,NCP,i,alea,H
                    if(LQ<=1):
                        NCE=NCE+1
                        planifier_evt(ref,"FM",H+F2(alea.alea()))
                    else:
                        NCP=NCP+1
                    i=i+1
                    DA=H+F1(alea.alea())
                    if (DA<=720):
                        planifier_evt(i,"A",DA)
                
                def fin_magasinage(ref):
                    global C1,C2,LQ,file,NCPC
                    aleatoire=randint(1,100)
                    if(aleatoire<85):
                        if(C1==0 or C2==0):
                            if(C1==0):
                                C1=ref
                            elif(C2==0):
                                C2=ref
                            planifier_evt(ref,"FP",H+F3(alea.alea()))
                        else:
                            LQ=LQ+1
                            file.enfiler(ref)
                    else:
                        NCPC=NCPC+1
                        planifier_evt(ref,"FP",H+0)
                
                def fin_paiment(ref):
                    global LQ,C1,C2,file,alea,H
                    if(LQ==0):
                        if(C1==ref):
                            C1=0
                        elif(C2==ref):
                            C2=0
                    else:
                        j=file.file[0]
                        file.defiler()
                        LQ=LQ-1
                        if(C1==ref):
                            C1=j
                        elif(C2==ref):
                            C2=j
                        planifier_evt(j,"FP",H+F3(alea.alea()))
                
                
                def calculerTsmoy(NCE):
                    l=[]
                    for i in range(len(historique)):
                        if historique[i].type=="A":
                            for j in range(i,len(historique)):
                                if(historique[j].type=="FP" and historique[j].reference==historique[i].reference):
                                    a=abs(historique[i].date-historique[j].date)
                                    l=l+[a]
                    s = 0
                    for i in range(len(l)):
                        s = s + l[i]
                    return (s / NCE)
                
                def calculerTATmoy(NCE):
                    l=[]
                    for i in range(len(historique)):
                        if historique[i].type=="FM":
                            for j in range(i,len(historique)):
                                if(historique[j].type=="FP" and historique[j].reference==historique[i].reference):
                                    a=abs(historique[i].date-historique[j].date)
                                    l=l+[a]
                    s = 0
                    for i in range(len(l)):
                        s = s + l[i]
                    return (s / NCE)
                
                def calculerGermes(IX,IY,IZ):
                    IX=IX+5
                    IY=IY+5
                    IZ=IZ+5
                    return (IX,IY,IZ)
                
                
                def cam():
                    global CAM
                    for i in range(len(historique)):
                        for j in range(i,len(historique)):
                            if(historique[i].date==historique[j].date):
                                CAM=1+CAM
                
                
                #---------Programme Principale-----------------
                planifier_evt(1,"A",F1(alea.alea()))
                while(len(calendrier)!=0):
                    
                    fct.date = calendrier[-1].date
                    a=selectionner_evt(calendrier)
                    H=a.date
                    if(a.type=="A"):
                        arrivee(a.reference)
                    if(a.type=="FM"):
                        fin_magasinage(a.reference)
                    if(a.type=="FP"):
                        fin_paiment(a.reference)
                    
                DFS=H
                #print(NCP,NCE,DFS)
                Tsmoy=round(calculerTsmoy(NCE),3)
                TATmoy=round(calculerTATmoy(NCE),3)
                IX=IX+5
                IY=IY+5
                IZ=IZ+5
            
                
                liste_information2+=[[NCP,NCE,DFS,Tsmoy,TATmoy]]
                
                cols[0].write(compteur+1)
                
                cols[1].write(liste_information2[int(compteur)][0])
                
                
                cols[2].write(liste_information2[int(compteur)][1])
                
                
                cols[3].write(liste_information2[int(compteur)][2])
                
                
                cols[4].write(liste_information2[int(compteur)][3])
                
                
                cols[5].write(liste_information2[int(compteur)][4])
                
                cols[6].write(fct.pn)
                cols[7].write(fct.pp)
                #cols[9].write(CAM)
                cols[8].write(NCPC)
                
                compteur=compteur+1
            
            
            
            with open("deux.txt", "w") as f:
                json.dump(liste_information2, f)
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][0] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCP"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCP"
            )
            
            st.plotly_chart(fig)
            
            
            
            
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][1] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCE"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)  
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "NCE"
            )
            
            st.plotly_chart(fig)
            
            
            
            
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][2] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "DFS"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)
            
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "DFS"
            )
            
            st.plotly_chart(fig)
            
            
            
            
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][3] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "Tsmoy"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "Tsmoy"
            )
            
            st.plotly_chart(fig)
            
            
            
            
            df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][4] for i in range(40)] 
            ))
        
            #The plot
            fig = px.line(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "TATmoy"
            )
            fig.update_traces(line_color = "maroon")
            st.plotly_chart(fig)  
            
            
            
            fig = px.bar(        
                df, #Data Frame
                x = "essaie", #Columns from the data frame
                y = "valeur",
                title = "TATmoy"
            )
            
            st.plotly_chart(fig)
            
if(sidebar_options == "Comparaison"):
    liste_information3=[]
    liste_information2=[]
    #d = st.sidebar.checkbox('Deux Caisses')
    #t = st.sidebar.checkbox('Troisieme Caisse')
    with open("trois.txt") as f:
        liste_information3 = json.load(f)
        
    with open("deux.txt") as f:
        liste_information2 = json.load(f)
    print(liste_information3)
    
    st.write("NCP")
    df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][0] for i in range(40)] 
            ))
    
    df2 = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][0] for i in range(40)] 
            ))
       
    fig = go.Figure()
    
    
    fig.add_trace(go.Scatter(x=df['essaie'], y=df['valeur'],
                    mode='lines+markers',
                    name='Trois Caisses'))
    fig.add_trace(go.Scatter(x=df2['essaie'], y=df2['valeur'],
                    mode='lines+markers',
                    name='Deux Caisses'))

    #fig.show()
    
    st.plotly_chart(fig)
    
    
    
    
    st.write("NCE")
    df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][1] for i in range(40)] 
            ))
    
    df2 = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][1] for i in range(40)] 
            ))
       
    fig = go.Figure()
    
    
    fig.add_trace(go.Scatter(x=df['essaie'], y=df['valeur'],
                    mode='lines+markers',
                    name='Trois Caisses'))
    fig.add_trace(go.Scatter(x=df2['essaie'], y=df2['valeur'],
                    mode='lines+markers',
                    name='Deux Caisses'))

    #fig.show()
    
    st.plotly_chart(fig)
    
    
    
    
    st.write("DFS")
    df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][2] for i in range(40)] 
            ))
    
    df2 = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][2] for i in range(40)] 
            ))
       
    fig = go.Figure()
    
    
    fig.add_trace(go.Scatter(x=df['essaie'], y=df['valeur'],
                    mode='lines+markers',
                    name='Trois Caisses'))
    fig.add_trace(go.Scatter(x=df2['essaie'], y=df2['valeur'],
                    mode='lines+markers',
                    name='Deux Caisses'))

    #fig.show()
    
    st.plotly_chart(fig)
    
    
    
    
    
    st.write("Tsmoy")
    df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][3] for i in range(40)] 
            ))
    
    df2 = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][3] for i in range(40)] 
            ))
       
    fig = go.Figure()
    
    
    fig.add_trace(go.Scatter(x=df['essaie'], y=df['valeur'],
                    mode='lines+markers',
                    name='Trois Caisses'))
    fig.add_trace(go.Scatter(x=df2['essaie'], y=df2['valeur'],
                    mode='lines+markers',
                    name='Deux Caisses'))

    #fig.show()
    
    st.plotly_chart(fig)
    
    
    
    
    
    st.write("TATmoy")
    df = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information3[i][4] for i in range(40)] 
            ))
    
    df2 = pandas.DataFrame(dict(
            essaie = [i for i in range(40)],
            valeur = [liste_information2[i][4] for i in range(40)] 
            ))
       
    fig = go.Figure()
    
    
    fig.add_trace(go.Scatter(x=df['essaie'], y=df['valeur'],
                    mode='lines+markers',
                    name='Trois Caisses'))
    fig.add_trace(go.Scatter(x=df2['essaie'], y=df2['valeur'],
                    mode='lines+markers',
                    name='Deux Caisses'))

    #fig.show()
    
    st.plotly_chart(fig)
            
        
        