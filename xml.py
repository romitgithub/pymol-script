#!/usr/bin/env python

# import xml.etree.ElementTree as ET
# tree = ET.parse('http://www.rcsb.org/pdb/rest/ligandInfo?structureId=1f88')
# root = tree.getroot()

# f = open("ligands.txt","a")

# for subroot in root:
# 	for child in subrot:
# 		print child.attrib['chemicalID']

# for child in root:
# 	f.write(child[1].text)

with open ("meta.txt", "r") as myfile:
    data=myfile.readlines()

f = open("residues.txt","a")

for item in data:
	item = item.replace("\n","")
	item = item.split(',')
	f.write(item[0] + '\n')
	items = [item[1], item[2]]
	cmd.reinitialize()
	cmd.load('http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId='+item[0])

	for x in items:
		stored.residues = []
        check = []
        f.write(x + '\n')
        cmd.select(x, 'resn ' + x )
        cmd.select (x+"_res","resn %s around %s" % (x,4))
        cmd.iterate(x+'_res', 'stored.residues.append(resn + resi)')

        for j in xrange(0,len(stored.residues)):
            if not(stored.residues.index(stored.residues[j]) < j):
                f.write(stored.residues[j] + ",")
        f.write('\n')
