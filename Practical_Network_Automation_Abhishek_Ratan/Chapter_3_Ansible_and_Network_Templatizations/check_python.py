from collections import namedtuple
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.utils.display import Display


def run_playbook(playbook_path, inventory_path):
    """Runs an Ansible playbook using the Python API."""

    # Initialize objects
    loader = DataLoader()
    display = Display()
    inventory = InventoryManager(loader=loader, sources=[inventory_path])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff', 'listhosts', 'listtasks', 'listtags', 'syntax'])
    options = Options(connection='local', module_path='', forks=100, become=None, become_method=None, become_user=None, check=False,
                    diff=False, listhosts=False, listtasks=False, listtags=False, syntax=False)
    
    # Create PlaybookExecutor object
    executor = PlaybookExecutor(
        playbooks=[playbook_path],
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords=dict(vault_pass='your_vault_password_if_needed'),
        options=options
    )

    # Run the playbook
    result = executor.run()

    return result

if __name__ == '__main__':
    result = run_playbook('check_template.yml', 'inventory')
    print(result)
