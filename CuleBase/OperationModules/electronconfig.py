ORBITALS = ['s','p','d','f','g','h','i']
ELEC_LIM = [2, 6, 10, 14, 18, 22, 26]



class ElectronConfig(object):

    def __init__(self, eCount:int, tag = ''):
        self._eCount = eCount
        self._tag = tag


    def GenerateConfiguration(self):
        orbitals = []
        el_count = []

        counter = 1
        pi = 1 #primary index, 'keeping track'
        si = 1 #secondary index, which orbital (see ORBITALS)
        ti = 1 #tertiary index, which principle quantum number

        while counter <= self._eCount:

            this_orbital = str(ti)+str(ORBITALS[si-1])

            if this_orbital not in orbitals:
                orbitals.append(this_orbital)
                el_count.append(0)

            if el_count[len(el_count)-1] < ELEC_LIM[si-1]:
                el_count[len(el_count)-1] += 1
                counter += 1
            else:
                if si == 1:
                    
                    if ti == 1: #base case 1
                        ti += 1
                        pi += 1
                    elif (ti == 2) or (ti == 3): #base case 2 and 3
                        si += 1
                    else: #all other cases
                        if ti % 2 != 0:
                            si = int(((ti-1)/2)+1)
                        else:
                            si = int((ti/2)+1)
                        ti = pi

                elif ((si > 1) and (si != pi)): #middle case
                    si -= 1
                    ti += 1
                    
                elif si == pi: #edge case
                    si -= 1
                    pi += 1
                    ti = pi

        ECONFIG = ''
        for i in range (0, len(orbitals)):
                ECONFIG += orbitals[i]+str(el_count[i])
                if i != len(orbitals)-1:
                    ECONFIG += ','

        return ECONFIG
