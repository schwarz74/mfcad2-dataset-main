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
              'stepdrill_cone_90deg' #26
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


#lists sorted decending
# radius : working length (in mm)
drill11620xxx = [(10, 55), (8.75, 51), (7.5, 45), (6.25, 43), (5, 35), (3.75, 29), (2.5, 20), (2, 17), (1.5, 14), (1, 11), (0.5, 4.5)]
# radius
stepdrill107020xx = [10, 9, 8, 7, 6, 5, 4, 3, 2.5, 2, 1.5, 1]
def largest_tuple_below(x,y,lst):
    """

    Args:
        x (_type_): radius
        y (_type_): length
        lst (_type_): _description_

    Returns:
        _type_: diameter, length
    """    
    for tup in lst:
        if tup[0] < x and tup[1] < y:
            return tup 
    return (0,0)