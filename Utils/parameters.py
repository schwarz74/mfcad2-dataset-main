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
#lists sorted decending
# (radius,working length, floor(cone_height), cylinder_depth) (in mm)
drill11620xxx = [(10, 55, 3.63, 51.37), (8.75, 51, 3.18, 47.82), (7.5, 45, 2.72, 42.28), (6.25, 43, 2.27, 40.73), (5, 35, 1.81, 33.19), (3.75, 29, 1.36, 27.64),
                  (2.5, 20, 0.90, 19.1), (2, 17, 0.72, 16.28), (1.5, 14, 0.54, 13.46), (1, 11, 0.36, 10.64), (0.5, 4.5, 0.18, 4.32)]
# radius (in mm)
spotdrill107020xx = [10, 9, 8, 7, 6, 5, 4, 3, 2.5, 2, 1.5, 1]
#(in mm)
stepdrill10767xxxxx = [
{'tipcone_height':5.10, 'cylinder_height':38.5, 'sink_height':2, 'height_total':46.5, 'inner_radius':14, 'outer_radius':18}, #m16
{'tipcone_height':4.37, 'cylinder_height':34.5, 'sink_height':2, 'height_total':40.87, 'inner_radius':12, 'outer_radius':16}, #m14
{'tipcone_height':3.71, 'cylinder_height':30,   'sink_height':1.9, 'height_total':35.61, 'inner_radius':10.2, 'outer_radius':14}, #m12
{'tipcone_height':3.09, 'cylinder_height':25.5, 'sink_height':1.75, 'height_total':30.34, 'inner_radius':8.5, 'outer_radius':12}, #m10
{'tipcone_height':2.48, 'cylinder_height':21,   'sink_height':1.6, 'height_total':25.08, 'inner_radius':6.8, 'outer_radius':10}, #m8
{'tipcone_height':1.82, 'cylinder_height':16.5, 'sink_height':1.5, 'height_total':19.82, 'inner_radius':5, 'outer_radius':8}, #m6
{'tipcone_height':1.53, 'cylinder_height':13.6, 'sink_height':0.9, 'height_total':16.03, 'inner_radius':4.2, 'outer_radius':6}, #m5
{'tipcone_height':1.27, 'cylinder_height':11.4, 'sink_height':1.35, 'height_total':14.02, 'inner_radius':3.3, 'outer_radius':6}, #m4
{'tipcone_height':0.91, 'cylinder_height':8.8,  'sink_height':1.75, 'height_total':11.46, 'inner_radius':2.5, 'outer_radius':6} #m3
]