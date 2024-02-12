# Stock Cube Parameters
stock_min_x = 10.0
stock_min_y = 10.0
stock_min_z = 10.0

stock_max_x = 50.0 #50
stock_max_y = 50.0 #50
stock_max_z = 50.0 #50

stock_dim_x = None
stock_dim_y = None
stock_dim_z = None

# General Feature Parameters
min_len = 2.0 #2
clearance = 1 #1
inner_bounds_clearance = 2

# Round Parameters
round_radius_min = 0.1
round_radius_max = 5.0

# Chamfer Parameters
chamfer_depth_min = 0.1 # 1
chamfer_depth_max = 4.0 #4

# Possible Machining Features
feat_names = ['chamfer', #0
              'through_hole', #1
              'triangular_passage', #2
              'rectangular_passage', #3
              '6sides_passage', #4
              'triangular_through_slot', #5
              'rectangular_through_slot', #6
              'circular_through_slot', #7
              'rectangular_through_step', #8
              '2sides_through_step', #9
              'slanted_through_step', #10
              'Oring', #11
              'blind_hole', #12
              'triangular_pocket', #13
              'rectangular_pocket', #14
              '6sides_pocket', #15
              'circular_end_pocket', #16
              'rectangular_blind_slot', #17
              'v_circular_end_blind_slot', #18
              'h_circular_end_blind_slot', #19
              'triangular_blind_step', #20
              'circular_blind_step', #21
              'rectangular_blind_step', #22
              'round', #23
              'stock', #24
              'drill_pocket_140deg',#25
              'spotdrill_cone_90deg', #26
              'stepdrill_pocket_90deg' #27
              ]

feat_names_planar = ['rectangular_through_slot', #0
             'triangular_through_slot', #1
             'rectangular_passage', #2
             'triangular_passage', #3
             '6sides_passage', #4
             'rectangular_through_step', #5
             '2sides_through_step', #6
             'slanted_through_step', #7
             'rectangular_blind_step', #8
             'triangular_blind_step', #9
             'rectangular_blind_slot', #10
             'rectangular_pocket', #11
             'triangular_pocket', #12
             '6sides_pocket', #13
             'chamfer', #14
             'stock'] #15

#certain values are precalculated to save runtime
#all lists sorted decending
#all lists use scale 1:10
drill11620xxx = [
{'radius':1.000, 'total_height':5.5, 'cone_height':0.3640, 'cylinder_height':5.1360}, #DC20
{'radius':0.875, 'total_height':5.1, 'cone_height':0.3185, 'cylinder_height':4.7815}, #DC17.5
{'radius':0.750, 'total_height':4.5, 'cone_height':0.2730, 'cylinder_height':4.2270}, #DC15
{'radius':0.625, 'total_height':4.3, 'cone_height':0.2275, 'cylinder_height':4.0725}, #DC12.5
{'radius':0.500, 'total_height':3.5, 'cone_height':0.1820, 'cylinder_height':3.3180}, #DC10
{'radius':0.250, 'total_height':2.0, 'cone_height':0.0910, 'cylinder_height':1.9090}  #DC5
]

# radius
spotdrill107020xx = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.25]

stepdrill10767xxxxx = [
{'tipcone_height':0.255, 'cylinder_height':3.85, 'sink_height':0.200, 'height_total':4.305, 'inner_radius':0.700, 'outer_radius':0.9}, #m16
{'tipcone_height':0.218, 'cylinder_height':3.45, 'sink_height':0.200, 'height_total':3.868, 'inner_radius':0.600, 'outer_radius':0.8}, #m14
{'tipcone_height':0.186, 'cylinder_height':3.00, 'sink_height':0.190, 'height_total':3.376, 'inner_radius':0.510, 'outer_radius':0.7}, #m12
{'tipcone_height':0.155, 'cylinder_height':2.55, 'sink_height':0.175, 'height_total':2.880, 'inner_radius':0.425, 'outer_radius':0.6}, #m10
{'tipcone_height':0.124, 'cylinder_height':2.10, 'sink_height':0.160, 'height_total':2.384, 'inner_radius':0.340, 'outer_radius':0.5}, #m8
{'tipcone_height':0.091, 'cylinder_height':1.65, 'sink_height':0.150, 'height_total':1.891, 'inner_radius':0.250, 'outer_radius':0.4}, #m6
{'tipcone_height':0.076, 'cylinder_height':1.36, 'sink_height':0.090, 'height_total':1.526, 'inner_radius':0.210, 'outer_radius':0.3}, #m5
{'tipcone_height':0.060, 'cylinder_height':1.14, 'sink_height':0.135, 'height_total':1.335, 'inner_radius':0.165, 'outer_radius':0.3}, #m4
{'tipcone_height':0.045, 'cylinder_height':0.88, 'sink_height':0.175, 'height_total':1.100, 'inner_radius':0.125, 'outer_radius':0.3}  #m3
]