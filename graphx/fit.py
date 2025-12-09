import numpy as np
import matplotlib.pyplot as plt

class PolynomialM:
    def __init__(self,x,y,coef,x_err=None,y_err=None):
        self.x_data=np.array(x)
        self.y_data=np.array(y)        
        self.coef=coef
        self.x_err = np.array(x_err) if x_err is not None else None
        self.y_err = np.array(y_err) if y_err is not None else None

    def predecir(self,x):
        return np.polyval(self.coef, np.array(x))
    def plot(self):
        #Trabajemos con plt.
        x_min=min(self.x_data)
        x_max=max(self.x_data)

        grilla_x=np.linspace(x_min,x_max,200)
        y_en_grilla=np.polyval(self.coef,grilla_x)
        
        plt.scatter(self.x_data,self.y_data,color="blue", label="Datos")
        plt.plot(grilla_x,y_en_grilla, color="red", label="Ajuste polinómico")
        plt.errorbar(self.x_data, self.y_data,
             yerr=self.y_err if hasattr(self, 'y_err') else None,
             xerr=self.x_err if hasattr(self, 'x_err') else None,
             fmt='o', capsize=5)
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Ajuste polinómico")
        plt.grid(True)
        plt.show()
def fit(x, y, coef, x_err=None, y_err=None):
    coeffs = np.polyfit(x, y, coef)
    model = PolynomialM(x, y, coeffs, x_err=x_err, y_err=y_err)
    return model



def fit(x, y, coef, x_err=None, y_err=None):
    coeffs = np.polyfit(x, y, coef)
    model = PolynomialM(x, y, coeffs, x_err=x_err, y_err=y_err)
    return model

