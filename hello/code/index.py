from faasit_runtime import function, FaasitRuntime

# Modified on 2025-04-01 19:08:23 UTC+8
@function
def hello(rt: FaasitRuntime):
    return rt.output({
        "input": rt.input(),
        "isCanary": False
    })

hello = hello.export()