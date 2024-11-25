def cscan(arm_position, lrequests, disk_size, debug=False):
    """
    Circular SCAN implementation.

    Args:
        arm_position (int): Posición inicial del brazo del disco.
        lrequests (list<int>): Lista de solicitudes de disco.
        disk_size (int): Tamaño del disco.
        debug (bool): Si es True, imprime información de depuración.

    Returns:
        dict: Secuencia de accesos, distancia total y promedio.
    """
    requests = sorted(lrequests)
    sequence = []
    distance = 0
    current_pos = arm_position

    # Solicitudes por debajo y por encima de la posición actual
    lower = [r for r in requests if r < arm_position]
    higher = [r for r in requests if r >= arm_position]

    # Procesa solicitudes en la dirección ascendente
    for req in higher:
        distance += abs(req - current_pos)
        sequence.append(req)
        current_pos = req

    # Salta al inicio del disco
    if higher:
        distance += abs(disk_size - 1 - current_pos)
        current_pos = 0
        sequence.append(current_pos)

    # Procesa solicitudes restantes desde el inicio
    for req in lower:
        distance += abs(req - current_pos)
        sequence.append(req)
        current_pos = req

    average_distance = distance / len(lrequests)
    return {
        "sequence": [arm_position] + sequence,
        "distance": distance,
        "average": average_distance
    }
