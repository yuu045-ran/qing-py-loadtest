
import logging
import asyncio
import azure.functions as func
import time
async def first_func(response):
    response.append('Python HTTP trigger function processed first function.')
async def second_func(response):
    response.append('Python HTTP trigger function processed second function.')
async def third_func(response):
    response.append('Python HTTP trigger function processed third function.')
async def main(req: func.HttpRequest) -> func.HttpResponse:
    start_time = time.perf_counter()
    response = []
    await asyncio.gather(*[first_func(response),second_func(response),third_func(response)])
    end_time = time.perf_counter() - start_time
    return func.HttpResponse(
        "This api function took {}".format(round(end_time*1000,2)),
        status_code=200
)
