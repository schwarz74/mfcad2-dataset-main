import math
import numpy as np
import Utils.occ_utils as occ_utils

from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.gp import gp_Circ, gp_Ax2, gp_Pnt, gp_Dir
from Features.machining_features import MachiningFeature
import Utils.shape_factory as shape_factory
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone, BRepPrimAPI_MakeCylinder
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut

from Utils.parameters import drill11620xxx

class Drill140deg(MachiningFeature):
    def __init__(self, shape, label_map, min_len, clearance, feat_names):
        super().__init__(shape, label_map, min_len, clearance, feat_names)
        self.shifter_type = 4
        self.bound_type = 4
        self.depth_type = "blind"
        self.feat_type = "drill_pocket_140deg"

    #genau wie blind_hole
    def _add_sketch(self, bound):
        dir_w = bound[2] - bound[1]
        dir_h = bound[0] - bound[1]
        width = np.linalg.norm(dir_w)
        height = np.linalg.norm(dir_h)

        dir_w = dir_w / width
        dir_h = dir_h / height
        self.normal = np.cross(dir_w, dir_h)

        self.radius = min(width / 2, height / 2)

        self.center = (bound[0] + bound[1] + bound[2] + bound[3]) / 4

        #Isn't used really
        circ = gp_Circ(gp_Ax2(gp_Pnt(self.center[0], self.center[1], self.center[2]), occ_utils.as_occ(self.normal, gp_Dir)), self.radius)
        edge = BRepBuilderAPI_MakeEdge(circ, 0., 2 * math.pi).Edge()
        outer_wire = BRepBuilderAPI_MakeWire(edge).Wire()

        face_maker = BRepBuilderAPI_MakeFace(outer_wire)

        return face_maker.Face()
    
    def _apply_feature(self, old_shape, old_labels, feat_type, feat_face, depth_dir):
        
        depth_norm = np.linalg.norm(depth_dir)

        for tuple in drill11620xxx:
            if tuple[0] < self.radius and tuple[1] < depth_norm:
                self.radius = tuple[0]
                depth_total = tuple[1]
                cone_depth = tuple[2]
                cylinder_depth = tuple[3]
                break
        else:
            return old_shape, old_labels

        # make the shapes
        cylinder = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(self.center[0], self.center[1], self.center[2]), occ_utils.as_occ(-self.normal, gp_Dir)), self.radius, cylinder_depth)
        cone_center = self.center + (-self.normal*cylinder_depth)
        cone = BRepPrimAPI_MakeCone(gp_Ax2(gp_Pnt(cone_center[0], cone_center[1], cone_center[2]), occ_utils.as_occ(-self.normal, gp_Dir)), self.radius,0 , cone_depth)
 
        # combine the shapes
        fused = BRepAlgoAPI_Fuse(cone.Shape(),cylinder.Shape())
        result = BRepAlgoAPI_Cut(old_shape, fused.Shape())
        shape = result.Shape()
        
        
        fmap = shape_factory.map_face_before_and_after_feat(old_shape, result)
        new_labels = shape_factory.map_from_shape_and_name(fmap, old_labels, shape, self.feat_names.index(feat_type))

        return shape, new_labels