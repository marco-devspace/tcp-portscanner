import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from services import get_service_name


def scan_port(target, port, timeout):
    """
    Checks whether a TCP port is open.
    """

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.settimeout(timeout)

            result = sock.connect_ex((target, port))

            if result == 0:
                return {
                    "port": port,
                    "service": get_service_name(port),
                    "status": "open",
                }

    except socket.error:
        pass

    return None


def scan_ports(target, start_port, end_port, threads, timeout):
    """
    Scans multiple ports using threads.
    """

    open_ports = []
    total_ports = end_port - start_port + 1
    completed_ports = 0

    with ThreadPoolExecutor(max_workers=threads) as executor:

        futures = [
            executor.submit(scan_port, target, port, timeout)
            for port in range(start_port, end_port + 1)
        ]

        for future in as_completed(futures):

            result = future.result()

            if result:
                open_ports.append(result)

            completed_ports += 1

            progress = (completed_ports / total_ports) * 100

            print(f"\rProgress: {progress:.1f}%", end="")

    print()

    open_ports.sort(key=lambda x: x["port"])
    return open_ports
