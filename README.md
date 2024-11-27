# 3D-Structre-Prediction
A Docker image to predict the 3D structures of given sequences in a FASTA file

## Usage 
- Get the docker image from DokcerHub
```
docker pull mohmedsoudy/protein_structure_prediction:latest
```
- Run the Command 
```
docker run -v "$(pwd)/output:/app/output" -v "$(pwd)/sample_test_data.fasta:/app/sample_test_data.fasta" mohmedsoudy/protein_structure_prediction:latest -p "/app/sample_test_data.fasta" -o "/app/output/"
```
## Notes
- Make sure that you have a folder output in the directory where you run the command
- Change sample_test_data.fasta with your input FASTA file
