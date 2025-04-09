from faasit_runtime import function, FaasitRuntime

@function
def hello(rt: FaasitRuntime):
    return rt.output({
        "deploy_time": "2025-04-09 11:15:27 UTC+8",
        "input": rt.input(),
        "isCanary": False
    })

hello = hello.export()