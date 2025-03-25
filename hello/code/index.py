from faasit_runtime import function, FaasitRuntime

# Modified on 2025-03-25 23:26:54 UTC+8
@function
def hello(rt: FaasitRuntime):
    return rt.output(rt.input())

hello = hello.export()