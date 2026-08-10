def print_results(target, results, duration):
    """
    Prints scan results.
    """

    print("\n" + "=" * 50)
    print("Scan Results")
    print("=" * 50)

    print(f"Target: {target}")
    print(f"Time: {duration:.2f}s")

    if not results:
        print("\nNo open ports found.")
        return

    print("\nOpen Ports:")

    for result in results:
        print(f"[+] {result['port']} " f"- {result['service']}")
