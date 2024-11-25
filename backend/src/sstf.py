def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First implementation.

    Args:
        arm_position (int): Posición inicial del brazo del disco.
        lrequests (list<int>): Lista de solicitudes de disco.
        debug (bool): Si es True, imprime información de depuración.

    Returns:
        dict: Secuencia de accesos, distancia total y promedio.
    """
    requests = lrequests[:]  # Copia para evitar modificar la lista original
    current_pos = arm_position
    sequence = [current_pos]
    distance = 0

    while requests:
        # Encuentra la solicitud más cercana
        closest_request = min(requests, key=lambda x: abs(x - current_pos))
        distance += abs(closest_request - current_pos)
        current_pos = closest_request
        sequence.append(current_pos)
        requests.remove(closest_request)
        if debug:
            print(f"Moviéndose a {closest_request}, distancia acumulada: {distance}")

    average_distance = distance / len(lrequests)
    return {
        "sequence": sequence,
        "distance": distance,
        "average": average_distance
    }

