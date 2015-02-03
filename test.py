select DMS=(r;DMS)
select DMS_res, br. polymer within 4 of DMS
label DMS_res, resn
stored.residues = []
iterate DMS_res, stored.residues.append(resn)


#########################################

cmd.select("DMS", 'resn DMS' )
cmd.select ("waters","resn %s around %s" % ('DMS',4))
cmd.iterate('sele', stored.residues.append('resn'))