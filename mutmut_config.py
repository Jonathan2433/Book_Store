# mutmut_config.py

def pre_mutation(context):
    """Script to run before mutation testing begins."""
    # Ajoutez ici les commandes à exécuter avant le début des tests de mutation

def post_mutation(context):
    """Script to run after mutation testing."""
    # Ajoutez ici les commandes à exécuter après les tests de mutation

# Commande pour exécuter les tests
def test_command(context):
    return "pytest"

# Chemin vers le code source à muter
paths_to_mutate = "./APPLICATION/"

# Vous pouvez spécifier des commandes supplémentaires, des chemins à ignorer, etc.
