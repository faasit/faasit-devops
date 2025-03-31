from faasit_runtime import function, FaasitRuntime

# Modified on 2025-03-31 15:06:43 UTC+8
@function
def hello(rt: FaasitRuntime):
    return rt.output(rt.input())

hello = hello.export()