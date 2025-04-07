from faasit_runtime import function, FaasitRuntime

@function
def hello(rt: FaasitRuntime):
    return rt.output({
        "deploy_time": "2025-04-01 19:08:23 UTC+8",
        "input": rt.input(),
        "isCanary": False
    })

hello = hello.export()