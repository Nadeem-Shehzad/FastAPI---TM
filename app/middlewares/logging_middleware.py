import time
from fastapi import Request


async def logging_middleware(request: Request, call_next):
    start_time = time.time()

    method = request.method
    url = str(request.url)

    print(f"➡️ Incoming Request: {method} {url}")

    try:
        response = await call_next(request)
    except Exception as e:
        print(f"➡️ Incoming Request: {method} {url}")
        raise e 

    status_code = response.status_code
    process_time = time.time() - start_time

    print(f"⬅️ Response: {method} {url} - {status_code} - {process_time:.3f}s")

    return response   