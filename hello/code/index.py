from faasit_runtime import function, FaasitRuntime

@function
def hello(rt: FaasitRuntime):
    print(1)
    return rt.output(rt.input())

hello = hello.export()