include .env
export $(cat .env | xargs)

reinstall_package:
	@pip uninstall -y oracle-prophecy || :
	@pip install -e .

run_test_create_connection:
	cd app && python main.py --method test_connection


reset_local_files:
	rm -rf ${LOCAL_MLOPS_DIRECTORY}
	mkdir -p ${LOCAL_MLOPS_DIRECTORY}/training_outputs/pipelines/heart-attack
	mkdir ${LOCAL_MLOPS_DIRECTORY}/training_outputs/params

print_local_mlops_directory:
	@echo ${LOCAL_MLOPS_DIRECTORY}
