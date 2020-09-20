import matlab.engine
eng = matlab.engine.start_matlab()
tf = eng.ipcam_basics1()
print(tf)