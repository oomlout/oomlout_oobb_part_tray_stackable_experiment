import os


def main(**kwargs):
    folder = kwargs["folder"]
    file_name_top = f"{folder}/3dpr_slice_top.gcode"
    file_name_bottom = f"{folder}/3dpr_slice_bottom.gcode"
    file_name_output = f"{folder}/3dpr_slice_output.gcode"
    split_height = kwargs["split_height"]

    top_gcode = ""

    #open the file using os
    with open(file_name_top) as f:    
        for line in f:
            top_gcode += line
    
    bottom_gcode = ""

    #open the file using os
    with open(file_name_bottom) as f:
        for line in f:
            bottom_gcode += line

    
    bottom_gcode_include = ""

    
    #grab bottom gcode
    if True:
        string_find = "AFTER_LAYER_CHANGE"
        index = 0
        lines = bottom_gcode.split("\n")
        running = True
        while running:
            line_current = lines[index]
            if string_find in line_current:
                bottom_gcode_include += line_current + "\n"    
                index += 1
                line_next = lines[index]
                line_next_working = line_next.replace(";","")
                line_next_working_float = float(line_next_working)
                error_plus_or_minus = 0.015
                error = abs(line_next_working_float - split_height)
                if error < error_plus_or_minus:
                    index += 1
                    running = False
                    break            
            bottom_gcode_include += lines[index] + "\n"
            index += 1
        
        #add splice here comment
        bottom_gcode_include += ";oomlout splice here\n"

    #grab top gcode
    if True:
        top_gcode_include = "G90 ;absolute positioning\n"
        index = 0
        lines = top_gcode.split("\n")
        print_splice = False
        running = True
        include_line = False
        while running:
            line_current = lines[index]
            z_height = ""
            if "G1 Z" in line_current and "X" in line_current and "Y" in line_current:
                z_height = line_current.split("Z")[1].split(" ")[0]
                z_height = float(z_height)
                #print(f"z_height: {z_height}")
                if print_splice == False:
                    print_splice = True
                    print(f"splice at: {z_height}")                
                if z_height >= split_height:
                    include_line = True
            if include_line:
                top_gcode_include += line_current + "\n"
            index += 1
            #stop if at end of file
            if index >= len(lines):
                running = False
                break

    #join top and bottom
    gcode = bottom_gcode_include + top_gcode_include

    #save to output
    with open(file_name_output, "w") as f:
        f.write(gcode)
    


    









if __name__ == '__main__':
    kwargs = {}
    kwargs["folder"] =  "scad_output\oobb_part_oomlout_oobb_part_tray_stackable_experiment_stackable_7_4_width_2_height_18_mm_depth"
    kwargs["split_height"] = 1.2


    main(**kwargs)