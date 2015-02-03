#
# -- basicCodeBlock.py
#
from pymol import cmd, stored
 
def yourFunction( arg1, items = [] ):
    '''
DESCRIPTION
 
    Brief description what this function does goes here
    '''
    #
    # Your code goes here
    #

    f = open("residues.txt","a")

    for x in items:
        stored.residues = []
        check = []
        f.write(arg1 + '\n')
        f.write(x + '\n')
        cmd.select(x, 'resn ' + x )
        cmd.select (x+"_res","resn %s around %s" % (x,4))
        cmd.iterate(x+'_res', 'stored.residues.append(resn + resi)')

        for j in xrange(0,len(stored.residues)):
            if not(stored.residues.index(stored.residues[j]) < j):
                f.write(stored.residues[j] + ",")
        f.write('\n')



cmd.extend( "yourFunction", yourFunction );