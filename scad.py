import copy
import opsc
import oobb
import oobb_base
import yaml
import os

thickness_wall = 1.2 #1.5 #0.8
thickness_base = 3
thickness_bottom = 1.5

thickness_layer = 0.25

thickness_bottom_angle_piece = 1
thickness_bottom_straight_piece = 2

thickness_stack_interface = thickness_bottom_angle_piece + thickness_bottom_straight_piece

thickness_extra_middle = 0.75
extra_middle = 1.5
#set in routine now thickness_stack_interface = 1.5
clearance_inset_stacking = 0.2#0#0.25#0#0.5
inset_bottom = 0.5 #1.5

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        filter = "stackable_3"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        navigation = False
        navigation = True    

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

        sizes = []
        size = [4,2,18]
        sizes.append(size)
        size = [2,2,18]
        sizes.append(size)
        size = [4,4,18]
        sizes.append(size)
        

        for size in sizes:
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

    #add joiner
    if True:        
        #add plate
        removal = thickness_wall * 2 + clearance_inset_stacking * 2
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle_extra"    
        wid = width_bottom_mm - removal 
        hei = height_bottom_mm - removal
        dep = thickness_bottom_angle_piece
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
        #add angle cutout
        if True:
            p4 = copy.deepcopy(p3)
            p4["type"] = "n"
            size2 = copy.deepcopy(p3.get("size",[]))
            size2[0] += -2*thickness_wall
            size2[1] += -2*thickness_wall
            p4["size"] = size2     
            p4["radius"] = radius_4            
            p4["m"] = "#"
            #more complicated becaue of slicing a cone but part of thickness bottom so not needed
            #oobb_base.append_full(thing,**p4)

        #straight piece
        p4 = copy.deepcopy(p3)
        p4.pop("inset","")
        size2 = copy.deepcopy(p3.get("size",[]))
        size2[2] = thickness_bottom_straight_piece
        p4["size"] = size2            
        poss2 = copy.deepcopy(poss)
        for pos2 in poss2:
            pos2[2] += thickness_bottom_straight_piece
        p4["pos"] = poss2
        #p4["m"] = "#"
        oobb_base.append_full(thing,**p4)
        #cutout
        if True:
            p5 = copy.deepcopy(p4)
            p5["type"] = "n"
            size2 = copy.deepcopy(p4.get("size",[]))
            size2[0] += -2*thickness_wall
            size2[1] += -2*thickness_wall
            size2[2] += -thickness_bottom + thickness_bottom_angle_piece + thickness_bottom
            poss3 = copy.deepcopy(poss2)
            for pos3 in poss3:
                pos3[2] += +thickness_bottom
            p5["pos"] = poss3
            p5["size"] = size2
            p5["radius"] = radius_5
            p5["m"] = "#"
            oobb_base.append_full(thing,**p5)

        


    

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
        #add plate minus one layer
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"    
        wid = width_mm
        hei = height_mm
        dep = depth_mm - thickness_stack_interface - thickness_layer #depth_mm - thickness_stack_interface
        wid_top = wid
        hei_top = hei
        size = [wid, hei, dep]
        p3["size"] = size     
        p3["radius"] = radius_1
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += thickness_stack_interface + thickness_layer#thickness_stack_interface+thickness_stack_interface
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        
        #thin half step out slice
        p4 = copy.deepcopy(p3)
        ins = thickness_wall #+ inset_bottom
        p4["size"][0] += -ins
        p4["size"][1] += -ins
        p4["size"][2] = thickness_layer
        p4["radius"] += -ins
        pos1 = copy.deepcopy(pos)
        pos1[2] += thickness_stack_interface
        p4["pos"] = pos1
        #p4["m"] = "#"
        oobb_base.append_full(thing,**p4)

        p5 = copy.deepcopy(p4)
        p5["type"] = "n"
        p5["size"][0] = width_mm - thickness_wall
        p5["size"][1] = height_mm - thickness_wall
        p5["radius"] = radius_1 - thickness_wall/2
        #p5["m"] = "#"
        p5["pos"][2] = depth - thickness_layer
        oobb_base.append_full(thing,**p5)




        #add cutout
        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        p4["size"][0] += -2*thickness_wall
        p4["size"][1] += -2*thickness_wall
        les = -thickness_bottom + thickness_layer    
        p4["size"][2] += les
        p4["radius"] = radius_2
        #p3["holes"] = True         uncomment to include default holes
        #p4["m"] = "#"
        p4["pos"][2] += -les        
        oobb_base.append_full(thing,**p4)

    #add joiner
    if True:        
        scalar = 2
        width_bottom_mm = scalar * 15
        height_bottom_mm = scalar * 15
        width_count = int(width / scalar)
        height_count = int(height / scalar)
        for x in range(width_count):
            for y in range(height_count):                
                #add plate
                removal = thickness_wall * 2 + clearance_inset_stacking * 2
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"rounded_rectangle_extra"    
                wid = width_bottom_mm - removal 
                hei = height_bottom_mm - removal
                dep = thickness_bottom_angle_piece
                size = [wid, hei, dep]
                p3["size"] = size     
                p3["radius"] = radius_3
                p3["inset"] = inset_bottom *2
                #p3["holes"] = True         uncomment to include default holes
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos) 
                pos1[0] += -(((width-scalar)*15)/2)  + x * 15 * scalar
                pos1[1] += -(((height-scalar)*15)/2) + y * 15 * scalar
                pos1[2] += dep#thickness_stack_interface    
                p3["pos"] = pos1
                pos_main = copy.deepcopy(pos1)
                rot1 = copy.deepcopy(rot)
                rot1[1] = 180
                p3["rot"] = rot1
                oobb_base.append_full(thing,**p3)
                #add angle cutout
                if True:
                    p4 = copy.deepcopy(p3)
                    p4["type"] = "n"
                    size2 = copy.deepcopy(p3.get("size",[]))
                    size2[0] += -2*thickness_wall
                    size2[1] += -2*thickness_wall
                    p4["size"] = size2     
                    p4["radius"] = radius_4            
                    p4["m"] = "#"
                    #more complicated becaue of slicing a cone but part of thickness bottom so not needed
                    #oobb_base.append_full(thing,**p4)

                #straight piece
                p4 = copy.deepcopy(p3)
                p4.pop("inset","")
                size2 = copy.deepcopy(p3.get("size",[]))
                size2[2] = thickness_bottom_straight_piece
                p4["size"] = size2            
                pos2 = copy.deepcopy(pos1)
                pos2[2] += thickness_bottom_straight_piece
                p4["pos"] = pos2
                #p4["m"] = "#"
                oobb_base.append_full(thing,**p4)
                #cutout
                if True:
                    p5 = copy.deepcopy(p4)
                    p5["type"] = "n"
                    size2 = copy.deepcopy(p4.get("size",[]))
                    size2[0] += -2*thickness_wall
                    size2[1] += -2*thickness_wall
                    size2[2] += -thickness_bottom + thickness_bottom_angle_piece + thickness_bottom
                    pos3 = copy.deepcopy(pos2)
                    pos3[2] += +thickness_bottom
                    p5["pos"] = pos3
                    p5["size"] = size2
                    p5["radius"] = radius_4
                    #p5["m"] = "#"
                    oobb_base.append_full(thing,**p5)

            #add sawtooth for overhangs
                if True:
                    #side_sawtooths
                    if True:  
                        end_skip = 2
                        pass  
                        thickness_sawtooth = thickness_layer * 2
                        width_saw_tooth = 0.2
                        width_gap_saw_tooth = 0.6
                        height_saw_tooth = 3.5
                        #repeats_width = int(width_bottom_mm / (width_saw_tooth*2))
                        #repeats_height = int(height_bottom_mm / (width_saw_tooth*2))
                        repeats_width = int(width_bottom_mm / (width_saw_tooth + width_gap_saw_tooth))
                        repeats_height = int(height_bottom_mm / (width_saw_tooth + width_gap_saw_tooth))
                        for xx in range(end_skip,repeats_width-end_skip):                                                   
                            p3 = copy.deepcopy(kwargs)
                            p3["type"] = "n"
                            p3["shape"] = f"oobb_cube"    
                            wid = width_saw_tooth                        
                            hei = height_saw_tooth
                            if xx == 2 or xx == repeats_height - 3:
                                #hei = height_saw_tooth * 1.5
                                #wid = width_saw_tooth * 1                        
                                pass
                            if xx == 1 or xx == repeats_width - 2:
                                #hei = 1
                                #hei = height_saw_tooth * 3
                                pass
                            if xx == 0 or xx == repeats_width - 1:
                                #hei = height_saw_tooth * 5
                                #wid = width_saw_tooth * 1.5                        
                                pass
                            dep = thickness_sawtooth
                            size = [wid, hei, dep]
                            p3["size"] = size                                 
                            #p3["holes"] = True         uncomment to include default holes
                            p3["m"] = "#"
                            pos1 = copy.deepcopy(pos_main)                         
                            #pos1[0] += -((width_bottom_mm)/2)  + (xx+1) * width_saw_tooth * 2 - width_saw_tooth                                                 
                            pos1[0] += -((width_bottom_mm)/2)  + (xx+1) * (width_saw_tooth + width_gap_saw_tooth) - width_saw_tooth                                                 
                            pos1[2] = thickness_stack_interface
                            poss = []
                            pos11 = copy.deepcopy(pos1)
                            pos11[1] += -((height_bottom_mm)/2)
                            pos12 = copy.deepcopy(pos1)
                            pos12[1] += ((height_bottom_mm)/2)
                            poss.append(pos11)
                            poss.append(pos12)
                            p3["pos"] = poss
                            oobb_base.append_full(thing,**p3)
                        for xx in range(end_skip,repeats_height-end_skip):                                                   
                            p3 = copy.deepcopy(kwargs)
                            p3["type"] = "n"
                            p3["shape"] = f"oobb_cube"    
                            hei = width_saw_tooth                        
                            wid = height_saw_tooth
                            if xx == 2 or xx == repeats_height - 3:
                                #hei = width_saw_tooth * 1
                                #wid = height_saw_tooth * 1.5
                                pass
                            if xx == 1 or xx == repeats_width - 2:
                                #hei = width_saw_tooth * 1
                                #wid = height_saw_tooth * 3
                                pass
                            if xx == 0 or xx == repeats_width - 1:
                                #hei = width_saw_tooth * 1.6
                                #wid = height_saw_tooth * 3
                                pass
                            dep = thickness_sawtooth
                            size = [wid, hei, dep]
                            p3["size"] = size                                 
                            #p3["holes"] = True         uncomment to include default holes
                            p3["m"] = "#"
                            pos1 = copy.deepcopy(pos_main)                         
                            #pos1[1] += -((width_bottom_mm)/2)  + (xx+1) * width_saw_tooth * 2 - width_saw_tooth                                                 
                            pos1[1] += -((width_bottom_mm)/2)  + (xx+1) * (width_saw_tooth + width_gap_saw_tooth) - width_saw_tooth                                                 
                            pos1[2] = thickness_stack_interface
                            poss = []
                            pos11 = copy.deepcopy(pos1)
                            pos11[0] += -((height_bottom_mm)/2)
                            pos12 = copy.deepcopy(pos1)
                            pos12[0] += ((height_bottom_mm)/2)
                            poss.append(pos11)
                            poss.append(pos12)
                            p3["pos"] = poss                        
                            oobb_base.append_full(thing,**p3)                            
                    #corner_angles
                    if True:
                        inset_layer = 1
                        p3 = copy.deepcopy(kwargs)
                        p3["type"] = "n"
                        p3["shape"] = f"oobb_cube"
                        wid = 4.5
                        hei = 4.5
                        dep = thickness_layer
                        size = [wid, hei, dep]
                        p3["size"] = size
                        p3["m"] = "#"
                        pos1 = copy.deepcopy(pos_main)
                        pos1[2] = thickness_stack_interface
                        shift_x = width_bottom_mm/2
                        shift_y = height_bottom_mm/2
                        poss = []
                        pos11 = copy.deepcopy(pos1)
                        pos11[0] += -shift_x
                        pos11[1] += -shift_y
                        pos12 = copy.deepcopy(pos1)
                        pos12[0] += shift_x
                        pos12[1] += -shift_y
                        pos13 = copy.deepcopy(pos1)
                        pos13[0] += -shift_x
                        pos13[1] += shift_y
                        pos14 = copy.deepcopy(pos1)
                        pos14[0] += shift_x
                        pos14[1] += shift_y
                        poss.append(pos11)
                        poss.append(pos12)
                        poss.append(pos13)
                        poss.append(pos14)
                        p3["pos"] = poss
                        oobb_base.append_full(thing,**p3)
                        
                        #one layer up
                        p4 = copy.deepcopy(p3)
                        p4["size"][0] += -inset_layer
                        p4["size"][1] += -inset_layer
                        poss = p4["pos"]
                        for pos1 in poss:
                            pos1[2] += thickness_layer
                        p4["m"] = "#"
                        oobb_base.append_full(thing,**p4)
                        #one layer up
                        




    

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