ansible-playbook -i inventory check_template.yml -c local -k

python check_python.py
> stuck with python 3.12, there is no options keyword on PlaybookExecutor
TypeError: PlaybookExecutor.__init__() got an unexpected keyword argument 'options'