#
#===IMPORT PACKAGES============================================================
#
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI
from scipy import integrate as integrate
from scipy.optimize import fsolve
import numpy as np
from math import exp
import scipy.integrate as spi
from math import log


class ORC(object):

    def __init__(self,inputs,parameters,display):

        self.display          = display
        self.T_max            = parameters['T_max']
        self.r_pump_1         = parameters['r_pump_1']
        self.r_pump_2         = parameters['r_pump_2']
        self.fluid            = parameters['fluid']
        self.k_cc_ex1         = parameters['k_cc_ex1']
        self.k_cc_ex2         = parameters['k_cc_ex2']
        self.T_cold_fluid_in  = parameters['T_cold_fluid_in']
        self.T_cold_fluid_out = parameters['T_cold_fluid_out']
        self.cold_fluid       = parameters['cold_fluid']
        self.T_pinch_ex = 1


        # Contraintes
        self.x6 = self.x1 = self.x2 = 0

       

    def T_pinch_cd(self,T5, T_cold_in, T_cold_out):

        return 1

    
    def evaluate(self):



        #region ETATS

        # region ETAT 6

        self.T_6 = self.T_cold_fluid_in + 1#self.T_pinch_cd()
        self.p_6 = PropsSI("P","T",self.T_6,"Q",self.x6,'H2O')
        #self.h_6 = PropsSI("")

        # region ETAT 3
        self.T_3 = self.T_max
        self.p_3 = 1



        # endregion ETAT3

        self.T_1 = 0

        # endregion
        # Rendements
 
        self.eta_toten = 0.4


        if self.display:
            print('Hello')
            print("P6 === ",self.p_6/1000,"kPa")


