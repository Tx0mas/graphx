import numpy as np
import matplotlib.pyplot as plt

class PolynomialM:
    def __init__(self,x,y,coef,x_err=None,y_err=None):
        self.x_data=np.array(x)
        self.y_data=np.array(y)        
        self.coef=coef

    def predecir(self,x):
        x=np.array(x)
        y=np.polyval(self.coef,x)
        return y
    def plot(self):
        #Trabajemos con plt.
        x_min=min(self.x_data)
        x_max=max(self.x_data)

        grilla_x=np.linspace(x_min,x_max,200)
        y_en_grilla=np.polyval(self.coef,grilla_x)
        
        plt.scatter(self.x_data,self.y_data,color="blue", label="Datos")
        plt.plot(grilla_x,y_en_grilla, color="red", label="Ajuste polinómico")
        plt.errorbar(x,y,yerr=y_err,xerr=x_err, fmt='o', capsize=5)
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Ajuste polinómico")
        plt.grid(True)
        plt.show()



def fit(x,y,coef):
    coeffs = np.polyfit(x, y, coef)
    model = PolynomialM(x,y, coeffs)
    return model
