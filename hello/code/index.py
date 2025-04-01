from faasit_runtime import function, FaasitRuntime

# Modified on 2025-04-01 15:55:56 UTC+8
@function
def hello(rt: FaasitRuntime):
    rt.input()["isCanary"] = False
    return rt.output(rt.input())

hello = hello.export()