export PYTHONPATH=$PWD
`python3 services/rawTensor/rawTensor.py --interface ovtk  --device CPU --serving_mounted_modelDir /home/intel/anoob/aid/test/ai-dispatcher/models/ --remote_port 50055` 1>&3
