def get_user_ip_address(request):
    """
    Try to find the most accurate value for IP adress from given request object.

    Arguments:
        request (Request): The request object to inspect.

    Returns:
        string: Found IP adress.
    """
    req_headers = request.META
    x_forwarded_for_value = req_headers.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for_value:
        ip_address = x_forwarded_for_value.split(",")[-1].strip()
    else:
        ip_address = req_headers.get("REMOTE_ADDR")

    return ip_address
