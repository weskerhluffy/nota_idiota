'''
Created on 16/03/2017

@author: ernesto
'''
import logging

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None


def ransom_note(magazine, ransom):
    mapa_maga = {}
    mapa_ransom = {}
    logger_cagada.debug("la maga %s" % magazine)
    logger_cagada.debug("el ransom %s" % ransom)
    
    for fag in magazine:
        if(fag not in mapa_maga):
            mapa_maga[fag] = 1
        else:
            mapa_maga[fag] += 1
            
    logger_cagada.debug("el conteo magaz %s" % mapa_maga)
    for ransi in ransom:
        if(ransi not in mapa_ransom):
            mapa_ransom[ransi] = 1
        else:
            mapa_ransom[ransi] += 1
    logger_cagada.debug("el conteo ranson %s" % mapa_ransom)
    
    for ransi in ransom:
        num_mag = mapa_maga.setdefault(ransi, 0)
        num_rans = mapa_ransom[ransi]
        
        if(num_mag < num_rans):
            return False
    
    return True

    



if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)

    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")
