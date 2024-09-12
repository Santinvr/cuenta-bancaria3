__author__= "ian ordoñez"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ian.ordonez@campusucc.edu.co"

from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from Tiempo import Tiempo
from CDT import CDT

class CuantaBancaria:
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Atributos
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    NombreCliente = ""
    NumeroCedula = ""
    MesActual = Tiempo()
    
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Asociaciones 
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    CuentaCorriente= CuentaCorriente()
    CuentaAhorros= CuentaAhorros()
    CDT= CDT()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Metodos 
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def darNombreCliente(self):
    return self.Nombre_Cliente

__method__= "DepositarLaCuentaCorriente"
__parameter__= "monto"
__return__= "ninguno"
__description___="Muestra el saldo total de todas las cuentas"
def depositarCuentaCorriente(self, monto):
    self.__CuentaCorriente.ConsignarValor(monto)

__method__ = "PasarCuentaAhorrosCuentaCorriente"
__parameter__= "ninguno"
__return__= "ninguno"
__description__= "Metodo que permite pasar el saldo de la cuenta de ahorros a la cuenta corriente"
def pasarCuentaAhorrosCuentaCorriente(self):
    saldoAhorros = self.__CuentaAhorros.darSaldo()
    self.__CuentaAhorros.RetirarValor(saldoAhorros)
    self.__CuentaCorriente.ConsignarValor(saldoAhorros)
    
__method__= "RetirarAhorros"
__parameter__ = "monto"
__return__ = "ninguno"
__description__= "Metodo que permite retirar un saldo de la cuenta ahorros"
def retirarAhorro(self,monto):
    self.__CuentaAhorros.RetirarValor(monto)
    
    
__method__ = "DarSaldoCorriente"
__parameter__= "ninguno"
__return__= "ninguno"
__description__= "Metodo que permite dar el saldo de la cuenta corriente"
def darSaldoCorriente(self):
    self.__cuentaCorriente.darSaldo()


__method__ = "RetirarTodo"
__parameter__ = "ninguno"
__return__= "ninguno"
__description__= "Metodo de retirar el saldo existente de la cuenta ahorros y de la cuenta corriente"
def retirarTodo(self):
    self.__CuentaAhorros.retirarValor(self.__CuentaAhorros.darSaldo())
    self.__CuentaCorriente.retirarValor(self.__CuentaCorriente.darSaldo())
    
    
__method__ = "duplicarAhorro"
__parameter__= "ninguno"
__return__ = "ninguno"
__description__ = "Metodo que se duplica el valor existente de la cuenta"
def duplicarAhorro(self):
    self.__Cuenta.consignarSaldo(self.__Cuenta.darSaldo())
        
        
__method__= "CalcularElSaldoTotal"
__parameter__ = "None"
__return__ = 'saldo total de totas las cuentas'
__description__= 'Muestra el saldo total actual en todas las cuentas'
def calcularSaldoTotal(self):
    return self.__cuentaCorriente.darSaldo() + self.__cuentaCorriente.darSaldo() + self.__CDT.darSaldo()