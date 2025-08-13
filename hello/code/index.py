from faasit_runtime import function, FaasitRuntime

@function
def hello(rt: FaasitRuntime):
    return rt.output({
        "deploy_time": "2025-08-13 08:52:54 UTC+8",
        "input": rt.input(),
        "isCanary": False
    })

hello = hello.export()