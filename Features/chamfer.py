import random

from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeChamfer

import Utils.shape_factory as shape_factory
import Utils.parameters as param
from Features.machining_features import MachiningFeature


class Chamfer(MachiningFeature):
    def __init__(self, shape, label_map, min_len, clearance, feat_names, edges):
        super().__init__(shape, label_map, min_len, clearance, feat_names)
        self.shifter_type = None
        self.bound_type = None
        self.depth_type = None
        self.feat_type = "chamfer"
        self.edges = edges

    def add_feature(self):
        while True:
            chamfer_maker = BRepFilletAPI_MakeChamfer(self.shape)

            try:
                edge = random.choice(self.edges)
            except IndexError:
                print("No more edges")
                break

            try:
                depth = random.uniform(param.chamfer_depth_min, param.chamfer_depth_max)
                chamfer_maker.Add(depth, edge)
                shape = chamfer_maker.Shape()
                self.edges.remove(edge)
                break
            except RuntimeError:
                try:
                    chamfer_maker = BRepFilletAPI_MakeChamfer(self.shape)
                    depth = param.chamfer_depth_min
                    chamfer_maker.Add(depth, edge)
                    shape = chamfer_maker.Shape()
                    self.edges.remove(edge)
                    break
                except:
                    self.edges.remove(edge)
                    continue

        try:
            fmap = shape_factory.map_face_before_and_after_feat(self.shape, chamfer_maker)
            label_map = shape_factory.map_from_shape_and_name(fmap, self.label_map,
                                                              shape, self.feat_names.index('chamfer'))

            return shape, label_map, self.edges
        except:
            return self.shape, self.label_map, self.edges