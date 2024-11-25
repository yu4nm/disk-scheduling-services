def clook(arm_position, lrequests, debug=False):
    """
    Circular LOOK implementation.

    Args:
        arm_position (int): Posición inicial del brazo del disco.
        lrequests (list<int>): Lista de solicitudes de disco.
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

    # Salta al inicio de las solicitudes más bajas
    if lower:
        distance += abs(current_pos - lower[0])
        current_pos = lower[0]
        sequence.append(current_pos)

    # Procesa solicitudes restantes
    for req in lower[1:]:
        distance += abs(req - current_pos)
        sequence.append(req)
        current_pos = req

    average_distance = distance / len(lrequests)
    return {
        "sequence": [arm_position] + sequence,
        "distance": distance,
        "average": average_distance
    }
