from enum import Enum

Operation = Enum('Operations', ['EDITAR', 'DELETAR', 'LISTAR', 'SAIR'])

def get_operation_name(value):
    for member in Operation:
        if member.value == value:
            return member.name.lower()
    return None 