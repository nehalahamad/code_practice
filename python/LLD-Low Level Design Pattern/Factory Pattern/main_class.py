from shape_factory import ShapeFactory

class MainClass:
    def main(self):
        shape_factory_obj = ShapeFactory()
        # shape_obj = shape_factory_obj.get_shape("RECTANGLE")
        shape_obj = shape_factory_obj.get_shape("CIRCLE")
        shape_obj.draw()


main_class_obj = MainClass()
main_class_obj.main()