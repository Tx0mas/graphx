def fit(x,y,potencia):
    if len(x)!=len(y):
        exit("len(x)!=len(y)")
    else:
        #Queremos (V^t.V).a=V^t.y
        #V tiene la pinta
        #[1, x0, x0^2, ..., x0^degree]
        #[1, x1, x1^2, ..., x1^degree]

        #CREAMOS V
        V=[]
        for i in range(len(x)+1):
            fila=[]
            for k in range(potencia + 1):
                fila.append(x[i]**k)
            
            V.append(fila)
        
        #CALC V.V^t

        