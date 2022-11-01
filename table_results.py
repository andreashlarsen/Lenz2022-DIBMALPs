import numpy as np
import os

data_elements = [\
['154_J1_POPC_R2'],\
['154_J2_POPC_R4'],\
['154_J3_POPC_10CHOL_R4'],\
['154_J4_POPC_20CHOL_R4'],\
['154_J5_POPC_20CHOL_R8'],\
['196_J12_POPC_30CHOL_R4'],\
['154_J6_DMPC_R05'],\
['154_J7_DMPC_R1'],\
['154_J8_DMPC_R2'],\
['196_J9_DMPC_10CHOL_R2'],\
['196_J10_DMPC_20CHOL_R2'],\
['196_J11_DMPC_30CHOL_R2']\
]
os.system('mkdir -p output')

print('\n')
#for model in [11,19]:
for model in [11]:

    ## list of fit parameter names (model-dependent)
    if model == 11:
        names = ['poly_pr_lip ','scale_V_poly0 ','N_lip ','eps ','sigma_roughness','scale ','background ']
    elif model in [19]:
        names = ['poly_pr_lip ','scale_V_poly0 ','N_lip ','eps ','scale ','background ']
    else:
        print('\nvariable \'model\' is not in the list of models\n\n')
        exit()
    N = len(names)

    names_derived = ['r =','R ','h ','L =','N_poly ','T ']

    ## generate output file
    filename_out = 'output/output_model%d.txt' % model
    f_out = open(filename_out,'w')
    f_out.close()

    ## open output file
    f_out = open(filename_out,'a')

    ### write header in output file
    f_out.write('%-23s' % 'dataset')
    for n in names:
        #f_out.write('%-21s' % n)
        f_out.write(n.center(21))
    f_out.write('%-15s' % 'chi2r')
    for n in names_derived:
        f_out.write('%-15s' % n)
    f_out.write('%-25s' % 'R_major = r*eps+T')
    f_out.write('%-25s' % 'R_mean = (R_major+R)/2')
    f_out.write('\n\n')

    ## read fit parameter values and write to output file
    average = np.zeros(N)
    for d in data_elements:
        folder = d[0]
        if folder == '154_J6_DMPC_R05':
            f_out.write('\n')
        f_out.write('%-23s' % folder)
        filename_in = 'model_%d/%s/fit.log' % (model,folder) 
        f_in = open(filename_in,'r')
        line = f_in.readline()
        while line:
            for i in range(N):
                if names[i] in line:
                    dummy = line.split('fit =')[1]
                    p = float(dummy.split('+/-')[0])
                    dummy2 = dummy.split('+/-')[1]
                    dp = float(dummy2.split('(')[0])
                    if names[i] == 'N_lip ':
                        #f_out.write('%-15.1f' % p)
                        f_out.write('%8.1f +/- %-8.1f' % (p,dp))
                        dN_rel = dp/p # save for calculatioin of uncertainty of R_minor
                    elif names[i] in ['background ','scale ']:
                        #f_out.write('%-15.1e' % p)
                        f_out.write('%8.1e +/- %-8.1e' % (p,dp))
                    else:
                        #f_out.write('%-15.2f' % p)
                        f_out.write('%8.3f +/- %-8.3f' % (p,dp))

                    if names[i] == 'eps ':
                        eps = p # used later
                        deps_rel = dp/p # save for calculation of uncertainty for R_major
                    average[i] += p

            ## Chi2r
            if 'Chi2r ' in line:
                chi2r = float(line.split('=')[1])
                f_out.write('%-15.1f' % chi2r)

            ## derived parameters
            for name in names_derived:
                if name in line and 'Chi2r' not in line and 'dp_h' not in line:
                    p = float(line.split('=')[1])
                    f_out.write('%-15.2f' % p)
                    if name == 'T ':
                        T = p
                    if name == 'r =':
                        r = p
            line = f_in.readline()
        R_minor = r+T
        ## R_minor has samre relative uncertainty as N:
        dR_minor = dN_rel*R_minor
        R_major = r*eps+T
        ## R_major uncertainty found by error propagation
        dR_major = np.sqrt(dN_rel**2+deps_rel**2)*R_major
        #print(R_minor)
        R_mean = (R_major+R_minor)/2
        ## R_mean uncertainty found by error propagation
        dR_mean = np.sqrt(dR_minor**2+dR_major**2)/2
        f_out.write('%10.2f +/- %-10.2f' % (R_major,dR_major))
        f_out.write('%10.2f +/- %-10.2f' % (R_mean,dR_mean))
        f_out.write('\n') 
        f_in.close()

    ## print average values
    f_out.write('\n') 
    average /= len(data_elements)
    f_out.write('%-23s' % 'average')
    for i in range(N):
        if names[i] == 'N_lip ':
            f_out.write('%-21.1f' % average[i])
        elif names[i] in ['background ','scale ']:
            f_out.write('%-21.1e' % average[i])
        else:
            f_out.write('%-21.2f' % average[i])

    #Major_axis = r*eps+T
    
    ## wrap up 
    print('output table: %s' % filename_out)
    f_out.close()
print('\n')
