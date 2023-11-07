include .env
export $(cat .env | xargs)
# General
reinstall_package:
	@pip uninstall -y oracle-prophecy || :
	@pip install -e .

reset_local_files:
	rm -rf ${LOCAL_MLOPS_DIRECTORY}
	mkdir -p ${LOCAL_MLOPS_DIRECTORY}/training_outputs/pipelines/heart-attack
	mkdir ${LOCAL_MLOPS_DIRECTORY}/training_outputs/params

# API
run_api:
	uvicorn app.api.fast:app --reload

# Database
run_test_create_connection:
	python -c 'from app.main import test_connection; test_connection()'

# Heart Attack
run_train_heart_attack:
	python -c 'from app.interface.heart_attack.main import train; train()'

run_evaluate_heart_attack:
	python -c 'from app.interface.heart_attack.main import evaluate; evaluate()'
