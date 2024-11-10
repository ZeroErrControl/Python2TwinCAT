import pyads

plc = pyads.Connection("192.168.1.160.1.1",851)
plc.open()

#只有当i初始化才能看到变化  OK  这里其实是通过变量来控制eRob
#i = plc.read_by_name("GVL.int_val",pyads.PLCTYPE_INT)
Actual_Velocity = plc.read_by_name("GVL.Actual_Velocity",pyads.PLCTYPE_DINT)
Target_Velocity = plc.read_by_name("GVL.Target_Velocity",pyads.PLCTYPE_DINT)
#Control_word    = plc.read_by_name("GVL.Target_Velocity",pyads.PLCTYPE_DINT)
#print(i)


plc.write_by_name("GVL.int_val",12)
plc.write_by_name("GVL.Control_word",47)
Control_word    = plc.read_by_name("GVL.Control_word",pyads.PLCTYPE_UINT)
print(Control_word)

#if Control_word == 47:
Target_Velocity = -2000
plc.write_by_name("GVL.Target_Velocity", Target_Velocity)
print(Target_Velocity)


