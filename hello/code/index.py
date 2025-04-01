from faasit_runtime import function, FaasitRuntime

# Modified on 2025-04-01 16:04:07 UTC+8
@function
def hello(rt: FaasitRuntime):
    return rt.output({
        "input": rt.input(),
        "isCanary": True
    })

hello = hello.export()