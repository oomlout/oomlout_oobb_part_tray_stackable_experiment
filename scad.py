import copy
import opsc
import oobb
import oobb_base
import yaml
import os

thickness_wall = 1
thickness_base = 3
thickness_bottom = 1

thickness_extra_middle = 0.75
extra_middle = 1.5
#set in routine now thickness_stack_interface = 1.5
clearance_inset_stacking = 0.25#0#0.5
inset_bottom = 1 #1.5

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        #filter = ""
        filter = "stackable_2"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        navigation = False
        #navigation = True    

        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "oomlout_oobb_part_tray_stackable_experiment" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        

        names = ["base", "stackable_1"]
        sizes = []
        sizes.append([4, 2.5, 18])
        sizes.append([2, 2, 7])
        sizes.append([1, 1, 7])
        sizes.append([2, 2, 18])
        sizes.append([4, 2, 18])
        sizes.append([2, 2, 12])
        sizes.append([4, 2, 12])

        extras = []
        extras.append("")

        #extras.append("thickness_stack_interface_2d5")

        for size in sizes:
            for name in names:
                for extra in extras:
                    wid = size[0]
                    hei = size[1]
                    dep = size[2]
                    part = copy.deepcopy(part_default)
                    p3 = copy.deepcopy(kwargs)
                    p3["width"] = wid
                    p3["height"] = hei
                    p3["thickness"] = dep
                    if extra != "":
                        p3["extra"] = extra
                    part["kwargs"] = p3
                    part["name"] = name
                    parts.append(part)

        size = [4,2,18]
        name = "stackable_2"
        extra = ""
        wid = size[0]
        hei = size[1]
        dep = size[2]
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = wid
        p3["height"] = hei
        p3["thickness"] = dep
        if extra != "":
            p3["extra"] = extra
        part["kwargs"] = p3
        part["name"] = name
        parts.append(part)


        size = [4,2,18]
        name = "stackable_3"
        extra = ""
        wid = size[0]
        hei = size[1]
        dep = size[2]
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = wid
        p3["height"] = hei
        p3["thickness"] = dep
        if extra != "":
            p3["extra"] = extra
        part["kwargs"] = p3
        part["name"] = name
        parts.append(part)

    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")            
            extra = part["kwargs"].get("extra", "")
            if filter in name or filter in extra:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")


    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        generate_navigation(sort = sort)


def get_base(thing, **kwargs):
    global thickness_wall, thickness_base
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["width"] = width + 1/15
    p3["height"] = height + 1/15
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add cutout



    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_plate"    
    p3["width"] = (width + 1/15) - (2*thickness_wall)/15
    p3["height"] = height + 1/15 - (2*thickness_wall)/15
    p3["depth"] = depth - thickness_base
    #p3["holes"] = True         uncomment to include default holes
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    pos1[2] += thickness_base
    p3["pos"] = pos1

    oobb_base.append_full(thing,**p3)


    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    #oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_stackable_1(thing, **kwargs):
    global thickness_wall, thickness_base, thickness_stack_interface, clearance_inset_stacking, thickness_stack_interface   
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    if extra == "":
        thickness_stack_interface = 1#1.5
    else:
        value = extra.replace("thickness_stack_interface_","")
        thickness_stack_interface = float(value.replace("d","."))
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    width_mm = width * 15
    height_mm = height * 15
    depth_mm = depth

    radius_1 = 5
    radius_2 = radius_1 - thickness_wall
    radius_3 = radius_2 - clearance_inset_stacking
    radius_4 = radius_3 - thickness_wall
    radius_5 = radius_4 - thickness_wall

    wid_top = 0
    hei_top = 0
    wid_bot  =0
    hei_bot = 0

    #base tray
    if True:
    #if False:
        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_mm
        hei = height_mm
        dep = depth_mm - thickness_stack_interface
        wid_top = wid
        hei_top = hei
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_1
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface+thickness_stack_interface
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add cutout
        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        wid = wid - 2*thickness_wall
        hei = hei - 2*thickness_wall
        dep = dep
        size = [wid, hei, dep]
        p4["size"] = size     
        p4["radius"] = radius_2
        #p3["holes"] = True         uncomment to include default holes
        p4["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface + thickness_stack_interface 
        p4["pos"] = pos1
        oobb_base.append_full(thing,**p4)

    #add bottom inset        
    if True:
    #if False:
        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_mm - 2*thickness_wall - 2*clearance_inset_stacking
        hei = height_mm - 2*thickness_wall - 2*clearance_inset_stacking
        wid_bot = wid
        hei_bot = hei
        dep = thickness_stack_interface
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_3
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add cutout
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"rounded_rectangle"    
        wid = wid - 2*thickness_wall
        hei = hei - 2*thickness_wall
        dep = depth_mm - thickness_stack_interface
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = 5- thickness_wall
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += 0
        p3["pos"] = pos1
        #oobb_base.append_full(thing,**p3)

    #add joiner
    if True:
        #add plate
        removal = (clearance_inset_stacking*2 + thickness_wall*2)
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle_extra"    
        wid = wid_top - removal
        hei = hei_top - removal
        dep = thickness_stack_interface
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_3
        p3["inset"] = -removal
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add joiner to the top
        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_mm
        p4["pos"] = pos1        
        #p4["m"] = "#"
        oobb_base.append_full(thing,**p4)


        #add cutout
        removal = (clearance_inset_stacking*2 + thickness_wall*2)
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"rounded_rectangle_extra"    
        wid = wid_top - removal - 2*thickness_wall
        hei = hei_top - removal - 2*thickness_wall
        dep = thickness_stack_interface
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_4
        p3["inset"] = -removal
        #p3["holes"] = True         uncomment to include default holes
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
    


    

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_stackable_2(thing, **kwargs):
    global thickness_wall, thickness_base, thickness_stack_interface, clearance_inset_stacking, thickness_stack_interface   
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    if extra == "":
        thickness_stack_interface = 3
    else:
        value = extra.replace("thickness_stack_interface_","")
        thickness_stack_interface = float(value.replace("d","."))
    #pos = copy.deepcopy(pos)
    #pos[2] += -20


    width_mm = width * 15
    height_mm = height * 15
    depth_mm = depth

    width_bottom_mm = 2 * 15
    height_bottom_mm = 2 * 15

    radius_1 = 5
    radius_2 = radius_1 - thickness_wall
    radius_3 = radius_2 - clearance_inset_stacking
    radius_4 = radius_3 - thickness_wall
    radius_5 = radius_4 - thickness_wall

    wid_top = 0
    hei_top = 0
    wid_bot  =0
    hei_bot = 0

    #base tray
    if True:
    #if False:
        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_mm
        hei = height_mm
        dep = depth_mm - thickness_stack_interface #depth_mm - thickness_stack_interface
        wid_top = wid
        hei_top = hei
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_1
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface #thickness_stack_interface+thickness_stack_interface
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add cutout
        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        wid = wid - 2*thickness_wall
        hei = hei - 2*thickness_wall
        dep = dep  - thickness_bottom
        size = [wid, hei, dep]
        p4["size"] = size     
        p4["radius"] = radius_2
        #p3["holes"] = True         uncomment to include default holes
        #p4["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface + thickness_bottom
        p4["pos"] = pos1
        oobb_base.append_full(thing,**p4)

    #add bottom inset        
    #if True:
    if False:
        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_bottom_mm - 2*thickness_wall - 2*clearance_inset_stacking
        hei = height_bottom_mm - 2*thickness_wall - 2*clearance_inset_stacking
        wid_bot = wid
        hei_bot = hei
        dep = thickness_stack_interface
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_3
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += 0
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += -width_bottom_mm/2
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += width_bottom_mm/2
        poss.append(pos12)
        p3["pos"] = poss 
        oobb_base.append_full(thing,**p3)
        
        #add cutout
        # p3 = copy.deepcopy(kwargs)
        # p3["type"] = "n"
        # p3["shape"] = f"rounded_rectangle"    
        # wid = wid - 2*thickness_wall
        # hei = hei - 2*thickness_wall
        # dep = depth_mm - thickness_stack_interface
        # size = [wid, hei, dep]
        # p3["size"] = size     
        # p3["radius"] = 5- thickness_wall
        # #p3["holes"] = True         uncomment to include default holes
        # #p3["m"] = "#"
        # pos1 = copy.deepcopy(pos)         
        # pos1[2] += 0
        # poss = []
        # pos11 = copy.deepcopy(pos1)
        # pos11[0] += -width_bottom_mm/2
        # poss.append(pos11)
        # pos12 = copy.deepcopy(pos1)
        # pos12[0] += width_bottom_mm/2
        # poss.append(pos12)
        # p3["pos"] = poss 
        #oobb_base.append_full(thing,**p3)

    #add joiner
    if True:
        

        #add plate
        removal = thickness_wall * 2 + clearance_inset_stacking * 2
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle_extra"    
        wid = width_bottom_mm - removal 
        hei = height_bottom_mm - removal
        dep = thickness_stack_interface
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_3
        p3["inset"] = inset_bottom *2
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos) 
        pos1[2] += dep#thickness_stack_interface        
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += -width_bottom_mm/2
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += width_bottom_mm/2
        poss.append(pos12)
        p3["pos"] = poss 
        rot1 = copy.deepcopy(rot)
        rot1[1] = 180
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)

        #add extra cutouts to get theough the joiing layer in the bottom
        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"rounded_rectangle"    
        p3["radius"] = radius_3
        wid = width_bottom_mm - 2*thickness_wall #- extra_middle
        hei = height_bottom_mm - 2*thickness_wall
        wid_bot = wid
        hei_bot = hei
        dep = thickness_extra_middle
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_2
        #p3["holes"] = True         uncomment to include default holes
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface + thickness_stack_interface #+thickness_extra_middle/2
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += -width_bottom_mm/2 - extra_middle/2
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += width_bottom_mm/2 + extra_middle/2
        poss.append(pos12)
        p3["pos"] = poss 
        #oobb_base.append_full(thing,**p3)

        #add joiner to the top
        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        wid = width_mm - removal
        hei = height_mm - removal
        dep = thickness_stack_interface
        size = [wid, hei, dep]
        p4["size"] = size     
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth_mm        
        p4["pos"] = pos1        
        p4["m"] = ""
        oobb_base.append_full(thing,**p4)


        #add cutout
        removal = (clearance_inset_stacking*2 + thickness_wall*2)
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"rounded_rectangle_extra"    
        wid = hei - 4*thickness_wall
        hei = hei - 4*thickness_wall
        dep = thickness_stack_interface
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_5
        p3["inset"] = -removal
        #p3["holes"] = True         uncomment to include default holes
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_bottom# + thickness_extra_middle/2
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += -width_bottom_mm/2# - extra_middle/2
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += width_bottom_mm/2# + extra_middle/2
        poss.append(pos12)
        p3["pos"] = poss 
        oobb_base.append_full(thing,**p3)
    


    

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_stackable_3(thing, **kwargs):
    global thickness_wall, thickness_base, thickness_stack_interface, clearance_inset_stacking, thickness_stack_interface   
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    if extra == "":
        thickness_stack_interface = 1#1.5
    else:
        value = extra.replace("thickness_stack_interface_","")
        thickness_stack_interface = float(value.replace("d","."))
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    extra_middle = 0.75
    thickness_extra_middle = 1

    width_mm = width * 15
    height_mm = height * 15
    depth_mm = depth

    width_bottom_mm = 1 * 15 - 2*thickness_wall
    height_bottom_mm = 1 * 15 - 2*thickness_wall

    radius_1 = 5
    radius_2 = radius_1 - thickness_wall
    radius_3 = radius_2 - clearance_inset_stacking
    radius_4 = radius_3 - thickness_wall
    radius_5 = radius_4 - thickness_wall

    wid_top = 0
    hei_top = 0
    wid_bot  =0
    hei_bot = 0

    #base tray
    if True:
    #if False:
        #add plate
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_mm
        hei = height_mm
        dep = depth_mm - thickness_stack_interface
        wid_top = wid
        hei_top = hei
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_1
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface+thickness_stack_interface
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #add cutout
        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        wid = wid - 2*thickness_wall
        hei = hei - 2*thickness_wall
        dep = dep - thickness_extra_middle
        size = [wid, hei, dep]
        p4["size"] = size     
        p4["radius"] = radius_2
        #p3["holes"] = True         uncomment to include default holes
        #p4["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface + thickness_stack_interface + thickness_stack_interface
        p4["pos"] = pos1
        oobb_base.append_full(thing,**p4)

    #add bottom inset        
    if True:
        for x in range(width):
            for y in range(height):
                #add plate
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"rounded_rectangle"    
                wid = width_bottom_mm - 2*thickness_wall - 2*clearance_inset_stacking
                hei = height_bottom_mm - 2*thickness_wall - 2*clearance_inset_stacking
                wid_bot = wid
                hei_bot = hei
                dep = thickness_stack_interface
                size = [wid, hei, dep]
                p3["size"] = size     
                p3["radius"] = radius_3
                #p3["holes"] = True         uncomment to include default holes
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                pos1[0] += -((width-1)/2*15) + x*15
                pos1[1] += -((height-1)/2*15) + y*15
                pos1[2] += 0

                p3["pos"] = pos1
                oobb_base.append_full(thing,**p3)
   
                #add plate
                removal = (clearance_inset_stacking*2 + thickness_wall*2)
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"rounded_rectangle_extra"    
                wid = width_bottom_mm - removal
                hei = height_bottom_mm - removal
                dep = thickness_stack_interface
                size = [wid, hei, dep]
                p3["size"] = size     
                p3["radius"] = radius_3
                p3["inset"] = -removal
                #p3["holes"] = True         uncomment to include default holes
                #p3["m"] = "#"
                pos2 = copy.deepcopy(pos1) 
                pos2[2] += thickness_stack_interface        
                p3["pos"] = pos2
                oobb_base.append_full(thing,**p3)

                """
                #add extra cutouts to get theough the joiing layer in the bottom
                #add plate
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"rounded_rectangle"    
                p3["radius"] = radius_3
                wid = width_bottom_mm - 2*thickness_wall - extra_middle
                hei = height_bottom_mm - 2*thickness_wall
                wid_bot = wid
                hei_bot = hei
                dep = thickness_extra_middle
                size = [wid, hei, dep]
                p3["size"] = size     
                p3["radius"] = radius_2
                #p3["holes"] = True         uncomment to include default holes
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                pos1[2] += thickness_stack_interface + thickness_stack_interface +thickness_extra_middle/2
                poss = []
                pos11 = copy.deepcopy(pos1)
                pos11[0] += -width_bottom_mm/2 - extra_middle/2
                poss.append(pos11)
                pos12 = copy.deepcopy(pos1)
                pos12[0] += width_bottom_mm/2 + extra_middle/2
                poss.append(pos12)
                p3["pos"] = poss 
                oobb_base.append_full(thing,**p3)

                #add joiner to the top
                p4 = copy.deepcopy(p3)
                p4["type"] = "n"
                wid = width_mm - removal
                hei = height_mm - removal
                dep = thickness_stack_interface
                size = [wid, hei, dep]
                p4["size"] = size     
                pos1 = copy.deepcopy(pos)
                pos1[2] += depth_mm        
                p4["pos"] = pos1        
                p4["m"] = ""
                oobb_base.append_full(thing,**p4)


                #add cutout
                removal = (clearance_inset_stacking*2 + thickness_wall*2)
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"rounded_rectangle_extra"    
                wid = width_bottom_mm - removal - 2*thickness_wall - extra_middle
                hei = height_bottom_mm - removal - 2*thickness_wall 
                dep = thickness_stack_interface
                size = [wid, hei, dep]
                p3["size"] = size     
                p3["radius"] = radius_4
                p3["inset"] = -removal
                #p3["holes"] = True         uncomment to include default holes
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                pos1[2] += thickness_stack_interface + thickness_extra_middle/2
                poss = []
                pos11 = copy.deepcopy(pos1)
                pos11[0] += -width_bottom_mm/2 - extra_middle/2
                poss.append(pos11)
                pos12 = copy.deepcopy(pos1)
                pos12[0] += width_bottom_mm/2 + extra_middle/2
                poss.append(pos12)
                p3["pos"] = poss 
                oobb_base.append_full(thing,**p3)
                """


    

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]    
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        get_base(thing, **kwargs)   
    
    folder = f"scad_output/{thing['id']}"

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        

        opsc.opsc_make_object(f'{folder}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)  

    yaml_file = f"{folder}/working.yaml"
    with open(yaml_file, 'w') as file:
        part_new = copy.deepcopy(part)
        kwargs_new = part_new.get("kwargs", {})
        kwargs_new.pop("save_type","")
        part_new["kwargs"] = kwargs_new
        import os
        cwd = os.getcwd()
        part_new["project_name"] = cwd
        part_new["id"] = thing["id"]
        part_new["thing"] = thing
        yaml.dump(part_new, file)

def generate_navigation(folder="scad_output", sort=["width", "height", "thickness"]):
    #crawl though all directories in scad_output and load all the working.yaml files
    parts = {}
    for root, dirs, files in os.walk(folder):
        if 'working.yaml' in files:
            yaml_file = os.path.join(root, 'working.yaml')
            #if working.yaml isn't in the root directory, then do it
            if root != folder:
                with open(yaml_file, 'r') as file:
                    part = yaml.safe_load(file)
                    # Process the loaded YAML content as needed
                    part["folder"] = root
                    part_name = root.replace(f"{folder}","")
                    
                    #remove all slashes
                    part_name = part_name.replace("/","").replace("\\","")
                    parts[part_name] = part

                    print(f"Loaded {yaml_file}: {part}")

    pass
    for part_id in parts:
        part = parts[part_id]
        kwarg_copy = copy.deepcopy(part["kwargs"])
        folder_navigation = "navigation_oobb"
        folder_source = part["folder"]
        folder_extra = ""
        for s in sort:
            if s == "name":
                ex = part.get("name", "default")
            else:
                ex = kwarg_copy.get(s, "default")
            folder_extra += f"{s}_{ex}/"

        #replace "." with d
        folder_extra = folder_extra.replace(".","d")            
        folder_destination = f"{folder_navigation}/{folder_extra}"
        if not os.path.exists(folder_destination):
            os.makedirs(folder_destination)
        if os.name == 'nt':
            #copy a full directory auto overwrite
            command = f'xcopy "{folder_source}" "{folder_destination}" /E /I /Y'
            print(command)
            os.system(command)
        else:
            os.system(f"cp {folder_source} {folder_destination}")

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)