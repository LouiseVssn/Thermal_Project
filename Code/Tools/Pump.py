import scipy.integrate as intgr
from scipy.optimize import fsolve
from CoolProp.CoolProp import PropsSI  # Import du module PropsSI de CoolProp


class Pump1(object):

    def __init__(self, orc_instance):
        """
        Initialisation de la classe Pump1
        :param params: Liste des paramètres [p_in, p_out, T_in, eta_pump]
        :param orc_instance: Instance de la classe ORC pour accéder à fluid
        """

        self.orc = orc_instance
        self.fluid = self.orc.fluid  # Accès direct au fluide via ORC
        self.eta_pump = self.orc.eta_pump_1
        self.p_in = self.orc.p_6
        self.p_out = self.orc.r_pump_1 * self.orc.p_6
        self.T_in = self.orc.T_6

    def CP(self, T, p):
        """
        Calcul de la capacité calorifique spécifique (cp) pour une température et pression données
        :param T: Température en K
        :param p: Pression en Pa
        :param fluid: Nom du fluide (string)
        :return: Capacité calorifique spécifique en J/(kg.K)
        """
        return PropsSI('C', 'T', T, 'P', p, self.fluid)

    def T_out_func(self, T_guess, args):
        """
        Fonction pour calculer la sortie de température T_out par résolution.
        :param T_guess: Température supposée en K
        :param args: Arguments supplémentaires [T_in, p_in, p_out]
        :return: Équation à résoudre pour fsolve
        """
        T_in, p_in, p_out = args
        p_av = (p_in + p_out) / 2  # Pression moyenne

        # Calcul de la densité moyenne
        rho_av = intgr.quad(
            lambda T: PropsSI('D', 'T', T, 'P', p_av, self.fluid),
            T_in, T_guess
        )[0] / (T_guess - T_in)

        # Calcul de la capacité calorifique moyenne
        cp_av = intgr.quad(
            lambda T: self.CP(T, p_av),
            T_in, T_guess
        )[0] / (T_guess - T_in)

        # Équation pour fsolve
        return T_guess - T_in - (p_out - p_in) / (self.eta_pump * cp_av * rho_av)

    def evaluate_T_out(self):
        """
        Évaluation de la température de sortie (T_out) via fsolve
        """
        self.arg_T_out = [self.T_in, self.p_in, self.p_out]  # Arguments pour la fonction
        self.T_out = fsolve(self.T_out_func, self.T_in * 1.05, args=self.arg_T_out)[0]
        return self.T_out
       
class Pump2(object):

    def __init__(self, orc_instance):
        """
        Initialisation de la classe Pump1
        :param params: Liste des paramètres [p_in, p_out, T_in, eta_pump]
        :param orc_instance: Instance de la classe ORC pour accéder à fluid
        """
        self.orc = orc_instance
        self.fluid = self.orc.fluid  # Accès direct au fluide via ORC
        self.eta_pump = self.orc.eta_pump_2
        self.p_in = self.orc.p_1
        self.p_out = self.orc.r_pump_2 * self.orc.p_1
        self.T_in = self.orc.T_1
    def CP(self, T, p):
        """
        Calcul de la capacité calorifique spécifique (cp) pour une température et pression données
        :param T: Température en K
        :param p: Pression en Pa
        :param fluid: Nom du fluide (string)
        :return: Capacité calorifique spécifique en J/(kg.K)
        """
        return PropsSI('C', 'T', T, 'P', p, self.fluid)

    def T_out_func(self, T_guess, args):
        """
        Fonction pour calculer la sortie de température T_out par résolution.
        :param T_guess: Température supposée en K
        :param args: Arguments supplémentaires [T_in, p_in, p_out]
        :return: Équation à résoudre pour fsolve
        """
        T_in, p_in, p_out = args
        p_av = (p_in + p_out) / 2 

       
        rho_av = intgr.quad(
            lambda T: PropsSI('D', 'T', T, 'P', p_av, self.fluid),
            T_in, T_guess
        )[0] / (T_guess - T_in)

        
        cp_av = intgr.quad(
            lambda T: self.CP(T, p_av),
            T_in, T_guess
        )[0] / (T_guess - T_in)

        
        return T_guess - T_in - (p_out - p_in) / (self.eta_pump * cp_av * rho_av)

    def evaluate_T_out(self):
        """
        Évaluation de la température de sortie (T_out) via fsolve
        """
        self.arg_T_out = [self.T_in, self.p_in, self.p_out]  # Arguments pour la fonction
        self.T_out = fsolve(self.T_out_func, self.T_in * 1.05, args=self.arg_T_out)[0]

        return self.T_out