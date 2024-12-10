from .toast import flet_toast
import pkg_resources

if pkg_resources.get_distribution('flet').version < '0.25':
    print('Precisa ter a versão 0.25.1 no mínimo para usar o flet-toast 0.6.0\n')
    exit()