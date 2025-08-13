from faasit_runtime import function, FaasitRuntime

@function
def hello(rt: FaasitRuntime):
    return rt.output({
        "deploy_time": "2025-08-13 10:22:53 UTC+8",
        "input": rt.input(),
        "isCanary": True
    })

hello = hello.export()