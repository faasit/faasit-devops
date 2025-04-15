from faasit_runtime import function, FaasitRuntime

@function
def hello(rt: FaasitRuntime):
    return rt.output({
        "deploy_time": "2025-04-15 09:09:31 UTC+8",
        "input": rt.input(),
        "isCanary": True
    })

hello = hello.export()