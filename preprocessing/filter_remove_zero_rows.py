'''
   After running this code using the input file transcript_rpkm_in_go.txt,
    the new file should have 64429 transcripts.

'''


"""
*********************
        Main
*********************
"""
if __name__ == "__main__":

    path_to_rpkm_file = '../../../../Documents/Stanford/CS341_Data/transcript_rpkm_in_go.txt'
    path_to_new_rpkm_file =  '../../../../Documents/Stanford/CS341_Data/transcript_rpkm_in_go_nonzero_exp.txt'
    rpkm_file = open(path_to_rpkm_file)
    new_rpkm_file = open(path_to_new_rpkm_file, 'w')

    firstLine = True
    num_rows_retained = 0
    for line in rpkm_file:
        if firstLine:
            firstLine = False
            new_rpkm_file.write(line)
            continue

        exp_levels = line.rstrip().split('\t')[4:]
        nonzero = False
        for exp_level in exp_levels:
            if float(exp_level) != 0:
                nonzero = True
                break

        if nonzero:
            num_rows_retained += 1
            new_rpkm_file.write(line)

    print num_rows_retained
