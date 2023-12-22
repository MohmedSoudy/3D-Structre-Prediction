import os
import sys
import argparse
import shutil
import subprocess

def parse(args=None):
    '''arguments.
    '''
    parser = argparse.ArgumentParser(prog='3D-Structure-Prediction',
                                     description='Running colabfold for 3D structure prediction',
                                     epilog='(c) authors')
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s ' + '1',
                        help="Show program's version number and exit.")
    parser.add_argument('-p', '--path',
                        help='path to fasta file',
                        required=True)
    parser.add_argument('-o', '--out',
                        help='path to output directory',
                        required=True)
    results = parser.parse_args(args)
    return results

def run_prediction(fasta_path, output_path):
    """split fasta file into multiple files in a folder 

    Args:
        fasta_path (str): path to fasta file 
        output_path (str): path to output folder 
    """
    filename = os.path.splitext(os.path.basename(fasta_path))[0]
    os.mkdir(filename)
    new_path = filename + "/" + filename + ".fasta"
    shutil.copy(fasta_path, new_path)
    print("Start processing FASTA files...")
    os.chdir(filename)
    fasta_file = os.path.basename(new_path)
    command = ['awk', '/^>/ { file=substr($1,2) ".fasta" } { print > file }', fasta_file]
    subprocess.run(command, check=True)    
    os.remove(fasta_file)
    print("Processing FASTA files Finished...")
    log_path = filename + "_log.txt"
    print("We are starting predictions now...")
    os.system("/app/localcolabfold/colabfold-conda/bin/colabfold_batch " + "." + "/ " + output_path + "/ " + ">> " + log_path)
    

    
def main():
    args = parse(sys.argv[1:])
    if args.path and args.out:
        print('Analysis Started....')
        run_prediction(args.path, args.out)
        print('Analysis Finished!')
        
if __name__ == '__main__':
    main()