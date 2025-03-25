from faasit_runtime import function, FaasitRuntime

# Modified on 2025-03-26 00:13:53 UTC+8
@function
def hello(rt: FaasitRuntime):
    return rt.output(rt.input())

hello = hello.export()