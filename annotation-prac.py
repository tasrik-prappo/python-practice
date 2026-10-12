#without annotation: 

x = 5

def v(name,version):
    return(f"Language name: {name} and version: {version}")

#with annotation:

y : int = 5

def v(name: str, version: float) -> str:
    return(f"Language name: {name} and version: {version}")